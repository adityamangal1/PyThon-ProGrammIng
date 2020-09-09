import os


def soldier(path, file_name):
    os.chdir(path)
    os.rename(file_name, file_name.capitalize())
    print('Renamed successfully')


if __name__ == '__main__':
    user = input('Enter the directory\n')
    input = input('Enter the file name you want to rename\n')
    soldier(user, input)

