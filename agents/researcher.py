from agents.base_agent import BaseAgent
from tools.academic_search import AcademicSearchTool

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher", "负责课题拆解、多维度检索规划")
        self.search_tool = AcademicSearchTool()

    def run(self, topic):
        print(f"\n⚙️ [{self.role}] 开始长链推理，拆解课题: {topic}")
        # 模拟思维链（CoT）推理过程
        print(f"  [{self.role}] 推理步骤1: 拆解算法维度 (e.g., HRNet, AFEM, CSAM)")
        print(f"  [{self.role}] 推理步骤2: 拆解数据维度 (e.g., UAV multi-view, ERA5 variables)")
        print(f"  [{self.role}] 推理步骤3: 拆解应用维度 (e.g., yield prediction, phenotyping)")
        
        search_results = self.search_tool.search(topic)
        return search_results