from cryptography.fernet import Fernet

def load_key():
    return open("./secret.key", "rb").read()

def encrypt_pwd(password, key):
    f = Fernet(key)
    encrypted_passwd = f.encrypt(password.encode())
    return encrypted_passwd

def decrypt_pwd(encrypted_pwd, key):
    f = Fernet(key)
    decrypted_passwd = f.decrypt(encrypted_pwd).decode()
    return decrypted_passwd

