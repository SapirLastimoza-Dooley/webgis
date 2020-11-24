# # 3. if else within while loop, give reminders to guess magic number
magic_number = 12     
user_input = int(input('Guess the magic number:  ')) 

while user_input != magic_number:
    if user_input > magic_number:
        print('its greater than the magic number')
    else: 
        print('its less than the magic number')
    user_input = int(input('Guess the magic number:  ')) 

print('Congratulations, you got it!')