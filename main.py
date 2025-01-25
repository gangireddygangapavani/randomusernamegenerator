import random
import string

# Predefined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Brave", "Sunny", "Smart", "Lazy", "Strong"]
nouns = ["Tiger", "Dragon", "Eagle", "Panda", "Wolf", "Fox", "Bear"]

# Function to generate random username
def generate_username():
    # Combine random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    # Ask user for customization options
    add_numbers = input("Do you want to include numbers in the username? (y/n): ").lower() == 'y'
    add_special = input("Do you want to include special characters? (y/n): ").lower() == 'y'
    max_length = input("Enter the maximum length for the username (leave empty for no limit): ")

    # Add random number
    if add_numbers:
        username += str(random.randint(0, 99))
   
    # Add special character
    if add_special:
        username += random.choice(string.punctuation)

    # Adjust length if specified
    if max_length.isdigit():
        username = username[:int(max_length)]

    return username

# Function to save usernames to a file
def save_usernames_to_file(usernames, file_name="usernames.txt"):
    with open(file_name, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to '{file_name}'")

# Main program
def main():
    print("Welcome to the Random Username Generator!")
   
    # Ask user how many usernames to generate
    try:
        count = int(input("How many usernames would you like to generate? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    usernames = []
    for _ in range(count):
        username = generate_username()
        usernames.append(username)
        print(f"Generated Username: {username}")

    # Save usernames to a file
    save_to_file = input("Do you want to save these usernames to a file? (y/n): ").lower() == 'y'
    if save_to_file:
        save_usernames_to_file(usernames)

# Run the program
if _name_ == "_main_":
    main()
