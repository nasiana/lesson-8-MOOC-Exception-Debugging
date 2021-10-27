#!/usr/bin/env python
# coding: utf-8

# ## Today's agenda:
#
# 1.  Introduction  to Exception & Debugging
# 2.  Exceptions and Errors
# 3.  Exception Handling
# 4.  User Defined Exceptions
# 5.  Assertion
# 6.  Debugging

'''
All we will discuss today is Python's SMART way of dealing with potential errors and unexpected behaviour in our programs.
   We will also look at its MANY features and the debugging capabilities.
We can make certain mistakes while writing a program that lead to errors when we try to run it. A python program terminates
   as soon as it encounters an unhandled error.
'''

"""
Copy over the inputs to demo the function.
GOOD INPUT: add_vat(vat=20, prices=[24, 0.15, 32.45, 0])
BAD INPUT: add_vat(vat=20, prices=[24, 0.15, '10', 32.45]) --> it has a string in the list, hence it fails.
"""


def add_vat(vat, prices):
    """
    Add commission to every price item in the provided iterable.
    :param vat: float, vat percentage
    :param prices: iterable, net prices as per customers' receipt
    :return: list of prices with added vat
    """
    new_prices = [(price / 100 * vat) + price for price in prices]
    return new_prices


# add_vat(vat=20, prices=[24, 0.15, 32.45, 0])
# add_vat(vat=20, prices=[24, 0.15, '10', 32.45]) # --> it has a string in the list, hence it fails.


## BUILT IN ERRORS AND EXCEPTIONS

'''
There are different ways to classify errors in Python, but for today we will go for the simplest one: Syntax Errors and Logical Errors
```Syntax Error (or Parsing Error)```: caused (or a more pythonic way of saying it, **raised**) when the exact 
structure (or syntax) of Python is not followed. For example, we could forget to : of the *if statement*. </br>
'''

# Raises a SyntaxError
# ---------------------
# print("Hello, World)

# Raises an IdentationError
# -------------------------
# if my_grade < 10:
# print('Maybe next time')


'''
**LOGICAL ERRORS (Exceptions)**: these errors are the trickiest ones and they appear when there is an error in the runtime, after all syntax checks have passed
```Attribute Error```: is raised when an attribute reference or assignment fails. It could also fail because of spelling mistakes when you call a method.  
```NameError```: when a variable is called but not defined
```ZeroDivisionError```: raised when we try to divide by 0
```ModuleNotFoundError (or ImportError)```: raised when the name of the package we try to import is not found (maybe either due to a spelling 
mistake or maybe the package is not installed)
'''

apples = 10
# Raises an AttributeError
apples.append(6)

# Raises an AttributeError
string = "Hello { }".fst("world")
print(string)

# Raises a NameError
print(my_variable)

# Raises a ZeroDivisionError
grade = 10

# perform division with 0
my_grade = grade / 0
print(my_grade)

# Raises a ModuleNotFoundError
import whatever_package

'''
- There are many more errors and exceptions that Python can raise. 
- If you do not recognize an error, just try to find out what it means. This is the first step towards fixing your code. 
- There is also a hierarcy as everything in Python is an object and objects can inherit properties. Don't worry too much about this 
(Object Oriented Programming will be covered in the Software Pathway). Here is a useful resource for Python errors and exeptions 
and their hierarchy: https://airbrake.io/blog/python/class-hierarchy 
'''

# We can view all built-in python exceptions with the following function
print(dir(locals()['__builtins__']))

'''
# **So what do we do now?** 
## ERROR AND EXCEPTION HANDLING
"Traditional programming languages tended to treat errors as a catastrophic situation. 
An error usually meant that the script couldn't possibly continue, and would probably instantly crash. 
Therefore, the job of the programmer was to do everything in their power to avoid errors.
That meant that the programmer needed to check for everything that could go wrong before calling a function: 
Does the file exist? Is the network up? Etc. And if something unexpected went wrong, then the script crashed anyway.
The process of checking for every possible error condition ahead of time is known as Look Before You Leap, or LBYL." 
(LBYL is something we will cover later so feel free to ignore this for now)
Nice resource from where the above is taken: [link](http://conquerprogramming.com/blog/3-Exceptions.html)
'''

# ### Example:
#
#
# readFile (
#     open the file
#     determine its size
#     allocate that much memory
#     read the file into memory
#     close the file
# )
#

