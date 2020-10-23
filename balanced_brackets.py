# Program to find whether given input string has balanced brackets or not
def isBalanced(s):
    a=[]
    for i in range(len(s)):
        if s[i]=='{' or s[i]=='[' or s[i]=='(':
            a.append(s[i])
        if s[i]=='}':
            if len(a)==0:
                return "NO"
            else:
                if a[-1]=='{':
                    a.pop()
                else:
                    break
        if s[i]==']':
            if len(a)==0:
                return "NO"
            else:
                if a[-1]=='[':
                    a.pop()
                else:
                    break
        if s[i]==')':
            if len(a)==0:
                return "NO"
            else:
                if a[-1]=='(':
                    a.pop()
                else:
                    break
    if len(a)==0:
        return "YES"
    else:
        return "NO"

inp = input('Enter your query string: ')
#sample input: {)[](}]}]}))}(())(

print(isBalanced(inp))
