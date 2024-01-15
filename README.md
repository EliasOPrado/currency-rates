## Projeto Currency Rates

Este e um projeto para a demonstração e consumo de API de precificação de moedas.

#### Links para acessar o deploy da documentação da API e o Frontend:
- [Link da documentação API](https://currency-rate-app.onrender.com/swagger/// "Link da documentação API")
- [Link do Fronted](https://currency-rates-murex.vercel.app/ "Link do Fronted")

O backend (server) e o banco de dados foram hospedados no render.com:
<img src="https://lh3.googleusercontent.com/u/0/drive-viewer/AEYmBYRUonTKKuS7SduHxFdG7GDhCGwqkGoYl3V8HuXdr5Y-xtZjzXzG6XM-YzH3mTRyHAgAJNxpdPCQbIiq0YZNZ7ULmOl8gA=w1920-h911" alt="Alt text" width="500" />

Ja o frontend foi hospedado na vercel.com:
<img src="https://lh3.googleusercontent.com/drive-viewer/AEYmBYR0QtnVrEsKYiEz4Fq-6R16x65v2WKqz-AGsmJTzM2_M_qt37tegxhoKwpZ8b5WVGjYE5bQYVHSfc9aB4l6UK6Mpm-u=w1920-h911" alt="Alt text" width="500" />

#### Como rodar o projeto localmente:

##### Backend:
1. Va ao diretorio `backend/`
2. Instale o ambiente virtual: `python3 -m venv venv` e o ative `venv\Scripts\activate`
3. Com o ambiente ativado instale os pacotes com o comando `pip install -r requirements.txt`
4. Crie as tabelas no banco de dados `python manage.py migrate`
5. Rode o projeto `python manage.py runserver`

##### Frontend:
1. Va ao diretorio `frontend/`
2. Instale as dependencias `npm install`
3. Rode o projeto `npm start`