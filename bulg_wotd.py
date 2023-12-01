# This file reads in bulgarian words, and gives a random word as "word of the day"

import random

with open("wordlist_bulg.txt", "r") as file:
    no_of_lines = len(file.readlines())

word = ""

fp = open("wordlist_bulg.txt", "r")
while True:
    number = random.randint(40, no_of_lines)
    for i, line in enumerate(fp):
        if i == number:
            if len(line) > 2:
                with open("used_words.txt", "r") as fr:
                    had_lines = fr.readlines()
                    if line not in had_lines:
                        word = line
                if word == line:
                    break
    if word != "":
        break

fp.close()

print("Today's word of the day is:", word)
with open("used_words.txt", "a") as fw:
    fw.write(word)
