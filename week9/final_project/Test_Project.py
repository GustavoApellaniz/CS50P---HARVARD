import trab_Montadora as m

def test_trab_montadora():
    c1 = m.Montadora(3,'SP','Toyota Brasil')
    assert c1.get_cod() == 3
    assert c1.get_estado() == 'SP'
    assert c1.get_razao_social() == 'Toyota Brasil'

def test_trab_modelo():
    m1 = m.Modelo(5, 'GTR', 'FIAT')
    assert m1.get_cod() == 5
    assert m1.get_nome_modelo() == 'GTR'
    assert m1.get_montadora() == 'FIAT'

def test_trab_carro():
    c1 = m.Carro('CS50','GT turbo','1987')
    assert c1.get_placa() == 'CS50'
    assert c1.get_nome_modelo() == 'GT turbo'
    assert c1.get_ano_fabricacao() == '1987'


def test_modelo_criacao():
    montadora = m.Montadora(1, "SP", "Toyota Brasil")
    modelo = m.Modelo(10, "Corolla", montadora)
    assert modelo.get_cod() == 10
    assert modelo.get_nome_modelo() == "Corolla"
    assert modelo.get_montadora() == montadora
