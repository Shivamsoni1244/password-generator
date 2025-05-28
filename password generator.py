import random
print("////WELCOME TO PASSWORD GENERATOR////")
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '?']

num_of_letters=int(input("enter number of letters: "))
num_of_digits=int(input("enter number of digits: "))
num_of_symbols=int(input("enter number of symbols: "))

password_list=[]
for number in range(0,num_of_letters):
    password_list+=random.choice(letters)
   

for number in range(0,num_of_digits):
    password_list+=random.choice(digits)
   
for number in range(0,num_of_symbols):
    password_list+=random.choice(symbols)

random.shuffle(password_list)
    
for password in password_list:
    print(password,end='')
