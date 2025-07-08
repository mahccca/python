def tavan_2(x):
    return x**2


a=[3,4,5,6,7]
for i in range(len(a)):
    a[i]=tavan_2(a[i])


print(a)


tavan_a=map(tavan_2,a)
print(tavan_a)

for n in tavan_a:
    print(n)

print(list(tavan_a))

'''
حالا میخوایم بدونیم توابع ناشناخته چیه . گاهی یه تابع کوچولو داریم مثل توان 2 که میتونیم مثل پایین صداش کنیم و بسازیمش : 
'''

tavan_b=map(lambda x: x**2,a)


# filter

a=[1,1.5,1.75,2,2.1,2.2,2.3,3]
# az list bala faghgat adade ashar ro mikhaim bargardonim 

def is_ashari(x):
    return x != int(x)

print(list(filter(is_ashari,a)))

# ba anonuymous functions : 

print(list(filter(lambda x:x!=int(x),a)))