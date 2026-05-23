from abc import ABC, abstractmethod
 
 
# =========================
# INTERFAZ DEL MEDIADOR
# =========================
class ChatMediator(ABC):
 
    @abstractmethod
    def enviar_mensaje(self, mensaje, usuario):
        pass
 
    @abstractmethod
    def agregar_usuario(self, usuario):
        pass
 
 
# =========================
# MEDIADOR CONCRETO
# =========================
class SalaChat(ChatMediator):
 
    def __init__(self):
        self.usuarios = []
 
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"{usuario.nombre} se ha unido al chat.")
 
    def enviar_mensaje(self, mensaje, emisor):
 
        for usuario in self.usuarios:
 
            # No enviar el mensaje al mismo emisor
            if usuario != emisor:
                usuario.recibir_mensaje(mensaje)
 
 
# =========================
# CLASE USUARIO
# =========================
class Usuario(ABC):
 
    def __init__(self, mediador, nombre):
        self.mediador = mediador
        self.nombre = nombre
 
    @abstractmethod
    def enviar(self, mensaje):
        pass
 
    @abstractmethod
    def recibir_mensaje(self, mensaje):
        pass
 
 
# =========================
# USUARIO CONCRETO
# =========================
class UsuarioChat(Usuario):
 
    def enviar(self, mensaje):
        print(f"\n{self.nombre} envía: {mensaje}")
        self.mediador.enviar_mensaje(mensaje, self)
 
    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} recibe: {mensaje}")
 
 
# =========================
# PROGRAMA PRINCIPAL
# =========================
if __name__ == "__main__":
 
    # Crear la sala de chat
    sala = SalaChat()
 
    # Crear usuarios
    usuario1 = UsuarioChat(sala, "Ana")
    usuario2 = UsuarioChat(sala, "Carlos")
    usuario3 = UsuarioChat(sala, "Laura")
 
    # Agregar usuarios a la sala
    sala.agregar_usuario(usuario1)
    sala.agregar_usuario(usuario2)
    sala.agregar_usuario(usuario3)
 
    # Enviar mensajes
    usuario1.enviar("Hola a todos!")
    usuario2.enviar("Hola Ana, ¿cómo estás?")
    usuario3.enviar("Bienvenidos al grupo.")
 
 
"""
=========================
SALIDA ESPERADA
=========================
 
Ana se ha unido al chat.
Carlos se ha unido al chat.
Laura se ha unido al chat.
 
Ana envía: Hola a todos!
Carlos recibe: Hola a todos!
Laura recibe: Hola a todos!
 
Carlos envía: Hola Ana, ¿cómo estás?
Ana recibe: Hola Ana, ¿cómo estás?
Laura recibe: Hola Ana, ¿cómo estás?
 
Laura envía: Bienvenidos al grupo.
Ana recibe: Bienvenidos al grupo.
Carlos recibe: Bienvenidos al grupo.
"""
 