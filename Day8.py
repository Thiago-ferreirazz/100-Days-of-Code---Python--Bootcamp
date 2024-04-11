# Logo for the program
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# List representing the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Initialize variable to control the program loop
answer = False

# Function to perform Caesar cipher encryption or decryption
def caesar(text, shift, direction):
    new_text = ""
    # Adjust shift direction for decoding
    if direction == "decode":
         shift *= -1
    # Iterate through each character in the input text
    for letter in text:
        # Check if the character is in the alphabet
        if letter in alphabet:
            # Find the position of the character in the alphabet
            position = alphabet.index(letter)
            # Calculate the new position after applying the shift
            new_position = (position + shift) % 26
            # Append the shifted character to the new text
            new_text += alphabet[new_position]
        else:
            # Preserve non-alphabetic characters in the text
            new_text += letter
    # Display the result
    print(f"Your {direction}d text with a {shift} shift is: {new_text}")

# Main program loop
while not answer:
    # Prompt the user for the encryption/decryption direction
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
    # Prompt the user for the message to be encrypted/decrypted
    text = input("Type your message: ").lower()
    # Prompt the user for the shift value
    shift = int(input("Type the shift number: "))
    
    # Call the Caesar function with the provided inputs
    caesar(text, shift, direction)
    
    # Ask the user if they want to run the program again
    cont = input("\nDo you want to run again? Type [yes] or [no]: ").lower()
    if cont == "no":
        answer = True
        print("Goodbye")

    
    
