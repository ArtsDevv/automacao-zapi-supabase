from database import buscar_contatos_pendentes

def main():
    print("Buscando contatos pendentes...")
    contatos = buscar_contatos_pendentes()
    
    if not contatos:
        print("Nenhum contato pendente encontrado.")
    else:
        print(f"Encontrados {len(contatos)} contato(s):")
        for contato in contatos:
            print(f"- {contato['nome_contato']} ({contato['telefone']})")

if __name__ == "__main__":
    main()