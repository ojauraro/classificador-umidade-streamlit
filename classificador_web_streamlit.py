
import streamlit as st

def classificar_umidade(temperatura, umidade):
    if temperatura <= 15:
        faixa_ideal = (30, 60)
        if umidade > 80:
            return "Alta", "Pode causar sensação de frio úmido, formação de mofo", faixa_ideal
        elif 60 <= umidade <= 80:
            return "Moderada", "Sensação úmida e fria, possível desconforto leve", faixa_ideal
        elif 30 <= umidade < 60:
            return "Confortável", "Boa sensação térmica, especialmente em locais fechados", faixa_ideal
        else:
            return "Seca", "Desconforto respiratório leve, menor risco de mofo", faixa_ideal
    elif 16 <= temperatura <= 25:
        faixa_ideal = (60, 80)
        if umidade > 80:
            return "Muito Alta", "Sensação de abafamento, risco de mofo e ácaros", faixa_ideal
        elif 60 <= umidade <= 80:
            return "Confortável", "Faixa ideal para conforto térmico e saúde", faixa_ideal
        elif 30 <= umidade < 60:
            return "Moderada", "Leve ressecamento em pessoas sensíveis", faixa_ideal
        else:
            return "Baixa", "Ar seco, aumenta risco de irritações e doenças respiratórias", faixa_ideal
    else:
        faixa_ideal = (30, 60)
        if umidade > 80:
            return "Excessiva", "Sensação pegajosa, desconforto térmico acentuado", faixa_ideal
        elif 60 <= umidade <= 80:
            return "Alta", "Quente e úmido, pode causar fadiga", faixa_ideal
        elif 30 <= umidade < 60:
            return "Confortável", "Boa sensação térmica dependendo da ventilação", faixa_ideal
        else:
            return "Seca", "Pode causar desidratação e irritação das vias aéreas", faixa_ideal

def gerar_dica(umidade, faixa_ideal):
    ideal_min, ideal_max = faixa_ideal
    if umidade > ideal_max:
        return "Considere usar um desumidificador, manter o ambiente ventilado ou utilizar ar-condicionado com função desumidificação."
    elif umidade < ideal_min:
        return "Considere usar um umidificador, deixar recipientes com água no ambiente ou estender toalhas úmidas para aumentar a umidade."
    else:
        return "A umidade está dentro da faixa ideal para essa temperatura."

st.title("Classificador de Umidade Relativa x Temperatura")
st.write("Insira os dados abaixo para ver a classificação, efeitos e dicas.")

temperatura = st.number_input("Temperatura (°C)", min_value=-10.0, max_value=50.0, step=0.5)
umidade = st.number_input("Umidade Relativa (%)", min_value=0.0, max_value=100.0, step=1.0)

if st.button("Classificar"):
    classificacao, efeito, faixa_ideal = classificar_umidade(temperatura, umidade)
    dica = gerar_dica(umidade, faixa_ideal)

    faixa_formatada = f"{faixa_ideal[0]}–{faixa_ideal[1]}%"
    st.markdown(f"### Classificação: **{classificacao}**")
    st.markdown(f"**Efeitos prováveis:** {efeito}")
    st.markdown(f"**Faixa ideal de umidade para {temperatura:.1f} °C:** {faixa_formatada}")
    st.markdown(f"**Dica:** {dica}")
