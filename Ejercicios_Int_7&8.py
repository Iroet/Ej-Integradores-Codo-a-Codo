#Ejercicio 7

from abc import ABC, abstractmethod
import random



class Cuenta(ABC):
    def __init__(self, nombre, apellido, cantidad, saldo, numero_cuenta):
        self._nombre = nombre
        self._apellido = apellido
        self._cantidad = cantidad
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
        
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido    

    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    @property
    def numero_cuenta(self):
        return self._numero_cuenta
    
    @numero_cuenta.setter
    def numero_cuenta(self, nueva_cuenta):    
        self._numero_cuenta = nueva_cuenta

    @abstractmethod
    def nombrar_nombre(self):
        pass

    def nombrar_nombre(self):
        while True:
            self.nombre = str(input("Ingrese Nombre del titular: "))
            if self.nombre.isalpha()!=True:
                print("La celda no debe de tener números")
                continue
            else:
                break
            
    @abstractmethod
    def nombrar_apellido(self):
        pass

    def nombrar_apellido(self):
        while True:
            self.apellido = str(input("Ingrese Apellido del titular: "))
            if self.apellido.isalpha()!=True:
                print("La celda no debe de tener números")
                continue
            else:
                break
    
    @abstractmethod
    def cantidades(self):
        pass

    def cantidades(self):
        while True:
            try:
                print("")
                self.cantidad  = float(input("Ingrese cantidad de dinero en cuenta: "))
                print("")
            except ValueError:
                print("Se debe ingresar un número")
                continue
            else:
                break
        self.saldo = self.cantidad
        
    @abstractmethod
    def ingresar(self):
        pass
    def ingresar(self):        
        while True:
            try:
                self.cantidad  = float(input("Cantidad de dinero a depositar: "))
                if self.cantidad >0:
                    self.saldo = self.saldo + self.cantidad
                    print("")
                    print("{} {} ha ingresado ${} y su saldo es ${:.2f}".format(self.nombre, self.apellido, self.cantidad, self.saldo))
                    print("")
                    break
                else:
                    break
            except ValueError:
                print("Se debe ingresar un número")
                continue
            

    @abstractmethod
    def retirar(self):
        pass
    def retirar(self):
        while True:
            try:        
                self.cantidad  = float(input("Cantidad de dinero a retirar: "))
                self.saldo = self.saldo - self.cantidad
                print("")
                print("{} {} ha retirado ${} y su saldo es ${:.2f}".format(self.nombre, self.apellido, self.cantidad, self.saldo))
                print("")
                break
            except ValueError:
                print("S debe ingresar un número")
                continue
            

    @abstractmethod
    def mostrar(self):
        pass

    def mostrar(self):
        print("")
        print("Nombre del titular: {} {}\n" "Dinero en cuenta: {}\n" "N°Cuenta: {}\n".format(self.nombre, self.apellido, self.saldo, self.numero_cuenta))
        print("")

nueva_cuenta = Cuenta("","", 0, 0, 0)
nueva_cuenta.nombrar_nombre()
nueva_cuenta.nombrar_apellido()
nueva_cuenta.cantidades()
nueva_cuenta.numero_cuenta = random.randint(1, 100)
nueva_cuenta.ingresar()
nueva_cuenta.retirar()
nueva_cuenta.mostrar()



# Ejercicio 8:



class Cuenta_Joven(Cuenta):
    def __init__(self, nombre, apellido, cantidad, saldo, numero_cuenta, bonificacion, edad):
        super().__init__(nombre, apellido, cantidad, saldo, numero_cuenta)
        self._bonificacion = bonificacion
        self._edad = edad

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion_asignada):
        self._bonificacion = bonificacion_asignada
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad 

    @property
    def nombre(self):
        print("getter nombre called")
        return self._nombre


    @abstractmethod
    def ingrese_edad(self):
        pass

    def ingrese_edad(self):    
        while True:
            try:
                self.edad  = int(input("Escribe tu edad: "))
            except ValueError:
                print("Se debe ingresar un número entero")
                continue
            else:
                break
    
    
    @abstractmethod
    def es_titular_valido(self):
        pass
    def es_titular_valido(self):
        while True:
            if self.edad>=18 and self.edad<=25:
                self.titular_valido = True
                print("TITULAR VALIDO {}".format(self.titular_valido))
                break
            else:
                self.titular_valido = False
                print("Titular No apto {}" .format(self.titular_valido))
                break
        pass

    @abstractmethod
    def mostrar_joven(self):
        pass
    
    def mostrar_joven(self):
        while True:
            if self.titular_valido == True:
                self.bonificacion = float(input("Ingrese porcentaje de bonificación: "))
                print ("Cuenta Joven con una bonificacion de {}%\n" "Titular: {} {}\n" "Numero de cuenta: {}".format(self.bonificacion, nueva_cuenta.nombre, nueva_cuenta.apellido, nueva_cuenta.numero_cuenta))

                break
            else:
                print("nada que mostrar")
                break
        pass
    
    @abstractmethod
    def retirar_Cj(self):
        pass
    def retirar_Cj(self):
        if self.titular_valido == True:
                print("")
                print("Está Habilitado para retirar dinero.")
                print("")
                self.cantidad  = float(input("Ingrese cantidad de dinero a retirar: "))
                nueva_cuenta.saldo = nueva_cuenta.saldo - self.cantidad
                print("{} {} ha retirado ${} y su saldo es ${:.2f}".format(nueva_cuenta.nombre, nueva_cuenta.apellido, self.cantidad, nueva_cuenta.saldo))
                print("\nEl programa ha finalizado!")
        else:
            print("")
            print("No está Habilitado para retirar dinero.")
            print("\nEl programa ha finalizado!")

            pass

nueva_cuenta_joven = Cuenta_Joven("","",0,0,0,0,0)
nueva_cuenta_joven.ingrese_edad()
nueva_cuenta_joven.es_titular_valido()
nueva_cuenta_joven.mostrar_joven()
nueva_cuenta_joven.retirar_Cj()