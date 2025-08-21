import re

def normalize_phone(phone):
    pattern = r'^[0-9+\-()]+'
    if not re.fullmatch(pattern, phone):
        raise ValueError("Invalid phone number format")
    
    phone = re.sub(r"[^\d+]", "", phone)
    
    if phone.startswith('+380'):
        return phone

    if phone.startswith('380'): 
        return '+' + phone

    if phone.startswith('0'):
        return '+38' + phone
    
def normalize_name(name):
    name = name.strip()
    
    pattern = r'^[A-Za-z]+'
    if not re.fullmatch(pattern, name):
        raise ValueError("Invalid name format")
    
    return name.capitalize()

def add_contact(args, contacts):
    name, phone = args
    name = normalize_name(name)
    phone = normalize_phone(phone)
    contacts[name] = phone
    return f"Contact added. Name: {name}, Phone: {phone}"

def change_contact(args, contacts):
    if len(args) < 2:
        return "Please provide a name and new phone number."
        

    name, new_phone = normalize_name(args[0]), args[1]
    if name in contacts:
        try:
            new_phone = normalize_phone(new_phone)
            contacts[name] = new_phone
            return f"Contact {name} updated. New phone: {new_phone}"
        except ValueError as e:
            return f"Error: {e}"
    else:
        return f"Contact {name} not found."

def show_phone(args, contacts):
    if not args:
        return "Please provide a name."
    
    name = normalize_name(args[0])
    if name in contacts:
        return f"{name}'s phone: {contacts[name]}"
    else:
        return f"Contact {name} not found."

def show_all(contacts):
    if not contacts:
        return "No contacts saved yet."
    else:
        lines = ["Contacts list:"]
        for name, phone in contacts.items():
            lines.append(f"- {name}: {phone}")
        return "\n".join(lines)

