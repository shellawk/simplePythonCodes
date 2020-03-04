def user_interface():
    words = input('Enter two words separated by space to swap: ')
    words_to_swap = generate_word_list(words)
    if len(words_to_swap) == 2:
        display_words_swapped(words_to_swap)
    else:
        print('Enter only two words')
        print('GO AGAIN!!')
        user_interface()

def generate_word_list(words_entered):
    word_list = words_entered.split(' ')
    return word_list

def display_words_swapped(list_of_words):
    words_swapped = ' '.join(list_of_words[::-1])
    print(words_swapped)

user_interface()