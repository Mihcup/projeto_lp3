from validate_docbr import CPF

cpf = CPF()
#criando um objeto cpf

#gerar CPF
print(cpf.generate(True))
print(cpf.generate(False))

# Validar CPF
print(cpf.validate("315.838.341-17"))  # True
print(cpf.validate("50012240125"))  # True
