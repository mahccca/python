def hello():
    '''
    this is my comment
    '''
    print("Oh hello wolrd!!!")

# hello()
# hello()
# hello()

def hello2(name):
    print(f"Oh hello {name}!!!")

# hello2("Mahsa")

def hello3(name):
    for i in range(len(name)):
     print(f"Oh hello {name}!!!")

# hello3("Mahsa")

def chantatoosh(s,c):

    '''
    t
    t of code of prof
    '''
    counter=0
    for this_charecter in s:

        if this_charecter==c:
            counter+=1
    return counter

print(chantatoosh("Mahsa","a"))

def tavan(n,t):
    javab=1
    for i in range(t):
        javab*=n 
    return javab

print(tavan(2,4))


def is_even(n):
    '''
    '''
    return n%2 ==0

def get_odds(nums):
    odds=[]
    for num in nums:
        if not is_even(num):
            odds.append(num)
    return odds
