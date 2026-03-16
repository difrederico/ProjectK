from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
import random

# Conexão
client = MongoClient("mongodb://localhost:27017/project-ckDB")
db = client.get_default_database()

print("Iniciando Geracao de Sentimentos (Diario Emocional)...")

# 1. LIMPEZA
# Verifica qual é o nome da coleção. Geralmente é 'feelings' ou 'sentimentos'.
# O arquivo CSV anterior indicava 'feelings', mas vamos garantir.
col_feelings = db.feelings 
deleted = col_feelings.delete_many({})
print(f"Limpeza concluida: {deleted.deleted_count} registros antigos apagados.")

# 2. DEFINIÇÃO DOS ALUNOS (IDs Reais do Dump)
ALUNOS = [
    {
        "id": ObjectId("69111874ca4398a1897afba3"), 
        "nome": "Ana Sofia", 
        "perfil": ["feliz", "animado", "neutro", "feliz", "cansado"] # Perfil Calmo
    },
    {
        "id": ObjectId("69111874ca4398a1897afba4"), 
        "nome": "Lucas Silva", 
        "perfil": ["ansioso", "cansado", "triste", "neutro", "ansioso"] # Perfil Ansioso (bate com o IoT)
    },
    {
        "id": ObjectId("69111874ca4398a1897afba5"), 
        "nome": "Clara Lima", 
        "perfil": ["feliz", "neutro", "animado", "triste", "feliz"] # Perfil Normal
    },
    {
        "id": ObjectId("69111874ca4398a1897afba6"), 
        "nome": "Diogo Mendes", 
        "perfil": ["neutro", "cansado", "feliz", "neutro", "animado"] # Perfil Moderado
    }
]

# Mapeamento de Emojis (Para ficar bonito no banco)
EMOJIS = {
    "feliz": "😊",
    "animado": "🎉",
    "neutro": "😐",
    "cansado": "😫",
    "triste": "😢",
    "ansioso": "😰",
    "com raiva": "😡"
}

COMENTARIOS = {
    "feliz": ["Tive um bom dia!", "Gostei da aula de artes.", "Brinquei muito no recreio."],
    "ansioso": ["Estou nervoso com a prova.", "Muito barulho na sala.", "Quero ir para casa."],
    "cansado": ["Não dormi bem.", "Aula de educação física cansou.", "Com sono."],
    "neutro": ["Dia normal.", "Tudo bem.", "Nada a declarar."],
    "triste": ["Perdi meu lápis.", "Brigaram comigo.", "Estou chateado."],
    "animado": ["Vou jogar bola!", "Tirei nota boa!", "Dia incrível!"],
    "com raiva": ["Não gostei da atividade.", "Me empurraram.", "Estou bravo."]
}

# 3. GERAÇÃO NO TEMPO (Últimos 30 dias)
registros = []
data_hoje = datetime.datetime.utcnow()

print("[INFO] Gerando historico de 30 dias...")

for dia in range(30):
    data_base = data_hoje - datetime.timedelta(days=dia)
    
    # Pula fins de semana (Sábado=5, Domingo=6) para ser realista (escola)
    if data_base.weekday() >= 5:
        continue
        
    for aluno in ALUNOS:
        # 80% de chance de o aluno registrar algo nesse dia
        if random.random() < 0.8:
            # Escolhe sentimento baseado no perfil do aluno
            sentimento = random.choice(aluno['perfil'])
            
            # Define horário aleatório (entre 08:00 e 16:00)
            hora = random.randint(8, 16)
            minuto = random.randint(0, 59)
            data_registro = data_base.replace(hour=hora, minute=minuto, second=0, microsecond=0)
            
            registro = {
                "aluno_id": aluno['id'],
                "sentimento": sentimento,
                "emoji": EMOJIS.get(sentimento, "😐"),
                "descricao": random.choice(COMENTARIOS.get(sentimento, [""])),
                "timestamp": data_registro,
                # Campos extras para facilitar queries simples
                "student_email": f"{aluno['nome'].lower().replace(' ', '.')}@aluno.dev",
                "data_str": data_registro.strftime("%Y-%m-%d")
            }
            registros.append(registro)

# 4. INSERÇÃO
if registros:
    # Ordena por data (do mais antigo para o mais novo)
    registros.sort(key=lambda x: x['timestamp'])
    col_feelings.insert_many(registros)
    print(f"[OK] Sucesso! {len(registros)} sentimentos inseridos para os 4 alunos.")
else:
    print("[AVISO] Nenhum registro gerado.")

print("\n[OK] Agora o Dashboard vai mostrar graficos consistentes!")