from models.llm_handler import LLMHandler

class BaseAgent:
    def __init__(self, role, goal):
        self.role = role
        self.goal = goal
        self.llm = LLMHandler()

    def run(self, *args, **kwargs):
        raise NotImplementedError("子类必须实现 run 方法")