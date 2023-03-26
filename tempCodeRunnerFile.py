import random
word_list = ["apple", "banana", "orange", "grape", "watermelon"]
word = random.choice(word_list)
hidden_word = ["_"] * len(word)
incorrect_guesses = []
max_guesses = 6
while "_" in hidden_word and len(incorrect_guesses) < max_guesses:
    print(" ".join(hidden_word))
    print("Incorrect guesses: " + " ".join(incorrect_guesses))
    guess = input("Guess a letter: ")
    if guess in word:
        
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        
        incorrect_guesses.append(guess)
if "_" not in hidden_word:
    print("Congratulations, you won!")
else:
    print("Sorry, you lost. The word was " + word + ".")