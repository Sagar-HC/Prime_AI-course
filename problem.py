info = [
    ("ALice" , "maths"),
    ("bob", "science"),
    ("ALice" , "science"),
    ("charlie" , "maths"),
    ("bob","maths"),
    ("ALice" , "english"),
    ("charlie", "english"),
]

dict = {}

for name,course in info:
    if(dict.get(name) == None): # means the name aint int the dict yet so we create a shit load of new set wit that name 
        dict.update({name:set()})#the dict is updated with this name:set()
        dict[name].add(course) # this accessing the name makes the set to be opened so the set gets updated
    else:
        dict[name].add(course)
        
print(dict)

# print(unique_courses)