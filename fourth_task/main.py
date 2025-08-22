from parser import parse_input
from handler import add_contact, change_contact, show_phone, show_all

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter command: ")
            command, *args = parse_input(user_input)
    
            if command == 'add':
                print(add_contact(args, contacts))
            elif command == 'change':
                print(change_contact(args, contacts))
            elif command == 'phone':
                print(show_phone(args, contacts))
            elif command == 'all':
                print(show_all(contacts))
            elif command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == 'hello':
                print("Hello! How can I help you?")
            else:
                print("Unknown command.")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()