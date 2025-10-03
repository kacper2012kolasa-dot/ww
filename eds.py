word = input("Wpisz słowo, którego nie rozumiesz:").upper()
meme_dict = {
    "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
    "LOL": "Częsta reakcja na coś zabawnego"
}

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("nie mam tego w systemie")