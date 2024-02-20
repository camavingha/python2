# Dictionary
d = {'chess': 1, 'butter': 2, 'ant': 3, 'dip': 4, 'salt': 5, 'sugar': 6, 'elephant': 7}

# Function to check if key exists in the dictionary
def check_key_existence(key):
    if key in d:
        return "Yes, key is exist."
    else:
        return "No, key is not exist."

# Test cases
key_to_check = input("Input key to check : ").strip()

result = check_key_existence(key_to_check)
print(result)
