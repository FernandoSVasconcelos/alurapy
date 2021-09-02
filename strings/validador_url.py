import re

url = "htps://www.bytebank.com.br/cambio"

padrao_url = "(http(s)?://)?(www.)?bytebank.com(.br)?/cambio"
padrao_url = re.compile(padrao_url)

match = padrao_url.match(url)

if not match:
    raise ValueError(f"A URL: {url} não é valida.")
print(f"A URL {url} é valida")