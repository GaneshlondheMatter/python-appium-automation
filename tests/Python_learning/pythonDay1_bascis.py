# # #Variables and Data Types
# a=10
# print(type(a))  #int
# user_name="JohnDoe"
# print(user_name)
# is_logged_in=True
# print(is_logged_in)

#unsing if else and while loop for password validation with limited attempts.
# attempt = 3
# while attempt > 0:
#     passws = input("Enter your password: ")
#     if passws == "12345":
#         print("Access granted")
#         break
#     else:
#         attempt -= 1
#         print(f"Incorrect password. You have {attempt} attempts left.")
        
#     if attempt == 0:
#         print("Access denied. No attempts left.")


attempt = 2
while attempt > 0:
    password = input('enter your pass')
    if password == '123':
        print ('access grantes')
        break
    else: 
        attempt -= 1
        print (f'incorrect pass. you have {attempt} attempts left')
    if attempt == 0:
        print (' access denied')