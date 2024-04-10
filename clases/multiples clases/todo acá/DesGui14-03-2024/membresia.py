from abc import ABC, abstractmethod


class Membresia(ABC):
    def __init__(self, correo_subs: str, num_tarjeta: str):
        self.__correo_subs = correo_subs
        self.__num_tarjeta = num_tarjeta

    @property
    def correo_subs(self):
        return self.__correo_subs

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta

    @abstractmethod
    def cambiar_subscripcion(self,n_membresia: int,):
        pass

    def _crear_nueva_membresia(self, n_membresia : int):
        if n_membresia ==1:
            return MemBasica(self.correo_subs,self.num_tarjeta)
        elif n_membresia ==2:
            return MemFamiliar(self.correo_subs,self.num_tarjeta)
        elif n_membresia ==3:
            return MemSinConexion(self.correo_subs,self.num_tarjeta)
        elif n_membresia ==4:
            return MemPro(self.correo_subs,self.num_tarjeta)


class MemGratis(Membresia):
    valor = 0
    devices = 1

    def cambiar_subscripcion(self, n_membresia: int):
        if n_membresia < 1 or n_membresia > 4:
            return
        else:
            return self._crear_nueva_membresia(n_membresia)


class MemBasica(Membresia):
    valor = 3000
    devices = 2

    def __init__(self, correo_subs: str, num_tarjeta: int):  # constructor
        super().__init__(correo_subs, num_tarjeta)  # trae constructor padre

        if isinstance(self, MemFamiliar) or isinstance(
            self, MemSinConexion
        ):  # checker true or false en una de las dos opciones, usar con herencia en otras Mem
            self.dias_regalo = 7
        elif isinstance(self, MemPro):
            self.dias_regalo = 15

    def cancelar_mem(self):
        return MemGratis(self.correo_subs, self.num_tarjeta)

    def cambiar_subscripcion(self, n_membresia: int):
        if (
            n_membresia < 2 or n_membresia > 4
        ):  # checkea que membresía tiene o por cual cambiar
            return self
        else:
            return self._crear_nueva_membresia(n_membresia)


class MemFamiliar(MemBasica):
    valor = 5000
    devices = 5

    def cambiar_subscripcion(self, n_membresia: int):
        if n_membresia not in [1, 2, 3]:
            return self
        else:
            return self._crear_nueva_membresia(n_membresia)

    def modidicar_control_parental(self):
        pass


class MemSinConexion(MemBasica):
    valor = 3500
    devices = 2

    def cambiar_subscripcion(self, n_membresia: int):
        if n_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(n_membresia)

    def mas_contenido(self):
        pass


class MemPro(MemFamiliar, MemSinConexion):
    valor = 7000
    devices = 6

    def cambiar_subscripcion(self, n_membresia: int):
        if n_membresia < 1 or n_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(n_membresia)

g = MemGratis("correomccorreoface@correo.face", "numbermcnumberface")
print(type(g))

basica = g.cambiar_subscripcion(1)
print(type(basica))

familiar = basica.cambiar_subscripcion(2)
print(type(familiar))

sin_conexion = familiar.cambiar_subscripcion(3)
print(type(sin_conexion))

pro = sin_conexion.cambiar_subscripcion(4)
print(type(pro))

off = pro.cancelar_mem()
print(type(off))