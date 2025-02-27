from queue import Queue

def solution(progresses, speeds):
    n = len(progresses)
    q = Queue()
    answer = []
    for i in range(n):
        r = (100-progresses[i])/speeds[i]
        if (100-progresses[i]) % speeds[i] != 0:
            r = int(r) + 1
        else :
            r = int(r)
        q.put(r)
        
    while not q.empty():
        sum = q.get()
        count = 1
        while not q.empty() and q.queue[0] <= sum:
            q.get()
            count+=1
        answer.append(count)
        
    return answer
            