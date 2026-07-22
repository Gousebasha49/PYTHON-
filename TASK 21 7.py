1. # Count of Passed Students

n = int(input("Enter number of students: "))
count = 0
for i in range(1,n+1):
    marks = int(input("Enter marks: "))
    if marks >= 35:
        count += 1
print(count)


# 2. Shop Profit Days

n = int(input("Enter days: "))
count = 0
for i in range(1,n+1):
    profit = int(input("Enter profit: "))
    if profit > 1000:
        count += 1
print(count)


# 3. Largest Multiple of 5

n = int(input("Enter number of values: "))
largest = 0
for i in range(1,n+1):
    num = int(input("Enter number: "))
    if num % 5 == 0:
        if num > largest:
            largest = num
print(largest)


# 4. Average of Even Numbers

n = int(input("\nEnter number of values: "))
tot = 0
cou = 0
for i in range(1,n+1):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        tot += num
        cou += 1
if cou == 0:
    print("No Even Numbers")
else:
    avg=tot/cou
    print(avg)

# 5. Student Improvement

n = int(input("Enter number of tests: "))
prev = int(input("Enter marks: "))
count = 0
for i in range(1, n+1):
    marks = int(input("Enter marks: "))
    if marks > prev:
        count += 1
    prev = marks
print(count)


# 6. Divisors Count

n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print(count)


# 7. Smallest Odd Number

n = int(input("Enter number of values: "))
small = 99
for i in range(n):
    num = int(input("Enter number: "))
    if num % 2 != 0:
        if num < small:
            small = num
if small == 0:
    print("No Odd Number")
else:
    print(small)


# 8. Count Numbers Ending with 7

n = int(input("Enter number of values: "))
count = 0
for i in range(1,n+1):
    num = int(input("Enter number: "))
    if num % 10 == 7:
        count += 1
print(count)


# 9. Multiplication Table (1 to 15)

num = int(input("Enter a number: "))
for i in range(1, 16):
    print(f"{num} X {i} =",  num * i)


# 10. Sum Until Negative Number

total = 0
num = int(input("Enter a number: "))
while num >= 0:
    total += num
    num = int(input("Enter a number: "))
print(total)