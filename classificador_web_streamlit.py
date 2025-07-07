
import streamlit as st
import pandas as pd

# Carregar faixas de umidade do CSV
@st.cache_data
def carregar_faixas(path="faixas_umidade.csv"):
    return pd.read_csv(path)

def classificar_umidade_csv(temperatura, umidade, df):
    atual = None
    ideal = None
    for _, row in df.iterrows():
        # Verifica se está dentro da faixa ideal (Confortável)
        if row['faixa_temp_min'] <= temperatura <= row['faixa_temp_max'] and row['classificacao'] == "Confortável":
            ideal = (row['umidade_min'], row['umidade_max'])
        # Verifica a classificação atual
        if (row['faixa_temp_min'] <= temperatura <= row['faixa_temp_max'] and
            row['umidade_min'] <= umidade <= row['umidade_max']):
            atual = (row['classificacao'], row['efeito'])
    if atual:
        return atual[0], atual[1], ideal
    else:
        return "Desconhecida", "Faixa não encontrada.", ideal

def gerar_dica(umidade, faixa_ideal):
    if faixa_ideal is None:
        return "Não foi possível determinar a faixa ideal para essa temperatura."
    ideal_min, ideal_max = faixa_ideal
    if umidade > ideal_max:
        return "Considere usar um desumidificador, manter o ambiente ventilado ou utilizar ar-condicionado com função desumidificação."
    elif umidade < ideal_min:
        return "Considere usar um umidificador, deixar recipientes com água no ambiente ou estender toalhas úmidas para aumentar a umidade."
    else:
        return "A umidade está dentro da faixa ideal para essa temperatura."

# Interface Streamlit
st.title("Classificador de Umidade Relativa x Temperatura (com CSV)")
st.write("Insira os dados abaixo para ver a classificação, efeitos e dicas.")

# Entradas com valores vazios inicialmente
temperatura = st.number_input("Temperatura (°C)", min_value=-10.0, max_value=50.0, step=0.5, value=None, placeholder="Digite a temperatura")
umidade = st.number_input("Umidade Relativa (%)", min_value=0.0, max_value=100.0, step=1.0, value=None, placeholder="Digite a umidade")

df_faixas = carregar_faixas()

if st.button("Classificar"):
    if temperatura is None or umidade is None:
        st.warning("Por favor, preencha os dois campos antes de classificar.")
    else:
        classificacao, efeito, faixa_ideal = classificar_umidade_csv(temperatura, umidade, df_faixas)
        dica = gerar_dica(umidade, faixa_ideal)

        faixa_formatada = f"{faixa_ideal[0]}–{faixa_ideal[1]}%" if faixa_ideal else "-"
        st.markdown(f"### Classificação: **{classificacao}**")
        st.markdown(f"**Efeitos prováveis:** {efeito}")
        st.markdown(f"**Faixa ideal de umidade para {temperatura:.1f} °C:** {faixa_formatada}")
        st.markdown(f"**Dica:** {dica}")
