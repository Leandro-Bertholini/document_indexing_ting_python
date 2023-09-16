# `Projeto Document Indexing(ting) - Python (Estrutura de dados)`

## Visão Geral
Neste projeto, usando a linguagem **Python** no contexto da programação orientada a objetos(**POO**), eu implementei um programa que simule um algoritmo de indexação de documentos. A aplicação é capaz de identificar ocorrências de termos em arquivos _TXT_. Para isto, o programa foi desenvolvido em dois módulos:

- **Módulo de gerenciamento de arquivos** que permite anexar arquivos de texto (formato _TXT_) e;
- **Módulo de buscas** que permite operar funções de busca sobre os arquivos anexados.

⚠️ **Neste projeto não iremos focar na análise de significados ou busca por sinônimos.**


## Habilidades exercitadas
- Manipular Pilhas;
- Manipular Deque;
- Manipular Nó & Listas Ligadas.

## Tecnologias Utilizadas
- Python
- pytest
- Flake8
- VS Code

<details>
<summary> 🗄️ <strong>Execução Local do Projeto:</strong></summary><br>

Para executar, clone esse repositório com o comando:

    git clone git@github.com:Leandro-Bertholini/document_indexing_ting_python.git

Entre na pasta do projeto e crie o ambiente virtual:

    python3 -m venv .venv 


Ative o ambiente virtual:

    source .venv/bin/activate

Instale as dependências no ambiente virtual:

    python3 -m pip install -r dev-requirements.txt

**OBS:** Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente. Quando precisar desativar o ambiente virtual, execute o comando deactivate. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.
O arquivo `dev-requirements.txt` contém todas as dependências usadas no projeto.

***Para Executar os Testes***:

    Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

    python3 -m pytest
</details>

## Fases de Construção:

### Pacote `ting_file_management`

<details>
<summary><strong>Fase 1 - Foi Implementado uma fila para armazenar os arquivos que serão lidos</strong></summary><br>

- Nesta etapa, implementei a classe `Queue`, presente no arquivo `queue.py` utilizando as estruturas vistas no módulo durante o curso.

- A fila (Queue) é uma estrutura `FIFO`, ou seja, o primeiro item a entrar, deve ser o primeiro a sair. Utilizei seus conhecimentos de estruturas de dados para otimizar as operações implementadas.

- A fila implementou os métodos de inserção (`enqueue`), remoção (`dequeue`) e busca (`search`).

- O tamanho da fila foi exposto utilizando o método `__len__` que permitiu, após implementado, o uso do comando `len(instancia_da_fila)` para se obter o tamanho da fila.

- Na busca uma exceção do tipo `IndexError` com a seguinte mensagem: `"Índice Inválido ou Inexistente"` deve ser lançada caso um índice inválido seja passado. Para uma fila com `N` elementos, índices válidos são inteiros entre `0` e `N-1`.

<strong>Validações Feitas:</strong>

- 1.1 - Foi validado que o método `enqueue` deve adicionar um elemento à fila, modificando seu tamanho;

- 1.2 - Foi validado que o método `dequeue` deve remover o elemento a mais tempo na fila, modificando seu tamanho;

- 1.3 - Foi validado que o método `search` deve retornar um valor da fila a partir de um índice válido e;

- 1.4 - Foi validado que o método `search` deve lançar a exceção `IndexError` com a mensagem correspondente quando o índice passado for inválido.
</details> 

<br>
<details>
<summary><strong>Fase 2 - Foi Implementado uma função txt_importer dentro do módulo file_management capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.</strong></summary><br>

- Caso o arquivo TXT não exista, deve ser exibida a mensagem `Arquivo {path_file} não encontrado` na `stderr`, em que `{path_file}` é o caminho do arquivo;

- Caso a extensão do arquivo seja diferente de .txt, deve ser exibida a mensagem `Formato inválido` na `stderr`;

- A função deve retornar uma lista contendo as linhas do arquivo.

<strong>Validações Feitas:</strong>

- 2.1 - Foi validado que o método `txt_importer` deve retornar uma lista contendo as linhas do arquivo;

- 2.2 - Foi validado que ao executar o método `txt_importer` com um arquivo TXT que não exista, deve ser exibida a mensagem `Arquivo {path_file} não encontrado` na `stderr`, em que `{path_file}` é o caminho do arquivo e;

- 2.3 - Foi validado que ao executar o método `txt_importer` com uma extensão diferente de `.txt`, deve ser exibida a mensagem `Formato inválido` na `stderr`.

</details> 

<br>
<details>
<summary><strong>Fase 3 - Implementada a função process no módulo file_process. Essa função deverá ser capaz de transformar o conteúdo da lista gerada pela função txt_importer em um dicionário que será armazenado dentro da Queue.</strong></summary><br>

- A função irá receber como parâmetro um objeto instanciado da fila implementada e o caminho para um arquivo;

- A instância da fila recebida por parâmetro **deve** ser utilizada para registrar o processamento dos arquivos;

- A função deve processar o arquivo passado por parâmetro (ou seja, gerar um dicionário com o formato e informações especificadas abaixo);

- Deve-se ignorar arquivos que já tenham sido processados anteriormente (ou seja, arquivos com o mesmo nome e caminho (`nome_do_arquivo`) não devem ser readicionados a fila);

- Após cada nova inserção válida, a função deve mostrar via `stdout` os dados processados, conforme estrutura no exemplo abaixo.

<details>
<summary><b>Exemplo da estrutura de saída:</b></summary>

