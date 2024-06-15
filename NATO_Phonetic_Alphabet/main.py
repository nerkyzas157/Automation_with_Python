import pandas  # type: ignore


# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv(
    "nato_phonetic_alphabet.csv"
)
dictionary = {row.letter: row.code for (index, row) in df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def gen_phonetic():
    word = input("Please enter a word you'd like to get phonetic letters for: ").upper()
    word_in_list = [i for i in word]
    try:
        nato_word = [dictionary[l] for l in word_in_list if l in dictionary]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        gen_phonetic()
    else:
        print(nato_word)


# Launching the app:
gen_phonetic()
