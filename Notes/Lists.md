
In python, lists are a collection of items
We store values inside of lists
The value of the items can be of different [[Types]]
**Order matters in a list**

# Creating a List
To make a list, we use brackets /()
We separate the individual items with commas

```python
some_list = ("Jimmy", "Sarah", "Frederick")
```

# Access Elements in the list

We can access the individual things fro lists using bracket notation
In the example below, we'll use bracket notation to access "Sarah"

```Python
some_list[1] # sarah
some_list[2] # Frederick
some_list[3] # Jimmy
some_list[-1] # Sarah
```

Inside the brackets, we give the index of the item we want
Python uses 0 index counting, which means we start counting at 0




## 2 Dimensional Lists

so far, all the list we've used so far are one-dimensional

```python
some_list = ["air", "water", "fire"]
```

We can create 2-dimensional lists that in short. are multiple lists inside a bigger list.

```python
list2D = [
	[1,2,3],
	[4,5,6],
	[7,8,9]	  
]

list2D[0][0] # 1
list2D[0][1] # 2
list2D[2][3] # 9

```



## Tuples

Tuples(tooples or tuples) are like lists except for one main thing

Tuples are immutable. Immutable means that you can't change the contents of a tuple

Because Tuples are immutable, it has some benefits

To create a tuple, use parentheses instead of brackets


## Image and Tuples
The basic unit of measurement in images is a pixel 
The pixel information is stored in a tuple of three-values
(3-tuple)

The 3 tuple tells us for One PORTION of the image, what the RED, GREEN, BLUE values are (red, green, blue)

```python

RED - (255, 0, 0)
BLUE - 
```
