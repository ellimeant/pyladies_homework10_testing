#read in the file
poem_file = open('input.txt', encoding="utf-8")
content = poem_file.read()
print(content)

characters = len(content) # characters in the poem string
print("This poem contains", characters, "characters.")

word_list = content.split()
print("This poem has", len(word_list), "words.")

many_words = len(word_list)


specifics = content.count("and") # count specific words
print("The word 'and' appears ",specifics, "times.")

with open(r"input.txt", "r", encoding="utf-8") as goblin: # it needs the encoding too beacuse there seems to be an odd symbol somewhere.
    lines = len(goblin.readlines())
    print("Total number of lines: ", lines)


new_file = "output.txt"

#I found out about the write() function: it only takes 1 argument at a time, and it must be a string. Hence, I modified the above.
with open(new_file, "w", encoding="utf-8") as output_file:
    output_file.write("The excerpt from Goblin Market contains")
    output_file.write(many_words)
    output_file.write("words. These words and all other elements of the text make up ")
    output_file.write(characters)
    output_file.write("You can read them on")
    output_file.write(lines)
    output_file.write("lines. Enjoy!")
print(f"File{output_file} created successfully.")
#poem_file.close()          can't count lines in poem_file if this is in the code.