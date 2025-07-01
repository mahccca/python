# dic {"key":"value"}
nomre={
    'math':100,
    'programming':90,
    'art':70
}

print(nomre['math'])


students={
    "mahsa":{
        "math": 70,
        "programming":100,
        "art":90
    },
    "maryam":{
        "math": 70,
        "programming":100,
        "art":90
    }
}

print(students["mahsa"]["math"])
print(students.keys())
print(students.get("mahsa"))
print(students.get("zahra","not Found!!"))