```python
{
    "nome_do_arquivo": "arquivo_teste.txt", # Caminho do arquivo recém adicionado
    "qtd_linhas": 3,                        # Quantidade de linhas existentes no arquivo
    "linhas_do_arquivo": [...]              # linhas retornadas pela função do requisito 2
}
```
</details>

<br>
<strong>Validações Feitas:</strong>

- 3.1 - Foi validado que ao executar a função `process` com um arquivo já existente na fila a execução deverá ignorá-lo e;

- 3.2 - Foi validado que ao executar a função `process` com sucesso deverá mostrar dados via `stdout`.

</details> 

<br>
<details>
<summary><strong>Fase 4 - Implementado uma função **remove** dentro do módulo file_process capaz de remover o primeiro arquivo processado</strong></summary><br>

- A função recebe como parâmetro uma fila implementada;

- Caso não existam arquivos na fila, a função emiti a mensagem `Não há elementos` via `stdout`;

- Em caso de sucesso de remoção, é emitida a mensagem `Arquivo {path_file} removido com sucesso` via `stdout`, em que `{path_file}` é o caminho do arquivo.

<strong>Validações Feitas:</strong>

- 4.1 - Foi validado que ao executar a função `remove` com sucesso deverá exibir mensagem correta via `stdout` e;

- 4.2 - Foi validado que ao executar a função `remove` um arquivo inexistente deverá exibir a mensagem correta via `stdout`.

</details> 

<br>
<details>
<summary><strong>Fase 5 - Implementado uma função *file_metadata dentro do módulo *file_process capaz de apresentar as informações superficiais de um arquivo processado.</strong></summary><br>

- A função recebe como parâmetro a fila implementada no requisito 1 e o índice a ser buscado;

- Caso a posição não exista, deve ser exibida a mensagem de erro `Posição inválida` via `stderr`;

- Caso a posição seja válida, as informações relacionadas ao arquivo devem ser mostradas via `stdout`, seguindo o exemplo de estrutura abaixo.

<details>
<summary><b>Exemplo da estrutura de saída em caso de sucesso:</b></summary>

```python
{
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [...]
}
```
</details>

<br>
<strong>Validações Feitas:</strong>

- 5.1 - Foi validado que ao executar a função `file_metadata` com sucesso deverá exibir a mensagem correta via `stdout` e;

- 5.2 - Foi validado que ao executar a função `file_metadata` com posição inválida deverá exibir a mensagem correta via `stderr`.

</details> 

<br>
<details>
<summary><strong>Fase 6 - Implementado os testes para a classe `PriorityQueue` capaz de armazenar arquivos pequenos de forma prioritária.</strong></summary><br>

> Implemente em: tests/priority_queue/test_priority_queue.py

Foi implementado testes para a classe `PriorityQueue`, garantindo que a lógica de prioridades seja respeitada pelos métodos `enqueue`, `dequeue` e `search`.

Para estes testes que esperemos que falhe, o requisito será considerado atendido quando a resposta do Pytest for `XFAIL(Expected Fail)` ao invés de `PASS` ou `FAIL`.
</details> 

<br>

## Pacote `ting_word_searches`
<br>
<details>
<summary><strong>Fase 7 - Implementado uma função `exists_word`, dentro do módulo `word_search`, que verifique a existência de uma palavra em todos os arquivos processados.</strong></summary><br>

- A função irá receber como parâmetros a palavra a ser buscada e a fila implementada;

- A função deve retornar uma lista com as informações de cada arquivo e suas linhas em que a palavra foi encontrada, conforme exemplo da estrutura de retorno;

- A busca deve ser _case insensitive_ (não diferenciar maiúsculas e minúsculas);

- Caso a palavra não seja encontrada em nenhum arquivo, deve-se retornar uma lista vazia;

- A fila não deve ser modificada durante a busca. Ela deve permanecer com os mesmos arquivos processados antes e depois da busca.

<br>
<details>
<summary><b>Exemplo da estrutura de retorno:</b></summary>

```python
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 2
    },
    {
      "linha": 7
    }
  ]
}]
```

</details>

<br>
<br>
<strong>Validações Feitas:</strong>

 - 7.1 - Foi validado que ao executar a função `exists_word` com sucesso deverá retornar a estrutura correta;

- 7.2 - Foi validado que ao executar a função `exists_word` com palavra inexistente deverá retornar uma lista vazia e;

- 7.3 - Foi validado que ao executar a função `exists_word` a fila original não deverá ser alterada.

</details>

<br>
<details>
<summary><strong>Fase 8 - (Implementação pendente) Deverá ser implementada uma função `search_by_word` dentro do módulo `word_search`, que busque uma palavra em todos os arquivos processados.</strong></summary><br>

- Esta função deverá seguir os mesmos critérios da fase seis, mas deverá incluir na saída o conteúdo das linhas encontradas, conforme exemplo da estrutura de retorno.

<details>
<summary><b>Exemplo da estrutura de retorno:</b></summary>

```python
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 3,
      "conteudo": "Acima de tudo,"
    },
    {
      "linha": 4,
      "conteudo": "é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga"
    }
  ]
}]
```

</details>


<strong>Validações a serem feitas:</strong>

- 8.1 - Será validado que ao executar a função `search_by_word` com sucesso deverá retornar a estrutura correta;

- 8.2 - Será validado que ao executar a função `search_by_word` com palavra inexistente deverá retornar uma lista vazia e;

- 8.3 - Será validado que ao executar a função `search_by_word` a fila original não deverá ser alterada.

</details>


### Criação do projeto:

- Trybe - Curso de Desenvolvimento Web


###  ☝ Desenvolvimento da aplicação:

- Leandro Bertholini





