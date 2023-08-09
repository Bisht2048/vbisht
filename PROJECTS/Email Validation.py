import string

alpha=string.ascii_letters
num=string.digits
symbols=['@','.']
# print("num= ",num)
# print("alpha= ",alpha)
# print("symbols= ",symbols)
# a=input("Enter your email address here: ")
a="bisht.vaibhav@gmail.com"
# a=".@"
for i in a:
    if i in alpha or i in num or i in symbols:
        g="valid email"
        continue
    else:
        g="invalid Email Address"
        break

print(g)

# for i in a:
#     if i in alpha:
#         continue
#         print("y")
#
#     else:
#         print("n")

