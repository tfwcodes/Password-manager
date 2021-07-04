from cryptography.fernet import Fernet

print(
"""

                  _ __   __ _ ___ _____      _____  _ __ __| |
                 | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |
                 | |_) | (_| \__ \__ \\ V  V / (_) | | | (_| |
                 | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
                 |_|
                 ~>Simple password manager app<~
                ~~>Created By tfwcodes(github)<~~
                  _ __ ___   __ _ _ __   __ _  __ _  ___ _ __
                 | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|
                 | | | | | | (_| | | | | (_| | (_| |  __/ |
                 |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|
                                              |___/

"""
)
while True:
   try:
      # The help menu
      print("Enter --help or help for the help menu")
      # Enter a command
      x = input("[+] Enter the command: ")
      if x == "help" or x == "--help":
         # All the options
         print("[!] Enter 1 to create a strong password that cant be cracked" + "\n" + "[!] Enter 2 to save your username and password into a file" + "\n" + "[!] Enter Ctrl + C to exit the program")
      if x == "1":
         # Generate a strong password
         key = Fernet.generate_key()
         print(key)
      if x == "2":
         print("The file will be named by the app you use")
         z = input("[+] What app do you use for the username and password: ")
         u = input("[+] What is the username: ")
         p = input("[+] What is the password: ")
         # Name the file by the app you use
         file1 = open(z, "w")
         # Write the app, username and the password into the file
         file1.write("App: " + z + "\n" + "Username: " + u + "\n" +  "Password: " + p)
         # Close the file
         file1.close()
   # If the user presses Ctrl+C it will exit the program
   except KeyboardInterrupt:
      exit()
