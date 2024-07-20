def calculate_intra(liste):
            compte = 0
            n = len(liste)
            compteur = 0
            while compteur < n:
                element = liste[compteur]
                try:
                    compte += int(element)
                    compteur += 1
                except ValueError:
                    if element == '-':
                        liste[compteur + 1] = - int(liste[compteur + 1])
                        compteur +=1
                    else:
                        compteur += 1
            return compte

liste = ['']

print(calculate_intra(liste))