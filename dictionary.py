import json
import difflib

def load_dictionary(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading dictionary:", e)
        return None

def get_definition(dictionary, word, case_sensitive=False):
    if not case_sensitive:
        word = word.lower()
    return dictionary.get(word)

def suggest_similar_words(word, dictionary, cutoff=0.8):
    suggestions = difflib.get_close_matches(word, dictionary.keys(), n=3, cutoff=cutoff)
    return suggestions

dictionary = load_dictionary("dictionary.json")
if dictionary is None:
    exit()

while True:
    user_word = input("Enter a word to search (or 'q' to quit): ")
    if user_word.lower() == 'q':
        break
    if not user_word.isalpha():
        print("Please enter a valid word.")
        continue

    definition = get_definition(dictionary, user_word)
    if definition:
        print(f"\nDefinition: {definition}\n")
    else:
        suggestions = suggest_similar_words(user_word, dictionary)
        if suggestions:
            print(f"Word '{user_word}' not found. Did you mean:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
        else:
            print(f"Word '{user_word}' not found in the dictionary.")

print("\nExiting program.")
