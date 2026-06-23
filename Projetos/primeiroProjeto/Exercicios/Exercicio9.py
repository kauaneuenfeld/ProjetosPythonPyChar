# Sistema de votação simples usando while
joao = 0
ana = 0
pedro = 0
total = 0

print("Opções de voto (1-João, 2-Ana, 3-Pedro, 4-Encerrar e mostrar)")
voto = int(input("Voto: "))

while voto != 4:
	if voto == 1:
		joao += 1
		total += 1
		print("Você votou no João")
	elif voto == 2:
		ana += 1
		total += 1
		print("Você votou na Ana")
	elif voto == 3:
		pedro += 1
		total += 1
		print("Você votou no Pedro")
	else:
		print("Voto inválido")

	voto = int(input("Voto: "))

print(f"Total de votos: {total}")
print(f"Total de pedros: {pedro}")
print(f"Total de ana: {ana}")
print(f"Total de joao: {joao}")

if joao > ana and joao > pedro:
    print("O vencedor é o João")

if ana > pedro and ana > joao:
    print("O vencedor é a Ana")

if pedro > ana and pedro > joao:
    print("O vencedor é o Pedro")
