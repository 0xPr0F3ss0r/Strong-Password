import random as rand
import string
from colorama import init, Fore, Style
import math
import os
import time
# Initialize colorama
init(autoreset=True)
banner = '''  #####                                          ######                                                   
#     # ##### #####   ####  #    #  ####        #     #   ##    ####   ####  #    #  ####  #####  #####  
#         #   #    # #    # ##   # #    #       #     #  #  #  #      #      #    # #    # #    # #    # 
 #####    #   #    # #    # # #  # #      ##### ######  #    #  ####   ####  #    # #    # #    # #    # 
      #   #   #####  #    # #  # # #  ###       #       ######      #      # # ## # #    # #####  #    # 
#     #   #   #   #  #    # #   ## #    #       #       #    # #    # #    # ##  ## #    # #   #  #    # 
 #####    #   #    #  ####  #    #  ####        #       #    #  ####   ####  #    #  ####  #    # #####  '''

text_color = Fore.GREEN  # Green text
text_style = Style.BRIGHT  # Bright style
password_color = Fore.BLUE # blue password text
text_color_red  = Fore.RED
password = ""
def seconds_to_years(seconds):
    seconds_per_year = 60 * 60 * 24 * 365  # 31,536,000
    years = seconds / seconds_per_year
    return years
# Print the banner with styles
print(text_style + text_color + banner,'\n')
print("enter 'exit' if you want to left")
while True:
    password = input("enter you password #> ")
    if str(password).startswith("exit"):
        os.system("cls")
        break
    if len(password) > 6:
        print(text_color_red+"password must be at most 6 characters")
    elif len(password) < 4:
        print(text_color_red+"password must be at least 4 characters")
    else:
        upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J','K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        other_char = ['@','#','$','!','<','>']

        small_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        digit = [0,1,2,3,4,5,6,7,8,9]
        while len(password) < 10:
            for i in range(2):
                first_char = rand.choice(upper_case)
                password += first_char
                second_char = rand.choice(other_char)
                password += second_char
                third_char = rand.choice(small_case)
                password += third_char
                fourth_char = rand.choice(digit)
                password += str(fourth_char)
        print("your password is"+text_style+password_color+' '+password)
        password_length = len(password)
        ten_guess = 2*math.log2(78 ** password_length) / 10
        years = seconds_to_years(ten_guess)
        print(f"Time to crack this password when use 10 guess : {years} years")
        tweenty_guess = (2*math.log2(78 ** password_length)) / 20
        years = seconds_to_years(tweenty_guess)
        print(f"Time to crack this password when use 20 guess : {years} years")
