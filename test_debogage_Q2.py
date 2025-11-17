from datetime import datetime #modifier le import
import locale
locale.setlocale(locale.LC_TIME,'')

from Q2 import *

def test_afficher_jours_examens_1():
    horaire_examen = {
    "math": "10/12/2025",
    "anglais": "12/12/2025",
    "français": "15/12/2025"
    }
    resultat = afficher_jours_examens(horaire_examen)
    assert resultat == ['mer.', 'ven.', 'lun.']


def test_afficher_jours_examens_2():
    horaire_examen = {
        "math" : "9/12/2025",
        "anglais" : "8/11/2025",
        "français" : "24/12/2025"
    }
    resultat = afficher_jours_examens(horaire_examen)

    assert resultat == ['mar.', 'sam.', 'mer.']

def test_afficher_jours_examens_3():
    horaire_examen = {
        "math": "9/12/25",
        "anglais": "8/48/2025",
        "français": "4/12/2025"
    }
    resultat = afficher_jours_examens(horaire_examen)

    assert resultat == ['N/D', 'N/D', 'jeu.']

