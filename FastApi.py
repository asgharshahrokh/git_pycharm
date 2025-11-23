from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fakeItems = [{"item_name": "foo"}, {"item_name": "bar"}]


@app.get("/items/")
def read_items(skip: int = 0, limit: int = None):
    return fakeItems[skip:skip + limit]


def Fullname(Firstname: str, Lastname: str):
    return Firstname.title() + ' ' + Lastname.title()


print(Fullname('ali', 'mahdavi'))


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age


def process_items(items: list[str]):
    for item in items:
        print(item.title())


process_items(['ali', 'ahmad', 'reza', ])


def process_items(items_t: dict[int, str], items_s: set[bytes]):
    return items_t, items_s


process_items([1, "ali"], None)


def say_hi(name: str | None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


class Person:
    def __init__(self, name: str):
        self.name = name


class Person:
    name = ""
    famile = ""
    age = 0


p = Person()
p.name = 'ahmad'
p.famile = 'vali'
p.age = 'knp'
print(p.age)

for i in range(10):
    print(i)

for j in range(10):
    print(j)

print('reset...')


