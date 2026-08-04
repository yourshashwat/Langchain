from typing import TypedDict

class new_person(TypedDict):
    name:str
    age: int

person1= new_person({
    'name': "Shubham Shashwat",
    'age': 24
})

print(person1)