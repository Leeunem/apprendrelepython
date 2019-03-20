

def main():
    online_players = ["Graven","Anana", "Cleymax", "Bob"]

    ## AFFICHER VALEURS ##
    print(online_players) #afficher la liste
    print(online_players[0]) #afficher le contenant de la liste pour l index 0 (premiere valeur)
    print(online_players[len(online_players)-1]) #retourner la dernière valeur de la liste

    ## CHANGER VALEURS ##
    online_players[0] = "Gravenilvec" #modifier une valeur de la liste
    online_players.insert(2, "Bernardgamer123") #ajouter une valeur dans la liste
    online_players[2:4] = ["Paul", "Jacques"] #inserer des valeurs
    online_players.append("Gamer123") #inserer une valeur a la fin
    online_players.extend(["Gogumerler", "gigi2k"]) #inserer plusieurs valeur a la fin
    online_players.pop(1) #ou -del online_players[1]- ce qui permet de supprimer le 2ieme valeur (!) de la liste
    online_players.remove("gigi2k") # supprimer selon le string
    online_players.clear() #nettoyer toute la variable
    #print(online_players)

    ## EXERCICE ##
    notes = [8, 12, 10,9, 4, 20]
    notes = [
        8,12,10,
        9,4,20,
    ]
    print(notes)



if __name__ == '__main__':
    main ()