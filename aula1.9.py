distancia = float(input("digite a distancia percorrida (em metros ): "))
tempo = float(input("digite o tempo para percorrer a distancia: "))

#em m/s
ms = distancia / tempo
round(ms, 2)
print("a velocidade media foi de", ms, "m/s")

#em km/h

km = ms * 3.6
round(km, 2)
print("a velocidade media foi de", km, "km/h")