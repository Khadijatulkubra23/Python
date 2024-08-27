message: str="Hello, World!"
print(message)

message1: str="How are you?"
print("He said,", message1)

message2= "Are you okay?"
print("She said,", message2)

name="Khadija"
print("My name is", name)

print(f'"Hello {name}, would you like to learn Python today?"')

personName: str="Khadija Tul Kubra"
print(personName)

print(personName.lower())

print(personName.upper())

print(personName.title())

Person:str="Eleanor Roosevelt"
quote:str="""The future belongs to those who believe in the beauty of their dreams. """
print(f'{Person} once said,"{quote}"')

famous_person:str="Martin Luther King Jr"
message3:str="Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that."
print(f'{famous_person} once said,"{message3}"')

person_name:str="   Hey, Khadija   "

person_name1:str="   Hey, \n\tKhadija   "
print(person_name)
print(person_name1)

print(person_name.lstrip())

print(person_name.rstrip())

print(person_name.strip())

x=5
y=10
z=20
sum=x+y+z
print(sum)

a=20
b=10
print(f"before swap, a={a} and b={b}")

a,b=b,a
print(f"after swap,a={a} and b={b}")

color:str="Emerald green"
print(color)

color_name=color 
print(color_name)

pet_name: str="Buddy"
pet_name="Max"
print(pet_name)

# Assigning the value "Sunshine" to a variable 
# Printing the variable correctly 
# Attempting to print a variable with a different name, which will cause a NameError

score:int=100
print(score)

score:int=120
print(score)

city:str="Lahore"
print(city)

text:str="python programming"
print(text.title())

mixed_cases:str="PyThoN pROgRamMiNg"
print(mixed_cases.upper())

temperature:int=33
print(f"The current temperature is {temperature} degrees.")

poem: str="""In the realm of circuits and code,
A program lives, quite a heavy load.
It tries to compute, but fails to see,
Its logic's flawed, it’s clear to me.

It loops forever, stuck in a haze,
Lost in its own binary maze.
Syntax errors, it cannot mend,
A bug-filled journey without an end.

It prints gibberish, nonsense galore,
Spitting out strings that we can't ignore.
Its purpose, vague, intentions blurred,
A clueless machine, quite absurd.

Yet in its folly, there's a charm,
A digital being, causing no harm.
For even in glitches, there's a spark,
A testament to a coder's arc.

So let it run, this program dumb,
In its own way, it's somewhat fun.
A reminder that in tech’s grand scheme,
Imperfection's part of the dream."""

print(poem)