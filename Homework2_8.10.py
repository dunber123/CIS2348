#Rhahan Sarwar
#CIS 2348
#1818962

str1 = input()
cha1 = str1.replace(' ', '')
low = 0
high = len(s)-1
result = True
while(low<high):
    if(str1[low]==' '):
        low+=1
    elif(str1[high]==' '):
        high-=1
    elif(str1[low]!=str1[high]):
        result = False
        break
    else:
        low+=1
        high-=1
if (result):
    print(str1,"is a palindrome")
else:
    print(str1, "is not a palindrome")
