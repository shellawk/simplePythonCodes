from random import randint

coin_toss_intepreter = {
    0: 'head',
    1: 'tail'
}

def coin_toss():
    coin_toss_result = coin_toss_intepreter[randint(0,1)]
    message = 'You got a {}'.format(coin_toss_result)
    print(message)

coin_toss()