# CPF deverá ter 11 dígitos
# CPF não pode ter todos os dígitos iguais
# 
# O Email deve possuir @
# O Email não pode ter letras maiúsculas 
# O Email não deve ter caracteres especiais no início do domínio
# O Email deve ter pelo menos um (.) no domínio
# Usuário não pode conter o “ ” espaço em branco.
# Domínio não pode conter o “ ” espaço em branco.
class Validador(object):
    def validar_cpf(self, cpf):
        cpfvalido = True
        lista = []
        lista [:10] = cpf
        cpf = cpf.replace(" ","")
        check_numeros = cpf.isnumeric()
        digito1 = self.primeiroDigito(cpf)
        digito2 = self.segundoDigito(cpf)
        
        if len(cpf)!= 11:    
            print("CPF inválido !!!")
            cpfvalido = False
        elif(cpf[0] == cpf[1]) and (cpf[1] == cpf[2]) and (cpf[2]== cpf[3] ) and (cpf[3] == cpf[4]) and (cpf[4] == cpf[5]) and (cpf[5] == cpf[6]) and (cpf[6] == cpf[7]) and (cpf[7] == cpf[8]):   
            print("CPF inválido !!!") 
            cpfvalido = False
        elif(check_numeros == False):  
            print("CPF inválido !!!") 
            cpfvalido = False
        elif(digito1 != int(cpf[9])):
            cpfvalido = False
            print("CPF inválido !!!")
        elif(digito2 != int(cpf[10])):
            cpfvalido = False
            print("CPF inválido !!!")
            
        return cpfvalido  
            
    def primeiroDigito(self, cpf):
        result = 0
        cpf = cpf.replace(" ","")
        check_numeros = cpf.isnumeric()
        if check_numeros == True:
            digito1 = [10,9,8,7,6,5,4,3,2]
            soma = 0
            for i, j in zip(cpf,digito1):
                produto = int(i)*j
                soma = soma + produto
                result = (soma*10)%11
        return result

    def segundoDigito(self, cpf):
        result = 0
        cpf = cpf.replace(" ","")
        check_numeros = cpf.isnumeric()
        if check_numeros == True:
            digito2 = [11,10,9,8,7,6,5,4,3,2]
            soma = 0
            for i, j in zip(cpf,digito2):
                produto = int(i)*j
                soma = soma + produto
                result = (soma*10)%11
        return result
                  
    def valida_email(self,email):
        caracter_especial = ('~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`',
                    '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/')
        EmailValido = True
        lista_user = []
        email_real = email
        email = email.replace(" ","")

        lista_user [:]= email
        
        if(not email_real.islower()):
            EmailValido = False
        elif(email.count('@')!= 1):
            EmailValido = False
        elif(email_real.count(' ')!= 0):
            EmailValido = False
        elif(email.split("@")[0]==''):
            EmailValido = False
        elif(len(email.split('.')[0])==0):
            EmailValido = False
        elif(lista_user[0] in caracter_especial)== True:
            EmailValido = False
        return EmailValido     

        
        


    # lista = input("Insira seu CPF !!!")
    # email = input("Insira um Email !!!")

    # if validar_cpf(lista) == True:
    #     print("Cpf valido !!")

    # valida_email(email)

