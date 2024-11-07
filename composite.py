import unittest

from abc import ABC, abstractmethod

class Aluguel(ABC):
    @abstractmethod
    def get_custo(self):
        pass

    @abstractmethod
    def get_descricao(self):
        pass

class Carro(Aluguel):
    def __init__(self, modelo, custo):
        self.modelo = modelo
        self.custo = custo

    def get_custo(self):
        return self.custo

    def get_descricao(self):
        return f"Carro: {self.modelo}"
    
class ServicoAdicional(Aluguel):
    def __init__(self, descricao, custo):
        self.descricao = descricao
        self.custo = custo

    def get_custo(self):
        return self.custo

    def get_descricao(self):
        return f"Serviço adicional: {self.descricao}"
    
class PacoteAluguel(Aluguel):
    def __init__(self):
        self.itens = []

    def add_item(self, item):
        self.itens.append(item)

    def remove_item(self, item):
        self.itens.remove(item)

    def get_custo(self):
        return sum(item.get_custo() for item in self.itens)

    def get_descricao(self):
        return " + ".join(item.get_descricao() for item in self.itens)
    
if __name__ == "__main__":
    carro_basico = Carro("Fusca", 150)
    carro_luxo = Carro("Opala 3", 300)

    gps = ServicoAdicional("GPS", 20)
    seguro = ServicoAdicional("Seguro", 50)

    pacote_basico = PacoteAluguel()
    pacote_basico.add_item(carro_basico)
    pacote_basico.add_item(gps)

    pacote_completo = PacoteAluguel()
    pacote_completo.add_item(carro_luxo)
    pacote_completo.add_item(gps)
    pacote_completo.add_item(seguro)

    print(f"Pacote básico: {pacote_basico.get_descricao()}, Custo total: R${pacote_basico.get_custo()}")
    print(f"Pacote completo: {pacote_completo.get_descricao()}, Custo total: R${pacote_completo.get_custo()}")

