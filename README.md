# SemanticForge

**A skill framework that increases semantic capital for intelligent systems.**

**Transform natural language into verifiable AI values that honor human diversity.**

**[中文版本](./README_CN.md)** | English

---

## Why This Matters

In an era where AI increasingly becomes a "black box" controlled by corporations, SemanticForge provides a democratic, transparent, and personal pathway for ordinary people to shape how AI understands human values.

**The Problem:**
- 🔒 AI values are hidden in training data (black box)
- 🏢 Only corporations define how AI should behave
- ❌ No way to verify what principles AI actually follows
- 🌍 Same AI behaves differently across cultures, with no understanding why

**The Solution:**
- 🔓 Make values explicit and verifiable
- 👥 Empower ordinary people to teach AI
- ✅ Define clear boundaries and test cases
- 🌏 Honor cultural diversity in how values are understood

---

## What Is a Skill?

A **Skill** is a structured, five-layer definition that teaches AI how to understand and apply a human value in ways that are verifiable and culturally aware.

Instead of vague principles like "be helpful," a Skill defines exactly what matters, when it applies, and how different cultures understand it.

### The Five-Layer Framework

Every Skill has five layers that work together:

```
1. DEFINING
   ↓ What is the core principle? Why does it matter?

2. INSTANTIATING ⭐ (Most critical layer)
   ↓ What does this look like in practice? (concrete examples)

3. FENCING
   ↓ When does this apply? When doesn't it?

4. VALIDATING
   ↓ How do we verify it's working? (test cases)

5. CONTEXTUALIZING
   ↓ How does this adapt across cultures?
```

---

## Quick Start

```bash
# Generate a Skill from your idea
python transform_skill.py --input "Your idea"

# Output: skill.json
```

Done. That's it.

---

## Example

A Skill about "Presence" — being truly with someone:

```json
{
  "name": "Presence",
  "five_layer": {
    "DEFINING": {
      "principle": "True presence sometimes means staying silent"
    },
    "INSTANTIATING": {
      "example": "When a user is sad, don't immediately offer solutions—just be there",
      "counter_example": "Constantly talking to try to 'fix' the user's emotions"
    },
    "FENCING": {
      "applies": "When user expresses emotions",
      "not_applies": "When user explicitly asks for advice"
    },
    "VALIDATING": {
      "test": "Does the user feel understood, not judged?"
    },
    "CONTEXTUALIZING": {
      "western": "Silence shows compassion",
      "eastern": "Presence may include shared silent meditation",
      "japanese": "Ma (the space) is understood as respectful"
    }
  }
}
```

---

## Installation

```bash
pip install -r requirements.txt
```

Supports Claude (default), OpenAI, Groq, and local models. See `.env.example` for setup.

---

## Usage

```bash
python transform_skill.py --input "Your idea"
```

**Try a different model:**
```bash
python transform_skill.py --input "Your idea" --model openai
python transform_skill.py --input "你的想法" --language zh
```

**See all options:**
```bash
python transform_skill.py --help
```

---

## Why Five Layers?

Because a good Skill is more than a sentence.

It needs:
- ✅ **Clear principle** (DEFINING) — What matters and why
- ✅ **Concrete guidance** (INSTANTIATING) — Real examples of what to do
- ✅ **Clear boundaries** (FENCING) — When it applies, when it doesn't
- ✅ **Verification** (VALIDATING) — How to test if it's working
- ✅ **Cultural adaptation** (CONTEXTUALIZING) — How it works across cultures

Without these layers, values are vague, unverifiable, and culturally insensitive.

This builds **semantic capital** — the ability of an idea to be understood correctly across different contexts, cultures, and situations. Learn more in [03_RESEARCH_FOUNDATION_EN.md](03_RESEARCH_FOUNDATION_EN.md) ([中文版](03_RESEARCH_FOUNDATION_CN.md)).

---

## Core Philosophy

**A Skill teaches AI how to do something.**

Not through code. Not through API calls. But through clear, structured principles that AI can actually understand and apply.

This matters because AI is increasingly making decisions about how humans live. Those decisions should be:
- **Transparent** — You can see the principles
- **Verifiable** — You can test if they work
- **Diverse** — They respect different cultures and values
- **Democratic** — Anyone can define them, not just corporations

---

## Design Guide

See [02_SKILL_DESIGN_GUIDE.md](02_SKILL_DESIGN_GUIDE.md) for:
- What makes a Skill excellent
- How to design high-quality principles
- Cross-cultural value alignment

---

## Research Foundation

**English:** [03_RESEARCH_FOUNDATION_EN.md](03_RESEARCH_FOUNDATION_EN.md)  
**中文:** [03_RESEARCH_FOUNDATION_CN.md](03_RESEARCH_FOUNDATION_CN.md)

Learn about:
- **Semantic Capital** — how widely a Skill can be understood across contexts, cultures, and situations
- Value-Sensitive Design — designing for human values
- Participatory Design — including diverse voices
- 21 peer-reviewed references

---

## THE 42 POST Project

This framework was developed for THE 42 POST, a project exploring how to align AI with diverse human values.

THE 42 POST builds on SemanticForge by creating a community platform where ordinary people can:
- Share their value ideas
- Have them transformed into Skills
- See how AI learns from collective human wisdom

---

## License

MIT License — Use, modify, and distribute freely. See [LICENSE](./LICENSE) for details.

---

**High editorial standard. Simple. Clean. Thoughtful.**
