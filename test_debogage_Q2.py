from datetime import datetime #modifier le import
import locale
locale.setlocale(locale.LC_TIME,'')

from Q2 import *



def test_afficher_jours_examens():
    horaire_examen = {
        "math" : "9/12/2025",
        "anglais" : "8/11/2025",
        "français" : "24/12/2025"
    }
    resultat = afficher_jours_examens(horaire_examen)

    assert resultat == ['mar.', 'sam.', 'mer.']
