from abc import ABC, abstractmethod
class email(ABC):
    @abstractmethod
    def login(self):
        pass
class email_create(email):
    def login(self):
        global email,password
        email=input("Enter your email: ")
        if len(email) < 5 or "@" not in email:
            print("Invalid email format. Please try again.")
        else:
            password=input("Enter your password: ")
            print("Email created successfully.")
class email_login(email):
    def login(self):
        print("to login enter your email")
        email_input=input("Enter your email: ")
        if len(email_input) < 5 or "@" not in email_input:
            print("Invalid email format. Please try again.")
        else: 
         password_input=input("Enter your password: ")
        if email_input == email and password_input == password:
            print("Login successful.")
        else:
            print("Invalid email or password. Please try again.")
email_create().login()
if len(email) >= 5 and "@" in email:
    email_login().login()
else:    print("Email creation failed. Cannot proceed to login.")
save=input("Do you want to save your email and password? (yes/no): ")
if save.lower() == "yes":
    with open("credentials.txt", "w") as file:
        file.write(f"Email: {email}\nPassword: {password}\n")
    print("Credentials saved successfully.")
else:
    print("Credentials not saved.")



    


   
 





