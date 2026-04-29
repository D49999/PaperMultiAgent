from agents.base_agent import BaseAgent
from config import Config

class DrafterAgent(BaseAgent):
    def __init__(self):
        super().__init__("Drafter", "负责遵循学术规范的初稿撰写")

    def run(self, research_gap, outline):
        print(f"\n⚙️ [{self.role}] 根据 {Config.TARGET_JOURNAL} 期刊标准撰写初稿...")
        prompt = f"基于设定的研究空白：{research_gap}，请严谨地撰写 Introduction 和 Related Work 章节，并自动生成 LaTeX 格式的伪代码和图表占位符。"
        draft = self.llm.call_llm(prompt)
        return "生成了包含学术化表述和格式规范的初稿 v1.0"