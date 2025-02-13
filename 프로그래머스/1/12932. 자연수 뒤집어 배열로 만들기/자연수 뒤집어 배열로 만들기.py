#2번문제 (인터넷 참고)

def solution(n):
    answer= list(str(n))
    answer.reverse()

    return list(map(int,answer))