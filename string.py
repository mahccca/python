message="hello World!"
print(message)
# indexing 
print(message[0])
print(message[10])
# slicing [n:m:s]
# slice 
print(message[0:10])
ns="0123456789"
#  since 3 untill the end 
print(ns[3:])
# since begin until the 5 (without 5 )
print(ns[:5])
#  since begin till -5 ( we count from the edje (left) -1 )
print(ns[:-3])
#  to reverse the string 
print(ns[::-1])

#  using triples " to code easier 
print("""
    hi 
    my name is mahsa
    i'm 28 years old 
    and i'm happy :)
      
    """)

#  or we can write it like this 

print("\nhi\nmy name is mahsa \ni\'m 28 years old\nand i\'m happy :) \n\n")

print(type(ns))
print(message.islower())
print(ns.index("5"))

#  String interpolation
# # it comes from C
name="mahsa"
family="danandeh"
age=29.53453
print("hello %s %s %s" %(name,family,age))
# Frormat string
print("hello {} {} you are {}".format(name,family,age))
# or 
print("hello {1} {0} you are {2}".format(family,name,age))
# or
print("hello {Myname} {Myfamily} you are {Myage:5.1f}".format(Myfamily=family,Myname=name,Myage=age))\
# or
print(f"hello {name} {family} you are {age:1.1f}")

print(len(ns) ,"this is length")