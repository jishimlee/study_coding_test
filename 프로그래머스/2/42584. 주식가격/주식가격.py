def solution(prices):
    myStack = []
    n = len(prices)
    ans = [0] * n  
    
    for i in range(n):
        while myStack and prices[myStack[-1]] > prices[i]:
            index = myStack.pop()
            ans[index] = i - index
        
        myStack.append(i)
    
    while myStack:
        index = myStack.pop()
        ans[index] = n - index - 1
    
    return ans
