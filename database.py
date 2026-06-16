from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Credenciais do Supabase não encontradas no arquivo .env")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos_pendentes():
    """Busca no banco todos os contatos que ainda não receberam a mensagem."""
    try:
        response = supabase.table("contatos").select("*").eq("mensagem_enviada", False).execute()
        return response.data
    except Exception as e:
        print(f"Erro ao buscar contatos no Supabase: {e}")
        return []

def marcar_mensagem_como_enviada(contato_id):
    """Atualiza o status do contato indicando que a mensagem foi enviada."""
    try:
        supabase.table("contatos").update({"mensagem_enviada": True}).eq("id", contato_id).execute()
    except Exception as e:
        print(f"Erro ao atualizar o contato {contato_id}: {e}")