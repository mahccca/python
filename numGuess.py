import random 
computer=random.randint(1,20)
guess=0
def get_a_guess():
    ans=input("what is your guess ? ")
    return int(ans)

def win(computer,guess):
    return computer==guess
    
def answer(computer,user):
    if computer>user:
        res='My num is larger'
    elif computer <user :
        res="Oh.. you went so large! mine is smaller"
    else:
        res="wow! you won"
    return res




while(not win(computer,guess)):
    guess = get_a_guess()
    print(answer(computer,guess))
