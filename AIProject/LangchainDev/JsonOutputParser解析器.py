from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi

model = ChatTongyi(model = "qwen3-max")

first_template =PromptTemplate.from_template(
    "我邻居姓{lastname}，生了一个{gender}，帮忙起个名字"
    "封装为json格式，key是name，value是你起的名字"
)
second_template = PromptTemplate.from_template(
    "姓名是{name}，帮我解析含义"
)
str_parser=StrOutputParser()
json_parser=JsonOutputParser()

chain = first_template | model | json_parser | second_template | model | str_parser
for chunk in chain.stream({"lastname": "王","gender": "女孩"}):
    print(chunk , end = "",flush=True)
# print(res)
# print(type(res))