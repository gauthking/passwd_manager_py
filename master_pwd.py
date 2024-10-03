import getpass

def verify_master_pwd(stored_pwd):
    input_pwd = getpass.getpass("Enter the MASTER PWD: ")
    if input_pwd == stored_pwd:
        return True
    else:
        print("Incorrect master Password!!")
        return False
