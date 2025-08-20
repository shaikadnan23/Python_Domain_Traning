x = (input("Enter any string: "))
result1=""
for i in x:
    if i.isalpha():
        result1=result1+i
    
    result=result1.capitalize()
print(result)

# a = input("enter your string: ")
# res = ""

# for i in a:
#     code = ord(i)
#     if (65 <= code <= 90) or (97 <= code <= 122):   # manual isalpha check
#         res += i

# res = res.capitalize()
# print(res)