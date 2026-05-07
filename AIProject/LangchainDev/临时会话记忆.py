from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model = "qwen3-max")
prompt = PromptTemplate.from_template(
    "根据历史会话回应用户问题。对话历史：{chat_history}，用户提问：{input}，请回答"
)
str_parser = StrOutputParser()

base_chain = prompt | model | str_parser

#创建一个新的链，对原有链增强，自动附加历史消息
RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_message_key="chat_history"
)

