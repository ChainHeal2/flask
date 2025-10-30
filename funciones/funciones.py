"""DOCUMENTO DE FUNCIONES MAS USADAS EN ESTE MINIPROYECTO"""

def formato_nombre(arg):
    """formatea el nombre de recibido a partir de una lista"""
    nombre = [" ".join((user['nombres'],user['apaterno'],user['amaterno']))for user in arg]
    return nombre
def formato_id(arg):
    """envia solo el ID del usuario"""
    return [usuario['id'] for usuario in arg]

lista = [{'id': 1, 'nombres': 'jose heimer', 'apaterno': 'arenas', 'amaterno': 'ramirez'},
         {'id': 2, 'nombres': 'jose heimer', 'apaterno': 'arenas', 'amaterno': 'ramirez'}]
print(formato_id(lista))
