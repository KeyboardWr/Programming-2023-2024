

# Format Strings
We can evalute insied of strings using f-strings.
To create a f-string, we put an f before the openig quote

```python
fave_food = input("What's your favourite food?")
print(f"Oooo{fave_food} sounds good")
```

# Strings

[{Design}]

# String Methods

[[Methods]] are functions that we can use on [[Objects]] 

String methods allow us to modify and work with strings.

Say for example, we want to make all characters of a string lowercase

```python
mr_ubial_yelling = "PLEASE PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower()) #Lowercases the letters

```


## .Lower()

The .lower() method takes a string and converts all UPPERCASE characters lowercase

we can use .lower() to help with [[Errors]] (Semantic/Syntax)

## .Upper()

The .upper() method converts all lower case letters to upper case in a string

## .Strip(str) 

The .strip() removes characters from the beginning and end of the string

```python
user_feeling = input("how are you feeling?")
#Capture "good" "GOOD" "Good"
if user_feeling.lower().strip("!.,?") == "good"
	print("That's great")
```


## .split(str) -> List
The .split() method splits a string into a [[List]], separating the string based on the characters youi give it.

```python
grocery_list = "eggs, milk, cheese, hotwheels"

grocery_list = grocery_list.split("")
```



