import matplotlib.pyplot as plt

# Definição do sistema dinâmico
def competitive_system(X, t):
    x, y = X
    dxdt = x * (3 - x) - 2 * x * y
    dydt = y * (2 - y) - x * y
    return [dxdt, dydt]

# Geração da malha para o campo vetorial
x_vals = np.linspace(-0.5, 3.5, 20)
y_vals = np.linspace(-0.5, 2.5, 20)
X, Y = np.meshgrid(x_vals, y_vals)
U = X * (3 - X) - 2 * X * Y
V = Y * (2 - Y) - X * Y

# Normalizando os vetores
magnitude = np.sqrt(U**2 + V**2)
U /= magnitude
V /= magnitude

# Trajetórias de algumas condições iniciais
time = np.linspace(0, 10, 200)
initial_conditions = [[0.5, 0.5], [2, 1], [1, 1.5], [3, 2]]
solutions = [odeint(competitive_system, ic, time) for ic in initial_conditions]

# Plotando o diagrama de fase
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V, color='gray', alpha=0.6)

# Adicionando as trajetórias
for sol in solutions:
    plt.plot(sol[:, 0], sol[:, 1], label=f'CI: {sol[0]}')

# Marcando pontos críticos
critical_points = np.array([[0, 0], [3, 0], [0, 2], [1, 1]])
plt.scatter(critical_points[:, 0], critical_points[:, 1], color='red', marker='o', label='Pontos críticos')

plt.xlim(-0.5, 3.5)
plt.ylim(-0.5, 2.5)
plt.xlabel("População de Coelhos (x)")
plt.ylabel("População de Ovelhas (y)")
plt.title("Diagrama de Fase do Sistema Competitivo")
plt.legend()
plt.grid()
plt.show()
# Salvar o gráfico como uma imagem
plt.savefig("Phase Space.png")
plt.close()
