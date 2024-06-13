#!/usr/bin/env python3

#return_text_value() function
#AUthor ID: yzabala@myseneca.ca

cafeteria_food = ["sushi","mexican food","burger","ramen"]

for food in cafeteria_food:
    answer = input("Do you like " + food + " (y/n):")
   
# We can use a dictionary to save the user's responses associated with the "food" items.