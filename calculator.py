# 사칙연산 계산기 만들기
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def calculator():
    while True:
        print("1. 더하기")
        print("2. 빼기")
        print("3. 곱하기")
        print("4. 나누기")
        print("5. 종료")
        choice = int(input("선택: "))
        if choice == 5:
            break
        num1 = int(input("첫 번째 숫자: "))
        num2 = int(input("두 번째 숫자: "))
        if choice == 1:
            print(add(num1, num2))
        elif choice == 2:
            print(sub(num1, num2))
        elif choice == 3:
            print(mul(num1, num2))
        elif choice == 4:
            print(div(num1, num2))
    
    
calculator()        
