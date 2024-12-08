from Crypto.Cipher import AES,DES,DES3
from Crypto.Util.Padding import pad,unpad
des = DES.new(key=b'abcdefgh',mode=DES.MODE_CBC,IV=b'12345678')
#
# s = pad('你好'.encode('utf-8'),8)
# bs = des.encrypt(s)
# print(bs)
mi = b'$iL\xb2\x1c\xa3\xb0s'
# s = des.decrypt(mi)
s = unpad(des.decrypt(mi),8)
print(s.decode('utf-8'))