#!/usr/bin/env python3
"""
SemanticForge - Transform Natural Language into AI Values
Supports multiple AI models: Claude, OpenAI, Groq, and local models

Usage:
    python transform_skill.py --input "Your idea" --output skill.json
    python transform_skill.py --input "Your idea" --model openai
    python transform_skill.py --input "Your idea" --model groq
    python transform_skill.py --input "Your idea" --model local
"""

import os
import json
import argparse
import sys
from pathlib import Path
from abc import ABC, abstractmethod


class ModelProvider(ABC):
    """Abstract base class for AI model providers."""

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Generate response from the model."""
        pass


class AnthropicProvider(ModelProvider):
    """Anthropic Claude model provider."""

    def __init__(self):
        try:
            from anthropic import Anthropic
        except ImportError:
            raise ImportError("anthropic library not installed. Run: pip install anthropic")

        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "❌ ANTHROPIC_API_KEY not found.\n"
                "   Set it via: export ANTHROPIC_API_KEY='your-key'\n"
                "   Or add to .env file"
            )

        self.client = Anthropic(api_key=api_key)
        self.model = "claude-3-5-sonnet-20241022"

    def generate_response(self, prompt: str) -> str:
        """Generate response using Claude."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text


class OpenAIProvider(ModelProvider):
    """OpenAI model provider."""

    def __init__(self):
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("openai library not installed. Run: pip install openai")

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "❌ OPENAI_API_KEY not found.\n"
                "   Set it via: export OPENAI_API_KEY='your-key'\n"
                "   Or add to .env file"
            )

        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4-turbo"

    def generate_response(self, prompt: str) -> str:
        """Generate response using OpenAI."""
        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content


class GroqProvider(ModelProvider):
    """Groq model provider."""

    def __init__(self):
        try:
            from groq import Groq
        except ImportError:
            raise ImportError("groq library not installed. Run: pip install groq")

        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError(
                "❌ GROQ_API_KEY not found.\n"
                "   Set it via: export GROQ_API_KEY='your-key'\n"
                "   Or add to .env file"
            )

        self.client = Groq(api_key=api_key)
        self.model = "mixtral-8x7b-32768"

    def generate_response(self, prompt: str) -> str:
        """Generate response using Groq."""
        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content


class LocalModelProvider(ModelProvider):
    """Local model provider (e.g., Ollama)."""

    def __init__(self):
        try:
            import ollama
        except ImportError:
            raise ImportError(
                "ollama library not installed.\n"
                "   Install Ollama from: https://ollama.ai\n"
                "   Or run: pip install ollama"
            )

        self.client = ollama
        self.model = os.getenv("LOCAL_MODEL", "mistral")

    def generate_response(self, prompt: str) -> str:
        """Generate response using local model."""
        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        return response.get("response", "")


def get_provider(model_type: str = "claude") -> ModelProvider:
    """Get the appropriate model provider."""
    providers = {
        "claude": AnthropicProvider,
        "anthropic": AnthropicProvider,
        "openai": OpenAIProvider,
        "gpt": OpenAIProvider,
        "groq": GroqProvider,
        "local": LocalModelProvider,
        "ollama": LocalModelProvider,
    }

    provider_class = providers.get(model_type.lower())
    if not provider_class:
        available = ", ".join(providers.keys())
        raise ValueError(f"Unknown model type: {model_type}. Available: {available}")

    return provider_class()


