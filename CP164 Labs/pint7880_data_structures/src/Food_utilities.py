"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    name = input("Name: ")
    origin = int(input(Food.origins()))
    
    is_vegetarian = input('Vegetarian (Y/N):')
    
    if is_vegetarian == 'Y':
        is_vegetarian = True
    else:
        is_vegetarian = False
        
    calories = int(input("Calories: "))
    
    food = Food(name, origin, is_vegetarian, calories)
    
    
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    line = line.split("|")
    name = line[0]
    origin = int(line[1])
    
    if line[2] == "True":
        is_vegetarian = True
    else:
        is_vegetarian = False
        
    calories = int(line[3])
    
    food = Food(name, origin, is_vegetarian, calories)

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_food(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - a file of food data (file)
    Returns:
        foods - a list of food objects (list of food)
    -------------------------------------------------------
    """
    line = file_variable.readline()
    foods = []
    
    while line != "":
        a = read_food(line)
        foods.append(a)
        
        line = file_variable.readline()


    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    for i in foods:
        i.write(file_variable)

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    veggies = []
    for i in foods:
        if i.is_vegetarian == True:
            veggies.append(i)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    origins = []
    
    for i in foods:
        if i.origin == origin:
            origins.append(i)
    
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    calories = []
    
    for i in foods:
        calories.append(i.calories)
    
    total = 0
    for i in calories:
        total = total + i
        
    avg = total // len(calories)

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    
    avg = average_calories(foods)
   
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    foods.sort()
    
    print("Food                                Origin       Vegetarian Calories")
    
    print("----------------------------------- ------------ ---------- --------")
    
    
    for i in foods:
        name = i.name
        origin = Food.ORIGIN[i.origin]
        vegetarian = i.is_vegetarian
        
        if vegetarian == 0:
            veg_out = "False"
        else:
            veg_out = "True"

        calories = i.calories

        print('{:<36}{:<13}{:<11}{:<9}'.format(name, origin, veg_out, calories))


    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []
    
    if max_cals == 0:
        max_cals = 99999999
        
    if is_veg == False:
        is_veg = True
    
    for i in foods:
        if i.origin == origin:
            if i.is_vegetarian == is_veg:
                if i.calories < max_cals:
                    result.append(i)

    return result
