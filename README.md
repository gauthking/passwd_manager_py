
# Password Manager - FERNET ENCRYPTION

This python script can be configured to be used as a command line tool for password manager CRUD operations.

After cloning the project,
-  make sure to set the master password and secret key path (absolute) inside the config.py file.
-  create a .bat file that contains the following script and link the path to this .bat file in your system path variables.
```bash
@echo off
python "path_to\main.py" %*
```
- for powershell config, edit the .$PROFILE file with the following script and reload the profile file to apply the changes accordingly
```bash
Set-Alias pm "D:\Scripts\password_manager.bat"
```

