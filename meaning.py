import nltk

nltk.download("wordnet")
from nltk.corpus import wordnet

user_word = input("Enter your word ")
syns = wordnet.synsets(user_word)

print("******************")
print(len(syns))
word_list = [syns[i] for i, element in enumerate(syns)]

print(word_list)
for i, word  in enumerate(word_list, start=1):
    print(f"{i} - definition:  {word.definition()}")
    if len(word.examples()) != 0:
        print(f"example: {', '.join(word.examples())}")