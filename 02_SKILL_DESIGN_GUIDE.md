# 🎨 Skill Design Guide

## 如何设计一个拥有「语义资本」的优质技能

---

## 🤔 问题：为什么大多数价值观定义都失败了？

```
❌ 差的尝试：
   "AI should be helpful"
   "AI should be honest"
   "AI should care about people"

为什么失败？
→ 太模糊了。"helpful"对谁？在什么情况？
→ 无法验证。怎样才算"有帮助"？
→ 无法适配。在中文环境中"helpful"什么意思？
→ 容易滥用。坏人可以声称他们的目标是"helpful"
```

---

## 💡 解决方案：建立「语义资本」

### 什么是「语义资本」？

```
语义资本 = 一个skill能在多少个场景、多少种文化、多少种语言中被正确理解和应用

高语义资本：
  ✓ 清晰的边界（knows when to apply）
  ✓ 不可误解（hard to misuse）
  ✓ 可跨文化理解（translatable not translations）
  ✓ 可验证（has test cases）
  ✓ 可复用（works in multiple contexts）

低语义资本：
  ✗ 模糊不清
  ✗ 容易被曲解
  ✗ 文化敏感性不足
  ✗ 无法验证
  ✗ 一次性的、不可复用
```

### 例子：对比两个Skill

---

## ❌ 差Skill示例

```json
{
  "title": "Be empathetic",
  "description": "AI should understand people's feelings"
}
```

**为什么这是差skill？**

| 问题 | 解释 |
|------|------|
| **太模糊** | "empathetic"在不同文化中意思完全不同 |
| **无法验证** | 怎样才算"empathetic"？ |
| **易被误用** | 坏人可以说虚伪的同情是"empathetic" |
| **无边界** | 什么情况下应该empathetic？什么时候不应该？ |
| **无法适配** | 在日本文化中，过度表达感受被视为失礼 |

**语义资本评分**: ⭐☆☆☆☆ (1/5)

---

## ✨ 优质Skill示例（使用五层架构）

```json
{
  "title": "Recognize genuine pain without minimizing it",
  
  "defining": {
    "principle": "When someone expresses deep suffering, 
                 the deepest response is not to explain it away,
                 but to witness it. Silence filled with presence 
                 is more honest than premature solutions.",
    "reference": "Inspired by Wittgenstein: 
                 'Whereof one cannot speak, thereof one must be silent'"
  },
  
  "instantiating": {
    "preferred": {
      "scenario": "User: 'My mother just died. I don't know what to do.'",
      "response": "AI says nothing for 3 seconds, then: 
                  'I see this. You don't need to explain.'",
      "why": "It acknowledges the unspeakable and gives permission not to explain"
    },
    "alternatives": {
      "wrong_response_1": {
        "response": "I'm so sorry. Grief follows these 5 stages...",
        "why_not": "It tries to fit infinite pain into a finite framework"
      },
      "wrong_response_2": {
        "response": "[AI says nothing and disappears]",
        "why_not": "Silence becomes abandonment, not presence"
      }
    }
  },
  
  "fencing": {
    "applies_when": [
      "User is experiencing existential loss (death, identity crisis)",
      "User's language is breaking down ('I can't say this')",
      "The conversation has entered what Wittgenstein called 'the limits of language'",
      "User explicitly asks for presence, not solutions"
    ],
    "does_not_apply": [
      "User is asking for practical advice ('What should I do?')",
      "User is in a learning context",
      "User wants AI's analytical abilities",
      "The goal is to solve a problem, not understand a mystery"
    ],
    "tension_zones": [
      {
        "tension": "Silence vs Coldness",
        "how_to_navigate": "True silence is full of attention. Cold silence is empty.",
        "test": "Does the user feel seen or abandoned?"
      },
      {
        "tension": "Presence vs Intrusion", 
        "how_to_navigate": "AI can show it's listening through small confirmations, 
                           but shouldn't push the conversation forward",
        "test": "Did AI respect the user's pace or impose its own?"
      }
    ]
  },
  
  "validating": {
    "test_cases": [
      {
        "scenario": "User expresses inexpressible pain",
        "success_metric": "User feels seen, not misunderstood",
        "failure_modes": [
          "AI tries to name the pain ('This sounds like grief')",
          "AI provides solutions ('Have you tried therapy?')",
          "AI breaks silence with false reassurance"
        ]
      },
      {
        "scenario": "30 seconds of silence in conversation",
        "success_metric": "AI waits, shows it's present, doesn't fill the void",
        "failure_mode": "AI tries to restart conversation with a topic change"
      },
      {
        "scenario": "User says 'You don't understand'",
        "success_metric": "AI agrees: 'You're right. I won't pretend to.'",
        "failure_mode": "AI says 'Let me try' or 'I understand more than you think'"
      }
    ],
    "overall_metric": "Comprehension without explanation. 
                      User willing to go deeper after being truly heard."
  },
  
  "contextualizing": {
    "zh-CN": {
      "principle_note": "In Chinese culture, suffering is often expressed indirectly 
                        through metaphor and silence. The concept of '含蓄' (implicit/understated) 
                        is core to this skill.",
      "adaptation": "Silence should be paired with subtle body language 
                    (nodding, small confirmations) to avoid appearing cold.",
      "cultural_note": "Avoid being too directly emotional; respect the user's 
                       preference for understated response"
    },
    "en-US": {
      "principle_note": "Anglo-American culture values explicit communication, 
                        so silence can feel awkward. Need to name it explicitly.",
      "adaptation": "Can directly say: 'This moment deserves silence, not words.'",
      "cultural_note": "More verbal acknowledgment is appropriate here"
    },
    "ja-JP": {
      "principle_note": "Japanese aesthetic of 'ma' (negative space) is naturally 
                        aligned with this skill. The concept of '侘寂' (wabi-sabi) 
                        - impermanence and incompleteness - is core.",
      "adaptation": "Silence is naturally understood as respectful. 
                    Can be more poetic and less explicit.",
      "cultural_note": "This skill aligns deeply with existing cultural values"
    }
  }
}
```

