import requests
from config import ZAPI_INSTANCE_ID, ZAPI_TOKEN

def enviar_mensagem(telefone, nome_contato):
    """Envia uma mensagem de WhatsApp via Z-API."""
    
    if not ZAPI_INSTANCE_ID or not ZAPI_TOKEN:
        print("Erro: Credenciais da Z-API ausentes no .env")
        return False

    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    
    mensagem = f"Olá, {nome_contato} tudo bem com você?"
    
    payload = {
        "phone": telefone,
        "message": mensagem
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status() 
        
        print(f"✅ Mensagem enviada com sucesso para: {nome_contato}")
        return True
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao enviar para {nome_contato}: {e}")
        return False