import streamlit as st

st.title("Printing your first hello world program")
st.code('''print("Hello world")\n''', language='python')

st.title("Understanding variables with data types")
st.write('''A string type can be denoted with a str(), string means that it is a string of characters strung together 
to form words.''')
st.code('''a = "Hello world"\nprint(a)''', language='python')
st.write('''An integer type can be denoted with an int(), int means that it is a whole number.''')
st.code('''b = 1\nprint(b)''', language='python')
st.write('''A float is a number that contains decimal points. Which can be denoted using the float() function''')
st.code('''c= 1.00\nprint(c)''', language='python')
st.write('''A char data type denotes a character. Which can be denoted using the char() function''')
st.code('''d = 'd'\nprint(d)''', language='python')
st.write('''A boolean is a data type that can be set and returned using True or False values. 
(OR 0 and 1 if you do this in binary). Which can be denoted using the bool() function''')
st.code('''e = True\nprint(e)''', language='python')

st.title("Comments")
st.write("Comments are things you write beside your code so that "
         "you remember what you write when you need to revisit them in the future.")
st.code('''print("Hello world") # prints out Hello world to the console''', language='python')
st.code('''
"""Or
you
can write
them like
this"""
''', language='python')

st.title("Logic and operations")
st.write("Logic and operations can be thought of in such a way. "
         "If a condition is met, what would the code execute next? If not, then what else can it do?"
         " How many different conditions are there?"
         " What will be returned if the condition is met or not?"
         " This is where if statements come in.")
st.code('''if CONDITION/S:
    print(return value)''', language='python')
st.code('''if CONDITION/S:
    ANOTHER CONDITION:
        print(return value)''', language='python')
st.write("There are also while conditions. While loops come where if a condition is not met yet, "
         "then whatever code is in the loop will be executed.")
st.code('''while (CONDITION):
    Code executed within the loop...
    Breaks when condition is met so no infinite loop will be created.''', language='python')

st.write("There is also a 2nd way to deal with logic, called for loops. "
         "The amount of things to go through is known and the "
         "program is terminated once the conditions are all fulfilled.")
st.code('''p = 0
for p in range(10):
    print(p)
    p += 1''', language='python')

st.write("Incrementing and Decrementing conditions")
st.write("Sometimes, you may need to iterate something or increase a value till it meets a certain condition.")
st.write("This is where incrementing and decrementing operations come. This can be denoted with the following code.")
st.code('''i = 0
while i < 100:
    print(i)
    i += 1

x = 0
while x > -100:
    print(x)
    x -= 1''', language='python')
st.write("There are also for loops. Which is used when the number of elements is known.")
st.code('''# Here is an example
z = 0
for z in range(100):
    print(z)
    z += 1
''', language='python')

st.title("Functions")
st.write("Functions are code that executes within a single block and can "
         "only be executed when the function/method is called.")
st.code('''def factorial(n: int):
    m = 1
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return ValueError("Factorial of negative numbers is not allowed")
    while n >= 1:
        m *= n
        n -= 1
    return m
''', language='python')

st.title("Classes")
st.write("Classes are codes that define the template for making something.")
st.write("Here's an example")
st.code('''class Person:
    def __init__(self, name: str):
        self.name = name
        self.age = 0
        self.friends = []
        self.friends_age = []
obj1 = Person('John')
print(obj1.name)''', language='python')
st.write("In this class, we defined a function called __init__ which takes a name and returns it."
         " By instantiating the obj1 object, we can use it to create an instance."
         " We also instantiated the name of the person called 'John', which we then printed out"
         " using the print(obj1.name) method.)")
