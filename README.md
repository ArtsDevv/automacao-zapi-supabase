# Automação de Disparos WhatsApp (Supabase + Z-API)

Um sistema desenvolvido em Python para ler contatos armazenados no Supabase e enviar mensagens personalizadas via WhatsApp utilizando a Z-API.

## 🛠️ Tecnologias Utilizadas
* Python 3
* Supabase (PostgreSQL em nuvem)
* Z-API (API de integração com WhatsApp)
* Bibliotecas: `supabase`, `requests`, `python-dotenv`

## ⚙️ Setup do Banco de Dados (Supabase)
Crie uma tabela chamada `contatos` executando o seguinte SQL no Supabase:

```sql
create table contatos (
  id uuid default gen_random_uuid() primary key,
  nome_contato text not null,
  telefone text not null,
  mensagem_enviada boolean default false
);
