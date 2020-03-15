import nltk 
import random

nltk.download("words")
from nltk.corpus import words
# print(len(words.words()))

new_dict = []
new_dict = [word for word in words.words() if len(word) >= 3 and len(word) <= 5 and word[0].islower()]

# print(len(new_dict))

answer = random.randint(0, len(new_dict))
answer_index = new_dict[answer]
print(answer_index, answer)

while True:
    guess_word = input("Enter your word (at least 3 letters, no more than 5): ")
    
    if guess_word not in new_dict:
        print("Your word is not in the dictionary. Try again.")
    else:
        index = new_dict.index(guess_word)
        if guess_word == answer_index:
            print(f"You are right! The answer is {guess_word}.")
            break
        elif answer > index:
            print(f"Your word {guess_word} is ealier in the dictionary than our word.")
        elif answer < index:
            print(f"Your word {guess_word} is later in the dictionary than our word.")



