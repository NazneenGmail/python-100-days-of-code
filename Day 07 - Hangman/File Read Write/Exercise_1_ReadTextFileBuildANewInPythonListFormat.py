with open("words.txt") as f:
    content_list = f.readlines()

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)

with open("../HangmanWordsList.py", "w") as writeHandleToFile:
    writeHandleToFile.write("word_list = [\n")
    for word in content_list:
        writeHandleToFile.write(f"'{word}',\n")
    writeHandleToFile.write("]")