from dotenv import load_dotenv
import os
from openai import OpenAI

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

def generateReceipe(client, ings):
    ings_words = ", ".join(ings)
    prompt = "Generate a recipe from the listed ingredients: " + ings_words

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
    if ingredients:
        print('Your ingredients are: \n' + '\n'.join(ingredients))
    else:
        print('There were no ingredients entered.')

    recipe = generateReceipe(client, ingredients)
    print(recipe)
if __name__ == "__main__":
    main()