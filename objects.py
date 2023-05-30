


import os
import time


class add_user:
    def __init__(self, name, phone, cvv):
        self.name = name
        self.phone = phone
        self.cvv = cvv

    """def new_user(self):
        user_info = self.name, self.phone, self.cvv"""

    def display_info(self):
        print(f"""    "This Is How Your Info Has Been Saved" 
Name: {self.name} 
Phone number: {self.phone} 
Cvv: {self.cvv} """)


class atm:
    def __init__(self, phone, cvv):
        self.balance = None
        self.phone = phone
        self.cvv = cvv

    """def add_bal(deposit):
        amount = deposit"""

    def show_bal(self, balance):
        self.balance = balance
        print(balance)

    def display_info(self):
        print(f"just to make sure let's go over your information, "
              f"so your phone number is {self.phone} "
              f"and your cvv is {self.cvv}"
              f"and your balance is {self.balance}")


class change_ball:
    def __init__(self, phone, cvv):
        self.balance = None
        self.phone = phone
        self.cvv = cvv


class home:
    def __init__(self, qa, answer):
        self.qa = qa
        self.answer = answer

    def Gohome(self):
        qa = home(qa=input("Please Press 'ANY KEY' To Go To The Main Menu").upper(), answer="H")
        if qa.qa != qa.answer:
            print("Restarting...")
            time.sleep(2)  # 200ms to CTR+C twice
            os.system("python main.py")
            quit()
        else:
            print("Restarting...")
            time.sleep(2)  # 200ms to CTR+C twice
            os.system("python main.py")
            quit()




