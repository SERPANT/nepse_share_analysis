

def read_file(file_path):
    file = open(file_path, "r")
    contents = file.read()
    file.close()

    return contents