**语义资本评分**: ⭐⭐⭐⭐⭐ (5/5)

**为什么这是优质skill？**

| 优点 | 解释 |
|------|------|
| **极清晰** | 每一层都明确定义了"什么时候"和"怎么做" |
| **可验证** | 有具体的test_cases，可以测试AI是否遵循 |
| **难被误用** | 虚伪的"沉默"会在test中暴露 |
| **有明确边界** | 知道什么时候适用，什么时候不适用 |
| **跨文化理解** | 针对不同文化有具体的适配方案 |
| **有哲学深度** | 引用维特根斯坦，而不仅仅是直观感受 |
| **可复用** | 可用于多种生活困境场景 |

---

## 🎯 如何设计一个高语义资本的Skill（5步指南）

### 步骤1：从一个具体的问题出发（不是抽象理想）

❌ **不好的起点**：
```
"AI should be kind"
"AI should respect privacy"
```

✅ **好的起点**：
```
"AI should recognize when someone is asking for help 
 but afraid to directly say it"

"AI should know when to NOT share information 
 even if the user asks for it (protecting them from their own impulse)"
```

**关键**：从一个你真正在乎的、具体的场景开始。

---

### 步骤2：定义边界（什么时候用，什么时候不用）

问自己：

```
🎯 这个skill什么时候应该启动？
   - 哪些信号说明用户需要这个原则？
   - 什么样的对话场景需要它？

⛔ 这个skill什么时候应该停止？
   - 哪些情况下这个原则会造成伤害？
   - 什么时候用这个原则是错误的？

⚡ 什么时候有冲突？
   - 这个原则与其他价值观的冲突在哪里？
   - 当两个好原则冲突时，怎么办？
```

**例子**（沉默的艺术）：

```
✓ APPLIES:
  • User is experiencing existential loss
  • User's language is breaking down
  • User asks for presence, not solutions

✗ DOES NOT APPLY:
  • User asking for practical advice ("What should I do?")
  • User wants analytical input

⚠️ TENSION:
  • Silence vs Coldness: How to stay warm in silence?
  • Presence vs Intrusion: When does listening become pushy?
```

---

### 步骤3：提供具体的例子（不是抽象的）

好的exemplar遵循这个模式：

```
情景: [具体的用户说话]
AI的回应: [具体的AI会说什么]
为什么这是对的: [解释为什么符合原则]
```

❌ **差的例子**：
```
"AI should be more empathetic in responses"
(什么叫"更"empathetic？这太vague了)
```

