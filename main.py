def get_ingredients():
    ingredients = []
    print('List all of your ingredients and press the Enter key after each indivdual ingredient. Press the Enter key again when finished.:')
    while True:
        ingredient = input()
        if ingredient:
            ingredients.append(ingredient)
        else:
            break
    return ingredients

def main():

    ingredients = get_ingredients()
    if ingredients:
        print('Your ingredients are: \n' + '\n'.join(ingredients))
    else:
        print('There were no ingredients entered.')

if __name__ == "__main__":
    main()