import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for element in instance._queue:
        if element["nome_do_arquivo"] == path_file:
            return None

    file_rows = txt_importer(path_file)

    queue_element = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_rows),
        "linhas_do_arquivo": file_rows,
    }

    instance.enqueue(queue_element)
    print(str(queue_element), file=sys.stdout)
    # redireciona o print para saída padrão (stdout)


def remove(instance):
    if instance.__len__() == 0:
        print('Não há elementos', file=sys.stdout)
    else:
        item_removed = instance.dequeue()
        #  extrai valor da chave do dicionario removido
        file_removed = item_removed["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {file_removed} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
