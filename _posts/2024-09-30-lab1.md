---
layout: post
title: Lab 1 Write-Up
subtitle: By Aanya Gupta
cover-img: /assets/purple.png
thumbnail-img: /assets/pizza.png
share-img: /assets/pizza.png
tags: [Digimon, Python, Data Science, AOD]
---

First, I downloaded the `digimon.csv` file. I would put the table that's in the file here but it's quite large!

I didn't know what digimon were, so I looked it up and found that they were Japanese digital monsters! :D

## Task 1

Question 1 tasked us with finding the average HP of all the digimon in the dataset. 

I noticed that this task was similar to the one asked about the penguin dataset. Hence, I attempted to use the same method that I used before. 

I created a dictionary called `digimon_data`, and it contained empty lists for each column in the csv file. Next, I appended the values in each column to the corresponding list in the dictionary. 

Therefore, I got:

```
import csv
with open("digimon.csv", "r") as f:

data = csv.DictReader(f)

digimon_data = {
	"Number": [],
	"Digimon": [],
	"Stage": [],
	"Type": [],
	"Attribute": [],
	"Memory": [],
	"Equip Slots": [],
	"HP": [],
	"SP": [],
	"Atk": [],
	"Def": [],
	"Int": [],
	"Spd": []
}

   for row in data:

       digimon_data["Number"].append(row['Number'])
       digimon_data["Digimon"].append(row['Digimon'])
       digimon_data["Stage"].append(row['Stage'])
       digimon_data["Type"].append(row['Type'])
       digimon_data["Attribute"].append(row['Attribute'])
       digimon_data["Memory"].append(row['Memory'])
       digimon_data["Equip Slots"].append(int(row['Equip Slots']))
       digimon_data["HP"].append(int(row['HP']))
       digimon_data["SP"].append(int(row['SP']))
       digimon_data["Atk"].append(int(row['Atk']))
       digimon_data["Def"].append(int(row['Def']))
       digimon_data["Int"].append(int(row['Int']))
       digimon_data["Spd"].append(int(row['Spd']))
```

After that, I found the average of the HP values in the list by adding them, and then dividing that value by the length of the list. 

Hence, I got:

```
hp_avg = sum(digimon_data["HP"])/len(digimon_data["HP"])
   print(f'The average HP of all Digimon is: {hp_avg}')
```

*Note: I didn’t like how it took so many lines to create the dictionary. As a result, I did lots of trial and error.*

*For example, I tried including just the HP row and appending the values into that row, but then I realized that I would need all of the values of every column in order to answer question 2.*

*I also tried setting ‘digimon_data’ as an empty dictionary. Then, I made the first level within the dictionary `[row['Digimon']]`. After, I made the second level consist of separate lists of each row in the csv file, containing the corresponding int/str values:*

```
digimon_data = {}

for row in data:

digimon_data[row['Digimon']] = {
	'Stage': str(row['Stage']), 
	'Type': str(row['Type']), 
	'Attribute': str(row['Attribute']), 
	'Memory': int(row['Memory']), 
	'Equip Slots': int(row['Equip Slots']), 
	'HP': int(row['HP']), 
	'SP': int(row['SP']), 
	'Atk': int(row['Atk']), 
	'Def': int(row['Def']), 
	'Int': int(row['Int']), 
	'Spd': int(row['Spd']) }
```

*However, after I tried finding the average of the HP values, I kept getting error messages that I couldn’t divide by a string, or that the list was not iterable.*

*With the same dictionary, I attempted to change the method I used to find the average, instead using the `count` function. However, the code still did not result in the correct output.*

Even after lots of thinking, trial and error, and talking with my peers (Siddhant and Ruby), I couldn’t find a way to make it shorter. I would’ve liked to meet with Ms Feng about it, but I was sick and didn’t have the same frees on Friday or Monday. D:

## Task 2

Question 2 tasked us with creating a function that could count the number of Digimon with any specific attribute. 

At first, I had no idea how to proceed! I looked up how to create/define your own function on Python, and Google said to use the `def` function. Hence, I did that for `count_digimon`:

```
def count_digimon(attribute, value):
```

I realized that making the function work for values in the dataset would be more difficult than creating the desired output for data outside of the dataset. Hence, I used an `if` statement to show what would happen if values outside of the dataset were entered into the function:

```
if attribute not in digimon_data:
	return 0
```

(which makes sense because the output of the function is always a number). 

However, I needed a statement for what would happen if the input was in the dataset. Hence, I thought, “Hm, I need a line that counts (or adds up) how many times a value appears in a given attribute in the column of the csv file. For each time it does appear, I want to add 1 to the output.”

Starting with the return function, I them came to the line:

```
return sum(1 for item in digimon_data[attribute] if item == value)
```

Then, I came up with a way to enter the attribute and value into the function, and the mode in which the output is displayed:

```
att_input = input("Enter an attribute: ")
val_input = input("Enter a value: ")
   
digimon_count = count_digimon(att_input, val_input)
print(f"The number of Digimon that follow those parameters are: {digimon_count}")
```

## Task 3

Question 3 tasked us with finding ONE POSSIBLE TEAM of up to 3 digimons with a memory of up to 15 and an attack of at least 300. 

Since we only needed to find one possible team, I decided to find a one possible team of 3 digimon that followed the constraints. 

I started thinking about the question like a system of equations:

```
x + y + z <= 15
p + q + r >= 300
```

(where x, y, and z were memory values of the 3 Digimon, and p, q, and r were their attack values.)

After analyzing the problem more, I thought that I needed a way to map the name of each digimon to their (and others’) memory and attack values. 

Hence, I created a nested dictionary that contained the names of the digimon, and their corresponding memory and attack values:

```
digimon_mem_atk = {}

for row in data:
	digimon_mem_atk[row['Digimon']] = {
           'Memory': int(row['Memory']),
           'Atk': int(row['Atk'])
       }
```

After that, I hit a bit of a road block. So, I got my whiteboard out and drew the different lists/dictionaries that I would need in the form of a mind map. I knew that I would start with the nested dictionary containing the memory and attack values for each Digimon. Then, I said that I wanted to end with a list of sets of three Digimon *whose parameters fit the criteria*. So, in my head, I thought, “What are the steps in-between?” 

I expanded on the italicized above. In order to achieve the last step, I would need *two lists that identify the total memory and attack values of any three given Digimon.* Then, I would need to select the sets whose total memory <= 15 and total attack >= 300 and append them into the final set of teams. 

Then, I expanded on the italicized above. After some thinking (and some Googling on Python functions and collaborating with my peers), I realized I could achieve that using a for loop, which could run through all the possible combinations of 3 Digimon and could find the resulting memory/attack value based on how many Digimon were in the nested dictionary. 

Then, after trying some code, I realized that I needed to be able to access the information stored in the original nested dictionary using keys. 

As a result, I got the chunk of code that answered Q3!

## Conclusion

I learned how to overcome errors that I encounter when coding and think creatively about problems given a specific set of tools. Additionally, I learned how to effectively use nested dictionaries and loops! My code could probably be condensed even more, and I tried to find ways to do so, but I wasn’t really sure how to do that. In the future, though, as we learn more tools, I might be able to come back to this and apply what I've learned throughout the year. Overall, this was a fun lab!

