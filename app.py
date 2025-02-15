import streamlit as st
from sqlalchemy.orm import Session
from models import SessionLocal, Shine

from views.shine_view import render_shine

# Conectar ao banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Função principal do Streamlit
def main():
    st.title("💡 Shine Viewer")

    # Recebe o ID da Shine via input ou URL
    shine_id = st.number_input("Digite o ID da Shine:", min_value=1, step=1)

    # Buscar no banco de dados
    db = next(get_db())
    shine = db.query(Shine).filter_by(id=shine_id).first()

    if shine:
        render_shine(shine)

    else:
        st.error("⚠️ Shine não encontrada. Tente outro ID.")

if __name__ == "__main__":
    main()