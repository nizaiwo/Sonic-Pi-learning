# 使用F5进行REPL编译
# a=input()
# print(a)

# 也可以直接在代码进行修改来输入
import re

# 输入MIDI数字转音符
def num2cde(a):
    b=int(a)//12 -1
    c=int(a)%12
    d=['c','db','d','eb','e','f','gb','g','ab','a','bb','b']# s OR b
    y=':'+d[c]+str(b)
    return y

# 输入音符转MIDI数字
# a=input()
a=':c4'
def cde2num(a):
    b=int(re.sub('[a-zA-Z:]',"",a))
    c=re.sub('[0-9:]',"",a)
    d=['c','db','d','eb','e','f','gb','g','ab','a','bb','b']# s OR b
    # print(b,'+',c)
    y=0
    for i,di in enumerate(d):
        if di==c:
            y=(b+1)*12+i
            break
    return y

def main():
    num=60
    print(num2cde(num))
    cde=':c4'
    print(cde2num(cde))
