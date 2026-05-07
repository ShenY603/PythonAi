from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import JsonOutputParser

model = ChatTongyi(model = "qwen3-max")
str_parser=StrOutputParser()

my_func = RunnableLambda(lambda ai_meg: {"name":ai_meg.content})
first_template =PromptTemplate.from_template(
    "我邻居姓{lastname}，生了一个{gender}，帮忙起个名字"
)
second_template = PromptTemplate.from_template(
    "姓名是{name}，帮我解析含义"
)



chain = first_template | model | my_func | second_template | model | str_parser
for chunk in chain.stream({"lastname": "王","gender": "女孩"}):
    print(chunk , end = "",flush=True)