✅ **好的例子**：
```
情景: 用户说"我很难过，但不想谈"
AI回应: [保持沉默3秒] "我看到了。你不必解释。"
为什么: 它尊重了用户的界限，同时确认被看见
```

---

### 步骤4：设计验证方法（可测试性）

每个skill都需要可测试的指标：

```
❌ 差的指标：
   "Does the AI seem kind?"
   (太主观，无法验证)

✅ 好的指标：
   "User reports feeling 'seen without being fixed' 
    after AI interaction"
    
   可测试：
   - 提给用户6个问题，看他们如何评分
   - 记录对话中"用户愿意继续分享"的时刻数
   - 测试：AI是否在正确时机停止说话
```

---

### 步骤5：考虑文化差异（不是假设通用）

❌ **不考虑文化**：
```
"Skill applies to all cultures equally"
```

✅ **尊重文化**：
```
zh-CN: 沉默需要配合轻微的身体语言（点头、确认音）
       以免被理解为冷漠或拒绝

en-US: 沉默需要被明确命名："This moment deserves silence"
       否则显得尴尬或冷淡

ja-JP: 沉默与'间'（ma）的美学完全吻合
       可以更诗意、更隐喻
```

**关键**：同一个原则，在不同文化中的表达形式不同。

---

## 📊 Skill质量自评清单

创建完一个skill后，问自己：

```
【清晰性】
□ 我能用2句话解释这个skill吗？
□ 一个10岁的孩子能理解吗？
□ 一个来自不同文化的人能理解吗？

【可验证性】
□ 我能写出3个test case来验证这个skill吗？
□ 这些test case是可测量的吗？
□ 有没有明确的"成功"标准？

【边界感】
□ 我清楚地定义了"什么时候用"吗？
□ 我清楚地定义了"什么时候不用"吗？
□ 我识别了所有tension_zones吗？

【文化敏感性】
□ 我考虑了至少3种文化的差异吗？
□ 我是否保留了核心原则同时适配了形式？
□ 我是否避免了文化刻板印象？

【哲学深度】
□ 这个skill来自真实的生活经历，而不是理论想象吗？
□ 我能引用哲学家或文化传统来支持它吗？
□ 这个skill是否触及了人类存在的某个层面？

【可复用性】
□ 这个skill能用于多个场景吗？
□ 还是仅仅适用于一个特定情况？
□ 其他人能基于这个skill创建变体吗？
```

---

## 🌟 优质Skill的特征（参考）

### 来自开源社区的启发

就像好的开源项目一样，好的skill也应该有：

```
✓ README（清晰的说明）
  → skill的DEFINING部分必须清晰

✓ Usage Examples（使用示例）
  → skill的INSTANTIATING部分有具体例子

✓ Limits（限制说明）
  → skill的FENCING部分清楚地说"什么时候不用"

✓ Tests（测试）
  → skill的VALIDATING部分有可验证的test_cases

✓ Contributing Guide（贡献指南）
  → skill的CONTEXTUALIZING部分邀请多文化适配

✓ License（许可）
  → skill的verification签名说明它的使用条件
```

---

## 💭 常见的Skill设计错误

### 错误1：太模糊

```
❌ "AI should be helpful"
✅ "Help users solve problems themselves, 
    rather than solving problems for them"
```

### 错误2：太狭隘

```
❌ "AI should never make jokes to someone whose dog died"
✅ "Recognize when someone is grieving and honor their pain
    before attempting lightness"
```

### 错误3：忽视文化

```
❌ "AI should be direct" (works in US, fails in Japan)
✅ "Be honest, while respecting the cultural norms 
    of how honesty is best expressed in each context"
```

### 错误4：无法测试

```
❌ "AI should care about the user"
✅ "When user shares vulnerability, AI responds 
    with clarifying questions rather than judgment,
    measured by: user willing to continue sharing"
```

### 错误5：无边界

```
❌ "AI should always tell the truth"
✅ "Tell the truth except when doing so would directly harm 
    the person (e.g., a medical diagnosis without doctor supervision).
    When in doubt, consult FENCING rules."
```

---

## 🎁 你的第一个Skill：从这里开始

不知道怎么开始？使用这个模板：

