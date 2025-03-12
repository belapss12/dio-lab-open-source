from datetime import date

# Classe Historico
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Interface Transacao
class Transacao:
    def registrar(self, conta):
        pass

# Classe Deposito
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(f"Depósito: R${self.valor:.2f}")

# Classe Saque
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque: R${self.valor:.2f}")
            return True
        return False

# Classe Conta
class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)

    def sacar(self, valor):
        saque = Saque(valor)
        return saque.registrar(self)

    def nova_conta(cliente, numero, agencia):
        return Conta(numero, agencia, cliente)

# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

# Classe ContaCorrente
class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite, limite_saques):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
