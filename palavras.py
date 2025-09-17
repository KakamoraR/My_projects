import random

palavra = [
    "Carro", "Casa", "Janela", "Computador", "Telefone", "Monitor", "Mesa", "Cadeira", "Livro",
    "Caneta", "Garrafa", "Escola", "Trabalho", "Futebol", "Basquete", "Viagem", "Tempo", "Relogio",
    "Cachorro", "Gato", "Peixe", "Passaro", "Amigo", "Familia", "Alegria", "Tristeza", "Fome",
    "Sede", "Comida", "Bebida", "Praia", "Montanha", "Cidade", "Campo", "Floresta", "Jardim",
    "Roda", "Aviao", "Barco", "Moto", "Onibus", "Caminhao", "Estrada", "Rua", "Praca", "Loja",
    "Mercado", "Banco", "Esporte", "Musica", "Danca", "Teatro", "Cinema", "Filme", "Serie",
    "Cultura", "Historia", "Geografia", "Matematica", "Fisica", "Quimica", "Biologia", "Astronomia",
    "Planeta", "Sol", "Lua", "Estrela", "Universo", "Galaxia", "Cosmos", "Energia", "Forca",
    "Saude", "Doenca", "Hospital", "Clinica", "Remedio", "Vacina", "Medico", "Enfermeiro",
    "Paciente", "Exame", "Sangue", "Coracao", "Cerebro", "Corpo", "Pele", "Olho", "Boca", "Nariz",
    "Orelha", "Perna", "Braco", "Mao", "Pedal", "Dedo", "Unha", "Cabelo", "Barba", "Bigode",
    "Camisa", "Calca", "Sapato", "Chinelo", "Vestido", "Saia", "Short", "Jaqueta", "Blusa",
    "Meia", "Chapeu", "Boné", "Relogio", "Oculos", "Colar", "Anel", "Pulseira", "Brinco",
    "Lapis", "Borracha", "Regua", "Caderno", "Agenda", "Relatorio", "Trabalho", "Projeto",
    "Codigo", "Programa", "Sistema", "Aplicativo", "Jogo", "Internet", "Rede", "Servidor",
    "Usuario", "Senha", "Conta", "Dinheiro", "Moeda", "Nota", "Cartao", "Credito", "Debito",
    "Compra", "Venda", "Produto", "Servico", "Cliente", "Fornecedor", "Empresa", "Industria",
    "Comercio", "Loja", "Supermercado", "Padaria", "Restaurante", "Lanchonete", "Cafe", "Cha",
    "Suco", "Agua", "Refrigerante", "Cerveja", "Vinho", "Whisky", "Vodka", "Rum", "Tequila",
    "Pizza", "Hamburguer", "Sanduiche", "Arroz", "Feijao", "Carne", "Frango", "Peixe", "Ovo",
    "Batata", "Tomate", "Cenoura", "Abobora", "Laranja", "Maca", "Banana", "Uva", "Manga",
    "Abacaxi", "Melancia", "Pera", "Cereja", "Morango", "Coco", "Kiwi", "Limao", "Maracuja",
    "Chefe", "Professor", "Aluno", "Diretor", "Gerente", "Funcionario", "Colega", "Vizinho",
    "Turista", "Guia", "Piloto", "Motorista", "Passageiro", "Artista", "Cantor", "Ator", "Atriz",
    "Escritor", "Poeta", "Cientista", "Engenheiro", "Medico", "Advogado", "Juiz", "Policial",
    "Bombeiro", "Soldado", "Rei", "Rainha", "Principe", "Princesa", "Heroi", "Vilao", "Monstro",
    "Dragao", "Fantasma", "Alien", "Robot", "Cyborg", "Computador", "Codigo", "Bug", "Erro",
    "Acerto", "Teste", "Versao", "Atualizacao", "Backup", "Arquivo", "Pasta", "Documento",
    "Imagem", "Video", "Audio", "Texto", "Frase", "caminhao", "Letra", "Numero", "Simbolo",
    "Chave", "Porta", "Janela", "Parede", "Teto", "Chao", "Quarto", "Sala", "Cozinha", "Banheiro",
    "Garagem", "Quintal", "Varanda", "Elevador", "Escada", "Corredor", "Portao", "Muro",
    "Ferias", "Trabalho", "Estudo", "Exercicio", "Treino", "Corrida", "Nado", "Pedalada",
    "Academia", "Bola", "Rede", "Gol", "Ponto", "Vitoria", "Derrota", "Empate", "Campeao",
    "Medalha", "Trofeu", "Competicao", "Corrida", "Maratona", "Olimpiada", "Copa", "Campeonato",
    "Tempo", "Clima", "Chuva", "Sol", "Nuvem", "Vento", "Neve", "Granizo", "Frio", "Calor",
    "Primavera", "Verao", "Outono", "Inverno", "Ano", "Mes", "Semana", "Dia", "Hora", "Minuto",
    "Segundo", "Relogio", "Calendario", "Agenda", "Prazo", "Data", "Futuro", "Passado", "Presente"
]

def palavra_aleatoria():
    nume = random.choice(palavra)
    return nume