class SkillForge:
    """Transform natural language into five-layer skills."""

    def __init__(self, model: str = "claude"):
        """Initialize SkillForge with specified model provider."""
        self.provider = get_provider(model)
        self.model_type = model

    def generate_skill(self, idea: str, skill_name: str = None, language: str = "en", author: str = "anonymous") -> dict:
        """Generate a complete five-layer skill from a natural language idea."""

        if not skill_name:
            skill_name = idea.split()[0] if idea else "Skill"

        prompt = self._build_prompt(idea, language)

        print(f"   → Generating skill from idea (using {self.model_type})...")
        response_text = self.provider.generate_response(prompt)

        skill_json = self._parse_response(response_text)

        # Ensure required fields
        if "name" not in skill_json:
            skill_json["name"] = skill_name
        if "version" not in skill_json:
            skill_json["version"] = "1.0.0"
        if "author" not in skill_json:
            skill_json["author"] = author

        return skill_json

    def _build_prompt(self, idea: str, language: str) -> str:
        """Build the prompt for skill generation."""

        if language == "zh":
            return f"""你是一个Skill设计专家。请根据以下想法，生成一个完整的五层Skill定义。

想法：{idea}

请生成JSON格式的Skill，包含以下五层：

1. DEFINING - 核心原则是什么？为什么重要？
2. INSTANTIATING - 具体例子和反例
3. FENCING - 什么时候适用，什么时候不适用
4. VALIDATING - 怎样验证这个Skill是否有效？
5. CONTEXTUALIZING - 在不同文化、角色、情况下的适配

只返回JSON，格式如下：
{{
  "name": "技能名称",
  "five_layer": {{
    "DEFINING": {{"principle": "...", "description": "..."}},
    "INSTANTIATING": {{"preferred_example": {{}}, "counter_examples": []}},
    "FENCING": {{"applies_when": [], "does_not_apply_when": []}},
    "VALIDATING": {{"test_cases": [], "success_indicators": []}},
    "CONTEXTUALIZING": {{"across_cultures": {{}}, "across_roles": {{}}, "across_situations": {{}}}}
  }}
}}
"""
        else:
            return f"""You are a Skill design expert. Generate a complete five-layer Skill from this idea:

Idea: {idea}

Generate a JSON Skill with these five layers:

1. DEFINING - What is the core principle? Why does it matter?
2. INSTANTIATING - Concrete examples and counter-examples
3. FENCING - When to apply, when not to apply
4. VALIDATING - How to verify this skill is working
5. CONTEXTUALIZING - Adaptations across cultures, roles, situations

Return ONLY valid JSON in this format:
{{
  "name": "Skill name",
  "five_layer": {{
    "DEFINING": {{"principle": "...", "description": "..."}},
    "INSTANTIATING": {{"preferred_example": {{}}, "counter_examples": []}},
    "FENCING": {{"applies_when": [], "does_not_apply_when": []}},
    "VALIDATING": {{"test_cases": [], "success_indicators": []}},
    "CONTEXTUALIZING": {{"across_cultures": {{}}, "across_roles": {{}}, "across_situations": {{}}}}
  }}
}}
"""

    def _parse_response(self, text: str) -> dict:
        """Parse JSON from response, handling markdown code blocks."""

        # Try direct JSON parsing first
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Try extracting from markdown code block
        if "```json" in text:
            start = text.find("```json") + 7
            end = text.find("```", start)
            if end > start:
                try:
                    return json.loads(text[start:end].strip())
                except json.JSONDecodeError:
                    pass

        # Try extracting any JSON block
        if "```" in text:
            start = text.find("```") + 3
            end = text.find("```", start)
            if end > start:
                try:
                    return json.loads(text[start:end].strip())
                except json.JSONDecodeError:
                    pass

        raise ValueError(f"Could not parse JSON from response: {text[:200]}")


def main():
    parser = argparse.ArgumentParser(
        description="SemanticForge - Transform natural language into AI values"
    )
    parser.add_argument("--input", "-i", required=True, help="Natural language idea")
    parser.add_argument("--output", "-o", default="skill.json", help="Output file path")
    parser.add_argument("--name", "-n", help="Skill name (auto-generated if not provided)")
    parser.add_argument("--author", "-a", default="anonymous", help="Author email/name")
    parser.add_argument("--language", "-l", default="en", choices=["en", "zh"], help="Language")
    parser.add_argument(
        "--model", "-m",
        default="claude",
        help="AI model to use (claude, openai, groq, local). Default: claude"
    )
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="List available models"
    )

    args = parser.parse_args()

    # List available models
    if args.list_models:
        print("Available models:")
        print("  • claude (Anthropic Claude) - requires ANTHROPIC_API_KEY")
        print("  • openai (OpenAI GPT) - requires OPENAI_API_KEY")
        print("  • groq (Groq Mixtral) - requires GROQ_API_KEY")
        print("  • local (Ollama) - requires LOCAL_MODEL env var")
        return

    try:
        # Generate skill
        forge = SkillForge(model=args.model)
        skill = forge.generate_skill(
            idea=args.input,
            skill_name=args.name,
            language=args.language,
            author=args.author
        )

        # Save to file
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(skill, f, ensure_ascii=False, indent=2)

        print(f"✅ Skill saved to: {args.output}")
        print(f"   Name: {skill.get('name')}")
        print(f"   Author: {skill.get('author')}")
        print(f"   Model: {args.model}")

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
