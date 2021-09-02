def main():
    url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar"

    if(url == ""):
        raise ValueError("A URL está vazia")

    indice_interrogacao = url.find("?")
    url_base = url[: indice_interrogacao]
    print(f"Base da url: {url_base}")

    url_parametros = url[indice_interrogacao+1 :]
    print(f"Parâmetros da url: {url_parametros}")

    parametro_busca = "quantidade"
    indice_parametro = url_parametros.find(parametro_busca)

    indice_valor = indice_parametro + len(parametro_busca)+1
    indice_comercial = url_parametros.find("&", indice_valor)

    if(indice_comercial == -1):
        valor = url_parametros[indice_valor:]
    else:
        valor = url_parametros[indice_valor+2 : indice_comercial]
    print(f"Valor: {valor}")

main()