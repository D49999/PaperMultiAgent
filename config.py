import os

class Config:
    MODEL_NAME = "gpt-4-turbo" 
    TEMPERATURE = 0.2 # 学术任务需要较低的温度以保证严谨性
    MAX_TOKENS = 8192
    DB_PATH = "./vector_db"
    TARGET_JOURNAL = "Computers and Electronics in Agriculture (COMPAG)" # 目标一区期刊标准