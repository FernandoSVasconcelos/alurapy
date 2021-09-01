class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()

    def validar_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao +1:]
        return url_parametros

    def get_valor_parametros(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) +1
        indice_comercial = self.get_url_parametros().find("&", indice_valor)
        
        if(indice_comercial == -1):
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_comercial]
        return valor

if __name__ == '__main__':
    newExtrator = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
    valor_quantidade = newExtrator.get_valor_parametros("quantidade")
    print(valor_quantidade)
