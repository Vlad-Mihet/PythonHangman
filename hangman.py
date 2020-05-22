import random
playOptions = ['yes', 'no']

def play():
    words = open('1-1000.txt').readlines()
    random_word = words[random.randint(0, 1000)]
    letters_in_name = list(random_word)
    word_letters = letters_in_name[:len(letters_in_name) - 1]
    starred_word = len(word_letters) * 'x'
    starred_list = list(starred_word)
    already_guessed = []
    lives = 7
    for letter in starred_list:
        print(letter, end='')
    print()
    while lives:
        if starred_list == word_letters:
            print('You won!')
            break
        else:
            user_choice = input('Input a letter: ')
            if user_choice not in already_guessed:
                if user_choice in word_letters:
                    print('The letter you chose is right')
                    already_guessed.append(user_choice)
                    for i in range(len(random_word) - 1):
                        if word_letters[i] == user_choice:
                            starred_list[i] = word_letters[i]
                    for letter in starred_list:
                        print(letter, end='')
                    print()
                else:
                    lives -= 1
                    for letter in starred_list:
                        print(letter, end='')
                    print()
                    print('Wrong Answer! You now have ' + str(lives) + ' lives')
            else:
                while user_choice in already_guessed:
                    user_choice = input('Pick another letter: ')
    if not lives:
        print('You lost!')
    playAgain = input('Want to play again? (yes/no) ')
    if playAgain == 'yes':
        play()
    else:
        print('Have a good day!')
play()