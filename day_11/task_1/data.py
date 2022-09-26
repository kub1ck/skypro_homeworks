def get_data(file_path) -> list:
    with open(file_path) as file:
        return file.readlines()
