def inverter_string(texto):

  texto_invertido =""
  for i in range(len(texto) -1, -1, -1):
    texto_invertido += texto[i]
  return texto_invertido

if __name__ == "__main__":
  texto = input("DIGITE UM TEXTO:")
  texto_invertido = inverter_string(texto)
  print("Texto invertido:", texto_invertido)

#O CÓDIGO ACIMA PEDE AO USUÁRIO QUE ELE INSIRA UM TEXTO E ELE RETORNA COM O MESMO TEXTO INVERTIDO