
## Syntax Errors

These types of errors are ones that occur where you run your code and then it 'breaks'
Syntax errors are relatively easy to spot or fix

Syntax errors occur when we don't follow the rules of the language completely
## Semantic Errors

Semantic errors occur when our code doesn't MEAN what me intend it to mean

These errors, in Mr. Ubial's opinion, are FAR MORE challenging to spot and fix.

```Python
user_response = input("Do you like to eat food?")

if user_response == "yes":
	print("you are human")
else:
	print("You must be some sort of robot")
```

The problem with this code above is subtile. What Mr. Ubial means is that EVERY ANSWER OR YES should go into the YES block.

```python
mr_ubial_yelling = "PLEASE PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower()) #Lowercases the letters

```

We can use .lower() to fix these errors