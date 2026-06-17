# Automação de Disparos WhatsApp (Supabase + Z-API)

Um sistema desenvolvido em Python para ler contatos armazenados no Supabase e enviar mensagens personalizadas via WhatsApp utilizando a Z-API.

## 🛠️ Tecnologias Utilizadas
* Python 3
* Supabase (PostgreSQL em nuvem)
* Z-API (API de integração com WhatsApp)
* Bibliotecas: `supabase`, `requests`, `python-dotenv`

## ⚙️ Setup do Banco de Dados (Supabase)

Crie uma tabela chamada `contatos` executando o seguinte script no SQL Editor do Supabase:

```sql
create table contatos (
  id uuid default gen_random_uuid() primary key,
  nome_contato text not null,
  telefone text not null,
  mensagem_enviada boolean default false
);

## 🔐 Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto seguindo o modelo do arquivo .env.example (nunca suba o .env original para o GitHub). Ele deve conter a seguinte estrutura:

SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_anon_do_supabase

ZAPI_INSTANCE_ID=seu_id_da_instancia_zapi
ZAPI_TOKEN=seu_token_da_zapi

## 🚀 Como Executar o Projeto

1. Clone este repositório:

git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd automacao-zapi-supabase

2. Crie e ative um ambiente virtual:

python -m venv venv

# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate

3. Instale as dependências:

pip install -r requirements.txt

4. Execute o script principal:

python main.py
