#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()

with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

for name in name_list:
    name = name.strip("\n")
    invitation_letter = letter_contents.replace("[name]", name)
    with open(f"Output/letter_for_{name}.txt", mode="w") as output_letter:
        output_letter.write(invitation_letter)




