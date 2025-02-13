# 🔥 Ignitive

## Ideia inicial

### 📌 **1. Arquitetura do Projeto**
O aplicativo será desenvolvido com **Streamlit**, utilizando **SQLAlchemy** para gerenciar o banco de dados e **Streamlit-Auth** para autenticação. A estrutura básica terá:

- **Frontend (Streamlit)**: Interface para navegação e estudo.
- **Backend (Python + SQLAlchemy)**: Gerenciamento de dados, progresso do usuário e desbloqueio de módulos.
- **Banco de Dados (SQLite/PostgreSQL)**: Armazenamento dos módulos, progresso do usuário e flashcards.

---

### 🎯 **2. Funcionalidades do App**
Aqui está um detalhamento das funcionalidades com base na sua ideia:

#### 🔹 **Mapa do Conhecimento (Árvore de Áreas e Subáreas)**
- Criar uma estrutura hierárquica onde cada grande área contém subáreas, que por sua vez contêm módulos.
- Cada módulo terá um **arquivo Markdown** gerado automaticamente para armazenar conteúdos.

#### 🔹 **Criação e Aplicação de Perguntas Automatizadas**
- Criar um conjunto padrão de perguntas aplicáveis a qualquer assunto.
- Implementar um **modelo de IA** que gere respostas automáticas com base no conteúdo Markdown.
- Salvar essas perguntas/respostas no banco de dados para futuras revisões.

#### 🔹 **Autenticação e Gerenciamento de Progresso**
- Implementar **streamlit-auth** para autenticação do usuário.
- Criar um sistema de **progresso** que registra quais módulos foram estudados.
- Implementar um sistema de **desbloqueio de módulos** conforme o usuário avança.

#### 🔹 **Gerenciamento de Estudos com Flashcards**
- Cada vez que um módulo for concluído, **gerar flashcards** com os principais conceitos.
- Implementar um **algoritmo de repetição espaçada** para revisar os flashcards.

---

### 🛠️ **3. Tecnologias e Ferramentas**
Aqui estão as ferramentas que você pode usar para desenvolver o app:

| Componente | Tecnologia/Ferramenta |
|------------|---------------------|
| Frontend | Streamlit |
| Banco de Dados | PostgreSQL / SQLite (com SQLAlchemy) |
| Autenticação | Streamlit-Auth |
| Markdown | Python-Markdown (para renderizar conteúdo) |
| IA | OpenAI API ou LlamaIndex para perguntas/respostas |
| Flashcards | Algoritmo de repetição espaçada (SM2) |
| UI/UX | Streamlit + CSS personalizado |

---

### 🔄 **4. Fluxo do Usuário**
O fluxo do usuário no app será o seguinte:

1. **Login e Autenticação**: O usuário acessa o app e faz login.
2. **Mapa do Conhecimento**: O usuário vê uma árvore de áreas e escolhe um módulo para estudar.
3. **Estudo de um Módulo**: O usuário lê o material do módulo (Markdown gerado).
4. **Perguntas Automatizadas**: O sistema exibe perguntas sobre o módulo e permite que o usuário responda.
5. **Registro de Progresso**: O módulo é marcado como "estudado" no banco de dados.
6. **Desbloqueio de Novos Módulos**: O usuário pode acessar módulos seguintes.
7. **Flashcards para Revisão**: O sistema gera flashcards com base no módulo estudado e os adiciona à revisão recorrente.

---

### 🚀 **5. Próximos Passos**
Agora que temos o plano estruturado, os próximos passos são:

✅ **1. Criar o mapa de conhecimento** com áreas e subáreas.  
✅ **2. Criar um modelo de banco de dados** para armazenar módulos e progresso.  
✅ **3. Implementar autenticação com streamlit-auth**.  
✅ **4. Criar a interface inicial no Streamlit** com navegação entre módulos.  
✅ **5. Desenvolver a geração de perguntas automatizadas**.  
✅ **6. Implementar flashcards e repetição espaçada**.  


---