from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatTongyi(model = "qwen3-max")
parser=StrOutputParser()
prompt = PromptTemplate.from_template(
    "我邻居姓{lastname},刚生了{gender},帮他起个名字"
)

chain = prompt | model | parser | model

res = chain.invoke({"lastname":"林","gender":"女儿"})
print(res.content)