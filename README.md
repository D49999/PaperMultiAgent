
# Multi-Agent Academic Paper Assistant

这是一个面向 SCI 一区标准设计的多 Agent 协作学术辅助工作流原型。本项目通过模拟完整的科研逻辑流，解决海量文献精读、跨文档交叉验证以及符合学术规范的长文本生成问题。

## 架构特性 (Core Features)

1. **长链推理 (Long-Chain Reasoning)**：将宏观课题自动降维拆解为多模态检索维度（算法架构、数据集、气象特征等）。
2. **长上下文解析 (Long-Context RAG)**：通过向量检索与 LLM 结合，支持多篇长篇学术 PDF 的跨文档阅读与 Research Gap 提取。
3. **Actor-Critic 审查机制**：内置 Fact Checker Agent 逆向回溯引文，抑制 AI 幻觉，确保学术严谨性。
