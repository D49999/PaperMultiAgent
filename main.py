from agents.researcher import ResearcherAgent
from agents.literature_analyst import LiteratureAnalystAgent
from agents.drafter import DrafterAgent
from agents.fact_checker import FactCheckerAgent

def run_paper_pipeline(topic):
    print(f"========== 🚀 启动学术论文 Multi-Agent 自动化流 ==========")
    print(f"📝 目标课题: {topic}\n")

    # 阶段 1: 规划与检索
    researcher = ResearcherAgent()
    papers = researcher.run(topic)

    # 阶段 2: RAG 与长篇文献精读 (重度 Token 消耗区)
    analyst = LiteratureAnalystAgent()
    gap_analysis = analyst.run(papers)

    # 阶段 3: 学术撰写
    drafter = DrafterAgent()
    draft = drafter.run(gap_analysis, outline="Standard Academic Structure")

    # 阶段 4: 事实核查与反馈闭环
    checker = FactCheckerAgent()
    final_status = checker.run(draft, papers)

    print(f"\n========== 🏁 工作流结束: {final_status} ==========")

if __name__ == "__main__":
    # 使用极具学术深度的真实课题进行压测展示
    target_topic = "Improved HRNet (ACHRNet) for UAV-based Segmentation of Lychee Buds and Full-bloom Flowers with Yield Prediction Application"
    run_paper_pipeline(target_topic)