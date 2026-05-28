def get_full_name(first_name: str,last_name: str):
    full_name = first_name.title() + " " + last_name.title()

    return full_name

print(get_full_name("a","b"))


def get_name_age(name:str,age:int):
    name_with_age = name.title() + " " + str(age)

    return name_with_age

print(get_name_age("Abhi",20))