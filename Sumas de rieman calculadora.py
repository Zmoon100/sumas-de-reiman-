import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

expr_str = input("Ingresa la función f(x): ") 
a = float(input("Intervalo a: "))
b = float(input("Intervalo b: "))
c = int(input("Número de subintervalos: "))


x = sp.Symbol('x')
try:
    expr = sp.sympify(expr_str)
except sp.SympifyError:
    print("Error: expresión inválida.")
    exit()

f_num = sp.lambdify(x, expr, modules=["numpy"])

dx = (b - a) / c
area = 0.0
for i in range(c):
    xi = a + i * dx
    yi = expr.subs(x, xi)
    area += float(yi) * dx

print(f" Área bajo la curva: {area:.6f}")

x_vals = np.linspace(a, b, 1500)
y_vals = f_num(x_vals)
plt.plot(x_vals, y_vals, label=f"f(x) = {expr_str}", color="black", linewidth=2)

plt.title("Curva de la función")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()