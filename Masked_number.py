def mask_phone_number(phone):
    return "******" + phone[-4:]


phone = input("Enter your phone number:- ")
print("Mobile number:-", mask_phone_number(phone))
