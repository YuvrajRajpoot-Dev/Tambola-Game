import random #module used for generating random number

Tambola_list = [] # initilize list to append generated number
temp = input('Welcome to Tambola! Press y to start Game...: ').lower()

while temp == 'y':
    n = random.randint(1,10) # random no. generate between 1 to 10, you can increase limit
    if n not in Tambola_list: # checking n is present in list or not
        Tambola_list.append(n) # appending no. to list
        print('Tambola Number is :',n)
        temp = input('To Pickup Number press y : ') # taking input from users
    if len(Tambola_list) == 10:
        # Tambola_list.sort()
        print(Tambola_list)
        temp = 'n'
if temp != 'y': 
    print('OOPS ! You have entered wrong key')
if temp == 'n': 
    print('Thankyou !')
