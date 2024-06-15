try:
    file = open("nonexist.txt", 'r')
    content = file.read()
    file.close()
except FileNotFoundError:
    print("File not found !!!")