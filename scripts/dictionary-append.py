#!/usr/bin/env python3

import datetime
import shutil
import sys

if len(sys.argv) < 3:
    print("Spouštějte tento skript se dvěma argumenty. "
          "První je slovník, do kterého chcete přidávat slova. "
          "Druhý je soubor obsahující nová slova.")
    quit()

DIACRITICS = "ěščřžýáíéúůóťďňĚŠČŘŽÝÁÍÉÚŮŤĎŇ"
NO_DIACRITICS = "escrzyaieuuotdnESCRZYAIEUUTDN"


def remove_diacritics(input_word):
    result = ""
    for char in input_word:
        if char in DIACRITICS:
            result += NO_DIACRITICS[DIACRITICS.index(char)]
        else:
            result += char
    return result


dictionary = sys.argv[1]
new = sys.argv[2]

with open(dictionary) as dictionary_file:
    dictionary_words = dictionary_file.read().splitlines()

with open(new) as new_file:
    new_words = new_file.read().splitlines()

print(f"Původní slovník obsahoval {len(dictionary_words)} slov.")

new_words_all = new_words.copy()

for word in new_words:
    no_dia_word = remove_diacritics(word)
    new_words_all.append(no_dia_word)

dictionary_words = list(set(dictionary_words + new_words_all))

dictionary_words.sort(key=lambda s: (len(s), s))

timestamp = str(datetime.datetime.now().timestamp()).replace(".", "")
shutil.copyfile(dictionary, f"{dictionary}.{timestamp}.old")

with open(dictionary, "w") as file:
    file.write("\n".join(dictionary_words) + "\n")

print(f"Nový slovník obsahuje {len(dictionary_words)} slov.\n")
print(f"Původní slovník zálohován do \"{dictionary}.{timestamp}.old\"")
