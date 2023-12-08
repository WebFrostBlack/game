import random
from print_color import print

ascii_art = r'''
___________                      __ __________.__                 __    
\_   _____/______  ____  _______/  |\______   \  | _____    ____ |  | __
 |    __) \_  __ \/  _ \/  ___/\   __\    |  _/  | \__  \ _/ ___\|  |/ /
 |     \   |  | \(  <_> )___ \  |  | |    |   \  |__/ __ \\  \___|    < 
 \___  /   |__|   \____/____  > |__| |______  /____(____  /\___  >__|_ \
                      ________                       
                     /  _____/_____    _____   ____  
                    /   \  ___\__  \  /     \_/ __ \ 
                    \    \_\  \/ __ \|  Y Y  \  ___/ 
                     \______  (____  /__|_|  /\___ >

        This game consists in finding an equal number between 1 and 20.
            
'''

g = r'''

[--------------------(GAME)--------------------]

''' 

print(ascii_art, color='blue')

def startGame():
    def generateNumber():
        return random.randint(1, 20)

    def find():
        while True:
            try:
                chances = int(input('How many chances do you want ? '))
                break
            except ValueError:
                print("Enter a valid number !", tag='error', tag_color='red', color='white')

        number = generateNumber()
        print(g, color='yellow')
        for i in range(chances):
            while True:
                try:
                    n = int(input('What is the number ? '))
                    break
                except ValueError:
                    print("Enter a valid number !", tag='error', tag_color='red', color='white')
            remainingChances = chances - (i + 1)
            if number == n:
                print("You have found the right number.", tag='True', tag_color='green', color='white')
                return True
            else:
                print("You still have " + str(remainingChances) + " chances", tag='False', tag_color='red', color='white')
        else:
            print("Too bad... The number was", number, color='magenta')
            return False

    while True:
        if find():
            restart = input('Restart (y/n): ')
            if restart != 'y':
                print('Ok, Bye!')
                break
        else:
            restart = input('Restart (y/n): ')
            if restart != 'y':
                print('Ok, Bye!')
                break

startGame()