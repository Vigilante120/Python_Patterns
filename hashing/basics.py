# Creating a dictionary
phonebook = {
    "Alice": "123-4567",
    "Bob": "987-6543",
    "Charlie": "555-1234"
}

# Accessing a value by key
print(phonebook["Bob"])  # Output: 987-6543

# Adding a new key-value pair
phonebook["David"] = "111-2222"

# Checking if a key exists
if "Alice" in phonebook:
    print("Alice's number is", phonebook["Alice"])
