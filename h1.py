import random
word_list = ['horse','mouse','camel']
chosen_word = random.choice(word_list)
lives = 6
display = []
for _ in range(len(chosen_word)):
    display += '_'
print(display)
end_of_game = False
stages = ['''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
 +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''

  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
 +---+
  |   |
      |
      |
      |
      |
=========''']
logo = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''
print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"you've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word.you loses a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE.")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(stages[lives])
    print(lives)
