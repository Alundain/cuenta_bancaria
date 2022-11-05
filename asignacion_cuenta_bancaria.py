class CuentaBancaria:
    todas_las_ctas = []
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.todas_las_ctas.append(self)

    def hacer_deposito(self, monto):
        self.balance += monto
        return self

    def hacer_retiro(self, monto):
        if monto > self.balance:
            self.balance -= 5
            print ("Fondos insuficientes, se restarán $ 5")
        else: 
            self.balance -= monto
        return self

    def mostrar_balance(self):
        print(f"El cliente cuenta con el siguiente balance : $ {self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0 :
            interes = self.tasa_interes * self.balance
            self.balance = self.balance + interes
        return self

    @classmethod
    def imprimir_info(cls):
        for allcuenta in CuentaBancaria.todas_las_ctas:
            allcuenta.mostrar_balance()
        return cls
        
Andrea = CuentaBancaria(0.05, 3540)
Andrea.hacer_deposito(200).hacer_deposito(54099).hacer_deposito(20990).hacer_retiro(10000).mostrar_balance()

Manuel = CuentaBancaria(0.10, 4530)
Manuel.hacer_deposito(20000).hacer_deposito(1).hacer_retiro(40).hacer_retiro(54).generar_interes().mostrar_balance().allcuenta()
