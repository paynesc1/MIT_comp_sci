VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
# HAND_SIZE = 7

# SCRABBLE_LETTER_VALUES = {
#     'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
# }

# def get_word_score(word, n):
#     # word: string
#     # n: int >= 0
#     # returns: int >= 0

#     # set variale for score
#     score = 0
#     # correct for mixed case entries
#     word = word.lower()
#     word_length = len(word)
#     print(f"Word length: {word_length}")
#     # get first_component
#     for letter in word:
#         print(letter)
#         if letter in SCRABBLE_LETTER_VALUES:
#             score += (SCRABBLE_LETTER_VALUES[letter]) 
#     # second_component = (7 * word_length) - (3 * (n - word_length))
#     second_component = (7 * word_length - 3 * ( n- word_length))
#     if second_component < 1:
#         second_component = 1
#     print(f"Score: {score}")
#     print(f"2nd Component: {second_component}")
#     score = score * second_component
#     # next line          
#     print(score)

# get_word_score("WaYbILl", HAND_SIZE)

# def display_hand(hand):
#     for letter in hand.keys():
#         for j in range(hand[letter]):
#             print(letter, end=' ')
#     print()
# display_hand({'a':1, 'x':2, 'l':10, 'e':1})


n = 7
import math
import random

def deal_hand(n):
    hand = {}
    num_vowels = int(math.ceil(n/3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')
    print()

    return hand
deal_hand(n)

my_word = input("Guess a word: ")

def update_hand(hand, word):
    print()
    print(hand)
    print(word)
    
update_hand(deal_hand(n), my_word)