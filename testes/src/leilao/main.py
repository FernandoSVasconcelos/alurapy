from dominio import Usuario, Lance, Leilao, Avaliador

if __name__ == "__main__":
    gui = Usuario("Gui")
    fer = Usuario("Fer")

    lance_gui = Lance(gui, 100.0)
    lance_fer = Lance(fer, 120.2)

    newLeilao = Leilao("Celular")

    newLeilao.lances.append(lance_gui)
    newLeilao.lances.append(lance_fer)

    for lance in newLeilao.lances:
        print(f"O usuário {lance.usuario.nome} deu um lance de {lance.valor}")

    newAvaliador = Avaliador()
    newAvaliador.avalia(newLeilao)
    print(f"O menor lance foi de {newAvaliador.menor_lance} e o maior for {newAvaliador.maior_lance}")