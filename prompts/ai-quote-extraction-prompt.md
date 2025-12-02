## 任务说明
从书籍中提取有洞察力的英文原文quotes，并提供准确的中文翻译，按照指定的JSON格式输出。

## 输出格式

```json
  {
    "$schema": "https://github.com/tizee/quotes/raw/main/schema.json",
    "name": "书籍标题 - 作者 - 章节主题 Quotes",
    "quotes": [
      {
        "quote": "英文原文Quote\n中文翻译",
        "source": "书籍标题 - 作者 - 章节序号 章节名"
      }
    ]
  }
```

## 格式规范

### 1. Quote格式
- **结构**：一行英文原文，一行中文翻译
- **分隔符**：中英文之间用`\n`分隔
- **翻译要求**：
  - 准确传达原意，不曲解作者观点
  - 中文表达自然流畅，避免生硬直译
  - 保持专业术语翻译的一致性
  - 注意中英文标点符号的规范使用

### 2. Source格式
- **结构**：`"书籍标题 - 作者 - 章节序号 章节名"`
- **示例**：`"The Almanack of Naval Ravikant – Part 1: Wealth - On Building Wealth, Section: Understand How Wealth Is Created"`
- **规范**：
  - 使用英文破折号`–`（非连字符`-`）
  - 章节信息格式：`Section: 章节名`

## 内容选择标准

### 优先级（高到低）
1. **思维模型**：关于思考方式、决策框架的内容
2. **方法论**：具体的实践方法、行动指南
3. **经验总结**：作者的核心观点和经验提炼
4. **洞见性观点**：独特、反直觉但有价值的见解

### 过滤标准
- ✅ **选择**：具有洞察力、实用价值、可执行性
- ❌ **避免**：过于简单、常识性陈述、重复观点

## 质量控制检查清单

### 提取前检查
- [ ] 确保英文原文完整准确
- [ ] 验证quote的完整性和上下文
- [ ] 确认source信息准确无误

### 翻译质量检查
- [ ] 中文表达是否符合母语习惯
- [ ] 专业术语翻译是否准确一致
- [ ] 是否保留了原文的语气和重点
- [ ] 翻译是否存在文化差异问题

### 格式验证
- [ ] Schema引用是否正确
- [ ] 特殊字符是否正确转义
- [ ] 每章quotes数量控制在8-10条

## 执行步骤

1. **内容分析**：通读目标章节，理解核心观点
2. **Quote筛选**：按照内容选择标准标记高质量quotes
3. **翻译处理**：逐条翻译，确保质量
4. **质量检查**：使用检查清单验证输出

## 示例参考

### 优秀Quote示例
```json
{
  "quote": "Seek wealth, not money or status. Wealth is having assets that earn while you sleep.\n追求财富，而不是金钱或地位。财富是指在你睡觉时仍能为你赚钱的资产。",
  "source": "The Almanack of Naval Ravikant – Part 1: Wealth - On Building Wealth, Section: Understand How Wealth Is Created"
}
```

### 常见错误避免
- ❌ 翻译过于直白：`"Making money is not a thing you do"` → `"赚钱不是一件你做的事情"`
- ✅ 优化翻译：`"赚钱不是一件想做就能做的事情"`
