import re


def fun(s):
    try:
        username, extension = s.split('.')

    except:
        return False

    if 'rase23@ha_ch' in username:
        return False

    elif len(extension) > 3:
        return False

    else:

        appearencec_want = 1
        appearencec = 0
        for i in username:
            if i is '@':
                appearencec += 1
            else:
                pass
        if appearencec != appearencec_want:

            return False

        else:
            pattern = r'[a-z]+[-_]*[a-z]*[0-9]*[-_]*@[a-z]+[0-9]*.[a-z]+'
            return bool(re.search(pattern, s))


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
# N = int(input())
# l = []
# for i in range(N):
#     a = raw_input()
#     matchObj = re.search("^[a-zA-Z0-9_-]+\@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$", a)
#     if matchObj:
#         l.append(a)
# l.sort()
# print l
