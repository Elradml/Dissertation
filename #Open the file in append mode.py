# Open the file in append mode
with open('myfile.txt', 'a') as f:
    # List of lines to add
    lines_to_add = ['This is line 1.', 'This is line 2.', 'This is line 3.']

    # Loop through the lines to add, using enumerate to get the index
    for index, line in enumerate(lines_to_add, start=1):  # start=1 to
        # Write the line to the file
            f.write(f"{index}: {line}\n")  # Write the index and line,