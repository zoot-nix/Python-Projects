import time
entered_email = input("Enter Email: ").strip()
name = entered_email[:entered_email.index('@')]
domain = entered_email[entered_email.index('@') +1:]
if '.' in name:
    fname = name[:name.index('.')]
    lname = name[name.index('.') +1:]
    print("Your First Name is "+fname+" and Last Name is "+lname+" and your domain is "+domain)
else:
    print("Your name is "+name+" and your domain is "+domain)
    
