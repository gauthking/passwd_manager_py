import json
import os
from crypto_utils import encrypt_pwd, decrypt_pwd

def save_pwds(data, file="passwords.json"):
    with open(file, 'w') as f:
        json.dump(data, f)

def load_pwds(file="passwords.json"):
    if os.path.exists(file):
        with open(file,"r") as f:
            return json.load(f)
    return {}

def add_pwd(service, pwd, master_key):
    passwords = load_pwds()
    encrypted_pwd = encrypt_pwd(pwd, master_key)
    passwords[service] = encrypted_pwd.decode()
    save_pwds(passwords)
    print(f"Password for {service} stored successfully!!")

def get_pwd(service, master_key):
    passwords = load_pwds()
    if service in passwords:
        encrypt_pwd = passwords[service].encode()
        password = decrypt_pwd(encrypt_pwd, master_key)
        print(f"Password for {service}: {password}")
    else:
        print(f"No password found for {service}")

def update_pwd(service, new_password, master_key):
    passwords = load_pwds()
    if service in passwords:
        encrypted_password = encrypt_pwd(new_password, master_key)
        passwords[service] = encrypted_password.decode()
        save_pwds(passwords)
        print(f"Password for {service} updated!")
    else:
        print(f"No password found for {service}")

def delete_pwd(service):
    passwords = load_pwds()
    if service in passwords:
        del passwords[service]
        save_pwds(passwords)
        print(f"Password for {service} deleted!")
    else:
        print(f"No password found for {service}")
