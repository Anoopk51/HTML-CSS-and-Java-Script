number=int(input("Enter the number:"))
prime=True
for i in range(2,number):
    if number%i==0:
        prime=False
print(f"{number} is prime number .",prime)