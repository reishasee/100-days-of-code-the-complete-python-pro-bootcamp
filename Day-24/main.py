with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()

with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

for name in name_list:
    name = name.strip("\n")
    invitation_letter = letter_contents.replace("[name]", name)
    with open(f"Output/letter_for_{name}.txt", mode="w") as output_letter:
        output_letter.write(invitation_letter)
