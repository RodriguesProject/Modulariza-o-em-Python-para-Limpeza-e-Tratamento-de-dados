"""Funções reutilizáveis para limpeza e validação básica de cadastros.

As validações são introdutórias e não substituem verificações oficiais.
"""

import re

import pandas as pd


def limpar_numero(texto):
    """Retorna somente os dígitos de um valor; nulos viram string vazia."""
    if pd.isna(texto):
        return ""
    return re.sub(r"\D", "", str(texto))


def email_valido(email):
    """Verifica um padrão estrutural simples de endereço de e-mail."""
    if pd.isna(email):
        return False

    texto = str(email).strip()
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, texto))


def tratar_clientes(df):
    """Cria colunas normalizadas e indicadores básicos sem sobrescrever a origem."""
    resultado = df.copy()

    resultado["telefone_limpo"] = resultado["telefone"].apply(limpar_numero)
    resultado["cpf_limpo"] = resultado["cpf"].apply(limpar_numero)

    resultado["email_limpo"] = (
        resultado["email"].fillna("").astype("string").str.strip()
    )
    resultado["email_formato_ok"] = resultado["email_limpo"].apply(email_valido)

    resultado["telefone_tamanho_ok"] = resultado["telefone_limpo"].apply(
        lambda valor: len(valor) in (10, 11)
    )
    resultado["cpf_11_digitos"] = resultado["cpf_limpo"].apply(
        lambda valor: len(valor) == 11
    )

    return resultado


def gerar_relatorio_clientes(df):
    """Resume os indicadores gerados por tratar_clientes()."""
    return {
        "total_clientes": int(len(df)),
        "emails_com_formato_ok": int(df["email_formato_ok"].sum()),
        "telefones_com_tamanho_ok": int(df["telefone_tamanho_ok"].sum()),
        "cpfs_com_11_digitos": int(df["cpf_11_digitos"].sum()),
    }
