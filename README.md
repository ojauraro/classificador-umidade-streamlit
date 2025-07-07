# Classificador de Umidade Relativa x Temperatura

Este é um aplicativo em Streamlit que classifica a umidade relativa do ar com base na temperatura ambiente, fornece efeitos prováveis e dicas para atingir a faixa ideal de conforto.

## Como rodar localmente

```bash
pip install -r requirements.txt
streamlit run classificador_web_streamlit_v3.py
```

## Como publicar no Streamlit Cloud

1. Crie um repositório no GitHub e envie estes arquivos:
   - `classificador_web_streamlit.py`
   - `requirements.txt`
   - `README.md`
2. Acesse https://streamlit.io/cloud
3. Conecte sua conta GitHub e selecione o repositório.
4. Clique em “Deploy”.

A aplicação será hospedada gratuitamente e poderá ser acessada por qualquer navegador, incluindo no celular Android.

## Exemplo de uso

Insira a temperatura e umidade atuais e veja a classificação, faixa ideal e dicas para ajustar o ambiente.
