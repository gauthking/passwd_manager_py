MASTER_PWD = "put ur master pwd" 
SECRET_KEY_PATH = ""  

def load_key():
    with open(SECRET_KEY_PATH, 'rb') as key_file:
        return key_file.read()