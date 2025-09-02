email = input("Enter your email address: ")

if "@" in email:
    domain = email.split('@')[1]
    print(f"Domain: {domain}")
else:
    print("Not a regular email address!")