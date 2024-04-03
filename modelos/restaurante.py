class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} {self._categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')
            
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('pizza express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)

Restaurante.listar_restaurantes()
