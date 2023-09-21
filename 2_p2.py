
s1 = int(input('Enter Marks for Physics'))
s2 = int(input("Enter Marks for Chemistry"))
s3 = int(input("Enter Marks for Maths"))

sum = s1+s2+s3

if s3 >= 60 and s1 >= 50 and s2 >=40 and sum >=200:
    print("Eligible")
else:
    print("Not Eligible")

# if s3 >= 60:
#     if s1 >= 50:
#         if s2 >=40:
#             if sum >=200:
#                 print("Eligible")
#             else:
#                 print("Not Eligible")
#         else:
#             print("Not Eligible")
#     else:
#         print("Not Eligible")
# else:
#     print("Not Eligible")