alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

import CC_art


def caesar(plain_text, shift_amount, cypher_direction):
    cypher = ""
    for char in plain_text:
        if char in alphabet:
            if cypher_direction == "encode":
                x = alphabet.index(char) + shift_amount
                if x >= len(alphabet):
                    x -= len(alphabet)
                cypher += alphabet[x]
            elif cypher_direction == "decode":
                x = alphabet.index(char) - shift_amount
                cypher += alphabet[x]
        else:
            cypher += char
    print(f"The {cypher_direction}d text is '{cypher}'")


print(CC_art.logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text=text, shift_amount=shift, cypher_direction=direction)
    choice = input("\nWould you like to crypt again? (y/n) ").lower()
    if choice == "n":
        print("Goodbye!")
        break
