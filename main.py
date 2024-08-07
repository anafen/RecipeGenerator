from dotenv import load_dotenv
import os
from openai import OpenAI

def get_ingredients():
    ingredients = []
    print('List all of your ingredients and press the Enter key after each indivdual ingredient. Press the Enter key again when finished:')
   
    while True:
        ingredient = input()
        if not ingredient:
            break 

        confirmation = input(f'You entered "{ingredient}". Is this correct? (yes/no): ').strip().lower()

        if confirmation == 'yes':
            ingredients.append(ingredient)
        else:
            print("Let's try again.")

    return ingredients

def generateRecipe(client, ings, use_only_listed):
    ings_words = ", ".join(ings)
    prompt = "Generate a recipe from the listed ingredients: " + ings_words

    if not use_only_listed:
        prompt += " and any additional ingredients as needed."
    else:
        prompt += " do not use any ingredients that the user did not input."

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a chef with masterful alchemist of flavors, effortlessly blending creativity, technical skill, and an unwavering passion for crafting unforgettable culinary experiences."},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Access the OpenAI API key
    openai_api_key = os.getenv('OPENAI_API_KEY')
    client = OpenAI()

    ingredients = get_ingredients()
    recipe = None
    
    if ingredients:
        print('Your ingredients are: \n' + '\n'.join(ingredients))
        use_only_listed = input('Do you want the recipe generator to use only the listed ingredients to generate a recipe? (yes/no): ').strip().lower()

        if use_only_listed == 'yes':
            print('Generating a recipe using only the listed ingredients...')
            recipe = generateRecipe(client, ingredients, True)
        else:
            print('Generating a recipe using the listed ingredients and any required additional ingredients...')
            recipe = generateRecipe(client, ingredients, False)
        
        print(recipe)
    
    else:
        print('There were no ingredients entered.')

if __name__ == "__main__":
    main()