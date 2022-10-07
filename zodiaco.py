import random
import collections

class Zodiaco:
    def __init__(self):
        self.elementos = ['fuego cardinal', 'tierro fijo', 'agua cardinal', 'aire cardinal', 'tierra cardinal', 'aire fijo'] 
        self.nombres = ['ares', 'tauro', 'cancer', 'libra', 'capricornio', 'acuario']
        # creamos un diccioanrio apartir de los array
        self.diccionario_respuestas = dict(zip(self.elementos, self.nombres))
        self.repetidas_correctas = []
        self.repetidas_incorrectas = []
        self.correctas = 0
        self.incorrectas = 0

    # funcion para la opcion de repasar elementos
    def repasar_elementos (self):
        # mostramos aleatoriamente el elemento que se va a mostrar
        # element_random = [x for x in random.choices(self.elementos, k=6)]
        element_random = random.shuffle()
        for i in range(len(element_random)):
            print('\t\t %d. ¿Cual es el nombre de %s?' % (i+1, element_random[i]))
            nombre = input('\t\tIngrese el nombre del signo: ')
            if (self.diccionario_respuestas[element_random[i]] == nombre.lower()):
                # contador para ver si necesita repaso
                self.correctas += 1
                self.repetidas_correctas.append(element_random[i])
                print(self.repetidas_correctas)
            else:
                # contador para ver si necesita repaso
                self.incorrectas += 1
                self.repetidas_incorrectas.append(element_random[i])
                print(self.repetidas_incorrectas)
    
    def ranking_peores(self):
        conteo = collections.Counter(self.repetidas_incorrectas)
        most_fail = collections.Counter(conteo).most_common(3) 
        return most_fail
    
    def rankin_mejores(self):
        conteo = collections.Counter(self.repetidas_correctas)
        most_best = collections.Counter(conteo).most_common(3) 
        return most_best

if __name__ == '__main__':
    zodiaco = Zodiaco()
    # Ciclo para mostrar el menu
    while (True):
        # Menu que se va a mostrar
        print('1. Repasar Elementos')
        print('2. Repasar Figura')
        print('3. Salir')
        opcion = input('Ingrese una opcion: ')
        if (opcion == '1'):
            print('*----* VAMOR A REPASAR LOS ELEMENTOS *----*')
            flag = True
            while flag:
                print('\t1. Estudiar')
                print('\t2. Mostrar Informacion')
                segunda_opcion = input('\t¿Desea continuar?: ')
                if (segunda_opcion == '1'):
                    zodiaco.repasar_elementos()
                elif (segunda_opcion == '2'):
                    # mostramos los top 3 de correctas
                    correctas = zodiaco.rankin_mejores()
                    print('\tMEJORES RESULTADOS')
                    for values, count in correctas:
                        print('\t\t%s: %s' % (values, count))

                    # mostramos los top 3 de incorrectas
                    incorrectas = zodiaco.ranking_peores()
                    print('\tPEORES RESULTADOS')
                    for values, count in incorrectas:
                        print('\t\t%s: %s' % (values, count))
                    flag = False  
        if (opcion == '2'):
            print('2. Repasar Figura')
        if (opcion == '3'):
            break
