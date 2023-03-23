# Matthew Schuh
def encode_pass(password): # this is a comment i added
    encoded_pass = ""
    for number in password:
        shifted_number = str((int(number) + 3) % 10)
        encoded_pass += shifted_number
    return encoded_pass

def decode_pass(encoded_pass):
    decoded_pass = ""
    for number in encoded_pass:
        shifted_number = str((int(number) - 3) % 10)
        decoded_pass += shifted_number
    return decoded_pass


# hello here is a comment
# hello here is another comment



program = True
if __name__ == "__main__":
    while program == True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode_pass(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            if encoded_pass:
                decoded_pass = decode_pass(encoded_pass)
                print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.\n")
                pass
        elif option == 3:
            program = False
            break




