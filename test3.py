def printInfo():
    print("수식을 입력하세요. 종료하려면 '0'을 입력해 주세요.")

def exitSequence(cal):
    if cal == '0' :
        exit()

def splitDigit(cal):
    for i,char in enumerate(cal):
        if not char.isdigit():
        # isdigit() 메소드는 이런식으로 구현되어있음
        # 48<= character <=57
            return int(cal[:i]),int(cal[i+1:]),cal[i]

def calculation(a,b,c):
    if c == '+' :
        result = add(a,b)
    elif c == '-' :
        result = sub(a,b)
    elif c == '*' :
        result = mul(a*b)
    elif c =='/' :
        result = div(a/b)
    return result

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def main():
    while True :
        printInfo()
        cal = input()
        exitSequence(cal)
        a,b,c=splitDigit(cal)
        result = calculation(a,b,c)
        print(a,c,b,'=',result)

if __name__ == "__main__":
    main()
