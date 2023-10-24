from one import one
from two import two

# 调用初始化文件内的对象
# import __init__ as init

print("hello setuptools")
O = one.One()
O.run()

T = two.Two()
T.run()
