from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models import ChatTongyi

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人可以作诗"),
        MessagesPlaceholder("history"),
        ("human","再来一首诗")
    ]
)
history_data=[

    ("human","写一首唐诗"),
    ("ai","床前明月光，疑是地上光，举头望明月，低头思故乡"),
    ("human","好诗再来一首")
]
model = ChatTongyi(model = "qwen3-max")
chain = chat_prompt | model
# res = chain.invoke({"history":history_data})
# print(res.content)
for chunk in chain.stream({"history":history_data}):
    print(chunk.content,end="",flush=True)