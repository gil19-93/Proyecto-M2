
#no logre hacer la fucion de conteo de letras sobre la misma frase debido a que solo sacaba las letras divididas 
# o conteo total sin poder generar la diferencia establecida sin embargo lo que logre hace con lo enseñado fue 
# hacer el conteo tanto dividido de letras con numerales para poder hacer el conteo total de lo obtenido 
# y de esa misma manera poder manejar la informacion entrante me apoye en el ciclo def, if, elif y else 

def contar_letras(palabra):
    letras = 0
    digitos = 0
    for c in palabra:
        if c.isdigit():
            digitos += 1 
        elif c.isalpha():
            letras += 1
        else:
            pass
    return digitos, letras

texto = input('Ingresa una plabra entre 4 a 8 letras: ')
resultado = contar_letras(texto)

print('cantidad de digitos: %i' % resultado[0])
print('Cantidad de letras: %i'% resultado[1])

#Se me hizo bastante sencilla esta parte del proyecto debido a que solo fue relacion de valores comparativos numericos
#con respuestas bastante directas creo que de cierta manera lo complique un poco en esta parte por que replique 
#bastante el if ,elif  pero creo que de misma manera lo maneje de la manera mas simple para no generar conflictoe n lo solicitado
#Lo que me ayudo bastante fue esta tabla que agregaron en la descripsion del proyecto
# # (+,+) => Cuad. I; 
# # (-,+) => Cuad. II; 
# # (-,-) => Cuad. III; 
# # (+,-) => Cuad. IV

print('ingrese las cordenadas para encontrar el cuadrante')
x = input('Ingrese X: ')
y = input('Ingrese Y: ')

if x == '0':
    print('No se puede usar 0')
elif y == '0':
    print('No se puede usar 0')
elif y >= '1':
    if x >= '1':
        print('El punto se encuentra en el cuadrante I')
    elif x <= '0':
        print('El punto se encuentra en el cuadrante II')   
elif x <= '1':
    if y <= '0':
        print('El punto se encuentra en el cuadrante III')
elif y <= '0':
    if x >= '1':
        print('El punto se encuentra en el cuadrante IV')        
