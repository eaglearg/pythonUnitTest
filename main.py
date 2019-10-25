from random import randint
import sys

def do_stuff(num=0):
    try:
        if num is None or isinstance(num, str):
             return 'please enter a number'
        else:
           return int(num) + 5
    except ValueError as err:
        return err

def guess_function(guess, answer):
  if  0 < guess < 11:
      if guess == answer:
          print('you are a genius!')
          return True
  else:
      print('hey bozo, I said 1~10')
      return False

if __name__ == '__main__':
    # generate a number 1~10
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if(guess_function(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue