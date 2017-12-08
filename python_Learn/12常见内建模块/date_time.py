
from datetime import datetime

# 获取当前日期和时间
now = datetime.now() # 获取当前datetime
print(now)

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)


# datetime转换为timestamp
ti = dt.timestamp() # 把datetime转换为timestamp
print(ti)


# timestamp转换为datetime
da = datetime.fromtimestamp(ti) # 本地时间
print(da)

# timestamp也可以直接被转换到UTC标准时区的时间：

utc = datetime.utcfromtimestamp(ti) # UTC时间
print(utc)
