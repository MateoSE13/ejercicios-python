MAX_COLABORADORES = 15

def leer_colaboradores(archivo):
    try:
        with open(archivo, 'r') as f:
            return [linea.strip() for linea in f]
    except FileNotFoundError:
        return []

def agregar_colaborador(archivo, colaborador):
    colaboradores = leer_colaboradores(archivo)
    if len(colaboradores) < MAX_COLABORADORES:
        colaboradores.append(colaborador)
        with open(archivo, 'w') as f:
            f.write('\n'.join(colaboradores) + '\n')
        print(f"Colaborador {colaborador} agregado.")
    else:
        print("Límite de colaboradores alcanzado.")

def main():
    archivo = "colaboradores.txt"
    colaboradores = leer_colaboradores(archivo)
    print("Colaboradores:\n" + "\n".join(colaboradores[:5]))
    if input("¿Agregar nuevo colaborador? (s/n): ").lower() == 's':
        nuevo_colaborador = input("Nombre del nuevo colaborador: ").strip().upper()
        agregar_colaborador(archivo, nuevo_colaborador)

if __name__ == "__main__":
    main()
