
messages_gr5 = {
    "pseudo" : "IronCode",
    "messages" : ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
    "signatures" : ["fresea", "odivai", "nses14"]
}

for mot in messages_gr5["messages"]:
    # Réf. Examen passée
    # https://github.com/simporechris/1G3_A25_Examen2_Gr5_jeudi/blob/master/debogage_mot_long.py
    if len(mot.strip()) >= 3:
        for lettre in mot[-2:-1]:

            mot = "bonjour"
            code = []
            for lettre in mot[-2]:
                code.append(lettre)

            print(lettre)
            print(mot[-3], mot[-2])
