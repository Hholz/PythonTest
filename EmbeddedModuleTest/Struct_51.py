'''struct'''
import struct
# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换

# struct的pack函数把任意数据类型变成bytes：
# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print(struct.pack('>I', 10240099))

# unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))