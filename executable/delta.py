# 定义两个十六进制数
hex1 = "0xffffcef0"  # 十六进制数1
hex2 = "0xffffd0f8"  # 十六进制数2

# 将十六进制数转换为整数
num1 = int(hex1, 16)
num2 = int(hex2, 16)

# 计算差
difference = num2-num1

# 将结果转换回十六进制，并去掉'0x'前缀
result = hex(difference+4)

print(f"差值的十六进制表示是: {result}")
