def input_to_output(text_file, outcome):
    poem_file = open(text_file, encoding="utf-8")
    content = poem_file.read()
    print(content)
    characters = str(len(content))
    word_list = (content.split())
    print("This poem contains", characters, "characters.")
    delete_char = " "
    while delete_char in word_list:
        word_list.remove(delete_char)
    print(word_list)
    print("This poem has", len(word_list), "words.")
    with open(text_file, "r", encoding="utf-8") as goblin:
        lines = str(len(goblin.readlines()))
    print("Total number of lines: ", lines)
    new_file = outcome
    with open(new_file, "w", encoding="utf-8") as output_file:
        output_file.write("The excerpt from Goblin Market contains ")
        output_file.write(str(len(word_list)))
        output_file.write(" words. These words and all other elements of the text make up ")
        output_file.write(characters)
        output_file.write(" characters. You can read them on ")
        output_file.write(lines)
        output_file.write(" lines. Enjoy!")
    print(f"File{output_file} created successfully.")


input_to_output("input.txt", "return.txt")