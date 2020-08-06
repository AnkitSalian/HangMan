'''
Project 2
Hangman
'''

from os import system, name
import random

player = 1
word_selected = ''
correct_guess_letters = []
start_flag = True
wrong_guess = 0
guess_letter_length = 0
max_allowed_chance = 7

word_set = []
hang_man = [[' ','-','-','-','-','-','-','-','-', ' ', ' ', ' '],
            [' ',' ',' ',' ',' ',' ',' ',' ','|', ' ', ' ', ' '],
            [' ',' ',' ',' ',' ',' ',' ',' ','|', ' ', ' ', ' '],
            [' ',' ',' ',' ',' ',' ',' ',' ','|', ' ', ' ', ' '],
            [' ',' ',' ',' ',' ',' ',' ',' ','|', ' ', ' ', ' '],
            [' ',' ',' ',' ',' ',' ',' ',' ','|', ' ', ' ', ' '],
            [' ',' ',' ',' ',' ','-','-','-','-', '-', '-', '-']]

def clear():
    if name == 'nt':
        system('cls') # For windows
    else:
        system('clear') # For Mac and Linux

def list_index_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

def check_guess_letters(letter):
    global wrong_guess
    global word_selected
    global correct_guess_letters
    if letter in word_selected:
        index_list = list_index_of(word_selected, letter)
        if len(index_list) > 1:
            letter_count = 0
            for i in index_list:
                if correct_guess_letters[i] == '_':
                    correct_guess_letters[i] = letter
                    break
                else:
                    letter_count += 1
            if letter_count >= len(index_list):
                wrong_guess += 1

        else:
            if correct_guess_letters[index_list[0]] == '_':
                correct_guess_letters[index_list[0]] = letter
            else:
                wrong_guess += 1
        pass
    else:
        wrong_guess += 1

def draw_hang_man():
    global wrong_guess
    if wrong_guess == 1:
        hang_man[1][2] = 'O'
    elif wrong_guess == 2:
        hang_man[2][2] = '|'
    elif wrong_guess == 3:
        hang_man[2][1] = '\\'
    elif wrong_guess == 4:
        hang_man[2][3] = '/'
    elif wrong_guess == 5:
        hang_man[3][2] ='|'
    elif wrong_guess == 6:
        hang_man[4][1] = '/'
    elif wrong_guess == 7:
        hang_man[4][3] = '\\'

    for i, row in enumerate(hang_man):
        for j, column in enumerate(row):
            print(column, end="")
        print()

def check_correct_letters():
    global guess_letter_length
    guess_letter_length = 0
    for i in correct_guess_letters:
        if i != '_':
            guess_letter_length += 1

with open('words.txt', 'rt') as text:
    word_set = text.read().split(' ')

draw_hang_man()

total_players = int(input('Select number of players 1 or 2: '))
if total_players == 2:
    while True:
        if word_selected == '':
            for index, word in enumerate(word_set):
                print(index, word)
            print('Note: Index is starting from 0')
            selected_index = int(input('Select the index of the word you want to challege to player 2: '))
            player = 2
            print(word_set[selected_index])
            word_selected = word_set[selected_index]
            clear()
        else:
            if start_flag:
                correct_guess_letters = list('_'*len(word_selected))
                print(''.join(correct_guess_letters))
                start_flag = False
            guess_letter = input('Enter the letter:')
            check_guess_letters(guess_letter)
            draw_hang_man()
            print(''.join(correct_guess_letters))
            print('Incorrect attempt', wrong_guess)
            check_correct_letters()
            if wrong_guess == max_allowed_chance:
                print('You lost the game')
                break
            elif guess_letter_length == len(word_selected):
                print('You won the game')
                break
else:
    while True:
        if start_flag:
            word_selected = random.choice(word_set)
            correct_guess_letters = list('_' * len(word_selected))
            print(''.join(correct_guess_letters))
            start_flag = False
        guess_letter = input('Enter the letter:')
        check_guess_letters(guess_letter)
        draw_hang_man()
        print(''.join(correct_guess_letters))
        print('Incorrect attempt', wrong_guess)
        check_correct_letters()
        if wrong_guess == max_allowed_chance:
            print('You lost the game')
            break
        elif guess_letter_length == len(word_selected):
            print('You won the game')
            break
