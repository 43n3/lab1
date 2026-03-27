'''Дано двузначное и трехзначное число. Для каждого выведите на экран сумму
и произведение цифр.'''

a = int(input()) 
b = int(input())  

a1 = a // 10
a2 = a % 10

sum_a = a1 + a2
prod_a = a1 * a2

b1 = b // 100
b2 = (b // 10) % 10
b3 = b % 10

sum_b = b1 + b2 + b3
prod_b = b1 * b2 * b3

print(sum_a, prod_a)
print(sum_b, prod_b)