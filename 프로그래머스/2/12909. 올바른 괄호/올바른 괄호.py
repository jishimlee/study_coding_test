def solution(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack.pop() != '(':
                return False

    return len(stack) == 0
