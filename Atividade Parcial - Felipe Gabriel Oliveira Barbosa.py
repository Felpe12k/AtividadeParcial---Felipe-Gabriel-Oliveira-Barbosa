class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao):
        self._titulo = titulo
        self.ano_publicacao = ano_publicacao

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, novo_ano):
        if isinstance(novo_ano, int) and novo_ano > 0:
            self._ano_publicacao = novo_ano
        else:
            print("Erro: O ano de publicação deve ser um número inteiro positivo.")

    def apresentar_detalhes(self):
        return f"Título: {self._titulo} | Ano: {self._ano_publicacao}"


class Livro(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, autor, num_paginas):
        super().__init__(titulo, ano_publicacao)
        self._autor = autor
        self.num_paginas = num_paginas

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, novo_autor):
        self._autor = novo_autor

    @property
    def num_paginas(self):
        return self._num_paginas

    @num_paginas.setter
    def num_paginas(self, novo_num_paginas):
        if isinstance(novo_num_paginas, int) and novo_num_paginas > 50:
            self._num_paginas = novo_num_paginas
        else:
            print("Erro: O número de páginas deve ser maior que 50.")

    def apresentar_detalhes(self):
        return (f"[LIVRO] Título: {self._titulo} | Ano: {self._ano_publicacao} | "
                f"Autor: {self._autor} | Páginas: {self._num_paginas}")


class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, edicao, volume):
        super().__init__(titulo, ano_publicacao)
        self._edicao = edicao
        self._volume = volume

    @property
    def edicao(self):
        return self._edicao

    @edicao.setter
    def edicao(self, nova_edicao):
        self._edicao = nova_edicao

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, novo_volume):
        self._volume = novo_volume

    def apresentar_detalhes(self):
        return (f"[REVISTA] Título: {self._titulo} | Ano: {self._ano_publicacao} | "
                f"Edição: {self._edicao} | Volume: {self._volume}")


l1 = Livro("Dom Casmurro", 1899, "Machado de Assis", 256)
r1 = Revista("Super Interessante", 2023, 314, 12)
l2 = Livro("Python para Todos", 2020, "John Zelle", 350)
acervo = [l1, r1, l2]


def menu():
    while True:
        print("\n===== MENU BIBLIOTECA =====")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Revista")
        print("3. Listar Acervo")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            ano = int(input("Ano de publicação: "))
            autor = input("Autor: ")
            paginas = int(input("Número de páginas: "))
            livro = Livro(titulo, ano, autor, paginas)
            acervo.append(livro)
            print("Livro cadastrado com sucesso.")

        elif opcao == "2":
            titulo = input("Título da revista: ")
            ano = int(input("Ano de publicação: "))
            edicao = int(input("Edição: "))
            volume = int(input("Volume: "))
            revista = Revista(titulo, ano, edicao, volume)
            acervo.append(revista)
            print("Revista cadastrada com sucesso.")

        elif opcao == "3":
            print("\n===== ACERVO DA BIBLIOTECA =====")
            for item in acervo:
                print(item.apresentar_detalhes())

        elif opcao == "4":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
