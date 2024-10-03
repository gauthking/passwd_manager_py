from cryptography.fernet import Fernet

# Function to generate and store the encryption key
def generate_key(file_path='secret.key'):
    key = Fernet.generate_key()  # Generate a random key
    with open(file_path, 'wb') as key_file:
        key_file.write(key)  # Store the key in a file
    print(f"Secret key saved to {file_path}")

# Call this function once to generate the key
generate_key()