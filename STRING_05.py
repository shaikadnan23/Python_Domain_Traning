
# a=input("enter string:")
# res=""
# for i in a:
#     if i.isalpha():
#         res=res+i
#     res=res.capitalize()
# print(res)

a = input("enter your string: ")
res = ""

for i in a:
    code = ord(i)
    if (65 <= code <= 90) or (97 <= code <= 122):   # manual isalpha check
        res += i

res = res.capitalize()
print(res)