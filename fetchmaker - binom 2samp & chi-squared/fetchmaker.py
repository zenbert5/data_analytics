import pandas as pd
import numpy as np

dogs = pd.read_csv("dog_data.csv")

def get_attribute(breed, attribute):
	return dogs[dogs["breed"] == breed][attribute]

def get_weight(breed):
	return dogs[dogs["breed"] == breed]["weight"]

def get_tail_length(breed):
	return dogs[dogs["breed"] == breed]["tail_length"]

def get_color(breed):
	return dogs[dogs["breed"] == breed]["color"]

def get_age(breed):
	return dogs[dogs["breed"] == breed]["age"]

def get_is_rescue(breed):
	return dogs[dogs["breed"] == breed]["is_rescue"]

def get_likes_children(breed):
	return dogs[dogs["breed"] == breed]["likes_children"]

def get_is_hypoallergenic(breed):
	return dogs[dogs["breed"] == breed]["is_hypoallergenic"]

def get_name(breed):
	return dogs[dogs["breed"] == breed]["name"]
