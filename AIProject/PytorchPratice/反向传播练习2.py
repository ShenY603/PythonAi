import torch
# y_hat = w1 * x^2 + w2 * x + b
# loss = (y_hat - y)^2
# 示例真值：y = 1*x^2 + 2*x + 1（可用训练学出 w1≈1, w2≈2, b≈1）
x_data = [1.0, 2.0, 3.0]
y_data = [4.0, 9.0, 16.0]

w1 = torch.Tensor([0.5])
w2 = torch.Tensor([0.5])
b = torch.Tensor([0.5])
w1.requires_grad = True
w2.requires_grad = True
b.requires_grad = True


def forward(x):
    return w1 * (x**2) + w2 * x + b


def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) ** 2


print("predict (before training)", 4, forward(4).item())

for epoch in range(10000):
    for x, y in zip(x_data, y_data):
        l = loss(x, y)
        l.backward()
        print("\tgrad:", x, y, w1.grad.item(), w2.grad.item(), b.grad.item())
        w1.data = w1.data - 0.01 * w1.grad.data
        w2.data = w2.data - 0.01 * w2.grad.data
        b.data = b.data - 0.01 * b.grad.data
        w1.grad.data.zero_()
        w2.grad.data.zero_()
        b.grad.data.zero_()
    print("轮次:", epoch, "损失:", l.item())
print("predict (after training)", 4, forward(4).item())
