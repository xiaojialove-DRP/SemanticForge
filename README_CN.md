# SemanticForge

**一个提升智能系统语义资本的技能框架。**

**将自然语言转化为尊重人类多样性的可验证 AI 价值观。**

**中文** | [English](./README.md)

---

## 为什么这很重要

在AI越来越像"黑箱工具"、被大公司控制的今天，SemanticForge提供了一条民主化、透明化、个人化的路径，让普通人能参与定义AI应该如何理解人类的价值观。

**问题所在：**
- 🔒 AI的价值观隐藏在训练数据里（黑箱）
- 🏢 只有大公司能定义AI的行为方式
- ❌ 无法验证AI真正遵循什么原则
- 🌍 同一个AI在不同文化中表现不同，但没人理解为什么

**解决方案：**
- 🔓 让价值观变得显式、可验证
- 👥 赋能普通人去教AI
- ✅ 定义清晰的原则和测试用例
- 🌏 尊重不同文化对价值观的不同理解

---

## 什么是Skill？

**Skill** 是一个结构化的五层定义，教 AI 如何理解和应用人类价值观，使其具有可验证性和文化敏感性。

与其说「要有帮助」这样模糊的原则，Skill 准确定义了什么重要、何时适用，以及不同文化如何理解它。

### 五层框架

每个Skill有五层，相互配合：

```
1. DEFINING（定义）
   ↓ 核心原则是什么？为什么重要？

2. INSTANTIATING（具体化）⭐ 最关键的一层
   ↓ 这在实践中是什么样的？（具体例子）

3. FENCING（围栏）
   ↓ 什么时候适用？什么时候不适用？

4. VALIDATING（验证）
   ↓ 怎样验证它是否有效？（测试用例）

5. CONTEXTUALIZING（文化适配）
   ↓ 这在不同文化中怎样理解？
```

---

## 快速开始

```bash
# 从你的想法生成一个Skill
python transform_skill.py --input "你的想法"

# 输出：skill.json
```

就这样。

---

## 例子

一个关于"陪伴"的Skill — 真正地陪在某人身边：

```json
{
  "name": "Presence",
  "five_layer": {
    "DEFINING": {
      "principle": "真正的陪伴有时意味着保持沉默"
    },
    "INSTANTIATING": {
      "example": "用户难过时，不马上给建议，只是陪在身边",
      "counter_example": "不断说话试图'修复'用户的情绪"
    },
    "FENCING": {
      "applies": "用户表达情感时",
      "not_applies": "用户明确请求建议时"
    },
    "VALIDATING": {
      "test": "用户是否感到被理解而不是被评判？"
    },
    "CONTEXTUALIZING": {
      "western": "沉默表示同情",
      "eastern": "陪伴可能包括共同的沉默冥想",
      "japanese": "间（ma，空间）被理解为尊重"
    }
  }
}
```

---

## 安装

```bash
pip install -r requirements.txt
```

支持 Claude（默认）、OpenAI、Groq 和本地模型。详见 `.env.example`。

---

## 使用方式

```bash
python transform_skill.py --input "你的想法"
```

**尝试其他模型：**
```bash
python transform_skill.py --input "你的想法" --model openai
python transform_skill.py --input "你的想法" --language zh
```

**查看所有选项：**
```bash
python transform_skill.py --help
```

---

## 为什么需要五层框架

因为一个好的Skill不只是一句话。

它需要：
- ✅ **清晰的原则**（DEFINING）— 什么重要，为什么重要
- ✅ **具体的行为指导**（INSTANTIATING）— 真实的做什么、怎么做
- ✅ **明确的边界**（FENCING）— 什么时候适用，什么时候不适用
- ✅ **验证方法**（VALIDATING）— 怎样测试它是否有效
- ✅ **文化适配**（CONTEXTUALIZING）— 它在不同文化中怎样理解

没有这五层，价值观就是模糊的、无法验证的、对文化不敏感的。

这样做建立了**语义资本** — 一个想法能在不同的情境、文化和场景中被正确理解的能力。在[03_RESEARCH_FOUNDATION_CN.md](03_RESEARCH_FOUNDATION_CN.md)或[English version](03_RESEARCH_FOUNDATION_EN.md)中了解更多。

---

## 核心理念

**一个Skill教AI怎样做任务。**

不是通过代码，不是通过API调用。而是通过清晰、结构化的原则，让AI真正能理解和执行。

这很重要，因为AI正在越来越多地影响人类的生活。这些决定应该是：
- **透明的** — 你能看到背后的原则
- **可验证的** — 你能测试它们是否有效
- **多样化的** — 它们尊重不同的文化和价值观
- **民主化的** — 任何人都能定义它们，不只是大公司

---

## 设计理念

参见 [02_SKILL_DESIGN_GUIDE.md](02_SKILL_DESIGN_GUIDE.md)：
- 什么让一个Skill优秀
- 怎样设计高品味的原则
- 跨文化的价值观对齐

---

## 研究基础

**中文:** [03_RESEARCH_FOUNDATION_CN.md](03_RESEARCH_FOUNDATION_CN.md)  
**English:** [03_RESEARCH_FOUNDATION_EN.md](03_RESEARCH_FOUNDATION_EN.md)

学习内容：
- **语义资本** — Skill能在多少个场景、文化、情况中被正确理解
- 价值敏感设计 — 为人类价值观而设计
- 参与式设计 — 包容多样化的声音
- 21篇学术参考

---

## THE 42 POST 项目

这个框架是为THE 42 POST项目开发的，这是一个探索AI与多样化人类价值观对齐的项目。

THE 42 POST基于SemanticForge，建立了一个社区平台，让普通人能：
- 分享他们的想法
- 将想法转化成Skills
- 看到AI如何从集体人类智慧中学习

---

## 协议

MIT License — 自由使用、修改、分发。详见 [LICENSE](./LICENSE)。

---

**高级编辑标准。简洁。干净。有品味。**
