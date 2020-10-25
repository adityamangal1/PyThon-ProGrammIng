user = input()
upercase = []
lowercase = []
odd = []
even = []
for i in user:
    if i.isupper():
        upercase.append(i)
    elif i.islower():
        lowercase.append(i)
    if i.isnumeric():
        if int(i) % 2 != 0:
            odd.append(i)
        else:
            even.append(i)
    else:
        continue

upper = ''.join(sorted(upercase))
lower = ''.join(sorted(lowercase))
odd = ''.join(sorted(odd))
even = ''.join(sorted(even))

print(lower + upper + odd + even)
