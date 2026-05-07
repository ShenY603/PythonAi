from openai import OpenAI
from openai.resources.containers.files import content

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是一个Python编程专家，不说多余废话"},
        {"role":"assistant","content":"ok,你要问我Python的知识吗？"},
        {"role":"user","content":"输出一个爱心图案，使用Python代码"}
    ]
)
print(response.choices[0].message.content)
# print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2 + (y*0.1)**2 - 1)**3 - (x*0.05)**2 * (y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))