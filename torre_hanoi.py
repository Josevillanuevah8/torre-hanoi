
import time

def torre_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        movimientos.append((origen, destino))
    else:
        torre_hanoi(n - 1, origen, destino, auxiliar)
        movimientos.append((origen, destino))
        torre_hanoi(n - 1, auxiliar, origen, destino)

def ejecutar(n):
    global movimientos
    movimientos = []

    inicio = time.perf_counter()
    torre_hanoi(n, "A", "B", "C")
    fin = time.perf_counter()

    print(f"\nDiscos: {n}")
    print(f"Movimientos: {len(movimientos)}")
    print(f"Tiempo: {fin - inicio:.6f} segundos")

    if n <= 10:
        print("Lista de movimientos:")
        for i, movimiento in enumerate(movimientos, start=1):
            print(f"{i}. Mover disco de {movimiento[0]} a {movimiento[1]}")

if __name__ == "__main__":
    for cantidad in [5, 10, 30, 64]:
        ejecutar(cantidad)
