from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def ver_mesas(self, gestion_mesas):
        pass

    @abstractmethod
    def realizar_funcion(self):
        pass

# Interface para Mesa
class IMesa(ABC):
    @abstractmethod
    def agregar_pedido(self, pedido):
        pass
    
    @abstractmethod
    def calcular_total(self):
        pass
    
    @abstractmethod
    def cambiar_estado(self, estado):
        pass

# Clase concreta Mesa que implementa IMesa
class Mesa(IMesa):
    def __init__(self, id):
        self.id = id
        self.estado = 'Disponible'
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)
        self.estado = 'Ocupada'

    def calcular_total(self):
        return sum(pedido.calcular_total() for pedido in self.pedidos)

    def cambiar_estado(self, estado):
        self.estado = estado

# Interface para Pedido
class IPedido(ABC):
    @abstractmethod
    def agregar_producto(self, producto, cantidad):
        pass
    
    @abstractmethod
    def calcular_total(self):
        pass

# Clase concreta Pedido que implementa IPedido
class Pedido(IPedido):
    def __init__(self):
        self.productos = {}
        self.estado = 'Pendiente'

    def agregar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.productos.items():
            total += producto.obtener_precio() * cantidad
        return total

# Gestion de Pedidos
class GestionPedido:
    def __init__(self):
        self.pedidos = []

    def crear_pedido(self):
        pedido = Pedido()
        self.pedidos.append(pedido)
        return pedido

    def cancelar_pedido(self, pedido):
        if pedido in self.pedidos:
            self.pedidos.remove(pedido)

# Clase que representa un producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self):
        return self.precio

# Clase que representa un Mesero
class Mesero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos_atendidos = []
        self.propinas = 0

    def registrar_pedido(self, mesa, pedido):
        mesa.agregar_pedido(pedido)
        self.pedidos_atendidos.append(pedido)

    def liquidar_factura(self, pedido, propina):
        factura = Factura(pedido, propina)
        self.propinas += factura.calcular_propina()
        factura.liquidar()

# Clase Factura para gestionar la liquidacion de un Pedido
class Factura:
    def __init__(self, pedido, propina):
        self.pedido = pedido
        self.propina = propina

    def calcular_total(self):
        return self.pedido.calcular_total() + self.calcular_propina()

    def calcular_propina(self):
        return self.pedido.calcular_total() * (self.propina / 100)

    def liquidar(self):
        self.pedido.estado = 'Facturado'

# Gestion de Mesas
class GestionDeMesas:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

    def visualizar_mesas(self):
        for mesa in self.mesas:
            print(f"Mesa {mesa.id} - Estado: {mesa.estado} - Total: {mesa.calcular_total()}")

