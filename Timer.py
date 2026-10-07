# 3분타이머 만들기
import time

def timer():
    start = time.time()
    end = start + 30
    while True:
        if time.time() >= end:
            print("3분 경과!")
            break

print("3분 타이머를 시작합니다.")
timer() 
