from datetime import datetime #modifier le import
import locale
locale.setlocale(locale.LC_TIME,'')

def afficher_jours_examens(horaire_examen: dict) -> list[str]:
    """
    Cette fonction sert à extraire les jours de la semaines où il y a des examens
    :param horaire_examen: dictionnaire contenant les dates d'examens
    :return: une liste de jours de la semaine
    """

    # Réf. Notes de cours
    # https://projets420.gitbook.io/notes-de-cours/les-collections-de-donnees/les-dictionnaires
    # https://projets420.gitbook.io/notes-de-cours/tests-unitaires/tests-unitaires
    jours = [] # déplacer hors de la fonction
    for classe, date_examen in horaire_examen.items():
        try:
            date = datetime.strptime(horaire_examen[classe], "%d/%m/%Y") # La détection de la date était dans le mauvais format (c'était Y/m/d)
            j = date.strftime("%a")
            jours.append(j)
        except ValueError:
            jours.append("N/D")
        except UnboundLocalError:
            jours.append("N/D")


    return jours # déplacer tab

if __name__ == '__main__':
    horaire_examen = {
        "math" : "10/12/2015",
        "anglais" : "12/12/2025",
        "français" : "15/12/2025"
    }
    print("Les examens sont :", ", ".join(afficher_jours_examens(horaire_examen)))
