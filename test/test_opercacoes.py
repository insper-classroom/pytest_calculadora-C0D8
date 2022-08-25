import pytest 
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores
import numpy as np

@pytest.mark.op_simples
def test_soma_dois_valores_positivos () :
    v1 = 5.0
    v2 = 8.0 
    assert 13 == soma(v1, v2)



@pytest.mark.op_simples
def test_subtracao_dois_valores_positivos () :
    v1 = 8.0
    v2 = 5.0 
    assert 3 == sub(v1, v2)



@pytest.mark.op_complexas
def test_multiplicacao_dois_valores_positivos () :
    v1 = 5.0
    v2 = 8.0 
    assert 40 == multiplicacao(v1, v2)



@pytest.mark.op_complexas
def test_divisao_dois_valores_positivos () :
    v1 = 10.0
    v2 = 2.0 
    assert 5 == divisao(v1, v2)



@pytest.mark.op_complexas
def test_media_lista_de_valores_positivos () :
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert 5.5 == media_lista_valores(lista)


@pytest.mark.exercicio_1
@pytest.mark.op_complexas
def test_media_lista_de_valores_positivos_com_valores_nao_numericos () :
    lista = [1, 2, 3, 4, 5, 6, '2','m', 7, 8, 9, 10]
    assert 5.5 == media_lista_valores(lista)


@pytest.mark.exercicio_1
@pytest.mark.op_complexas
def test_media_lista_de_valores_vazia () :
    lista = []
    assert 0 == media_lista_valores(lista)



@pytest.mark.exercicio_1
@pytest.mark.op_complexas
def test_divisao_com_denominador_zero () :
    v1 = 10.0
    v2 = 0
    assert np.inf == divisao(v1, v2)