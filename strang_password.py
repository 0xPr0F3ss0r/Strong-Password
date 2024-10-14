import random as rand
from colorama import init, Fore, Style

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
# Print the banner with styles
print(text_style + text_color + banner,'\n')
while True:
    password = input("enter you password #> ")
    if len(password) > 6:
        print(text_color_red+"password must be at most 6 characters")
    elif len(password) < 4:
        print(text_color_red+"password must be at least 4 characters")
    else:
        upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J','K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        other_char = ['@','#','$','!','<','>']

        small_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        while len(password) < 10:
            for i in range(2):
                first_char = rand.choice(upper_case)
                password += first_char
                second_char = rand.choice(other_char)
                password += second_char
                third_char = rand.choice(small_case)
                password += third_char
        print("your password is"+text_style+password_color+' '+password)



