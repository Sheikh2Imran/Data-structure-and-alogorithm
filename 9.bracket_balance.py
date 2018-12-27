'''
Name : Parentheses, curly braces, square brackets balanced check using python's list   
Author,
Md Imran Sheikh
Dept. of CSE, JUST
'''

def is_balanced(str):
    s = list()
    for ch in str:
        if ch == "(":
            s.append(ch)
        if ch == ")":
            if not s:
                return False
            s.pop()

        if ch == "{":
            s.append(ch)
        if ch == "}":
            if not s:
                return False
            s.pop()
            
        if ch == "[":
            s.append(ch)
        if ch == "]":
            if not s:
                return False
            s.pop()
    return not s

if __name__=="__main__":
    str = "{()}]"
    print(is_balanced(str))