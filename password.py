import random

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nums = [1,2,3,4,5,6,7,8,9,0]
sybs = ['#','!','@','&','*','%']

def password(name):
    print(f'Hey! Hi {name}, hope you are having an amazing day!\n1. Random Strong Password Generator.\n2. Password Strength Checker.')
    choice = input('Enter your choice (1/2): ')
    if (choice == '1'):
        password_generator()
    elif(choice == '2'):
        password_strength()
    else:
        print(f'The choice {choice} is an invalid choice.')

def password_generator():
    count1 = 5
    first = ''
    for _ in range(count1):
        first += random.choice(alpha)
    f = first

    count2 = 2
    mid = ''
    for _ in range(count2):
        mid += random.choice(sybs)
    m = mid

    count3 = 4
    last = ''
    for _ in range(count3):
        last += str(random.choice(nums))
    l = last

    print(f'Hey! {name}, here is your password: {f+m+l}')

def password_strength():
    print('Note: A good password must contain 10 characters: with 2 symbols and 4 numbers')
    password = input('Enter the password to check the strength: ')
    nums_count = 0
    sybs_count = 0 
    strg_count = 0
    for char in password:
        if char.isdigit():
            nums_count += 1
        elif char in sybs:
            sybs_count += 1
        else:
            strg_count += 1
    
    s = strg_count
    sy = sybs_count
    nu = nums_count
    if ((s >= 4) and (sy >= 2) and (nu >= 4)):
        print(f'The password {password} is VERY STRONG.')
    elif ((s >= 4) and (sy >= 2) and (nu <= 4)):
        print(f'The password {password} is STRONG.')
    elif ((s <= 4) and (sy >= 2) and (nu >= 4)):
        print(f'The password {password} is MEDIUM.')
    elif ((s >= 4) and (sy <= 2) and (nu >= 4)):
        print(f'The password {password} is WEAK.')
    else:
        print(f'The password {password} is VERY WEAK.')

name = input('Enter your name: ')
password(name)

while True:
    check = input('Do you wanna use this again? (Yes/No): ').lower()
    if (check == 'yes'):
        password(name)
    elif (check == 'no'):
        print('Thanks for using this! Have a Great Day!')
        break
