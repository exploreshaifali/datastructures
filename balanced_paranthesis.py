def balanced_paranthesis(exp):
    """Return True if exp has balanced parantheses, else False."""
    pair = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i in exp:
        if i in pair.values():
            stack.append(i)
        elif i in pair.keys():
            if stack.pop() != pair[i]:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
