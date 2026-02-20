a=int(input())
b=int(input())

a1=a//10
a2=a%10

b3=b%10
b1=b//100
b2=(b//10)%10

print(a1+a2, a1*a2)
print(b1+b2+b3, b1*b2*b3)