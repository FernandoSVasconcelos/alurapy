from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador

class TestAvaliador(TestCase):
    def test_retorna_maior_menor_valor_de_lance_adicionado_ordem_crescente(self):
        fer = Usuario("Fer")
        gui = Usuario("Gui")

        lance_gui = Lance(gui, 100.0)
        lance_fer = Lance(fer, 120.2)
        
        newLeilao = Leilao("Celular")

        newLeilao.lances.append(lance_gui)
        newLeilao.lances.append(lance_fer)
        
        newAvaliador = Avaliador()
        newAvaliador.avalia(newLeilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 120.2

        self.assertEqual(menor_valor_esperado, newAvaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, newAvaliador.maior_lance)

    def test_retorna_maior_menor_valor_de_lance_adicionado_ordem_decrescente(self):
        gui = Usuario("Gui")
        fer = Usuario("Fer")

        lance_fer = Lance(fer, 120.2)
        lance_gui = Lance(gui, 100.0)
        
        newLeilao = Leilao("Celular")

        newLeilao.lances.append(lance_fer)
        newLeilao.lances.append(lance_gui)
        
        newAvaliador = Avaliador()
        newAvaliador.avalia(newLeilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 120.2

        self.assertEqual(menor_valor_esperado, newAvaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, newAvaliador.maior_lance)

    def test_um_lance(self):
        gui = Usuario("Gui")

        lance = Lance(gui, 150.0)

        leilao = Leilao("Celular")
        leilao.lances.append(lance)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(150.0, avaliador.menor_lance)
        self.assertEqual(150.0, avaliador.maior_lance)

    def test_tres_lances(self):
        gui = Usuario("Gui")
        fer = Usuario("Fer")
        vini = Usuario("Vini")

        lance_fer = Lance(fer, 120.2)
        lance_gui = Lance(gui, 100.0)
        lance_vini = Lance(vini, 200.0)
        
        newLeilao = Leilao("Celular")

        newLeilao.lances.append(lance_fer)
        newLeilao.lances.append(lance_gui)
        newLeilao.lances.append(lance_vini)
        
        newAvaliador = Avaliador()
        newAvaliador.avalia(newLeilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, newAvaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, newAvaliador.maior_lance)