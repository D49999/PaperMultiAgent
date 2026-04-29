from config import Config

class LLMHandler:
    def __init__(self, model_name=Config.MODEL_NAME):
        self.model_name = model_name

    def call_llm(self, prompt, context="", role_system="You are an expert academic researcher."):

        estimated_tokens = len(prompt) + len(context)
        print(f"  [LLM Request] Model: {self.model_name} | Estimated Context Tokens: {estimated_tokens}")
        return f"[模拟 {self.model_name} 的学术级回复...]"