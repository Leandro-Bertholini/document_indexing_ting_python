import sys


def txt_importer(path_file):
    file_name = path_file.split(".")

    if file_name[-1] != "txt":
        return sys.stderr.write("Formato inválido")

    try:
        with open(path_file, "r") as file:
            data = file.read()
            return data.split('\n')
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
