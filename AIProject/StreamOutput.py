from openai import OpenAI
from openai.resources.containers.files import content

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是一个Python编程专家"},
        {"role":"assistant","content":"ok,你要问我Python的知识吗？"},
        {"role":"user","content":"输出1到10的数字，使用Python代码"}
    ],
    stream = True
)
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=" ", #每一段之间以空格分隔
        flush=True
    )