## Projeto Currency Rates

Este e um projeto para a demonstração e consumo de API de precificação de moedas.

#### Links para acessar o deploy da documentação da API e o Frontend:
- [Link da documentação API](https://currency-rate-app.onrender.com/swagger/// "Link da documentação API")
- [Link do Fronted](https://currency-rates-murex.vercel.app/ "Link do Fronted")

O backend (server) e o banco de dados foram hospedados no render.com:
<img src="https://lh3.googleusercontent.com/u/0/drive-viewer/AEYmBYRUonTKKuS7SduHxFdG7GDhCGwqkGoYl3V8HuXdr5Y-xtZjzXzG6XM-YzH3mTRyHAgAJNxpdPCQbIiq0YZNZ7ULmOl8gA=w1920-h911" alt="Alt text" width="500" />

Ja o frontend foi hospedado na vercel.com:
<img src="https://lh3.googleusercontent.com/fife/AGXqzDlLZ5oPnK26lnvaMlSxdi1DWa-kfBRtlOkfnxc0T4DdLdqJH3sQ26IK9T1tuvAn6ISljzF49A4VtXhspwwydVmrOy1iTrZakQYlmbAdw3ONSth-FU1k7F5UKadxPkibF2XM3fCBGVbpH27avWXITP-oIwxOYw60djZlG5qj0wSAI-N5XvMg92pyBGp5wosOlQoPFdh5M3Md7gLWc1Y-JekotvI21g3JQQIUiVok-h1vOHoNRI0EnqiF2eq5fSZiDDUxcuWp-fCue70GF-l9TBeBmAv48XLsnP405KDKR4d_GqAIrNSGELVfu_CjTA7_A6GHARWlSTEdmj_kBbuGRyT3Kh6wUel9k4eNwv6eQoR_GlTUgFZeSF184gqQvl2HdN1a0evvVgbBxYsz0V4Oj3NVqLOTUuE9H_UyB63fA2rh85bKearsBNtUYZSZTluFh8nzsf3NeHIBwVF87psQmKg_vziMGmOPSKvzAsqPYWiyYFGeaMBmVsZ_RPxd1_4L0bNOiuAp2HgMmtDG6av85iVgZRyT6S4tBdaCXWeN6mE7WChxuY2b7tIf8KlCgTJ9kEJQqR1JAk9Ai_MK6C8rE0UbvK58EE7t8utNKWqlHLLxoYQPw-CWcis2RCwv2VO0zTiTGj6KdVVVejMq39G-ROOP7__929SSaLZVlK9I2busOiGcQIRLRZAKzNNTa6DjyozMuBYNjo_6hxlnBRbw-mIJkJcr7fzjKbFtj_j21-yU-CcJPJWwXfHDwkHQ99WgpcnEWcILPEd4xaJQIxyGr5HVLTRnd17Ve3SDZ_liOv4geq8aP6HkGx_8SAUGDw3jg7zu3l_0JoNCkdAs6-1gYu9GZvoPgfxwT3yf0eZKSJPQRL8sI7mOiJtu6c3wncSqByjOJkEwuTudaPXTKHylv8Zd8a7Ss05fA0SG4BzCn_lwH7eIh-ZL2WUTI8-2mmV2tZk72BZbSleaoVajuMCpRVLItrf1eKTU7jfeuuTzB6BfA_aJSnLRBxHME-f4peXLp6e5W2Oyslwl3KyAIQQMkdD_9wGSYLa6kjyuM46D-yBgjEjhqXyf4mIDZI5sOiURMIf_h6soefyEwjvJnvUY0pSnkPo81-qllimkDM6oPow0yKNHNVK3vutLLQFPgAaSS2A6eZklbB6TG0jphmmXQv6fybjlNI5t2-vbdqohaBg8i4lCbynOtIugRBrPs4g0GJ7KAdIVwN3cv5NtIqxEYVgUuvYKQ-10bAR1jfLr7P3BqATW9BFOjNXEaEskdKqv7_ySxfL5-tRxHJtfyXNxxqMZMY2-RzWAbwPYsAmNd6pG-TL-fvBnGfeVK5g87oiSsAcJC-LNdD1diBeDK2o1u-A5IzVizgwmBPqhRb7MHYLcFMaYy5U_LrVdfP3b_ndpAX1XSA2Dk6VKtQsQ8P9pd5hGfX4lDtfBSuq_Jj9r0ey6Hyggi8m5_2iPvtfPjBtCg3PmbwwIJhdxQ0v3rFlL-HDIJ3RFqmezgxekpIcD9bPhW6zSfTiVCCBRaiQX0_h9WnqvWqrhekCRDEDKldcivfnhsU0=w1920-h911" alt="Alt text" width="500" />

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