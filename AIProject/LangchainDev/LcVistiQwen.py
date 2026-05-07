from langchain_community.llms.tongyi import Tongyi
#阿里云云上模型
model = Tongyi(model="qwen-max")
a=input()
res = model.invoke(a)
print(res)