from composite import *

class TestAluguel(unittest.TestCase):
    def test_criar_carro(self):
        carro = Carro("Fusca", 150)
        self.assertEqual(carro.get_custo(), 150)
        self.assertEqual(carro.get_descricao(), "Carro: Fusca")

    def test_criar_servico_adicional(self):
        seguro = ServicoAdicional("Seguro", 50)
        self.assertEqual(seguro.get_custo(), 50)
        self.assertEqual(seguro.get_descricao(), "Serviço adicional: Seguro")


    def test_pacote_aluguel_com_carro_e_servico(self):
        carro = Carro("Fusca", 150)
        gps = ServicoAdicional("GPS", 20)
        pacote = PacoteAluguel()
        pacote.add_item(carro)
        pacote.add_item(gps)
        self.assertEqual(pacote.get_custo(), 170)
        self.assertEqual(pacote.get_descricao(), "Carro: Fusca + Serviço adicional: GPS")


if __name__ == "__main__":
    unittest.main()
