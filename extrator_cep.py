import re
endereco = "Rua Praguai 11, apartamento 12, Quisisana, Poços de Caldas, MG, 37701-244"

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)

if(busca):
    cep = busca.group()
    print(f"CEP = {cep}")
else:
    print(f"Padrão não encontrado")