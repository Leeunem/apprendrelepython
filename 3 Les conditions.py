def main():
    print ("Hello World")
    wallet = 5000
    computer_price = 900

    print(computer_price < 1000)

    if computer_price < 1000:
        print ("Inferieur")
    else:
        print ("Superieur")

    computer_price = 2900
    if computer_price < 1000:
        print ("Inferieur")
    else:
        print ("Superieur")

    computer_price = 900
    if computer_price > wallet:
        print ("Trop cher")
    else:
        print ("Achat")
        wallet -= computer_price
        print ("La valeur restant de votre portefeille est {}€".format(wallet))

    if 1000 < computer_price <= wallet:
        print("Le portefeuille vaut plus aue 1000")
    else:
        print("Non")

    computer_price = 1000
    text = ("Lachat est possible", "Lachat est impossible") [computer_price < 1000] #condition ternaire où variable = (true, false) [condition]
    print(text)

    password = input("Entrer mot de passe")
    passwordlenght = len(password)
    if passwordlenght <= 8:
        print ("Password autorisé")
    elif 8 < passwordlenght <= 12
        print("mot de passe moyen")
    else:
        print("password trop court")


if __name__ == '__main__':
    main()