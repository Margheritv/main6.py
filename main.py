def transform_to_row(infile, outfile):
    with open(infile, 'r') as reader:  # opens the file text
        contents = reader.read()  # the content von dem text soll gelesen werden
        content_list = contents.split(",")  # the split wird mit dem Beistrich identifiziert

    # print(content_list)

    with open(outfile, 'w') as writer:  # opens new output file with my name on it
        for element in content_list:  # for every el in list
            writer.write(element)  # write el in new file (outfile)
            writer.write("\n")  # insert the separator - new line


def add_greeting(infile, outfile):
    with open(infile, 'r') as reader:
        contents = reader.readlines()
        # print(contents)

    with open(outfile, 'w') as writer:
        for element in contents:
            element = 'Hello ' + element
            writer.write(element)

def strip_greeting(infile, outfile):
    with open(infile, 'r') as reader:
        contents = reader.readlines()
        # print(contents)

    with open(outfile, 'w') as writer:
        for element in contents:
            element = element[6:]   # el = el from out2 but starting from index 6
            writer.write(element)

def combine_files(file1, file2, outfile):
    with open(file1, 'r') as reader1:
        with open(file2, 'r') as reader2:
            with open(outfile, 'w') as writer:
                reader1 = reader1.readlines()
                reader2 = reader2.readlines()

                if len(reader1) != len(reader2):    # raise exc. creates personal error basically
                    raise Exception('It only allows files with the same number of lines.')
                else:
                    for element in range(len(reader1)):
                        element = reader1[element].strip() + " " + reader2[element]
                        writer.write(element)


print(transform_to_row('text.txt', 'outfile.txt'))
print(add_greeting('outfile.txt', 'output2.txt'))
print(strip_greeting('output2.txt', 'greeting2.txt'))
print(combine_files('output2.txt', 'surnames.txt', 'output3'))