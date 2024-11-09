# KNN Flask API

---

### 1. Descrição / Description
### [PT-BR]
Este projeto cria uma API com Flask que utiliza o modelo K-Nearest Neighbors (KNN) para prever a espécie de uma flor do dataset Iris. O usuário envia dados via método POST http, e a API retorna a predição da espécie com base nas características fornecidas.

### [ENG]
This project creates an API with Flask that uses a K-Nearest Neighbors (KNN) model to predict the species of a flower from the Iris dataset. The user sends data via POST http method, and the API returns the species prediction based on the provided features.

---

### 2. Versão / Version
- python: 3.9.4
- VSCode
- Bibiotecas / Libraries
  - Flask
  - scikit-learn
  - requests
  - numpy

---

### 3. Como usar / How to

#### 3.1. Rodar o app.py / Run app.py
Para iniciar a API, execute o arquivo 'app.py', utilizando o botão de rodar o código do VSCode (Run Python File), Isso irá iniciar o servidor Flask localmente no endereço http://127.0.0.1:5000.

To start the API, run the 'app.py' file, using the VSCode code run button (Run Python File). This will start the Flask server locally at http://127.0.0.1:5000.

---

#### 3.2. Enviar uma Solicitação com o Client / Send a Request with the Client
Para realizar o médoto POST http, basta abrir outro terminal, clicando nos 3 pontinhos localizados em cima da tela, terminal e new terminal, após isso digite "py ./client.py" para rodar o arquivo 'client.py'.

To perform the POST http method, simply open another terminal, clicking on the 3 dots located at the top of the screen, terminal and new terminal, then type py ./client.py to run the 'client.py' file.

---

### 3.3 Resultado / Result
O programa vai retornar o código de status, que se der certo vai ser 200, e em seguida a predição, que será uma das 3 espécies de iris.

The program will return the status code, which if successful will be 200, and then the prediction, which will be one of the 3 iris species.


