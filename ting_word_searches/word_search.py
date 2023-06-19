def exists_word(word, instance):
    found_files = []

    for i in range(len(instance)):
        word_rows = []
        for e, line in enumerate(instance.search(i)["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                word_rows.append({"linha": e + 1})

        if word_rows:
            found_files.append({
                "palavra": word,
                "arquivo": instance.search(i)['nome_do_arquivo'],
                "ocorrencias": word_rows,
            })

    return found_files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
