
# Módulo_2
# Exercícios
# 1.Listas
filmes_web = ['1. Um Sonho de Liberdade',
              '2. O Poderoso Chefão',
              '3. O Poderoso Chefão II',
              '4. Batman: O cavaleiro das trevas',
              '5. 12 Homens e uma Sentença',
              '6. A Lista de Schindler',
              '7. O Senhor dos Anéis: O retorno do Rei',
              '8. Pulp Fiction: Tempo de Violência',
              '9. Três Homens em Conflitos',
              '10. O Senhor dos Anéis: A Sociedade do Anel']
print(filmes_web)
troca1 = filmes_web.pop(0)
torca2 = filmes_web.pop(0)
filmes_web.insert(0, "2. Um Sonho de Liberdade")
filmes_web.insert(0, "1. O Poderoso Chefão")
print(filmes_web)

# 2.Conjunto

filmes = ['1. Um Sonho de Liberdade',
          '2. O Poderoso Chefão',
          '3. O Poderoso Chefão II',
          '4. Batman: O cavaleiro das trevas',
          '5. 12 Homens e uma Sentença',
          '6. A Lista de Schindler',
          '7. O Senhor dos Anéis: O retorno do Rei',
          '8. Pulp Fiction: Tempo de Violência',
          '9. Três Homens em Conflitos',
          '10. O Senhor dos Anéis: A Sociedade do Anel',
          '8. Pulp Fiction: Tempo de Violência',
          '9. Três Homens em Conflitos',
          '10. O Senhor dos Anéis: A Sociedade do Anel']
print(filmes)
print(len(filmes))
alt_filmes = list(set(filmes))
print(alt_filmes)
print(len(alt_filmes))




# 3. Dicionários

filmes_disponiveis = []
filme_top = {"nome": "Um sonho de Liberdade", "ano": 1994}
filmes_disponiveis.append(filme_top)
rede = {"nome": "O poderoso Chefão", "ano": 1972}
filmes_disponiveis.append(filme_top)
rede = {"nome": "O poderoso Chefão II", "ano": 1974}
filmes_disponiveis.append(filme_top)
rede = {"nome": "Batman: O cavaleiro das trevas", "ano": 2008}
filmes_disponiveis.append(filme_top)
rede = {"nome": "12 Homens e uma Sentença", "ano": 1957}
filmes_disponiveis.append(filme_top)
rede = {"nome": "A Lista de Schindler", "ano": 1993}
filmes_disponiveis.append(filme_top)
rede = {"nome": "O Senhor dos Anéis: O retorno do Rei", "ano": 2003}
filmes_disponiveis.append(filme_top)
rede = {"nome": "Pulp Fiction: Tempo de Violência", "ano": 1994}
filmes_disponiveis.append(filme_top)
rede = {"nome": "Três Homens em Conflitos", "ano": 1966}
filmes_disponiveis.append(filme_top)
rede = {"nome": "O senhor dos Anéis: A sociedade do Anel", "ano": 2001}
filmes_disponiveis.append(filme_top)
print(type(rede))

print(filmes_disponiveis)
print(type(filmes_disponiveis))











