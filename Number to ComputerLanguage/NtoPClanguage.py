print("\033[1;32m Welcome to Number to Computer Language\033[m")

Number = int(input("Type the number here:\n"))

if len(str(Number)) > 7: # If is "big" than 7 or equals to 7
    Question_A1 = input(f"Do you want to convert {str(Number)[:7]}... \033[1;32mto bin (binary), oct (octal) or hexa (hexadecimal)?\033[m\n").strip().lower()
    if Question_A1 == "bin" or Question_A1 == "binary": 
        print(bin(f"\033[1;32m{Number[2:]}\033[m")) # Binary (0 and 1)
    elif Question_A1 == "oct" or Question_A1 == "octal":
        print(oct(f"\033[1;35m{Number[2:]}\033[m")[2:]) # Octal (8)
    elif Question_A1 == "hexa" or Question_A1 == "hexadecimal":
        print(hex(f"\033[1;33m{Number[2:]}\033[m")[2:]) # Hexadecimal (16)
    else:
        print(f"Error! You typed {Question_A1}") # Please code... DON'T DO AN ERROR!!!!!!!
elif len(str(Number)) <= 7: # If is "small" than 7
    Question_A1 = input(f"Do you want to convert {str(Number)} \033[1;32mto bin (binary), oct (octal) or hexa (hexadecimal)?\033[m\n").strip().lower()
    if Question_A1 == "bin" or Question_A1 == "binary": 
        print(bin(f"\033[1;32m{Number[2:]}\033[m")) # Binary (0 and 1)
    elif Question_A1 == "oct" or Question_A1 == "octal":
        print(oct(f"\033[1;35m{Number[2:]}\033[m")[2:]) # Octal (8)
    elif Question_A1 == "hexa" or Question_A1 == "hexadecimal":
        print(hex(f"\033[1;33m{Number[2:]}\033[m")[2:]) # Hexadecimal (16)
    else:
        print(f"Error! You typed {Question_A1}") # Please code, again, DON'T DO AN ERROR!!!!!!!
else: # else :skull:
    print(f"Error! You typed {Number}") # Please code, double again, DON'T DO AN ERROR!!!!!!!