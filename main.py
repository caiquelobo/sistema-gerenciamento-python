"""
============================================================================
PROJETO: Sistema de Gerenciamento de Registros / Tarefas
TECNOLOGIAS: Python 3.10+ | Programação Orientada a Objetos (POO)
============================================================================
"""

import sys
from typing import List, Optional


# ----------------------------------------------------------------------------
# 1. CLASSE DE MODELO (Entidade do Sistema)
# ----------------------------------------------------------------------------
class Item:
    def __init__(self, item_id: int, titulo: str, descricao: str):
        self.id = item_id
        self.titulo = titulo
        self.descricao = descricao
        self.ativo = True

    def alternar_status(self) -> None:
        """Alterna o status do item entre Ativo e Inativo."""
        self.ativo = not self.ativo

    def __str__(self) -> str:
        status = "[ATIVO]" if self.ativo else "[INATIVO]"
        return f"ID: {self.id:03d} | Status: {status:<9} | Título: {self.titulo:<20} | Descrição: {self.descricao}"


# ----------------------------------------------------------------------------
# 2. CLASSE DE GERENCIAMENTO (Regras de Negócio e Operações CRUD)
# ----------------------------------------------------------------------------
class GerenciadorDeItens:
    def __init__(self):
        self._itens: List[Item] = []
        self._proximo_id: int = 1

    def adicionar(self, titulo: str, descricao: str) -> Item:
        novo_item = Item(self._proximo_id, titulo, descricao)
        self._itens.append(novo_item)
        self._proximo_id += 1
        return novo_item

    def listar_todos(self) -> List[Item]:
        return self._itens

    def buscar_por_id(self, item_id: int) -> Optional[Item]:
        for item in self._itens:
            if item.id == item_id:
                return item
        return None

    def remover(self, item_id: int) -> bool:
        item = self.buscar_por_id(item_id)
        if item:
            self._itens.remove(item)
            return True
        return False


# ----------------------------------------------------------------------------
# 3. INTERFACE E EXECUÇÃO PRINCIPAL
# ----------------------------------------------------------------------------
def exibir_cabecalho():
    print("=" * 50)
    print("     SISTEMA DE GERENCIAMENTO (PYTHON)           ")
    print("=" * 50)


def exibir_menu():
    print("\n---------------- MENU PRINCIPAL ----------------")
    print("1. Cadastrar Item")
    print("2. Listar Todos os Itens")
    print("3. Buscar Item por ID")
    print("4. Alternar Status (Ativo/Inativo)")
    print("5. Remover Item")
    print("0. Sair")
    print("------------------------------------------------")


def main():
    gerenciador = GerenciadorDeItens()
    exibir_cabecalho()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- CADASTRAR ITEM ---")
            titulo = input("Digite o título: ").strip()
            descricao = input("Digite a descrição: ").strip()

            if titulo and descricao:
                item_criado = gerenciador.adicionar(titulo, descricao)
                print(f"✅ Item cadastrado com sucesso! ID: {item_criado.id}")
            else:
                print("⚠️ Título e descrição não podem ser vazios.")

        elif opcao == "2":
            print("\n--- LISTA DE ITENS ---")
            itens = gerenciador.listar_todos()
            if not itens:
                print("Nenhum item cadastrado.")
            else:
                for item in itens:
                    print(item)

        elif opcao == "3":
            print("\n--- BUSCAR POR ID ---")
            try:
                item_id = int(input("Digite o ID do item: "))
                item = gerenciador.buscar_por_id(item_id)
                if item:
                    print(f"\nEncontrado: {item}")
                else:
                    print("❌ Item não encontrado.")
            except ValueError:
                print("⚠️ Digite apenas números inteiros válidos.")

        elif opcao == "4":
            print("\n--- ALTERAR STATUS ---")
            try:
                item_id = int(input("Digite o ID do item: "))
                item = gerenciador.buscar_por_id(item_id)
                if item:
                    item.alternar_status()
                    print(f"✅ Status do item {item.id} alterado com sucesso.")
                else:
                    print("❌ Item não encontrado.")
            except ValueError:
                print("⚠️ Digite apenas números inteiros válidos.")

        elif opcao == "5":
            print("\n--- REMOVER ITEM ---")
            try:
                item_id = int(input("Digite o ID a ser removido: "))
                if gerenciador.remover(item_id):
                    print("✅ Item removido com sucesso.")
                else:
                    print("❌ Item não encontrado.")
            except ValueError:
                print("⚠️ Digite apenas números inteiros válidos.")

        elif opcao == "0":
            print("\nEncerrando a aplicação... Até mais!")
            sys.exit(0)

        else:
            print("⚠️ Opção inválida. Escolha um número de 0 a 5.")


if __name__ == "__main__":
    main()
