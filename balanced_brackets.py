# Program to find whether given input string has balanced brackets or not
def isBalanced(s):
    a=[]
    for i in range(len(s)):
        if s[i] in ['{', '[', '(']:
            a.append(s[i])
        if s[i]=='}':
            if a:
                if a[-1]=='{':
                    a.pop()
                else:
                    break
            else:
                return "NO"
        if s[i]==']':
            if a:
                if a[-1]=='[':
                    a.pop()
                else:
                    break
            else:
                return "NO"
        if s[i]==')':
            if a:
                if a[-1]=='(':
                    a.pop()
                else:
                    break
            else:
                return "NO"
    if a:
        return "NO"

    else:
        return "YES"

inp = input('Enter your query string: ')
#sample input: {)[](}]}]}))}(())(

print(isBalanced(inp))
