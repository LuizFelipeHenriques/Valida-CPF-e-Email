import validador2 as val

class TestCPF(object):
    
    def test_tam_invalido(self):
        v = val.Validador()
        cpf = '933572652'
        assert v.validar_cpf(cpf) == False

    def test_numeros_repetidos_invalido(self):
        v = val.Validador()
        assert v.validar_cpf('11111111111') == False

    def test_letras_invalido(self):
        v = val.Validador()
        assert v.validar_cpf('aa987654321') == False

    def test_primeiroDigito_invalido(self):
        v = val.Validador()
        assert v.validar_cpf('93357265269') == False
        
    def test_segundoDigito_invalido(self):
        v = val.Validador()
        assert v.validar_cpf('93357265247') == False
    

class TestEmail(object):
    def test_letra_maiuscula_invalido(self):
        v = val.Validador()
        assert v.valida_email("Luizfelipeh89@mail.com") == False
        
    def test_mais_de_um_arroba_invalido(self):
        v = val.Validador()
        assert v.valida_email("luizfel@ipeh@gmail.com") == False

    def test_espaco_invalido(self):
        v = val.Validador()
        assert v.valida_email("luiz felipeh89@gmail.com") == False

    def test_comeca_sem_digito(self):
        v = val.Validador()
        assert v.valida_email("@email.com") == False

    def test_ponto(self):
        v = val.Validador()
        assert v.valida_email(".hgdsga@.com") == False

    def test_caracter_especial_invalido(self):
        v = val.Validador()
        assert v.valida_email("#hgdsga@gmail.com") == False