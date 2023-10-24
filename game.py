import random 


def mult(a):
    for i in range (2,10):
        if a%i == 0:
            print("It Is A Multiple Of",i)
        




flag = True
while flag:
    num=input('Type a upper limit : ')
    if num.isdigit():
        print('Start Game')
        num = int(num)
        flag = False 
    else:
        print('Enter a digit')
secret = random.randint(1,num)
guess = None
count = 1
while guess != secret:
    guess = input('Type a number between 1 and ' + str(num) +":")
    if guess.isdigit():
        guess = int(guess)
    if guess == secret:
        print('Yor Guess Is Right')
    else:
        print('Incorrect Guess, Please Try Again')
        count=count+1
        if guess > secret:
            print("The Required Number Is Lower Than The",count-1,"th Guess")
            mult(secret)
        elif guess < secret:
            print("The Required Number Is Higher Than The",count-1,"th Guess")
            mult(secret)
        



print('The Amount Of guesses : ', count)




