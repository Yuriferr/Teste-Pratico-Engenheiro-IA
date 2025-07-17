# Buscador de Detalhes de Filmes com OpenAI

Este projeto consiste em um script Python que utiliza a API da OpenAI para buscar informações detalhadas sobre um filme, como data de lançamento, bilheteria e sinopse. A resposta é sempre retornada em um formato JSON estruturado.

## Funcionalidades

-   Recebe o título de um filme como entrada.
-   Consulta a API de Chat Completions da OpenAI.
-   Utiliza a funcionalidade de "Function Calling" para garantir uma saída de dados estruturada.
-   Retorna os detalhes do filme em formato JSON.
-   Possui tratamento básico de erros para chamadas de API.

## Pré-requisitos

-   Python 3.6 ou superior
-   Acesso à internet

## Instalação

1.  **Clone o repositório ou baixe os arquivos.**

    Se estiver usando Git, você pode clonar o repositório com o comando:
    ```bash
    git clone [https://github.com/Yuriferr/Teste-Pratico-Engenheiro-IA.git](https://github.com/Yuriferr/Teste-Pratico-Engenheiro-IA.git)
    cd seu-repositorio
    ```
    Caso contrário, apenas salve o arquivo `buscar_filme.py` em uma pasta de sua preferência.

2.  **Instale as dependências.**

    Este projeto requer a biblioteca `openai`. Você pode instalá-la usando `pip`:
    ```bash
    pip install openai
    ```

## Como Usar

1.  **Abra seu terminal ou prompt de comando.**

2.  **Navegue até a pasta onde o script está salvo.**

    ```bash
    cd /caminho/para/sua/pasta
    ```

3.  **Execute o script.**

    ```bash
    python buscar_filme.py
    ```

4.  **Informe o título do filme.**

    O script irá solicitar que você digite o título do filme. Após digitar e pressionar Enter, ele fará a busca e exibirá o resultado no terminal.

    **Exemplo de execução:**

    ```
    Digite o título do filme que você deseja pesquisar: Interestelar

    Buscando detalhes para o filme: 'Interestelar'...

    --- Resultado da Busca ---
    {
      "release_date": "6 de novembro de 2014",
      "box_office": "US$ 701.8 milhões",
      "synopsis": "Um grupo de exploradores faz uso de um buraco de minhoca recém-descoberto para superar as limitações das viagens espaciais humanas e conquistar as vastas distâncias envolvidas em uma jornada interestelar."
    }
    --------------------------
    ```

## Estrutura do Código

-   **`get_movie_details(movie_title: str)`**: A função principal que orquestra a chamada para a API da OpenAI. Ela constrói o prompt, define a estrutura da função (tool) para garantir a saída em JSON e trata as respostas e possíveis erros.
-   **Bloco `if __name__ == "__main__":`**: É o ponto de entrada do script. Ele gerencia a interação com o usuário (pede o título do filme) e exibe o resultado final de forma formatada.
