"""
	Data Analytics Intro - Code Academy
		Assignment: 	Betty's Bakery
		Author	  :	Shawn Chen
 	 	Date:	  :	Jan 1, 2018
"""
import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
ingredients = np.array(['Flour', 'Sugar', 'Eggs', 'Milk', 'Butter'])
recipe_names = np.array(['Cupcakes', 'Pancake', 'Cookie', 'Bread'])


# load recipes with csv
recipes = np.genfromtxt("recipes.csv", delimiter=',')
print recipes

# get all the value of eggs
eggs = recipes[:,2]

# 1 egg?
yes_eggs = [x==1 for x in eggs]
egg_map = zip (recipe_names, yes_eggs)
print egg_map

# get cookies
cookies = recipes[2,:]

# calculate 2 batch of cupcakes
double_batch = cupcakes * 2

# add up all the ingredients to buy
grocery_list = cookies + double_batch

# create an eaiser read
better_list = zip(ingredients, grocery_list)

print better_list