'''
# This function seems simple enough, but it ignores all these potential errors.
# - What happens if the file can’t be opened?
# - What happens if the length of the file can’t be determined?
# - What happens if enough memory can’t be allocated?
# - What happens if the read fails?
# - What happens if the file can’t be closed?
- Exception and Error handling increases the robustness of your code;
- It guards against potential failures that would cause your program to exit in an uncontrolled fashion;
- separates error-handling code from “regular” code which also helps with readibility

Some more examples about exception handling in Python: [link](https://www.naftaliharris.com/blog/nontrivial-exception-handling-python/)

We have 3 very important keywords for handling errors and exceptions: 

```try```: try to run this specific command. The try clause includes the code that could potentially raise an exception. 

```except```: 
- **If everything works well** in the ```try``` clause, then the ```except``` will not be executed. The ```try...except``` 
block is completed and the program will proceed. (this is where the ```else``` statement shows up - see diagram below)
- **If an exception is raised** in the ```try``` clause, Python will pass the exception to the ```except``` clause to see 
if this particular error is handled there. 

```finally```: this is always executed after ```try```, ```else```, and ```except``` clauses, even if they raised another 
error or executed a ```break```, ```continue```, ```return```. This is useful to clean-up code that should be run no matter 
what else happens in the program (for example, closing a file)
```
try:
       # Some Code.... 
except:
       # optional block
       # Handling of exception (if required)
else:
       # execute if no exception
finally:
      # Some code .....(always executed)
```
'''

''' EXAMPLE 1 '''

# Without try / except

# number = int(input("Please enter a number to divide by: "))
# division_result = 100 / number
# print(division_result)

# With try / except

# number = int(input("Please enter a number to divide by: "))
# try:
#     division_result = 100 / number
#     print(division_result)
# except ZeroDivisionError:
#     print("You cannot divide by 0, please try gain")

'''
We can have multiple exceptions passed to the except block. They need to be
passed as a tuple (i.e., within paranthesis and separated by comma). 
However, in our case there is something weird happening. If we input something
that would raise a ValueError (such as a letter), the except does not work
as expected. 
# number = int(input("Please enter a number to divide by: "))
# try:
#     division_result = 100 / number
#     print(division_result)
# except (ZeroDivisionError, ValueError):
#     print("You can either not divide by 0 or your number is not an integer, please try again")    
This is because the error is not caused within the try block, it is caused 
before, when we do the assignment to the variable. Let's try the following instead:
'''
number = input("Please enter a number to divide by: ")
try:
    number = int(number)
    division_result = 100 / number
    print(division_result)
except (ZeroDivisionError, ValueError):
    print("You can either not divide by 0 or your number is not an integer, please try again")

'''
The example above uses the ```try...except``` block to print something when an in-built error/exception is raised. 
In this case it was the ZeroDivisionError. 
But what do we do when Python does not raise an error, but the code will not behave as we except it to? 
## RAISE KEYWORD FOR EXCEPTION HANDLING
- the ```raise``` keyword is another way to handle exceptions in Python;
- in this case, you will be able to raise your own exceptions;
- These are exceptions that get raised when an issue outside the scope of *expected errors* occurs;
'''

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")

try:
    if not type(x) is int:
        raise Exception
except:
    print("Only integers are allowed")

print('Our program still works even though we had an error')

''' EXAMPLE 2 '''

# Without try/except - This code will not print anything if the input is not within the specified range

# number = int(input('Enter a number in the range 5-10: '))
# if number > 5 or number < 10:
#     division_result = 100 / number
#     print(division_result)
#     print("Well Done")
# # We could indeed add an else statement and get printed a message in case it is outside the range
# else:
#     print("Your number is NOT in the requested range")

# With try/except

number = int(input('Enter a number in the range 5-10: '))

try:
    if number < 5 or number > 10:  # this needs a number between 5 - 10
        raise Exception

    division_result = 100 / number
    print(division_result)
    print("Well Done")

except:
    print("Your number is NOT in the requested range")

'''
**General rule of thumb:** You should use if / else to handle all cases you expect. 
You should not use try {} catch {} to handle everything (in most cases) because a useful Exception 
could be raised and you can learn about the presence of a bug from it. You should use try {} catch {} 
in situations where you suspect something can/will go wrong and you don't want it to bring down the 
whole system, like network timeout/file system access problems, files doesn't exist, etc.

When to use exception handling in Python is not a yes/no answer, but usually general guides exist 
and it depends on the programme and user preference as well.
'''

''' 
EXAMPLE 3 - is not in any of the materials 
If there is no time during the session, you can have a look yourself at home
'''

# let's assume we have a list with students that took the CFG Nano Assessment. This list has 2 parts (it is a nested list):
#   - a list with the first and last name of each student
#   - a list with the grades on the assignment

grades = [
    [['Hassan', 'Munir'], [90.0, 80.0, 90.0]],
    [['Rehana', 'Soltane'], [80.0, 90.0, 90.0]],
    [['Andreea', 'Avramescu'], []]
]


