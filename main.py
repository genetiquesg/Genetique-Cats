def main():
    # Print the banner
    print("Welcome to Genetique Cats - https://genetiquebengals.com")

    # Options
    options = {
        "1": ("Kitten available", "https://genetiquebengals.com/adopt-available-kittens/"),
        "2": ("Kitten waiting list", "https://genetiquebengals.com/kitten-adoption-waiting-list-form-singapore/"),
        "3": ("Suitability form", "https://genetiquebengals.com/suitability-form/"),
        "4": ("[Quiz] What cat breed are you?", "https://genetiquebengals.com/what-breed-of-cat-are-you/"),
        "5": ("Contact us", "https://genetiquebengals.com/contact-us/"),
        "6": ("Whatsapp us", "https://wa.me/6586170470")
    }

    # Display options
    for key, (text, url) in options.items():
        print(f"{key}) {text} - {url}")

    # User input for selection
    choice = input("Please select an option: ")

    # Process the user input
    if choice in options:
        print(f"You selected: {options[choice][0]}")
        print(f"URL: {options[choice][1]}")
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
