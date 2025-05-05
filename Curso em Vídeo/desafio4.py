texto = input('Digite um texto: ')

print(f'O texto "{texto}" é considerado um "{type(texto)}')
print(f'O texto "{texto}" é considerado numérico? {"Sim" if texto.isnumeric() else "Não"}')
print(f'O texto "{texto}" é considerado alfabético? {"Sim" if texto.isalpha() else "Não"}')
print(f'O texto "{texto}" é considerado alfanumérico? {"Sim" if texto.isalnum() else "Não"}')
print(f'O texto "{texto}" é considerado decimal? {"Sim" if texto.isdecimal() else "Não"}')