def gerar_sugestoes(pedido):
    pedido = pedido.lower()

    sugestoes = []

    if "fantasia" in pedido or "magia" in pedido:
        sugestoes.append(
            "Harry Potter — J. K. Rowling: fantasia com magia e aventura."
        )
        sugestoes.append(
            "O Senhor dos Anéis — J. R. R. Tolkien: aventura em um mundo fantástico."
        )

    if "romance" in pedido:
        sugestoes.append(
            "Orgulho e Preconceito — Jane Austen: um clássico romance."
        )
        sugestoes.append(
            "Como Eu Era Antes de Você — Jojo Moyes: romance contemporâneo."
        )

    if "aventura" in pedido:
        sugestoes.append(
            "Percy Jackson — Rick Riordan: aventura com mitologia."
        )

    if "mistério" in pedido or "suspense" in pedido:
        sugestoes.append(
            "O Assassinato no Expresso do Oriente — Agatha Christie: mistério clássico."
        )

    if not sugestoes:
        sugestoes.append(
            "O Pequeno Príncipe — Antoine de Saint-Exupéry: uma leitura clássica e inspiradora."
        )
        sugestoes.append(
            "1984 — George Orwell: ficção clássica."
        )
        sugestoes.append(
            "A Menina que Roubava Livros — Markus Zusak: drama histórico."
        )

    return "\n\n".join(sugestoes)