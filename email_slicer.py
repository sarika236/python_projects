'''
while True:
    email = input("enter ur mail: ").strip()
    username = email[:email.index("@")]
    domain_name = email[email.index("@"):]
    format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
    print(format_)
'''
user_input = str(input("enter e-mail address :"))
result = user_input.split("@")
print('username :',result[0])
print('domain name :',result[1])