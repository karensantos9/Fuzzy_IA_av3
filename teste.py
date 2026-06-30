import pandas as pd
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

from fuzzy import sistema, atendimento, comida, espera, gorjeta

# Função para calcular a gorjeta
def calcular_gorjeta(atendimento_val, comida_val, espera_val):
    simulador = ctrl.ControlSystemSimulation(sistema)

    simulador.input['atendimento'] = atendimento_val
    simulador.input['comida'] = comida_val
    simulador.input['espera'] = espera_val

    simulador.compute()

    return simulador.output['gorjeta'], simulador


# 20 cenários de teste
cenarios = [
    (1, 1, 60),
    (2, 2, 50),
    (3, 4, 40),
    (4, 5, 35),
    (5, 5, 30),
    (6, 6, 25),
    (7, 7, 20),
    (8, 8, 15),
    (9, 9, 10),
    (10, 10, 5),
    (8, 5, 40),
    (5, 9, 15),
    (9, 3, 20),
    (6, 4, 50),
    (10, 8, 10),
    (4, 9, 5),
    (2, 8, 55),
    (7, 3, 45),
    (9, 10, 0),
    (5, 2, 60)
]

resultados = []

print("=" * 60)
print("RESULTADOS DOS TESTES")
print("=" * 60)

for i, (a, c, e) in enumerate(cenarios, start=1):
    gorjeta_recomendada, simulador = calcular_gorjeta(a, c, e)

    resultados.append({
        "Cenário": i,
        "Atendimento": a,
        "Comida": c,
        "Espera (min)": e,
        "Gorjeta (%)": round(gorjeta_recomendada, 2)
    })

    print(
        f"Cenário {i:02d} | "
        f"Atendimento={a} | "
        f"Comida={c} | "
        f"Espera={e:2d} min | "
        f"Gorjeta={gorjeta_recomendada:.2f}%"
    )

# Cria um DataFrame
df = pd.DataFrame(resultados)

# Salva em CSV
df.to_csv("resultados_gorjeta.csv", index=False, encoding="utf-8-sig")

print("\nArquivo 'resultados_gorjeta.csv' salvo com sucesso!")

# Mostra a tabela completa
print("\nTabela de resultados:")
print(df)

# Exibe e salva o gráfico do cenário de exemplo
_, simulador = calcular_gorjeta(8, 9, 15)

gorjeta.view(sim=simulador)
plt.savefig("resultado_cenario8.png")
plt.close()

# Gráfico Atendimento
atendimento.view()
plt.savefig("atendimento.png")
plt.close()

# Gráfico Comida
comida.view()
plt.savefig("comida.png")
plt.close()

# Gráfico Espera
espera.view()
plt.savefig("espera.png")
plt.close()

# Gráfico Gorjeta (funções de pertinência)
gorjeta.view()
plt.savefig("gorjeta.png")
plt.close()