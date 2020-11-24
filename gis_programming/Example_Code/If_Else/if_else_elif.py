# 2. if,elif,else example
magic_number = 12     
user_input = int(input('Guess the magic number:  '))   
if user_input > magic_number:
    print('its greater than the magic number')
elif user_input < magic_number: 
    print('its less than the magic number')
else:
    print('Congratulations, you got it!')
