import os


def replaceId(filePath, old, new):
    with open(filePath, "r") as reading_file:
        new_file_content = ""
        for line in reading_file:
            print(line)
            stripped_line = line.strip()
            print(stripped_line)
            oldId = stripped_line.split(' ')[0]
            print(oldId)
            if(oldId == old):
                newId = new
                print(newId)
            else:
                print((filePath, oldId))
            new_line = stripped_line.replace(oldId, newId, 1)
            new_file_content += new_line + "\n"
    with open(filePath, "w") as writing_file:
        writing_file.write(new_file_content)


# pass the path of folder
path = r'D:/Mangal/LOGIBRICKS/objects/CALENDER/Images(labels)'
for file in os.listdir(path):
    if file.endswith('.txt'):
        replaceId(path + '/' + file, "519", "538")
