import unittest
import pandas as pd
from limpeza import limpar_numero, normalizar_telefone, telefone_tamanho_valido, email_valido, cpf_valido, tratar_clientes, gerar_relatorio_clientes

class TestLimpeza(unittest.TestCase):
    def test_limpar_numero(self):
        self.assertEqual(limpar_numero("(21) 98888-1111"), "21988881111")
        self.assertEqual(limpar_numero(None), "")
        self.assertEqual(limpar_numero("sem telefone"), "")
    def test_telefone(self):
        self.assertEqual(normalizar_telefone("+55 (21) 98888-1111"), "21988881111")
        self.assertTrue(telefone_tamanho_valido("+55 (21) 98888-1111"))
        self.assertFalse(telefone_tamanho_valido("12345"))
    def test_email(self):
        self.assertTrue(email_valido("ana.souza@email.com"))
        self.assertFalse(email_valido("ana@email"))
        self.assertFalse(email_valido(None))
    def test_cpf(self):
        self.assertTrue(cpf_valido("529.982.247-25"))
        self.assertFalse(cpf_valido("111.111.111-11"))
        self.assertFalse(cpf_valido("123.456.789-10"))
    def test_preserva_origem_e_relatorio(self):
        base = pd.DataFrame({"telefone":["+55 (21) 98888-1111"],"cpf":["529.982.247-25"],"email":[" ana@email.com "]})
        original = base.copy(deep=True)
        tratado = tratar_clientes(base)
        pd.testing.assert_frame_equal(base, original)
        rel = gerar_relatorio_clientes(tratado)
        self.assertEqual(rel["total_clientes"], 1)
        self.assertEqual(rel["cpfs_validos_pelos_digitos_verificadores"], 1)
    def test_colunas_obrigatorias(self):
        with self.assertRaises(ValueError):
            tratar_clientes(pd.DataFrame({"nome":["Ana"]}))

if __name__ == "__main__":
    unittest.main()
