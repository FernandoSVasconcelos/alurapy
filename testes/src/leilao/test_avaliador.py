from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador

class TestAvaliador(TestCase):
    def test_avalia(self):
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
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, newAvaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, newAvaliador.maior_lance)