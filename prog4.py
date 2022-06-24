print(":: Conversor de m/s para km/h::" .center(80, "."))

entrada = input("\nDigite a velocidade (m/s):")

v_ms = float(entrada)
v_kmh = v_ms * 3.6

print(v_kmh)
saida = "{0:9.3f} m/s = {1:+9.3f} km/h"
print(saida.format(v_ms, v_kmh))
