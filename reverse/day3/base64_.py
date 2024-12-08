'''
被加密解密的一般是字节，要转换成字符串进行传输，需要用到base64模块

把字节转换成字符串
'''
import base64
s = '我爱你222hdh'
bs = s.encode('utf-8')
print(bs)
# 将字节编码成base64字符串
# ==表示填充
b64bs = base64.b64encode(bs)
print(b64bs.decode('utf-8'))
