#! /urs/bin/env python3

import requests
import textwrap


def show_title():
    """ 
        This method displays title to screen 
    """ 
    print("The Recipes Program")


def show_menu():
    """ 
        This method displays menu to screen
    """ 
    print("\nCOMMAND MENU\n"
          "1 - List all Categories \n"
          "2 - List all Meals for a Category \n"
          "3 - Seach Meal by Name \n"
          "4 - Random Meal \n"
          "5 - List all Areas \n"
          "6 - Search Meals by Area \n"
          "7 - Menu \n"
          "0 - Exit the program")

  
def list_meals_by_category(categories): 
  """ 
      This method prompts user to enter a Category and display the meal        
      list based on the Category 
  """
  lookup_category = input("Enter a Category: ")

  found = False
  if categories is None:
      print("Technical difficulties, please try again later!")
  else:
      for i in range(len(categories)):
        category = categories[i]
        if category.get_name().lower() == lookup_category.lower():
            found = True
            break

      while found:
          meals = requests.get_meals_by_category(lookup_category)
          display_item_list(lookup_category + " MEALS", meals)
          break
      else:
          print("Invalid Category, please try again. \n"
          "What would you like to do? ")


def display_meal_by_name():
  """ 
      This method prompts user to enter a meal name and will display 
      the meal name and info 
  """
  lookup_meal_name = input("Enter Meal Name: ")
  
  meal_info = requests.get_meal_by_name(lookup_meal_name)
  
  if meal_info is None:
      print("Invalid Meal Name, please try again. \n"
            "What would you like to do? ")
  # Compare user's meal name input with the result of the get_meal_by_name() request. If equal, display meal name and info. 
  # If search request is none, ask user to try again.
  elif meal_info[0].get_name().lower() == lookup_meal_name.lower():
            display_meal("Recipe: ", meal_info)


def list_meals_by_area(areas): 
  """ 
      This method prompts user to enter an Area and display the meal
      list based on the Area 
  """
  lookup_area = input("Enter an Area: ")
  found = False
  
  if areas is None:
      print("Technical difficulties, please try again later!")
  else:
      for i in range(len(areas)):
        area = areas[i]
        if area.get_name().lower() == lookup_area.lower():
            found = True
            break

      while found:
          meals = requests.get_meals_by_area(lookup_area)
          display_item_list(lookup_area + " MEALS", meals)
          break
      else:
          print("Invalid Area, please try again. \n"
          "What would you like to do? ")

      

def display_item_list(title, items):
    """ 
        This method displays the list of meals for a Category or 
        Area on the screen 
    """
    if items is None:
        print("Technical difficulties, please try again later!")
    else:
        print("\n", title.upper())
        for j in range(len(items)):
            item = items[j]
            print("   " + item.get_name())
        print()


def display_meal(title, items):
    """ 
        This method displays the meal name and meal info based on 
        the meal name inputted by user 
    """
    if items is None:
        print("Technical difficulties, please try again later!")
    else:
        strRecipeName = items[0].get_name()
        print("\nRecipe:  ", strRecipeName, sep="")
      
        print("\nInstructions:")
        strInstructions = (items[1].get_name())
        # set recipe intructions text to wrap at 80 characters.
        print('\n'.join(textwrap.wrap(strInstructions, width=80, replace_whitespace=False)))
      
        print("\nIngredients:")
        print('{:<25}{:<20}'.format("Measure", "Ingredient"))
        print("-" * 80)  
        for i in range(19):    
            strMeasure = items[22 + i].get_name()
            strIngredient = items[2 + i].get_name()
            # print measure and ingredient pair even if there is no measurement listed
            if (strMeasure != "" and strIngredient!= "") or \
               (strMeasure == "" and strIngredient!= ""):
              print('{:<25}{:<20}'.format(strMeasure, strIngredient))

 
def main(): 
    """ 
        This method controls the flow of the program 
    """
    show_title()
    show_menu()

    categories = requests.get_categories()
    areas = requests.get_areas()

    while True:
        command = input("\nCommand: ")
        if command == "1":
            display_item_list("CATEGORIES", categories)
        if command == "2":
            list_meals_by_category(categories)
        if command == "3":
            display_meal_by_name()
        if command == "4":
            random_meal = requests.get_random_meal()
            print("\nA random meal was selected just for you!")      
            display_meal("RANDOM MEAL", random_meal)
        if command == "5":
            display_item_list("AREAS", areas)
        if command == "6":
            list_meals_by_area(areas)
        if command == "7":
            show_menu()
        if command == "0":
            print("\nThank you for dining with us!")
            break

          
# Run the program          
if __name__ == "__main__":
    main()

  
    
