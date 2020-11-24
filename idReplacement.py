import os


def replaceId(filePath, old, new):
    reading_file = open(filePath, "r")
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
    reading_file.close()

    writing_file = open(filePath, "w")
    writing_file.write(new_file_content)
    writing_file.close()


# pass the path of folder
path = r'D:/Mangal/LOGIBRICKS/objects/CALENDER/Images(labels)'
for file in os.listdir(path):
    if file.endswith('.txt'):
        replaceId(path + '/' + file, "519", "538")
