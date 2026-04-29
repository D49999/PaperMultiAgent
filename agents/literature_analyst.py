from agents.base_agent import BaseAgent
from tools.vector_store import VectorStoreManager
from config import Config

class LiteratureAnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__("Literature Analyst", "负责大规模文献阅读与 Research Gap 提取")
        self.db = VectorStoreManager(Config.DB_PATH)

    def run(self, search_results):
        print(f"\n⚙️ [{self.role}] 启动多文档交叉验证工作流...")
        self.db.add_documents(search_results)
        
        # 强调这里消耗大量上下文
        prompt = "基于 RAG 检索到的全文数据，对比现有..."
        print(f"  [{self.role}] 向 LLM 发送超级长文本 prompt 进行逻辑推理...")
        analysis = self.llm.call_llm(prompt)
        return "提取完毕：。"