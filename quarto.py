SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53
TOTAL = 0
TOTAL = int (SP + RJ + MG + ES + OUTROS)

porcentagem_SP = (SP/TOTAL) * 100
porcentagem_RJ = (RJ/TOTAL) * 100
porcentagem_MG = (MG/TOTAL) * 100
porcentagem_ES = (ES/TOTAL) * 100
porcentagem_OUTROS = (OUTROS/TOTAL) * 100

print(f"A porcentagem de SP é: {porcentagem_SP:.2f} %")
print(f"A porcentagem de RJ é: {porcentagem_RJ:.2f} % ")
print(f"A porcentagem de MG é: {porcentagem_MG:.2f} % ")
print(f"A porcentagem de ES é: {porcentagem_ES:.2f} %")
print(f"A porcentagem de OUTROS é: {porcentagem_OUTROS:.2f} %") 