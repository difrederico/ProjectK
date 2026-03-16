"""
Constantes globais do sistema Project-CK
Centraliza valores usados em múltiplos módulos para evitar duplicação
"""

# ===== CORES DE SENTIMENTOS =====
# Mapeamento de cores para visualização de sentimentos no dashboard
SENTIMENT_COLORS = {
    'feliz': '#4CAF50',       # Verde para felicidade
    'animado': '#FFC107',     # Amarelo para animação
    'neutro': '#9E9E9E',      # Cinza para neutro
    'cansado': '#607D8B',     # Azul acinzentado para cansaço
    'triste': '#2196F3',      # Azul para tristeza
    'ansioso': '#FF5722',     # Laranja/Vermelho para ansiedade
    'com raiva': '#F44336',   # Vermelho para raiva
    'confuso': '#7B1FA2',     # Roxo para confusão
    'assustado': '#00BCD4',   # Azul claro para medo
}

# Lista ordenada de sentimentos (do mais positivo ao mais negativo)
SENTIMENTS_ORDER = [
    'feliz',
    'animado',
    'neutro',
    'cansado',
    'confuso',
    'triste',
    'ansioso',
    'assustado',
    'com raiva'
]

# ===== CONFIGURAÇÕES DE CRISE =====
# Parâmetros para detecção de crise (IoT)
CRISIS_THRESHOLDS = {
    'heart_rate_max': 130,     # bpm - Batimento cardíaco máximo
    'gsr_max': 1.5,            # GSR máximo (resposta galvânica da pele)
    'time_window_minutes': 5,  # Janela de tempo para considerar crise (minutos)
}

# ===== TIPOS DE USUÁRIO =====
# Tipos válidos de usuário no sistema
USER_TYPES = ['aluno', 'professor', 'responsavel', 'admin']

# ===== CONFIGURAÇÕES DE CACHE =====
# TTL (Time To Live) para cache do Streamlit (em segundos)
CACHE_TTL = {
    'students': 300,      # 5 minutos
    'classes': 300,       # 5 minutos
    'feelings': 600,      # 10 minutos
    'crisis_alerts': 120, # 2 minutos (mais frequente para alertas)
}

# ===== CONFIGURAÇÕES DE API =====
# Configurações do cliente de API
API_CONFIG = {
    'timeout': 10,           # Timeout de requisição em segundos
    'max_retries': 3,        # Número máximo de tentativas
    'base_url': 'http://localhost:5001/api',  # URL base da API
}

# ===== MENSAGENS DO SISTEMA =====
# Mensagens padrão usadas no sistema
MESSAGES = {
    'login_success': 'Login realizado com sucesso!',
    'login_error': 'Usuario ou senha incorretos',
    'api_error': 'Erro ao conectar com o servidor. Tente novamente.',
    'no_data': 'Nenhum dado disponivel no momento.',
    'loading': 'Carregando...',
    'feature_dev': 'Funcionalidade em desenvolvimento',
}

# ===== EMOJIS =====
# Emojis para diferentes contextos
EMOJIS = {
    'student': '👨‍🎓',
    'teacher': '👨‍🏫',
    'parent': '👨‍👩‍👧',
    'admin': '⚙️',
    'class': '🏫',
    'feeling': '😊',
    'crisis': '🚨',
    'chart': '📊',
    'calendar': '📅',
    'message': '💬',
}


