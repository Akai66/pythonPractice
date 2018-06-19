#练习
import base64
def safe_base64_decode(s):
    count=4-len(s)%4
    while count>0 and count!=4:
        if isinstance(s,bytes):
            s+=b'='
        elif isinstance(s,str):
            s+='='
        count-=1
    return base64.urlsafe_b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')