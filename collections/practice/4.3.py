from collections import deque


def brackets(line:str) -> bool:
    
    dq_line = deque(line)
    true_brackets = "()"
    result = False
    
    if len(dq_line) % 2 != 0:
        return result
    elif line == '':
        result = True
        return result
    else:
        while len(dq_line) != 0:
            
            left = dq_line.popleft()
            right = dq_line.pop()
            
            if left + right == true_brackets:
                result = True
            elif right + left  == true_brackets\
                and len(dq_line) != len(line) - 2:
                result = True
            else:
                return False
                
    return result

print(brackets("()"))