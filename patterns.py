def func(length):
    
    for i in range(1,length+1):
        print('* '*i)
    print()
    for i in range(1,length+1):
        for j in range(1,length+1):
            number=length+1-i
            if j<=number:
                print('* ',end='')
            else:
                print(' ',end='')
        print()

length=int(input("Enter the length of  tringle:"))
func(length)