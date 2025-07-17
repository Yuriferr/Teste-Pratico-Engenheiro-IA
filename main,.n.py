# -*- coding: utf-8 -*-
"""
Este script busca informações de um filme utilizando a API da OpenAI
e retorna os dados em um formato JSON estruturado.

Para executar:
1. Instale a biblioteca da OpenAI: pip install openai
2. Execute o script no seu terminal: python nome_do_arquivo.py
"""

import os
import json
from openai import OpenAI

# --- CONFIGURAÇÃO INICIAL ---

# Define a chave da API e a URL base para as requisições.
API_KEY = "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"
BASE_URL = "https://openrouter.ai/api/v1" # Usando OpenRouter como proxy

# --- FUNÇÃO PRINCIPAL ---

def get_movie_details(movie_title: str) -> dict:
    """
    Recebe o título de um filme, consulta a API da OpenAI para obter detalhes
    e retorna um dicionário com data de lançamento, bilheteria e sinopse.

    Args:
        movie_title (str): O título do filme a ser pesquisado.

    Returns:
        dict: Um dicionário contendo os detalhes do filme ou uma mensagem de erro.
    """
    print(f"Buscando detalhes para o filme: '{movie_title}'...")

    try:
        # Inicializa o cliente da OpenAI com a URL base e a chave.
        client = OpenAI(
            base_url=BASE_URL,
            api_key=API_KEY,
        )

        # Define o schema da função para forçar uma saída JSON estruturada.
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "format_movie_details",
                    "description": "Formata os detalhes de um filme em um objeto JSON.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "release_date": {
                                "type": "string",
                                "description": "A data de lançamento do filme, ex: '21 de junho de 2024'"
                            },
                            "box_office": {
                                "type": "string",
                                "description": "A bilheteria mundial do filme, ex: 'US$ 500 milhões'"
                            },
                            "synopsis": {
                                "type": "string",
                                "description": "Uma sinopse curta do filme."
                            }
                        },
                        "required": ["release_date", "box_office", "synopsis"]
                    }
                }
            }
        ]

        # Prepara as mensagens para a chamada da API (sistema e usuário).
        messages = [
            {"role": "system", "content": "Você é um assistente especialista em cinema. Sua tarefa é encontrar informações sobre filmes e formatá-las em JSON usando a ferramenta fornecida."},
            {"role": "user", "content": f"Por favor, forneça os detalhes do filme: {movie_title}."}
        ]

        # Chama a API com o modelo, mensagens e a ferramenta definida.
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=messages,
            tools=tools,
            tool_choice={"type": "function", "function": {"name": "format_movie_details"}}
        )

        # Extrai os argumentos da função chamada pelo modelo.
        tool_call = response.choices[0].message.tool_calls[0]
        movie_details_str = tool_call.function.arguments

        # Converte a string de argumentos (JSON) para um dicionário Python.
        try:
            return json.loads(movie_details_str)
        except json.JSONDecodeError:
            return {"error": "Falha ao decodificar o JSON recebido da API."}

    # Captura e trata exceções que podem ocorrer durante a chamada da API.
    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API: {e}")
        return {"error": f"Não foi possível contatar a API da OpenAI. Detalhes: {str(e)}"}


# --- BLOCO DE EXECUÇÃO ---

# Bloco principal para execução interativa do script.
if __name__ == "__main__":
    # Solicita o título do filme ao usuário.
    title = input("Digite o título do filme que você deseja pesquisar: ")

    if title:
        # Chama a função principal para obter os detalhes do filme.
        details = get_movie_details(title)

        # Imprime o dicionário de detalhes formatado como JSON.
        print("\n--- Resultado da Busca ---")
        print(json.dumps(details, indent=2, ensure_ascii=False))
        print("--------------------------\n")
    else:
        print("Nenhum título de filme foi fornecido.")