# Our task: you are the CFG Nano Instructor and you want to create a new list which, alongside the name and the grades, you also want to have the average.

# let's define a function that calculates the average for the grades
def avg(grades):
    return sum(grades) / len(grades)


# let's now define a function that creates our new list
def get_stats(grades):
    new_grades = []
    for i in grades:
        new_grades.append([i[0], i[1], avg(i[1])])
    return new_grades


get_stats(grades)

''' EXAMPLE 3 - continue'''

# let's assume we have a list with students that took the CFG Nano Assessment. This list has 2 parts (it is a nested list):
#   - a list with the first and last name of each student
#   - a list with the grades on the assignment

grades = [
    [['Hassan', 'Munir'], [90.0, 80.0, 90.0]],
    [['Rehana', 'Soltane'], [80.0, 90.0, 90.0]],
    [['Andreea', 'Avramescu'], []]
]

# Our task: you are the CFG Nano Instructor and you want to create a new list which, alongside the name and the grades, you also want to have the average.

# let's define a function that calculates the average for the grades that DOES NOT THROW A ZeroDivisionError
''' Approach 'flag the error and print a message' '''
# def avg(grades):
#     try:
#         return sum(grades)/len(grades)
#     except ZeroDivisionError:
#         print('There is a list with no grades')

''' Approach 'do something better' and add a return'''


def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print('There is a list with no grades')
        return 0.0

    # let's now define a function that creates our new list


def get_stats(grades):
    new_grades = []
    for i in grades:
        new_grades.append([i[0], i[1], avg(i[1])])
    return new_grades


get_stats(grades)

'''
# ## ASSERTION ERROR
- they are a good example of defensive programming; 
You have ```assert statements``` at the beginning of functions (typically) or at the end. They are used to 
make sure that the assumptions on computations are exactly what the function expects them to be. 
**For example**, if we want a function to take only positive numbers, then the ```assert statement``` will 
make sure (or assert :D) that function takes in an integer that is grater than 0. 
The assert syntax is: 
```
assert condition, message
```
- condition: the condition for which we want to test (required);
- message: the message that we want to display upon execution of the assert statement (optional);
Let's go back to our students' grades ...
'''


def apply_discount(product, discount):
    """
    Add a discount to the price.
    :param product: dict obj, item spec including price
    :param discount: float discount expressed in percent
    :return: float new price
    """
    price = round(product['price'] * (1.0 - (discount / 100)), 2)  # the last 2 is the no. of decimals
    assert 0 <= price <= product['price']  # if the condition is FALSE, "activate" assert
    return price


#### VALID INPUT (comment / uncomment  to use as necessary)###
# trainers = {'name': 'Running Trainers', 'price': 79.99}
# discount  = 25 #(represents 25%)
# print(apply_discount(trainers, discount))


#### INVALID INPUT (comment / uncomment to use  as necessary)###
# trainers = {'name': 'Running Trainers', 'price': 79.99}
# discount  = 20 #(represents 200%) --> Assertion Error will be raised
# print(apply_discount(trainers, discount))


''' EXAMPLE 3 - with ASSERT'''

# let's assume we have a list with students that took the CFG Nano Assessment.
#    This list has 2 parts (it is a nested list):
#      - a list with the first and last name of each student
#      - a list with the grades on the assignment

grades = [
    [['Hassan', 'Munir'], [90.0, 80.0, 90.0]],
    [['Rehana', 'Soltane'], [80.0, 90.0, 90.0]],
    [['Andreea', 'Avramescu'], []]
]

# Our task: you are the CFG Nano Instructor and you want to create a new list
#    which, alongside the name and the grades, you also want to have the average.

''' Approach 'do something better' and add a return but with ASSERT'''


def avg(grades):
    assert not len(grades) == 0, 'There is a list with no grades'
    return sum(grades) / len(grades)


# let's now define a function that creates our new list
def get_stats(grades):
    new_grades = []
    for i in grades:
        new_grades.append([i[0], i[1], avg(i[1])])
    return new_grades


get_stats(grades)

'''
Asserts are really good to stop propagating the errors. When an ```assert``` becomes false, that means the 
condition is not met, then the programme stops. The ```assert``` checks if the programme has the right input 
or does what you expect it to you, otherwise it will stop it.
- the goal is to spot bugs as soon as introduced and make clear where they happened;
- use as a supplement to testing (more on testing tomorrow);
- raise exceptions if users supply bad data input;
use ```assertions``` to:
- check types of arguments or values;
- check that invariants on data structures are met;
- check constraints on return values;
- check for violations of constraints on procedure (e.g. no duplicates in a list)
Some other important ```assert``` notes: 
- Do NOT pass a ```tuple``` to an ```assert```. It will never fail. This has to do with non-empty tuples 
always being true in Python. An assert statement that can never fail even though the condition is not met, it's useless. 
```
assert (1 == 2, "This should fail, but it doesn't")
```
NB: Do not use parenthesis to call assert like a function. It is a statement. If you do assert(condition, message) 
you'll be running the assert with a (condition, message) tuple as first parameter.
- Do NOT use ```assert``` for data validation:   
'''


