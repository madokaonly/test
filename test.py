from datetime import datetime

# 获取当前时间
now = datetime.now()

# 格式化输出
print("当前时间：", now.strftime("%Y-%m-%d %H:%M:%S"))