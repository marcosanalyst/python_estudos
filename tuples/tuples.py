# Tuples

# Armazenar mais de uma informação em variáveis
# Manter a sequência dos dados em uma variável
# DADOS NÃO PODEM SER ALTERADOS!! (Immutable)
# TUPLE usa-se parênteses
# Não consigo adicionar, remover itens de um TUPLE

cores_list = ['amarelo', 'vermelho', 'verde', 'azul']
cores_tuple = ('amarelo', 'vermelho', 'verde', 'azul') # não alterável!!

print(type(cores_list))     #<class 'list'>
print(type(cores_tuple))    #<class 'tuple'>

cores_list.append('roxa') # acrescentará 'roxa' na lista
cores_tuple.append('roxa') # trará um erro no código
# AttributeError: 'tuple' object has no attribute 'append'