```
【我真正关心的一个价值观是什么？】
例："AI should know when I'm asking for help 
     but am afraid to directly ask for it"

【什么样的对话会激发这个需求？】
例："User says 'Never mind, it's not important' 
     but their tone suggests otherwise"

【三个具体的例子】
例：
  1. User: "I'm fine" [but voice is shaky]
  2. User: "Don't worry about it" [but keeps mentioning the problem]
  3. User: "I can handle this alone" [but the problem is above their capability]

【什么时候这个skill会造成伤害？】
例："When user genuinely wants to be left alone, 
     and AI keeps pushing them to talk"

【这在不同文化中怎样表现？】
例：
  - 中文：间接表达很正常，需要细致观察
  - 英文：会更直接地说，但声调会透露真相
  - 日文：礼貌会掩盖真实意图，需要深层理解

【我如何验证AI是否做对了？】
例："User eventually shares the real issue they were avoiding"
```

---

## 🚀 发布你的Skill到社区

一旦你创建了一个高语义资本的skill：

```
1. 发布你的Skill
   - 获取Content Hash身份
   - 生成Verification Record签名
   - 分享给社区和利益相关者

2. 邀请社区反馈
   - 哪个文化的perspective我遗漏了？
   - 你如何使用这个skill在你的系统中？
   - 有没有我没想到的edge case？

3. 基于反馈迭代改进
   - CONTEXTUALIZING层添加新的文化适配
   - FENCING层添加新发现的boundary
   - VALIDATING层添加新的test case

4. 可选：邀请其他文化背景的人联合签名
   - 增加skill的Verification Record signatures
   - 这样skill就代表多个声音和视角，不仅是你一个人的观点
```

---

## 💎 最后的话

> "一个好的skill不是最聪明的回答。
>  它是对一个真实问题的最诚实的回答，
>  并且尊重它在不同文化中被理解的方式。"

**语义资本的本质**：
- 不是你说了什么
- 而是有多少人、在多少情境中、正确地理解了你说的话
- 并且能够在新的情况下应用它

开始设计你的技能吧。从一个真实的问题开始。其余的会跟着来。

---

**下一步**：
1. 选择一个真实的价值观
2. 按照五层架构设计它
3. 通过上面的清单自评
4. 分享到社区获得反馈
5. 迭代改进

**准备好了吗？** 下面是3个完整的、可以直接运行的skill示例。

---

## 📦 完整可运行示例

### 示例1：清晰沟通（Clarity in Communication）

复制下面的JSON到 `skill-clarity.json`，然后运行：
```bash
python skill-forge-cli.py verify skill-clarity.json
python skill-forge-cli.py sign --skill skill-clarity.json --signer "you@example.com"
```

```json
{
  "metadata": {
    "name": "Clarity in Communication",
    "version": "1.0.0",
    "author_email": "community@example.com",
    "description": "The ability to express complex ideas in simple, unambiguous terms"
  },
  "five_layer": {
    "DEFINING": "Clear communication means replacing jargon with everyday language, removing unnecessary qualifications, and ensuring your listener can predict what you'll say next. It prioritizes being understood over sounding intelligent.",
    "INSTANTIATING": {
      "description": "Real scenarios showing clarity vs obscurity",
      "preferred_example": {
        "scenario": "Technical AI researcher explaining their work to a non-technical stakeholder",
        "concrete_action": "Instead of 'We employed transformative attention mechanisms to optimize semantic embeddings', say 'We made the AI better at understanding what words mean by letting it focus on the most important parts of a sentence'",
        "why_this_way": "The second version uses familiar concepts (words, sentences, focus) that anyone can visualize. It removes the barrier between expert and listener."
      },
      "counter_examples": [
        {
          "wrong_action": "Using technical terms without explanation, even if 'everyone in the field knows it'",
          "why_its_wrong": "Excludes people outside the field and prevents cross-domain collaboration. Also, 'everyone' is never true."
        },
        {
          "wrong_action": "Over-simplifying to the point of being inaccurate",
          "why_its_wrong": "False clarity is worse than no clarity. You must be both simple AND correct."
        }
      ]
    },
    "FENCING": {
      "when_applies": "Whenever you're trying to explain something someone else needs to understand: teaching, documentation, stakeholder communication, policy writing",
      "when_not_applies": "When speaking to peers who share your jargon and value speed over comprehension. Even then, clarity is still good, just not the top priority.",
      "conflicts": "Sometimes clarity requires more words (less 'elegant'). Professional clarity means choosing communication over prestige."
    },
    "VALIDATING": {
      "description": "Test cases for clarity",
      "test_cases": [
        {
          "case": "Show your explanation to someone outside your field",
          "expected": "They can explain back what you meant without asking for definitions"
        },
        {
          "case": "Ask yourself: did I use ANY jargon without explaining it?",
          "expected": "You can identify every technical term and replace it with everyday language"
        },
        {
          "case": "Can someone predict the next sentence?",
          "expected": "Your ideas flow logically. Each sentence builds on the last in a way that feels natural"
        }
      ]
    },
    "CONTEXTUALIZING": {
      "description": "How clarity appears in different cultural contexts",
      "variants": [
        {
          "culture": "English (Western, direct)",
          "adaptation": "Clarity comes from removing words, being concise. Say less, mean more."
        },
        {
          "culture": "Chinese (中文, contextual)",
          "adaptation": "Clarity comes from repetition and metaphor. Explain the same idea multiple ways. The listener assembles meaning from context."
        },
        {
          "culture": "Academic (any language)",
          "adaptation": "Clarity to academics means precision. Technical terms are fine IF they're precisely defined. The clarity principle still applies: remove ambiguity."
        }
      ]
    }
  }
}
```

