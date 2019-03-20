def main ():
    for num_client in range (1,5):
        print ("Vous etes les client numero",num_client)

    emails = ["mail_a@mail.be", "mail_b@mail.be","mail_c@mail.be","mail_d@mail.be"]
    blacklist = ["mail_b@mail.be"]
    for mail in emails:
        print ("Email envoyé à", mail)

        if mail in blacklist:
            print("Envoie {} impossible car blacklist".format(mail))
        continue #to continue the for loop
        # break #to end the for loop

    wage = 1500
    while wage < 2000:
        print(wage)
        wage +=  100


if __name__ == '__main__':
    main()