#正则表达式
import re
s='a b   c'
print(s.split(' '))
print(re.split(r'\s+',s))
print(re.split(r'[\s\,]+','a,b, c  d'))
print(re.split(r'[\s\,\;]+','a,b, c ; d'))


#练习1   someone@gmail.com
reEmail=re.compile(r'^[\w\.]+\@[\w]+(\.[\w]+)*\.[\w]{2,6}')
def is_valid_email(addr):
    if reEmail.match(addr):
        return True
    else:
        return False
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

#练习2 可以提取出带名字的Email地址, <Tom Paris> tom@voyager.org => Tom Paris   bob@example.com => bob
reEmail=re.compile(r'^\<*([\w\s]+)\>*([\w\s]*)\@([\w]+)(\.[\w]+)?\.([\w]{2,6})$')
def name_of_email(addr):
    return reEmail.match(addr).group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

