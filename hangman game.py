print('''                                                                            
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
             ''')


word_list = ["ardvard", "baboon", "camel", "start"]
import random

stages = [ '''

      _______
     |      |
     |      (_)
     |      \|/
     |       |
     |      / \.
     |
    _|___
    
    
    ''',
    '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
    
    ''',
    '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
    
    ''',
    '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |  
     |
    _|___
    ''',
 
    '''
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    _|___

  ''',
 '''
      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___
 
 ''',
 '''
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___'''
 ]

chosen_word = random.choice(word_list)

life = 6

print(f"the solution is {chosen_word}")

display=[]


word_length = len(chosen_word)
for letter in range(word_length):
    display+="_"
print((display))

end_of_game = False

while not end_of_game :
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
    if guess not in chosen_word:

        life -=1
    if life == 0:
        end_of_game = True
        print("You Lose")

    if "_" not in display:
        end_of_game=True
        print("You win")
    print(stages[life])