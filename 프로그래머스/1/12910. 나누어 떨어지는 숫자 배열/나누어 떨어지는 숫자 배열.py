#3번문제
num = []
cnt = 0

def solution(arr, divisor):
    for i in arr:
        if i % divisor == 0:
            num.append(i)
    if len(num)==0:
        num.append(-1)
    return sorted(num)