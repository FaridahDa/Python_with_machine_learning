import numpy as np
import pandas as pd

titanic_dataset = pd.read_csv('train.csv')

print(titanic_dataset)


def check_login():
    user_details = {"username": "Faridah", "password": "faridah123"}
    username = input(" Please enter your username:")
    password = input("please enter your password:")
    if username == user_details["username"] and password == user_details["password"]:
        print(f"Welcome {username}")
    else:
        print("welcome")


check_login()