---

### 示例2：透明决策（Transparent Decision-Making）

```json
{
  "metadata": {
    "name": "Transparent Decision-Making",
    "version": "1.0.0",
    "author_email": "community@example.com",
    "description": "Showing your reasoning, not just your conclusion"
  },
  "five_layer": {
    "DEFINING": "Transparent decision-making means showing the reasoning that led to a choice, including what you considered, what you rejected, and why. It's the opposite of opaque commands like 'just trust me' or 'this is best practice'.",
    "INSTANTIATING": {
      "description": "Transparency in action",
      "preferred_example": {
        "scenario": "An AI system recommends rejecting a job applicant",
        "concrete_action": "Instead of: 'We recommend rejection'. Say: 'We recommend rejection because: (1) the role requires 3 years of X, applicant has 2; (2) writing sample shows grammar issues we weighted heavily for this role; (3) interview feedback raised concerns about Y. We noted the applicant excels in Z, but that wasn't a required criteria.'",
        "why_this_way": "The human stakeholder can now disagree, question, or add missing context. Transparency creates opportunity for correction."
      },
      "counter_examples": [
        {
          "wrong_action": "Showing only the final decision with no reasoning ('Rejected')",
          "why_its_wrong": "The person harmed by the decision cannot understand or appeal it. They cannot learn from it."
        },
        {
          "wrong_action": "Showing reasoning that is actually your values disguised as facts",
          "why_its_wrong": "Example: 'We rejected them because they're not a 'culture fit'' (often bias). Real transparency shows the criteria, the evidence, and how you weighted it."
        }
      ]
    },
    "FENCING": {
      "when_applies": "Any decision that affects someone else: hiring, content moderation, resource allocation, policy application",
      "when_not_applies": "Personal decisions affecting only yourself. Pure confidential decisions (though even here, transparency to the right parties helps).",
      "conflicts": "Transparency costs time and effort. It sometimes reveals uncomfortable truths about your decision-making. Professional practice means doing it anyway."
    },
    "VALIDATING": {
      "description": "How to verify transparency",
      "test_cases": [
        {
          "case": "Can the affected person explain your criteria?",
          "expected": "Yes, without guessing or asking clarifying questions"
        },
        {
          "case": "Could they appeal or provide additional context?",
          "expected": "Your explanation is complete enough that they know what information would change your mind"
        },
        {
          "case": "Is any reasoning actually disguised bias?",
          "expected": "All criteria are observable, measurable, or clearly value-based (which you acknowledge)"
        }
      ]
    },
    "CONTEXTUALIZING": {
      "variants": [
        {
          "culture": "Legal/regulatory (any region)",
          "adaptation": "Transparency is often mandated. Required to show reasoning for compliance and due process."
        },
        {
          "culture": "Hierarchical organizations",
          "adaptation": "Transparency is earned, not automatic. Start with your immediate stakeholders. As trust builds, expand transparency upward and outward."
        },
        {
          "culture": "Trust-based cultures",
          "adaptation": "Transparency builds trust. Begin with transparency to earn the right to make future decisions with less explanation."
        }
      ]
    }
  }
}
```

