import sys

from langchain_ollama import OllamaLLM
#本地ollma模型
model = OllamaLLM(model = "qwen3.5:4b")

a=input()
res = model.stream(a)
for i in res:
    print(i,end="",flush=True)
