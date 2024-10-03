MASTER_PWD = "butterscotch_sambhar" 
SECRET_KEY_PATH = "D:\MainFolders\programcodestuff\python\passwd_manager\secret.key"  

def load_key():
    with open(SECRET_KEY_PATH, 'rb') as key_file:
        return key_file.read()