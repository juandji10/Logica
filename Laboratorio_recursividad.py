import os

class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, valor):
        nuevo = NodoCola(valor)
        if self.final:
            self.final.siguiente = nuevo
        self.final = nuevo
        if not self.frente:
            self.frente = nuevo

    def desencolar(self):
        if not self.frente:
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if not self.frente:
            self.final = None
        return valor

    def esta_vacia(self):
        return self.frente is None

    def mostrar(self):
        actual = self.frente
        orden = []
        while actual:
            orden.append(actual.valor)
            actual = actual.siguiente
        return orden

def contar_fotos(ruta, cola):
    """
    Función recursiva que cuenta las fotos dentro de una carpeta y sus subcarpetas.
    """
    total = 0

   
    cola.encolar(ruta)

    
    try:
        for elemento in os.listdir(ruta):
            camino = os.path.join(ruta, elemento)
            if os.path.isfile(camino):
                # Si es archivo, verificar extensión
                if any(camino.lower().endswith(ext) for ext in extensiones):
                    total += 1
            elif os.path.isdir(camino):
                # Caso recursivo: entrar a la subcarpeta
                total += contar_fotos(camino, cola)
    except PermissionError:
        # Evita errores de permisos
        pass

    return total


# --------------------------
# Programa principal
# --------------------------
if __name__ == "__main__":
    ruta_principal = input("Ingrese la ruta de la carpeta principal: ")
    cola_carpetas = Cola()
    

    total_fotos = contar_fotos(ruta_principal, cola_carpetas)

    print("\n--- RESULTADOS ---")
    print("Total de fotos encontradas:", total_fotos)
    print("\nOrden de procesamiento de carpetas:")
    for carpeta in cola_carpetas.mostrar():
        print("→", carpeta)
