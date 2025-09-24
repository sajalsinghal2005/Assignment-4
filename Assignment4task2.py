user_input = input("Enter text to write to the file: ")

# Step 1: Write input to file
file1 = open('output.txt', "w")
file1.write(user_input + "\n")
file1.close()
print("Data successfully written to output.txt.\n")

# Step 2: Append extra text
append_input = input("Enter additional text to append: ")
file2 = open("output.txt", "a")
file2.write(append_input + "\n")
file2.close()
print("Data successfully appended.\n")

# Step 3: Read final content
print("Final content of output.txt:")
file3 = open("output.txt", "r")
reading_file = file3.read()
print(reading_file)
file3.close()
