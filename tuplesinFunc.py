def is_even(n):
    return n%2 ==0

def get_odds(nums):
    odds=[]
    count=0
    for num in nums:
        if not is_even(num):
            odds.append(num)
            count+=1
    return odds,count

my_list=[1,2,3,4,56,8,7,95,2,100,2323,3]

my_odds,odds_count= get_odds(my_list)
print(len(my_odds))
print(odds_count)


donates={
    "sara":20,
    "fateme":120,
    "nazi":200
}

def donationa_analysis(don):
    person=''
    total=0
    counrt=0
    max_donation=-1
    for name,value in don.items:
        print(name,value)
        total +=value
        count +=1
        if value > max_donation:
            person = name
            max_donation=value
    avg=total/count
    return avg,total,person

avg,total,max_person=donationa_analysis(donates)

