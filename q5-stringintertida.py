def inverter_string(string):
    nova_string = ""
    for i in range(len(string)-1, -1, -1):
        nova_string += string[i]
    return nova_string

# Exemplo de uso:
minha_string = "Ola, mundo!"
string_invertida = inverter_string(minha_string)
print(string_invertida)  # saída: "!odnum ,alO"
