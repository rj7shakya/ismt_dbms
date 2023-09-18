
str = 'madamr'
str_len = len(str)
flag = 0

for i in range(0,str_len):
    if str[i] != str[str_len-i-1]:
        flag =0
        break
    else:
        flag =1
    
if flag == 1:
    print('palindrome')
else:
    print('not palindrome')