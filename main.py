import random
from functions import *

word_list = ['каша']
print('Давайте играть в угадайку слов!')
word = get_word(word_list)
word_completion = '_' * len(word)
print(word_completion)
while True:

    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    user_input = input('Назовите букву: ')

    if user_input in word:
        guessed_letters.append(user_input)
        count = 0
        word_temp = word
        while count != word.count(user_input):
            index = word_temp.find(user_input)
            word_completion = word_completion[:index] + user_input + word_completion[index + 1:]
            word_temp = word_temp[index:]
            count += 1
        print(word_completion)  # строка, содержащая символы _ на каждую букву задуманного слова
        print(display_hangman(tries))
        count -= count
    else:
        tries -= 1

