def devolve_cidades(*cidades):
    for cidade in cidades:
        yield cidade

# Iterando com 'yield from'
def devolve_cidades2(*cidades):
    yield from cidades

lista_cidades = devolve_cidades2('Teresina', 'Araguaína', 'Palmas', 'Parnaíba')

print(f"Local de nascimento: {next(lista_cidades)}. Atualmente, morando em {next(lista_cidades)}.")