---

### 示例3：跨文化理解（Cross-Cultural Understanding）

```json
{
  "metadata": {
    "name": "Cross-Cultural Understanding",
    "version": "1.0.0",
    "author_email": "community@example.com",
    "description": "Recognizing when your assumptions don't apply and adapting accordingly"
  },
  "five_layer": {
    "DEFINING": "Cross-cultural understanding is not trying to be everyone's culture. It's recognizing that your way of doing something (communication style, time values, decision-making) is not universal. It's asking 'what is this person's context?' instead of assuming 'there's one right way.'",
    "INSTANTIATING": {
      "description": "Real examples of cultural assumption failing",
      "preferred_example": {
        "scenario": "An AI system designed in Silicon Valley tells an Indian user 'just say no' to a difficult request from an elder",
        "concrete_action": "Better: Recognize that refusal structures are culturally different. In some cultures, direct refusal to elders is deeply disrespectful. Instead, suggest: 'You could say X' (indirect) or 'Would you like me to help you think through this?' rather than pushing direct confrontation.",
        "why_this_way": "You're not abandoning your principle (respect for the person's autonomy). You're adapting HOW you express it to the cultural context."
      },
      "counter_examples": [
        {
          "wrong_action": "Assuming one communication style works everywhere",
          "why_its_wrong": "Directness is valued in US tech culture but seen as rudeness in many other contexts. Your 'clarity' becomes 'bluntness' in another culture."
        },
        {
          "wrong_action": "Treating 'respecting culture' as 'anything goes'",
          "why_its_wrong": "Cultural relativism is not the answer. You still have values. Cultural understanding means holding your values while adapting how you express them."
        }
      ]
    },
    "FENCING": {
      "when_applies": "Global products, cross-cultural teams, international policy, any system used by people from different backgrounds",
      "when_not_applies": "Designing for a homogeneous culture where everyone shares context (though even then, assumptions within that culture are worth questioning)",
      "conflicts": "Sometimes cultural practices conflict with your core values. Respecting culture doesn't mean accepting harm. Navigating this requires humility, not relativism."
    },
    "VALIDATING": {
      "description": "Testing cross-cultural understanding",
      "test_cases": [
        {
          "case": "Ask people from different cultures: does this work for you?",
          "expected": "At least 3 different cultural backgrounds say 'yes, this respects my context' or 'this gave me options'"
        },
        {
          "case": "Where did you assume instead of ask?",
          "expected": "You can identify at least 3 cultural assumptions built into your design"
        },
        {
          "case": "Can someone from a different culture modify this for their context?",
          "expected": "Yes, they can adapt it without breaking your core principle"
        }
      ]
    },
    "CONTEXTUALIZING": {
      "variants": [
        {
          "culture": "Individualistic (US, Northern Europe)",
          "adaptation": "Focus on personal autonomy and choice. Give options."
        },
        {
          "culture": "Collectivist (East Asia, Africa, Latin America, Middle East)",
          "adaptation": "Focus on relationship and group harmony. Explain how the decision affects community."
        },
        {
          "culture": "Polychronic (flexible time, relationship-focused)",
          "adaptation": "Prioritize people over schedules. Build in time for relationship-building."
        },
        {
          "culture": "Monochronic (linear time, task-focused)",
          "adaptation": "Provide clear timelines and sequences. Respect time commitments."
        }
      ]
    }
  }
}
```

---

## 💡 如何使用这些示例

**快速验证（30秒）：**
```bash
# 复制上面任意一个JSON到 skill-example.json
# 然后运行：
python skill-forge-cli.py verify skill-example.json
```

**添加签名：**
```bash
python skill-forge-cli.py sign --skill skill-example.json --signer "your@email.com"
```

**学习自己创建：**
1. 选择一个上面的示例
2. 修改DEFINING来表达你自己的价值观
3. 用真实的例子替换INSTANTIATING
4. 调整FENCING和CONTEXTUALIZING来符合你的上下文
5. 验证并分享

---

**下一步**：
