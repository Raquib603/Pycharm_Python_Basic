mark = int(input("Enter your exam number : "))

if 0 <= mark <= 100:
    if mark <= 33:
        print("You are fail, got less than 33% number")

    elif 33 <= mark <= 70:
        print("You got C")

    elif 70 <= mark <= 80:
        print('You got B')
    else:
        print('You got A')

else:
    print("Enter the right number you got")
