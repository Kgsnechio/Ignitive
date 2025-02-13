import streamlit as st

from models.models import Usuario

st.title("Gerenciamento de Usuários")

# Sidebar com opções do CRUD
opcao = st.sidebar.radio("Escolha uma opção:", ["Criar", "Ler", "Atualizar", "Deletar"])

# Criar usuário
if opcao == "Criar":
    st.subheader("Adicionar Novo Usuário")
    nome = st.text_input("Nome")
    email = st.text_input("E-mail")

    if st.button("Salvar Usuário"):
        if nome and email:
            Usuario.create(nome, email)
            st.success(f"Usuário {nome} cadastrado com sucesso!")
        else:
            st.error("Preencha todos os campos!")

# Ler usuários
elif opcao == "Ler":
    st.subheader("Lista de Usuários")
    usuarios = Usuario.get_all()
    if usuarios:
        for user in usuarios:
            st.write(f"**ID:** {user.id} | **Nome:** {user.nome} | **Email:** {user.email}")
    else:
        st.warning("Nenhum usuário encontrado!")

# Atualizar usuário
elif opcao == "Atualizar":
    st.subheader("Atualizar Usuário")
    usuarios = Usuario.get_all()

    usuario_dict = {f"{user.id} - {user.nome}": user.id for user in usuarios}
    
    if usuario_dict:
        usuario_selecionado = st.selectbox("Escolha um usuário para atualizar", list(usuario_dict.keys()))
        novo_nome = st.text_input("Novo Nome")
        novo_email = st.text_input("Novo E-mail")

        if st.button("Atualizar"):
            Usuario.update_by_id(usuario_dict[usuario_selecionado], novo_nome, novo_email)
            st.success("Usuário atualizado com sucesso!")
    else:
        st.warning("Nenhum usuário cadastrado!")

# Deletar usuário
elif opcao == "Deletar":
    st.subheader("Deletar Usuário")
    usuarios = Usuario.get_all()

    usuario_dict = {f"{user.id} - {user.nome}": user.id for user in usuarios}

    if usuario_dict:
        usuario_selecionado = st.selectbox("Escolha um usuário para deletar", list(usuario_dict.keys()))

        if st.button("Deletar"):
            Usuario.delete_by_id(usuario_dict[usuario_selecionado])
            st.success("Usuário deletado com sucesso!")
    else:
        st.warning("Nenhum usuário cadastrado!")