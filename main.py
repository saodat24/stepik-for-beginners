import random


start_game_answ = input("""Hello dear!\n\
Now let's play the game "Guess the number")\n\
You have 500 points by default. We have generated\n\
a number and you have to guess which number it is.\n\
Don't worry, there will be hints! But each hint will\n\
take away 50 points from you. Are you ready?\n\
Answer(Yes/No): """)
score = 500
rand_num = random.randint(1, 100)


if start_game_answ == 'Yes':
    user_name = input("Sooo... I'm happy that you are in!)\nHow should I call you?\nAnswer: ")
    print("Les's start! Guess the number from 1 to 100:", end='')
    while score >= 0:
        user_inp = int(input(' '))
        if user_inp == rand_num:
            print(f'{user_name} WON!')
            break
        else:
            print(f'Ahh {user_name}... Do you want a hint?')
            answ = input('Answer(Yes/NO): ')
            if answ == 'Yes':
                score -= 50
                if user_inp > rand_num:
                    print('Too much, enter the number less than this number\nTry again: ')
                elif user_inp < rand_num:
                    print('Too few, enter the number over than this number\nTry again: ')
            elif answ == 'No':
                continue
            else:
                print('Wrong answer! The end of the game!')
                break
    else:
        print(f'{user_name} you lost your all points!')
else:
    print('Ok(')
