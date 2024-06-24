#read in the file
poem_file = open('input.txt', encoding="utf-8")
content = poem_file.read()
print(content)

characters = len(content) # characters in the poem string
print("This poem contains", characters, "characters.")

word_list = content.split()
print("This poem has", len(word_list), "words.")




specifics = content.count("and") # count specific words
print("The word 'and' appears ",specifics, "times.")

with open(r"input.txt", "r", encoding="utf-8") as goblin: # it needs the encoding too beacuse there seems to be an odd symbol somewhere.
    lines = len(goblin.readlines())
    print("Total number of lines: ", lines)

#poem_file.close()          can't count lines in poem_file if this is in the code.