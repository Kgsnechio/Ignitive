import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models import Shine, SessionLocal

# Dados JSON que criamos
shines_data = [
    {"id": 1, "parent_id": None, "topic": "Programação", "answers": [
        "Programação é o processo de escrever código para criar softwares e automação, sendo essencial na era digital.",
        "Os conceitos essenciais incluem lógica de programação, algoritmos, sintaxe das linguagens e estrutura de dados.",
        "É aplicada em desenvolvimento de aplicativos, automação de tarefas, inteligência artificial e segurança cibernética.",
        "Se conecta com áreas como matemática, engenharia, ciência de dados e automação.",
        "Os próximos passos incluem aprender linguagens como Python, resolver problemas práticos e construir projetos."
    ]},
    {"id": 2, "parent_id": 1, "topic": "Python", "answers": [
        "Python é uma linguagem de programação versátil e fácil de aprender, usada para desenvolvimento web, análise de dados e IA.",
        "Os conceitos essenciais incluem sintaxe simples, orientação a objetos, bibliotecas populares e tipagem dinâmica.",
        "É aplicada em desenvolvimento web, automação, ciência de dados, aprendizado de máquina e cibersegurança.",
        "Se conecta com outras linguagens como C, JavaScript e frameworks como Django e Flask.",
        "Os próximos passos são aprender a sintaxe básica, praticar com projetos pequenos e explorar bibliotecas úteis."
    ]},
    {"id": 3, "parent_id": 1, "topic": "Estruturas de Dados", "answers": [
        "Estruturas de dados são formas organizadas de armazenar e gerenciar informações para otimizar desempenho.",
        "Os conceitos essenciais incluem listas, pilhas, filas, árvores, grafos e tabelas hash.",
        "São aplicadas em algoritmos de busca, ordenação, bancos de dados e otimização de software.",
        "Se conecta com algoritmos, complexidade computacional e linguagens de programação.",
        "Os próximos passos incluem estudar listas ligadas, árvores binárias e implementar estruturas em diferentes linguagens."
    ]},
    {"id": 4, "parent_id": None, "topic": "Física", "answers": [
        "Física é a ciência que estuda as leis naturais do universo, desde o movimento até as forças fundamentais.",
        "Os conceitos essenciais incluem mecânica, termodinâmica, eletromagnetismo e física quântica.",
        "É aplicada na engenharia, tecnologia, medicina e até na exploração espacial.",
        "Se conecta com matemática, química e astronomia.",
        "Os próximos passos são estudar cinemática, forças e aprofundar em teoria quântica."
    ]},
    {"id": 5, "parent_id": 4, "topic": "Mecânica Clássica", "answers": [
        "Mecânica Clássica estuda o movimento dos corpos e as forças que os afetam.",
        "Os conceitos essenciais incluem leis de Newton, energia, impulso e conservação do momento.",
        "É aplicada em engenharia, transportes, esportes e previsões de movimento.",
        "Se conecta com cálculo, dinâmica de fluidos e engenharia mecânica.",
        "Os próximos passos incluem resolver problemas de dinâmica e aprender sobre forças e aceleração."
    ]},
    {
        "id": 6,
        "parent_id": None,
        "topic": "História",
        "answers": [
            "História é o estudo dos eventos passados, ajudando a entender a evolução da sociedade e suas culturas.",
            "Os conceitos essenciais incluem períodos históricos, fontes primárias e secundárias, historiografia e civilizações antigas.",
            "É aplicada na educação, política, preservação cultural e análise de padrões sociais.",
            "Se conecta com antropologia, sociologia e arqueologia.",
            "Os próximos passos são estudar eventos marcantes, interpretar documentos históricos e entender diferentes perspectivas."
    ]},
    {
        "id": 7,
        "parent_id": 6,
        "topic": "Idade Média",
        "answers": [
            "A Idade Média foi um período da história entre os séculos V e XV, marcado pelo feudalismo e pela influência da Igreja.",
            "Os conceitos essenciais incluem feudalismo, cruzadas, renascimento comercial e sociedade medieval.",
            "É aplicada no estudo das origens das nações modernas, influências culturais e evolução política.",
            "Se conecta com a história do cristianismo, a formação da Europa moderna e as influências islâmicas.",
            "Os próximos passos incluem estudar a transição para a Idade Moderna e as revoluções culturais e políticas da época."
    ]},
    {
        "id": 8,
        "parent_id": None,
        "topic": "Biologia",
        "answers": [
            "Biologia é a ciência que estuda os seres vivos e seus processos vitais, sendo essencial para a medicina e ecologia.",
            "Os conceitos essenciais incluem células, genética, evolução, ecossistemas e fisiologia.",
            "É aplicada na medicina, biotecnologia, conservação ambiental e agricultura.",
            "Se conecta com química, física e geociências.",
            "Os próximos passos são estudar biologia molecular, genética e impactos ambientais."
    ]},
    {
        "id": 9,
        "parent_id": 8,
        "topic": "Genética",
        "answers": [
            "Genética é o estudo dos genes e hereditariedade, sendo fundamental para entender a evolução e doenças genéticas.",
            "Os conceitos essenciais incluem DNA, RNA, mutações, herança genética e engenharia genética.",
            "É aplicada na medicina, biotecnologia, melhoramento genético e estudos de evolução.",
            "Se conecta com biologia molecular, bioquímica e microbiologia.",
            "Os próximos passos incluem estudar mapeamento genético, edição de genes e aplicações em saúde."
    ]},
    {"id": 10,
        "parent_id": None,
        "topic": "Filosofia",
        "answers": [
            "Filosofia é o estudo das questões fundamentais sobre a existência, conhecimento e ética.",
            "Os conceitos essenciais incluem metafísica, epistemologia, ética, lógica e filosofia política.",
            "É aplicada na argumentação, reflexão crítica, ética profissional e política.",
            "Se conecta com psicologia, ciência política e história das ideias.",
            "Os próximos passos incluem estudar filósofos clássicos, desenvolver pensamento crítico e explorar diferentes correntes filosóficas."
    ]},{
        "id": 11,
        "topic": "Programação Orientada a Objetos",
        "parent_id": 1,
        "answers": [
            "Programação Orientada a Objetos (POO) é um paradigma que organiza o código em classes e objetos.",
            "Conceitos essenciais incluem classes, objetos, herança, encapsulamento e polimorfismo.",
            "POO é usada para estruturar código de forma modular e reutilizável.",
            "Se conecta com padrões de design e boas práticas de desenvolvimento.",
            "Para aprofundar, estude padrões de projeto como Singleton e Factory."
        ]
    },
    {   "id": 12,
        "topic": "Herança na POO",
        "parent_id": 11,
        "answers": [
            "Herança é um mecanismo da POO que permite que uma classe derive características de outra.",
            "Conceitos essenciais incluem classes base, subclasses e sobrescrita de métodos.",
            "Usada para reutilizar código e criar hierarquias de classes.",
            "Relaciona-se com encapsulamento e polimorfismo.",
            "Para aprofundar, estude exemplos práticos e frameworks que utilizam herança."
        ]
    },
    {
        "id": 13,
        "topic": "Polimorfismo na POO",
        "parent_id": 11,
        "answers": [
            "Polimorfismo permite que métodos tenham diferentes comportamentos com base no contexto.",
            "Conceitos essenciais incluem sobrescrita e sobrecarga de métodos.",
            "É útil para flexibilidade e reutilização de código.",
            "Se conecta com herança e interfaces.",
            "Para aprofundar, implemente exemplos práticos em diferentes linguagens."
        ]
    },
    {
        "id": 14,
        "topic": "Machine Learning",
        "parent_id": 2,
        "answers": [
            "Machine Learning é um campo da IA que permite que computadores aprendam a partir de dados.",
            "Conceitos essenciais incluem modelos supervisionados, não supervisionados e deep learning.",
            "Aplicado em reconhecimento de padrões, previsão e recomendação.",
            "Relaciona-se com estatística, matemática e ciência de dados.",
            "Para aprofundar, explore algoritmos como regressão linear e redes neurais."
        ]
    },
    {
        "id": 15,
        "topic": "Redes Neurais Artificiais",
        "parent_id": 14,
        "answers": [
            "Redes neurais são modelos inspirados no funcionamento do cérebro humano.",
            "Conceitos essenciais incluem neurônios artificiais, camadas e funções de ativação.",
            "Aplicadas em reconhecimento de imagens, processamento de linguagem e previsão.",
            "Relacionam-se com deep learning e inteligência artificial.",
            "Para aprofundar, estude frameworks como TensorFlow e PyTorch."
        ]
    }
]

# Criar sessão
session = SessionLocal()

# Inserir os dados
for shine_data in shines_data:
    shine = Shine(**shine_data)
    session.add(shine)

# Commitando as alterações
session.commit()

# Fechando a sessão
session.close()
