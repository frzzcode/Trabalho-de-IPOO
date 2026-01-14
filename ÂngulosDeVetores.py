import numpy as np
import matplotlib.pyplot as plt
import math


# ===== FUNÇÃO PARA PEDIR DADOS =====
def pedir_vetor(nome):
    print(f"\nDigite os valores do vetor {nome}:")
    x = float(input(f"{nome}x: "))
    y = float(input(f"{nome}y: "))
    z = float(input(f"{nome}z: "))
    return np.array([x, y, z])


# ===== FUNÇÃO PARA GERAR GRÁFICO =====
def gerar_grafico(v1, v2, nome1, nome2, titulo):
    # Vetores no plano XY
    x1, y1 = v1[0], v1[1]
    x2, y2 = v2[0], v2[1]

    # Ângulos dos vetores em relação ao eixo X
    ang1 = math.atan2(y1, x1)
    ang2 = math.atan2(y2, x2)

    # Garante ordem correta para desenhar o arco
    ang_inicio = min(ang1, ang2)
    ang_fim = max(ang1, ang2)

    # Cria o arco do ângulo
    angulos = np.linspace(ang_inicio, ang_fim, 100)
    raio = 0.3 * min(
        math.sqrt(x1**2 + y1**2),
        math.sqrt(x2**2 + y2**2)
    )

    arco_x = raio * np.cos(angulos)
    arco_y = raio * np.sin(angulos)

    # Vetores
    plt.quiver(0, 0, x1, y1, scale=1, scale_units='xy', label=nome1)
    plt.quiver(0, 0, x2, y2, scale=1, scale_units='xy', label=nome2)

    # Arco do ângulo
    plt.plot(arco_x, arco_y, 'r', linewidth=2)

    # Eixos
    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    plt.axis('equal')

    # Texto do ângulo
    angulo_graus = abs(math.degrees(ang_fim - ang_inicio))
    plt.text(
        raio * math.cos((ang_inicio + ang_fim) / 2),
        raio * math.sin((ang_inicio + ang_fim) / 2),
        f"{angulo_graus:.1f}°",
        color="red"
    )

    plt.legend()
    plt.title(titulo)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()



# ===== RETA x RETA =====
def reta_reta():
    print("\n=== Ângulo entre duas retas ===")

    u = pedir_vetor("u")
    v = pedir_vetor("v")

    produto_escalar = (u[0]*v[0]) + (u[1]*v[1]) + (u[2]*v[2])

    modulo_u = math.sqrt((u[0]**2) + (u[1]**2) + (u[2]**2))
    modulo_v = math.sqrt((v[0]**2) + (v[1]**2) + (v[2]**2))

    cos_theta = produto_escalar / (modulo_u * modulo_v)

    if cos_theta > 1:
        cos_theta = 1
    elif cos_theta < -1:
        cos_theta = -1

    angulo = math.degrees(math.acos(cos_theta))
    print(f"\nÂngulo entre as retas: {angulo:.2f}°")

    gerar_grafico(u, v, "Reta 1", "Reta 2", "Reta x Reta (projeção XY)")


# ===== RETA x PLANO =====
def reta_plano():
    print("\n=== Ângulo entre reta e plano ===")

    v = pedir_vetor("v (reta)")
    n = pedir_vetor("n (normal do plano)")

    produto_escalar = (v[0]*n[0]) + (v[1]*n[1]) + (v[2]*n[2])

    modulo_v = math.sqrt((v[0]**2) + (v[1]**2) + (v[2]**2))
    modulo_n = math.sqrt((n[0]**2) + (n[1]**2) + (n[2]**2))

    seno_theta = abs(produto_escalar) / (modulo_v * modulo_n)

    if seno_theta > 1:
        seno_theta = 1

    angulo = math.degrees(math.asin(seno_theta))
    print(f"\nÂngulo entre a reta e o plano: {angulo:.2f}°")

    gerar_grafico(v, n, "Reta", "Normal do plano", "Reta x Plano")


# ===== PLANO x PLANO =====
def plano_plano():
    print("\n=== Ângulo entre dois planos ===")

    n1 = pedir_vetor("n1 (plano 1)")
    n2 = pedir_vetor("n2 (plano 2)")

    produto_escalar = (n1[0]*n2[0]) + (n1[1]*n2[1]) + (n1[2]*n2[2])

    modulo_n1 = math.sqrt((n1[0]**2) + (n1[1]**2) + (n1[2]**2))
    modulo_n2 = math.sqrt((n2[0]**2) + (n2[1]**2) + (n2[2]**2))

    cos_theta = produto_escalar / (modulo_n1 * modulo_n2)

    if cos_theta > 1:
        cos_theta = 1
    elif cos_theta < -1:
        cos_theta = -1

    angulo = math.degrees(math.acos(cos_theta))
    print(f"\nÂngulo entre os planos: {angulo:.2f}°")

    gerar_grafico(n1, n2, "Plano 1", "Plano 2", "Plano x Plano")


# ===== MENU =====
while True:
    print("\n=== MENU ===")
    print("1 - Reta x Reta")
    print("2 - Reta x Plano")
    print("3 - Plano x Plano")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        reta_reta()
    elif opcao == "2":
        reta_plano()
    elif opcao == "3":
        plano_plano()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")

