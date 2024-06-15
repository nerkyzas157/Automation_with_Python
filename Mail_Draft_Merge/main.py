with open(
    "Input\\Names\\invited_names.txt", mode="r"
) as name_file:
    name_list = name_file.readlines()
    for i in name_list:
        name = i.strip("\n")
        starting_letter = open(
            "Input\\Letters\\starting_letter.txt"
        )
        letter_draft = starting_letter.read()
        starting_letter.close()
        with open(
            f"Output\\ReadyToSend\\{name}.txt",
            mode="w+",
        ) as personal_letter:
            personal_letter.write(letter_draft.replace("[name]", name))
