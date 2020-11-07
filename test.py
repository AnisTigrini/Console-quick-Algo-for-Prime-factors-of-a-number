
# 1) On émet une variable 'running' qui est vraie pour faire rouler la boucle indéfiniment.
running = True

# 2) Tant que cette variable est vraie, on va continuer à demander l'input de l'utilisateur.
while running:
    userInput = input('Entrez un nombre entier positif (0 pour terminer): ')

    # 3) Afin d'éviter une erreure de conversion causée par int() on va vérifier si la valeur
    # peut être convertie en nombre entier. Si c'est le cas, on transforme le 'string' en 'int'.
    if userInput.isnumeric():
        number = int(userInput)

        # 4) Dans le vif du sujet, on vérifie si le nombre est positif.
        if number > 0:
            # 4.1) Si c'est 1, on redonne les facteurs de 1 (cas special).
            if number == 1:
                print('La décomposition en facteurs premiers est: 1')            

            # 4.2) Ceci est le programme principal
            else:
                # 4.3 ) On enregistre quelques variables dont 'primeFactors' qui est l'initialisation
                # de la Séquence.
                primeFactors = ()
                x = 2

                # 4.4) Les facteurs d'un nombre s'inversent à partir de sa racine carée. Par conséquent, il est
                # intéressant d'utiliser la boucle while jusqu'à la racine carée du nombre.           
                while x <= number / x:
                    # 4.4.1) Si la division du nombre par "x" n'a pas de reste, on a un diviseur premier. On l'ajoute à
                    # la liste, on divise notre nombre par "x" et on réinitalise "x" à 2 (premier facteur premier);
                    if number % x == 0:
                        number = int(number / x)
                        primeFactors += (x,)
                        x = 2
                    # 4.4.2) Si notre nombre n'est pas divisble par "x", on incrémente et continue à chercher.
                    else:
                        x += 1
                # 4.4.3) Ne pas oublier de sauvegarder le dernier nombre premier qui nous reste car il ne le sera évidemment
                # pas par notre boulce while (il n'a aucun diviseur)!
                primeFactors += (number, )
                
                # 4.5) On imprime sur la console la décomposition de notre nombre en facteur premiers.
                print('La décomposition en facteurs premiers est: ', end='')
                print(*primeFactors, sep=' * ')

        # 5) Dans le cas où le nombre n'est pas égal à un nombre positif on ferme le programme en 
        # rendant 'running' faux, ce qui arrête la boucle principale (PS : seulement 0 va rendre 
        # 'running' faux).
        else:
            print('Le programme va maintenant se fermer. Merci et au revoir!')
            running = False
    
    # 6) Dans le cas ou on entre un caractere qui ne rend pas 'isnumeric()' vrai (incluant les nombres négatifs)
    # on va dire à l'utilisateur qu'il à fait une entrée non valide.
    else:
        print('Erreur, entrée non valide.')
