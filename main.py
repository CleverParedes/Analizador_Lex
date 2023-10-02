from analizador_léxico import lexer 

def analizar_entrada(entrada):
    lexer.input(entrada)
    
    # Tokenización
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'ID':
            print(f'ID: {tok.value}')
        elif tok.type == 'NUMERO':
            print(f'NUMERO: {tok.value}')
        elif tok.type == 'SIGNO':
            print(f'SIGNO: {tok.value}')
        elif tok.type == 'OPREL':
            print(f'OPREL: {tok.value}')
        else:
            print(f'PC: {tok.value}')

entradas = [
    "Select name FroM table2 WHEre a2 = 15",
    "SELECT col1, col2 from mi_Tabla wHERE col1 < 20",
    "SELECT tabla, correo FROM empleados WHERE salario > 50000;",
    "SELECT alumnos, carrera  * FROM calificaciones where nota > 16+1;"
]

for entrada in entradas:
    print(f"Entrada: {entrada}")
    analizar_entrada(entrada)
    print("\n")
