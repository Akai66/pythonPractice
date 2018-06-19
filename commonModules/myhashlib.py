#摘要算法
import hashlib,random,hmac
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def calc_md5(password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def login(user,password):
    if user in db:
        if db[user] == calc_md5(password):
            return True
    return False
#测试
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


#升级版,注册和登录
#模拟数据库数据
data={}
class User(object):
    def __init__(self,name,password):
        self.name=name
        self.__salt=''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.__password=hmac_md5(self.__salt,password)

    @property
    def password(self):
        return self.__password

    @property
    def salt(self):
        return self.__salt

def hmac_md5(key,str):
    return hmac.new(key.encode('utf-8'),str.encode('utf-8'),'MD5').hexdigest()

def register(username, password):
    newUser=User(username,password)
    data[newUser.name]=newUser

def login(username, password):
    if username in data:
        if hmac_md5(data[username].salt,password)==data[username].password:
            return True
    return False

register('michael','123456')
register('bob','123456')
register('alice','123456')

assert login('michael', '123456')
assert login('bob', '123456')
assert login('alice', '123456')
assert not login('michael', 'lalalal')
assert not login('bob', 'lalalal')
assert not login('alice', 'lalalal')
print('ok')




