
messages_gr5 = {
    "pseudo" : "IronCode",
    "messages" : ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
    "signatures" : ["fresea", "odivai", "nses14"]
}




def trouver_deux_lettres(mot):
    # Réf. Examen passée
    # https://github.com/simporechris/1G3_A25_Examen2_Gr5_jeudi/blob/master/debogage_mot_long.py
    if len(mot.strip()) >= 3:
        deux_lettres = str(f"{mot[-3]+mot[-2]}")
        return deux_lettres

def trouve_les_mots(lettre, phrase):
    """
    Fonction qui prend un message et crée une liste de chacun de ses mots
    :param lettre: une lettre du message
    :param phrase: la phrase contenant les mots
    :return: list contenant chaque mots du message
    """
    list_mots = []
    while True:
        for lettre in phrase:
            mot = ""
            if lettre == "":
                list_mots.append(mot)

            elif lettre != "":
                mot += lettre


list_deux_lettres = []
for phrase in messages_gr5["messages"]:
    for lettre  in phrase:

        nouveau_deux_lettres = trouver_deux_lettres(mot)
        list_deux_lettres.append(nouveau_deux_lettres)
    print(list_deux_lettres)
    #list_deux_lettres_hashmd5_decode = trouver_deux_lettres(mot, deux_lettres, list_deux_lettres)

