
# import random
# import string
#
# def randomPassword(charecters):
#     letters = string.ascii_letters
#     # password = ""
#     # for x in range(charecters):
#     #     password += random.choice(letters)
#     # return password
#     return ''.join(random.choice(letters) for x in range(charecters))

idno = "2020"
name = "RAVITEJA"
contact = "8919318221"
email = "rama@gmail.com"

# password=str(int(idno)+len(name))
password=contact[0]+(str(int(idno)+len(name)))+contact[-1]
# x = int(len(password)/2)
password = email[0]+password[:(int(len(password)/2))]+email[1]+password[(int(len(password)/2)):]+email[2]
print(password)
print(type(password))

# print(type(password))
# print(password)
# print(len(password))

# print(password)
# print(name[0])
# print(name[-1])
# print(name[-1])
# print(email[0:3])