def greet(fname, lname):
    print(f"Hello, {fname} {lname}!")

greet("Jess", "Lee")

# Using Keyword args
greet(fname="Jess", lname="Lee")

greet(lname="Lee", fname="Jess")

def describe_pet(pet_name, animal_type="dog"): # animal_type has a default value
    print(f"I have a {animal_type} named {pet_name}")

# Postitional Argument
describe_pet("wilie")

# Positional and default argument
describe_pet("Harry", "Hamster")

# Keyword Arguments
describe_pet(animal_type="cat", pet_name="Tofu")