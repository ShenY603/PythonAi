from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = ChatTongyi(model="qwen3-max")

s =str(input())

messages=[
    ("system","你是一个爱情诗人"),
    ("ai","你已经离开爱人很久,处于异地恋，但即将见面"),
    ("human",s)
    # SystemMessage(content="你是一个爱情诗人"),
    # AIMessage(content="你已经离开爱人很久,处于异地恋，但即将见面"),
    # HumanMessage(content=s)

]
res = model.stream(messages)
print(s)
for i in res:
    print(i.content,end="",flush=True)