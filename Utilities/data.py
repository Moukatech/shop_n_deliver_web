import pandas as pd
import os
import random
import string

def generate_phone_number_and_password():
# Generate an 8-digit random number
    # eight_digit_number = random.randint(10000000, 99999999)

    # print(eight_digit_number)
    mobile_num = ""
    prefex = "07" + str(random.randrange(10 ** (8 - 1), 10 ** 8))
    mobile_num=prefex
    
    password_length = 6
    password_string = ''.join(random.choices(string.ascii_lowercase, k=password_length))
    
    return mobile_num, password_string
    
def get_login_data():
    file_path = os.path.join(os.path.dirname(__file__),'..','users.xlsx')

    df = pd.read_excel(file_path)
    data_list = df.to_dict(orient='records')
    User = data_list[0]["phone_number"]
    Pass = data_list[0]["Password"]
    return User, Pass
    
