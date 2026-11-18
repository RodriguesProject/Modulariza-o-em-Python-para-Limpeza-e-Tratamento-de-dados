"""Rotinas reutilizáveis de limpeza e validação introdutória de cadastros."""
import re
import pandas as pd

OBRIGATORIAS = {"telefone", "cpf", "email"}

def limpar_numero(valor):
    if pd.isna(valor):
        return ""
    return re.sub(r"\D", "", str(valor))

def normalizar_telefone(valor):
    digitos = limpar_numero(valor)
    if digitos.startswith("55") and len(digitos) in (12, 13):
        digitos = digitos[2:]
    return digitos

def telefone_tamanho_valido(valor):
    return len(normalizar_telefone(valor)) in (10, 11)

def email_valido(valor):
    if pd.isna(valor):
        return False
    texto = str(valor).strip()
    padrao = r"[A-Za-z0-9.!#$%&'*+/=?^_\x60{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"
    return bool(re.fullmatch(padrao, texto))

def cpf_valido(valor):
    digitos = limpar_numero(valor)
    if len(digitos) != 11 or digitos == digitos[0] * 11:
        return False
    nums = [int(x) for x in digitos]
    for n in (9, 10):
        soma = sum(nums[i] * (n + 1 - i) for i in range(n))
        dv = (soma * 10) % 11
        if dv == 10:
            dv = 0
        if dv != nums[n]:
            return False
    return True

def tratar_clientes(df):
    faltantes = sorted(OBRIGATORIAS - set(df.columns))
    if faltantes:
        raise ValueError("DataFrame sem as colunas obrigatórias: " + ", ".join(faltantes))
    resultado = df.copy()
    resultado["telefone_limpo"] = resultado["telefone"].apply(normalizar_telefone)
    resultado["telefone_tamanho_ok"] = resultado["telefone_limpo"].str.len().isin([10, 11])
    resultado["cpf_limpo"] = resultado["cpf"].apply(limpar_numero)
    resultado["cpf_11_digitos"] = resultado["cpf_limpo"].str.len().eq(11)
    resultado["cpf_valido"] = resultado["cpf"].apply(cpf_valido)
    resultado["email_limpo"] = resultado["email"].fillna("").astype("string").str.strip()
    resultado["email_formato_ok"] = resultado["email_limpo"].apply(email_valido)
    return resultado

def gerar_relatorio_clientes(df):
    necessarias = {"email_formato_ok", "telefone_tamanho_ok", "cpf_11_digitos", "cpf_valido"}
    faltantes = sorted(necessarias - set(df.columns))
    if faltantes:
        raise ValueError("DataFrame sem os indicadores necessários: " + ", ".join(faltantes))
    return {
        "total_clientes": int(len(df)),
        "emails_com_formato_ok": int(df["email_formato_ok"].fillna(False).sum()),
        "telefones_com_tamanho_ok": int(df["telefone_tamanho_ok"].fillna(False).sum()),
        "cpfs_com_11_digitos": int(df["cpf_11_digitos"].fillna(False).sum()),
        "cpfs_validos_pelos_digitos_verificadores": int(df["cpf_valido"].fillna(False).sum()),
    }
