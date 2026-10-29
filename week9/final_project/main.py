
class Montadora:
    def __init__(self,cod_montadora: int, estado: str, razao_social: str):
        self.cod_montadora = cod_montadora
        self.estado = estado
        self.razao_social = razao_social
    
    def get_cod(self) -> int:
        return self.cod_montadora
    def get_estado(self) -> str:
        return self.estado
    def get_razao_social(self) -> str:
        return self.razao_social
    
    def set_cod(self,novo_cod: int) -> int:
        self.cod_montadora = novo_cod
    def set_estado(self,novo_estado: str) -> str:
        self.estado = novo_estado
    def set_razao_social(self, novo_razao_social: str) -> str:
        self.razao_social = novo_razao_social
    
    def __str__(self):
        return(f'{self.cod_montadora} {self.estado} {self.razao_social}')


class Modelo:
    def __init__(self, cod_modelo: int, nome_modelo: str, montadora: Montadora):
        self.cod_modelo = cod_modelo
        self.nome_modelo = nome_modelo
        self.montadora = montadora
    

    def get_cod(self):
        return self.cod_modelo
    def get_nome_modelo(self):
        return self.nome_modelo
    def get_montadora(self):
        return self.montadora

    def set_cod(self,novo_cod: int):
        self.cod_modelo = novo_cod
    def set_modelo(self,novo_modelo: str):
        self.nome_modelo = novo_modelo
    def set_montadora(self,nova_montadora: Montadora):
        self.montadora = nova_montadora

    def __str__(self):
        return(f'{self.cod_modelo} {self.nome_modelo} {self.montadora}')


class Carro:
    def __init__(self, atributos_placa: str, nome_modelo: Modelo, ano_fabricacao: int):
        self.atributos_placa = atributos_placa
        self.nome_modelo = nome_modelo
        self.ano_fabricacao = ano_fabricacao

    def get_placa(self):
        return self.atributos_placa
    def get_nome_modelo(self):
        return self.nome_modelo
    def get_ano_fabricacao(self):
        return self.ano_fabricacao
    
    def set_placa(self, nova_placa: str):
        self.atributos_placa = nova_placa
    def set_modelo(self, novo_modelo: Modelo):
        self.nome_modelo = novo_modelo
    def set_ano_fabricacao(self, novo_ano_fabricacao: int):
        self.ano_fabricacao = novo_ano_fabricacao
    
    def __str__(self):
        return f'{self.atributos_placa} {self.nome_modelo} {self.ano_fabricacao}'
    
def main():
    while True:
        try:
            print('''
            1 – Cadastro Montadora
            2 – Cadastro Modelo
            3 - Cadastro Carro
            4 – Listar Montadoras
            5 – Listar Modelos
            6 – Listar Carros
            7 – Sai''')
            
            opcoes = {1: cadastro_montadora,
                    2: cadastro_modelo,
                    3: cadastro_carro,
                    4: listar_montadoras,
                    5: listar_modelos,
                    6: listar_carros}
            escolha = int(input('coloque o número '))

            resultado = opcoes.get(escolha)
            if resultado:
                resultado()
            else:
                print('erro')
            
            if escolha == 7:
                sys.exit('programa encerrado')
        except ValueError:
            print('opção inválida')


montadoras: list[Montadora] = []
modelos: list[Montadora] = []
carros: list[Modelo] = []


def cadastro_montadora():
    cod = input('Cod: ')
    estado = input('Estado: ')
    razao_social = input('razao social: ')
    montadora = Montadora(cod,estado,razao_social)
    montadoras.append(montadora)

def cadastro_modelo():
    if not montadoras:
        print('sem montadoras no sistema')
        return
    else:     
        for m in montadoras:
            print(f"    [{m.get_cod()}] {m.get_razao_social()} ({m.get_estado()})")
        escolha = input('coloque o cod da montadora ')
        for i in montadoras:
            if escolha == i.get_cod():
                cod = input('cod: ')
                nome = input('nome: ')
                montadora = f"{i.get_razao_social()}"
                modelo = Modelo(cod,montadora,nome)
                modelos.append(modelo)
            else:
                print('código inválido')
                return


def cadastro_carro():
    if not modelos:
        print('sem modelos disponíveis')
        return
    else:
        for i in modelos:
            print(f'{i.get_cod()} {i.get_nome_modelo()} {i.get_montadora()}')   
        escolha = input('escolha pelo nome do modelo: ')
        for m in modelos:
            if escolha == m.get_nome_modelo():
                placa = input('placa: ')
                ano = input('ano de fabricação: ')
                carro = Carro(placa,escolha,ano)
                carros.append(carro)
            else:
                print('nome inválido')
                return

def listar_montadoras():
    for m in montadoras:
         print(f"    [{m.get_cod()}] {m.get_razao_social()} ({m.get_estado()})")

def listar_modelos():
     for i in modelos:
            print(f'{i.cod_modelo()} {i.get_nome_modelo()} {i.get_montadora()}')   

def listar_carros():
    for i in carros:
        print(f'{i.get_placa()} {i.get_nome_modelo()} {i.get_ano_fabricacao()}')
        
if __name__ == '__main__':
    m1 = Montadora(5,'RS','TOYOTA')
    c1 = Modelo(4,'gt',m1)

    print(c1.get_montadora())
