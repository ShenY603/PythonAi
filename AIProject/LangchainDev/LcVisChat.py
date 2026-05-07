from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = ChatTongyi(model="qwen3-max")

s =str(input())

messages=[
    SystemMessage(content="你是一个爱情诗人"),
    AIMessage(content=""),
    HumanMessage(content=s)

]
res = model.stream(messages)
for i in res:
    print(i.content,end="",flush=True)