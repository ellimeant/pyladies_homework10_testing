#Task 1: The following Python program contains four common programming errors. For each error that you find, write its line number and a brief description of the problem.
#I have not copied the incorrect code because it would throw the error messages. Here are the things that I identified:
# line 2: you need to add int() around the input so that num is recognised as a number in line 5 and 7. Otherwise, it cannot return e.g. "***" or "==="
# line 6: else if should be elif
# line 8: else needs to be followed by a :

#Task 2: correct the code:
def find_max(numbers):
  if not numbers:
    return None
  max_value = numbers[0]
  for num in numbers:
    if num > max_value:
      max_value = num
  return max_value


numbers = [3, 5, 7, 2, 8]
print(find_max(numbers))  # Expected output: 8


numbers = []
print(find_max(numbers))  # Expected output: Error message or appropriate handling

#What are the issues in the given script?
#The code needs to be aware that there is no limit to indices (no matter how high or if there are none).
#How did you identify and fix them?
#It would not read in the indices in the list "numbers". fix by adding if not numbers: return None; to give the program a way out.
#How would you handle an empty list in this function?
# the return None also handles empty lists because it will then return "None".


#Task 3:

#read in the file
poem_file = open('input.txt', encoding="utf-8")
content = poem_file.read()
print(content)

characters = str(len(content)) # characters in the poem string
print("This poem contains", characters, "characters.")

word_list = (content.split())
print("This poem has", len(word_list), "words.")

delete_char = " "
while delete_char in word_list:
    word_list.remove(delete_char)
print(word_list)

many_words = str(len(word_list))


specifics = content.count("and") # count specific words
print("The word 'and' appears ",specifics, "times.")

with open(r"input.txt", "r", encoding="utf-8") as goblin: # it needs the encoding too beacuse there seems to be an odd symbol somewhere.
    lines = str(len(goblin.readlines()))
    print("Total number of lines: ", lines)


new_file = "output.txt"

#I found out about the write() function: it only takes 1 argument at a time, and it must be a string. Hence, I modified the above.
with open(new_file, "w", encoding="utf-8") as output_file:
    output_file.write("The excerpt from Goblin Market contains ")
    output_file.write(str(many_words))
    output_file.write(" words. These words and all other elements of the text make up ")
    output_file.write(characters)
    output_file.write(" characters. You can read them on ")
    output_file.write(lines)
    output_file.write(" lines. Enjoy!")
print(f"File{output_file} created successfully.")


#test to open the output.txt file:
output_successful = open('input.txt', encoding="utf-8")
output_is_successful = poem_file.read()
print(output_is_successful)

#poem_file.close()          can't count lines in poem_file if this is in the code.


# Task 4: What is a breakpoint, and how is it used in debugging?
# The b(reak) function is used to invoke a breakpoint in the Python De-Bugger and indicates a specific line or function where we want to stop the code to run to investigate it.


# Task 5: How can you handle exceptions in Python as a debugging step?
# You can debug code by writing tests that raise exceptions. There you can already find the bugs and remove them because you know which error is caused.