# The code below is bad practice for 2 reasons and both reasons have to do with
#    our ability to disable assertions from the interpreter.

def cancel_membership(membership_id, user):
    # Cancel Gym membership for an existing member
    assert user.is_admin(), 'Must be admin to cancel'
    assert gym_members.membership_exists(membership_id), 'Unknown id'
    gym_members.find_membership(membership_id).delete()


''' 1ST ASSERT: Checking for admin privileges with an assert statement is 
dangerous. If assertions are disabled in the Python interpreter, this turns 
into a null-op. Therefore any user can now delete products. The privileges 
check doesn’t even run. This likely introduces a security problem and opens 
the door for attackers to destroy or severely damage the data in your customer’s 
or company’s online store. Not good.'''

''' 2ND ASSERT: The membership_exists() check is skipped when assertions are 
disabled. This means find_membership() can now be called with invalid product 
ids—which could lead to more severe bugs depending on how our program is written. 
If the store app crashes if we attempt to delete an unknown product, it might be 
possible for an attacker to bombard it with invalid delete requests and cause an outage.'''


# The right way to transform the above code can be something like this:

def cancel_membership(membership_id, user):
    # Cancel Gym membership for an existing member
    if not user.is_admin():
        raise AuthorizationError('Must be admin to cancel'):
        if not gym_members.membership_exists(membership_id):
            raise ValueError('Unknown id')
        gym_members.fin_membership(membership_id).delete()

    ''' AuthorizationError: in-built Python exception that is raised when the API key is not authorized to perform the attempted action.'''

    ''' ValueError: (confusing for now, but will become clearer later in the course) in-built Python exception raised when there is a problem with the content of 
    the object you tried to assign the value to. It has a similar explanation to TypeError, but it's slightly different.'''

    # ## DEBUGGING

    def debugging_n_breakpoints():
        my_list = []
        for i in range(10):
            new_i = 10 + i

            # import pdb          # - these 2 lines can be replaced by breakpoint() in Python 3.7 or later
            # pdb.set_trace()     # -

            breakpoint()

            print('new value is: ', i)
            my_list.append(new_i)
        return my_list

    ''' 
    Some commands: 
    n        - next / step over
    s        - step into 
    l        - list code (for context)
    j <line number> - jump to line
    b <line number> - jump to line
    c        - continue until breakpoint
    q        - to exit the debug mode
    '''

    debugging_n_breakpoints()

    '''
    ## PRACTICE
    **WITH YOUR INSTRUCTOR**
    Teenager club registration program:
    - Manage the program execution by validating user’s name and age. 
    - Raise Validation and Assertion errors for invalid input. 
    - Write a registration record into a new file.
    **INDEPENDENTLY**
    Write a function that can read contents of a file and can handle cases when provided file name does not exist:
    - Handle Error cases gracefully displaying an informative message to the user. 
    - What Error type can we use here?  (check Python documentation)
    '''

    def age_validated(age):
        """
        Checks whether the age is a positive number
        : param age: int, the age of the user
        Raise Assertion error if outside of range 12 - 19 (teenager classification)
        """
        if age < 0:
            raise ValueError("Only positive values are allowed")
        assert 12 <= age <= 19
        return True

    def name_validated(name_string):
        """
        Checks whether the age is a positive number
        : param name_string: str, the name of the user separated by comma
        Exceptions: ValueError for missing comma, ValueError for missing name/surname
        """
        if ',' not in name_string:
            raise ValueError("Missing comma")

        name, surname = name_string.split(',')

        if not len(name) or not len(surname):
            raise ValueError("Incorrect input: Name or surname missing")

    # Flag
    isSuccessful = False

    try:
        name = input("Please enter your surname separated by comma: ")
        name_validated(name)
        age = int(input("Please enter your age: "))
        age_validated(age)

    except ValueError as exc:
        print("Invalid input: %s" % exc)

    except AssertionError as exc:
        print("The age is not within the 'teenager' category")

    else:
        with open("registration_file.txt", 'a+') as file:
            file.write("New member name: {} and age {}".format(name, age))
        isSuccessful = True

    finally:
        if isSuccessful:
            print("Registration Process completed SUCCESSFULLY")
        else:
            print("Could not complete registration. Please try again")