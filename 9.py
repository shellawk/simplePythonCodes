def user_interface():
    word_to_check = input('Enter word to check: ')

    if len(word_to_check)>0:
        check_word(word_to_check)
    else:
        print('Enter a word.')

def check_word(word):
    reversed_word = []
    for char in word[::-1]:
        reversed_word.append(char)
    reversed_word = ''.join(reversed_word)
    if reversed_word == word:
        print(f'{word} is a palindrome.')
    else:
        print(f'{word} is not a palindrome.')

user_interface()