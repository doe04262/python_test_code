# open('02_program/test.txt', 'w')
# f.write(input('저장할 내용 >>> '))
# fwritelines(['\n파이썬\n', '프로그래밍'])
# f.close()

f = open('02_program/test.txt', 'r')
print(f.read())
print('-'*40)
f.close()
f = open('02_program/test.txt', 'r')
while True:
    line = f.readline()
    if not line: 
        break
    print(line, end='')
f.close()
print('-'*40)
f = open ('02_program/test.txt', 'r')
print(f.readlines())
f.close()

#pickle
import pickle
f = open('02_program/pickledata.txt', 'wb')
data = {1:['홍길동'],2:{'name':안정희}}
pickle.dump(data, f)
f.close()

f = open('02_program/pickledata.txt', 'rb')
dd = pickle.load(f)
f.close()
print(dd)
print(type(dd))