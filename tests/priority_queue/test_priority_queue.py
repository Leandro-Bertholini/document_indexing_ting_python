from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    has_priority = PriorityQueue()

    # Teste de prioridade na fila, retornando o valor correto
    has_priority.enqueue({"qtd_linhas": 3})
    has_priority.enqueue({"qtd_linhas": 4})
    has_priority.enqueue({"qtd_linhas": 2})
    has_priority.enqueue({"qtd_linhas": 10})
    has_priority.enqueue({"qtd_linhas": 15})

    assert has_priority.dequeue() == {"qtd_linhas": 3}

    assert has_priority.search(0) == {"qtd_linhas": 2}

    with pytest.raises(IndexError) as e:
        has_priority.search(1)

    assert str(e.value) == "Índice Inválido ou Inexistente"
    
# dica: ***
# Para usar a mensagem com o tipo de erro dentro do raises    
# with pytest.raises(TypeError, match="tipo inválido para message"):
#     # Código que deve gerar a exceção
