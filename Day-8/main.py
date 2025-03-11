from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    #If encode_or_decode is equal to 'decode,' multiply the shift number by -1
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        #If the character or string is not in the alphabet (e.g. !@#$%12345), add the character to the crypted text as is.
        if letter not in alphabet:
            output_text += letter
        #Otherwise, determine the crypted character based on the shift amount and add it to the crypted text
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

end_game = False

while not end_game:

    #Check if the input in direction is either 'decode' or 'encode.' Otherwise, the user will be asked again to enter a correct input.
    direction_answer = False
    while not direction_answer:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

        if direction != "encode" and direction != "decode":
            print("You've entered an invalid input. Please try again.")
        else:
            direction_answer = True

    text = input("Type your message:\n").lower()

    #Check if the input in shift is a number. Otherwise, the user will be asked again to enter a correct input.
    shift_answer = False
    while not shift_answer:
        shift = input("Type the shift number:\n")

        if shift.isnumeric():
            shift_answer = True
            shift = int(shift)
        else:
            print("You've entered an invalid input. Please try again")

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    #Check if the input is either 'y' or 'n.' Otherwise, the user will be asked again to enter a correct input.
    y_or_n_answer = False
    while not y_or_n_answer:
        y_or_n = input("Type 'Y' for YES if you want to continue. Otherwise, type 'N' for NO. ").lower()
        if y_or_n == "n":
            end_game = True
            y_or_n_answer = True
            print("Thank you for using Caesar Cipher. Have a nice day!")
        elif y_or_n != "n" and y_or_n != "y":
            print("You've entered an invalid input. Please try again.")
        else:
            y_or_n_answer = True
