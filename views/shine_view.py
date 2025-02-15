import streamlit as st
from models import questions

def render_shine(shine):
    """Renderiza uma página no Streamlit para exibir uma Shine."""
    
    if not shine:
        st.error("⚠️ Shine não encontrada. Tente outro ID.")
        return
    
    st.header(f"{shine.topic}")

    # Exibir perguntas e respostas
    for i, question in enumerate(questions):
        st.subheader(question.format(topic=shine.topic))
        st.write(shine.answers[i] if i < len(shine.answers) else "Sem resposta cadastrada.")
