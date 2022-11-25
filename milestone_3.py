#%%
import random

guess = input("Enter a single letter.")

word_list = ['banana','apple','orange','melon','pear'] 

word = random.choice(word_list)



def check_guess(guess):

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} in not in the word. Try again.")

def ask_for_input():
    while True: 
        guess = input("Enter a single letter.")
        guess = guess.lower()
        if len(guess) ==1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetic character")
    check_guess(guess)

ask_for_input()



# %%
