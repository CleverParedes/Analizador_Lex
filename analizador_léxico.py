import ply.lex as lex

# Lista de palabras clave
palabrasClave = {
    'SELECT': 'SELECT',
    'FROM': 'FROM',
    'WHERE': 'WHERE',
    'IF': 'IF'
}

# Definición de tokens
tokens = [
    'PC',
    'ID',  
    'OPREL',  
    'NUMERO',  
    'SIGNO'  
] + list(palabrasClave.values())

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabrasClave.get(t.value.upper(), 'ID')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_OPREL(t):
    r'<|>|='
    return t

def t_SIGNO(t):
    r','
    return t

# Errores
def t_error(t):
    print("ERROR: Valor no aceptado '%s'" % t.value[0])
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()

