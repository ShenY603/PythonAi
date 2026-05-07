
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template = PromptTemplate.from_template(
    "我的老婆叫{wifename},我叫{husbandname},我们生了一个{gender}，帮我们起个名字"
)
model = Tongyi(model = "qwen-max")
chain = prompt_template|model

#从命令行输入（可选，取消注释即可使用）
w, h, g = input("请输入（空格分隔）：").split()
res = chain.invoke(input={"wifename": w, "husbandname": h, "gender": g})

# res = chain.invoke(input={"wifename":"温言","husbandname":"南冥","gender":"女孩"})
print(res)