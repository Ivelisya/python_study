from Crypto.Cipher import AES,DES,DES3
from Crypto.Util.Padding import pad,unpad
import base64
import binascii
# binascii.a2b_hex把16进制转换成字节
# binascii.b2a_hex把字节转换成16进制
# mode_ecb 不需要iv
# mode_cbc  需要iv
s = 'pccWLqvFIfcnuAp4RHu+5Q=='
aes = AES.new(key=b'abcdefgh12345678',mode=AES.MODE_CBC,IV=b'12345678abcdefgh')
#只能解密字节
# 加密
# 16进制不可能有超过f的数字
r = unpad(aes.decrypt(base64.b64decode(s)),16)
print(r.decode())
# 2.加密一段数据试试
# s = 'hello world'
# 3.数据长度必须是16的倍数
# bs = s.encode('utf-8')
# bs = pad(bs, 16)#aes大多数是16位
# result = aes.encrypt(bs)
# print(result)#加密后的是杂乱无章的字节
# 需要对字节进行base64处理
# ss = base64.b64encode(result).decode()
# aes = AES.new
print(s.__len__())
# 解密