from dominio.cliente import Cliente


lucas = Cliente("Lucas", "9876-8976")
Jose = CLiente("Jose", "98754-2322")

conta1 = Conta(lucas,5654,9000)
conta2 = Conta(jose,7649,5000)

conta1.deposito(2000)

conta1.saque(8000)

conta1.saque(1000)

conta1.saque(2500)

conta1.resumo()