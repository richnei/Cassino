# Desafio Back-end Caleta | API_CASSINO

Essa API tem como objetivo simular a carteira digital de um cassino. A Api é capaz de gerenciar o saldo do jogador, permitindo apostas e ganhos.

* Um breve diagrama para ficar mais claro a estrutura da API. <br> <br>
[![](https://mermaid.ink/img/pako:eNptkM9qg0AQxl9lmVMDCfEYhBb8k4YcWiUKPaiUYXdsBN1t111KUZ-mhz5IXqxrvDTQOQ2_75th5huAK0HgQ92qT35GbVgel5K5CoogPb5GQZYdn5OKbTYP44k-LPVmZOHdYZ9v0yTLV4s5nHUWDWlyyu93nudNC4-uc848srgIsUXJqforzTtGti9CMv_wx-KlkTd8KxTvR3YoYsVtR9Lg5efyrZhA5s6tYA0d6Q4b4X4a5sESzJk6KsF3raAabWtKKOXkrGiNyr4kB99oS2uw7wINxQ2-aezAr7HtHSXRGKWflpyucU2_-Dphbg?type=png)](https://mermaid.live/edit#pako:eNptkM9qg0AQxl9lmVMDCfEYhBb8k4YcWiUKPaiUYXdsBN1t111KUZ-mhz5IXqxrvDTQOQ2_75th5huAK0HgQ92qT35GbVgel5K5CoogPb5GQZYdn5OKbTYP44k-LPVmZOHdYZ9v0yTLV4s5nHUWDWlyyu93nudNC4-uc848srgIsUXJqforzTtGti9CMv_wx-KlkTd8KxTvR3YoYsVtR9Lg5efyrZhA5s6tYA0d6Q4b4X4a5sESzJk6KsF3raAabWtKKOXkrGiNyr4kB99oS2uw7wINxQ2-aezAr7HtHSXRGKWflpyucU2_-Dphbg)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Tecnologias Utilizadas

* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Pytest](https://docs.pytest.org/en/7.4.x/)
* [Thunder Client](https://www.thunderclient.com/)
* [Visual Studio Code](https://code.visualstudio.com/)

## Dependências e Versões Necessárias
* Python - Versão: 3 +
* FastAPI - Versão: 0.104.1
* uvicorn - Versão: 0.24.0

### Como rodar o projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/richnei/Cassino.git

2. Navegue até o diretório do projeto:

    ```bash
    cd Cassino

3. Instale as dependências usando o seguinte comando:

    ```bash
    pip install -r requirements.txt

## Como rodar os testes
- No diretório do projeto, navegue até a pasta api e digite o comando
- 
    ```bash
    pytest

---

## API_CASSINO - Informações importantes sobre a aplicação

Nessa API temos 3 rotas, que são;

* **GET /balance:** Esse endpoint é usado para consultar a carteira de um jogador. Ele deverá receber como parâmetro na URL o ID do jogador.
  
    Requisição: `GET localhost:8000/balance?player=1` ou `GET localhost:8000/balance/1`
    
    Resposta: `{"player": 1, "balance": 1000}`

* **POST /bet:** Esse endpoint é utilizado para realizar apostas usando a carteira digital do jogador. Ele recebe no corpo da requisição um objeto JSON contendo o ID do jogador e o valor a ser sacado. Como resposta, retorna o saldo atualizado da carteira digital e o ID da transação.

  Requisição: `POST localhost:8000/bet` com body `{"player": 1, "value": 5}`
  
  Resposta: `"player": 1, "balance": 995, "txn": 1}`

* **POST /win:** Este endpoint é utilizado para realizar ganhos usando a carteira digital de um jogador. Ele receber no corpo da requisição um objeto JSON contendo o ID do jogador e o valor a ser depositado. Como resposta, retorna o saldo atualizado da carteira digital e o ID da transação.

  Requisição: `POST localhost:8000/win` com body `{"player": 1, "value": 1000}`
  
  Resposta: `{"player":1, "balance": 1995, "txn": 2}`

* **Documentação da API:** Utilizei o FastAPI para desenvolver essa API. Dentre outras facilidades que vem na esteira ao utilizar essa tecnologia, ele gera a documentação completa da API automaticamente. Para acessa-la, basta colocar /docs no final. Por exemplo:

  `localhost:8000/docs`

## Problemas enfrentados

Enfrentei dois problemas no decorrer desse desenvolvimento. Com o Docker e com o endpoint de POST/rollback. Vamos a eles.

* **POST/rollback:** Tive problemas na logica ao desenvolvedor essa requisição. Por algum motivo, esse endpoint não atrelava a transação que estava armazenando no dicionário ao o que eu solicitava no body. Talvez, dicionário não foi a melhor forma de armazenar/manipular os dados. Um SQLite seria mais robusto e seguro. Fiquei uns dois dias nesse endpoint. Sei que é um problema de lógica pois não acusava erro na sintaxe. As vezes uma parte do endpoint retornava correto, mas outras partes não. Ou seja, sem um banco de dados, o desafio principal foi garantir a consistência do estado das transações e dos saldos dos jogadores, exigindo que eu tentasse de várias formas para evitar condições de inconsistências nos dados.

*  **Docker:** Nunca tinha utilizado Docker. Já tinha um conhecimento teorico a alguma noção dos problemas que ele resolve pois já trabalhei em projetos que utilizam Docker. Mas eu, pessoalmente, não tinha mexido com ele. Mas esse desafio me fez ir atrás de informações mais profundas e concretas sobre o mesmo e comecei a colocar em prática a containerização. Achei amigável e fácil, com uma documentação tranquila e bem intuitiva. Porém, minha maquina (pessoal) não é das melhores para mexer com Containers. Um i3 de 7 geração, uma guerreira placa de video GT 630 e 6GB de RAM DDR3 pediu paz e não consegui rodar o Docker. Portanto, infelizmente não consegui gerar a imagem. Porém, fiquei positivamente supreso coma facilidade dessa ferramenta e quero me aprimorar cada vez mais.

## Próximos passos

Com minhas novas peças a caminho, pretendo terminar e containerizar a aplicação, bem como utilizar um banco de dados para facilitar as transações. Com isso, facilitar a solução e implementação do endpoimt rollback. Com o back mais estruturado, requer um frontend para consumir essa API e interagir com o usuário. Com a minha proficiência em ReactJS, quero construir o "rosto" da aplicação de forma bem intuitiva, moderna, envolvente e interativa. 


