# 🔥 Ignitive

## Ideia inicial

Aplicação web para permitir o estudo de diversas áreas do conhecimento.
Permitindo conhecer novos assuntos e espandir os conhecimentos de forma generalista.

----

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

## Shines ( aprendizados ou diciplinas )

---

### 🔥 **O que é um Shine?**

- Um **Shine** representa uma unidade de aprendizado dentro do app.
- Ele pode ser um **assunto macro** (amplo e abrangente) ou um **assunto específico** (mais detalhado e especializado).
- Cada **Shine** tem um conjunto de **perguntas padrão**, garantindo que ele forneça um conhecimento e entendimento mínimo sobre o tema.

---

### 🌳 **Estrutura e Rede de Shines**

- Os **Shines** estão organizados em uma **árvore de conhecimento**, criando uma conexão entre eles.
- Ao completar um Shine, o usuário **desbloqueia** os Shines relacionados na árvore.
- Isso permite um aprendizado **progressivo e interconectado**, ajudando a expandir os conhecimentos de forma estruturada.

---

### 🔄 **Revisão e Fixação de Conhecimento**

- Para revisar os conhecimentos estudados, cada Shine gera **Flashcards** baseados nas perguntas padrão.
- Os Flashcards são divididos em **3 grupos** para facilitar a revisão do aprendizado anterior.
- Esse método garante que o usuário tenha contato contínuo com os conceitos, reforçando a memorização e compreensão.

---

### 🧠 **Resumo da Jornada do Usuário**

1. O usuário escolhe um **Shine** para estudar.
2. Ele responde a uma lista de **perguntas padrão**, garantindo um aprendizado mínimo sobre o assunto.
3. Ao finalizar, novos **Shines relacionados são desbloqueados** na árvore de conhecimento.
4. O Shine gera **Flashcards** para que o usuário possa revisar futuramente.
5. O ciclo se repete, expandindo os conhecimentos de maneira **generalista e conectada**.

---

### 💡 **Pontos Positivos da Estrutura**

✅ Permite um **aprendizado estruturado e progressivo**.\
✅ Mantém o usuário **motivado** com o desbloqueio de novos conteúdos.\
✅ Usa **flashcards** para garantir a **fixação do conhecimento**.\
✅ Funciona tanto para quem quer uma visão geral quanto para quem busca especialização.

---


## Flash Cards ( Cartões para revisão espaçada )

---

### 📌 **Estrutura dos Flashcards no Ignitive**

Os **Flashcards** serão apresentados ao usuário para reforçar o aprendizado dos **Shines**, e o sistema usará um mecanismo de repetição baseada na dificuldade da resposta.

---

### 🔥 **Fluxo de Uso dos Flashcards**

1. **Apresentação do Flashcard** → O usuário vê a pergunta e tenta lembrar da resposta.
2. **Registro da Resposta** → O usuário avalia sua resposta em uma escala de dificuldade.
3. **Reorganização da Fila** → O Flashcard volta para a fila em uma nova posição com base na dificuldade.

---

### 🎯 **Escala de Dificuldade**

Cada Flashcard será classificado de acordo com o quão fácil foi lembrar a resposta:

1️⃣ **Muito Difícil** → Volta para o **início** da fila (será revisado em breve).\
2️⃣ **Difícil** → Volta para uma posição intermediária.\
3️⃣ **Fácil** → Vai para o final da fila.\
4️⃣ **Muito Fácil** → Pode ser removido temporariamente ou revisado apenas depois de um tempo maior.

---

### 📂 **Estrutura do Objeto Flashcard**

Cada **Flashcard** deve conter:

- **`id`** → Identificador único do flashcard.
- **`shine_id`** → Referência ao Shine ao qual pertence.
- **`question`** → Pergunta do flashcard.
- **`answer`** → Resposta esperada.
- **`difficulty`** → Última dificuldade registrada.
- **`review_count`** → Quantidade de vezes que foi revisado.
- **`next_review`** → Momento em que será revisado novamente.

---

### 🔄 **Mecânica de Revisão**

- O usuário responde o Flashcard e marca a dificuldade.
- Com base na dificuldade, o sistema decide **quando** ele será revisado novamente.
- Flashcards muito fáceis podem ser removidos temporariamente.
- Flashcards difíceis aparecerão com mais frequência até ficarem fáceis.

Isso segue um modelo inspirado no **Spaced Repetition System (SRS)**, usado em apps como Anki e Duolingo.

---
