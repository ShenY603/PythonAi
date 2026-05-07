from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model = "qwen3-max")
# prompt = PromptTemplate.from_template(
#     "根据历史会话回应用户问题。对话历史：{chat_history}，用户提问：{input}，请回答"
# )
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","根据历史会话回应用户问题。对话历史："),
        MessagesPlaceholder("chat_history"),
        ("human","请回答如下问题：{input}")
    ]
)
def print_prompt(prompt):
    print("="*10,prompt.to_string(),"="*10)
    return prompt
str_parser = StrOutputParser()

base_chain = prompt |print_prompt| model | str_parser


store = {}#sessonid 是key，value就是历史会话
#函数实现
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

#创建一个新的链，对原有链增强，自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain,             #被增强的原有chain
    get_history,            #通过会话id获取InMemoryChatMessageHistory类对象
    input_messages_key="input",
    history_messages_key="chat_history",  # 注意：是 history_messages_key（messages 复数）
)

if __name__ == '__main__':
    # 固定格式，添加langchain的配置，为当前程序配置所属的session_id
    session_config = {
        "configurable":{
            "session_id":"user001"
        }
    }
    res = conversation_chain.invoke({"input":"小明有2只狗"},session_config)
    print("第一次执行：",res)
    res = conversation_chain.invoke({"input": "小刚有1只猫"}, session_config)
    print("第二次执行：", res)
    res = conversation_chain.invoke({"input": "总共有几只宠物"}, session_config)
    print("第三次执行：", res)






