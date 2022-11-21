s1=input()
s2=input()
def sreverse(s2):
    str = ""
    for i in s2:
        str = i + str
    return str
s3=sreverse(s2)
count = 0
for i in s1:
    if i == s3[0]:
        count = count + 1
print(count)
