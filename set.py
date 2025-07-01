#  the diffrence between this and other variable types is first you must assign this like this : 
my_set=set()
my_set.add(1)
my_set.add(2)
my_set.add(2)
#  you can not repate values , the values of this list are unique!
print(my_set)
#!!!!!!!!!  you can not add an array to this set , it use easier type of varriables 

chess=set()
chess.add("jadi")
chess.add("Mahsa")
poetry=set()
poetry.add("marya")
poetry.add("Mahsa")
poetry.add("Arya")

# union of these two groups , but unique !
print(poetry.union(chess))
# intersection of these groups ! 
print(poetry.intersection(chess))




heyvoons=set(["sag","dog","malakh","gorg"])
print(heyvoons)
heyvoons.add("cat")
print(heyvoons)