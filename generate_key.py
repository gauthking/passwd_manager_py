from cryptography.fernet import Fernet

def generate_key(file_path='secret.key'):
    key = Fernet.generate_key()  
    with open(file_path, 'wb') as key_file:
        key_file.write(key)  
    print(f"Secret key saved to {file_path}")

generate_key()