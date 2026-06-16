import time
from database import buscar_contatos_pendentes, marcar_mensagem_como_enviada
from whatsapp import enviar_mensagem

def main():
    print("Iniciando automação de envios...\n")
    contatos = buscar_contatos_pendentes()
    
    if not contatos:
        print("Nenhum contato pendente para envio encontrado no Supabase.")
        return

    print(f"Encontrados {len(contatos)} contato(s) na fila.\n")
    
    for contato in contatos:
        id_contato = contato['id']
        nome = contato['nome_contato']
        telefone = contato['telefone']
        
        sucesso = enviar_mensagem(telefone, nome)
        
        if sucesso:
            marcar_mensagem_como_enviada(id_contato)
            print(f"🔄 Banco de dados atualizado para o contato ID: {id_contato}\n")
        
        time.sleep(2)
        
    print("🏁 Fluxo finalizado com sucesso!")

if __name__ == "__main__":
    main()