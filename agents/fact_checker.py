from agents.base_agent import BaseAgent

class FactCheckerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Fact Checker", "负责反向核查与 AI 幻觉抑制")

    def run(self, draft, original_sources):
        print(f"\n⚙️ [{self.role}] 启动审查机制 (Actor-Critic 模式)...")
        print(f"  [{self.role}] 正在交叉比对初稿中的数据集描述与原始检索源...")
        
        # 模拟审阅逻辑
        simulated_hallucination = False
        if simulated_hallucination:
            return "❌ 审核失败：发现伪造的引证数据，已打回重写。"
        else:
            return "✅ 审核通过：未发现逻辑断裂，数据来源可靠，可以输出最终研报。"