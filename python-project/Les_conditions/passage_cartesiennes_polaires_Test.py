#Ne pas oublier de changer le module à importer
module="Les_conditions/passage_cartesiennes_polaires"

import sys
import io
from ma_bao import *
tester("from passage_cartesiennes_polaires import mon_programme",globals())

#liste des couples input/output
input_output=[\
((0,1),"1.0 1.571"),\
((1,0),"1.0 0.0"),\
((0,-1),"1.0 -1.571"),\
((1,1),"1.414 0.785"),\
((-0.5,0.8660254037844386 ),"1.0 2.094"),\
((1.4142135623730951,-1.4142135623730951),"2.0 -0.785"),\
((-3.5,0),"3.5 3.142")\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"

def afficher_correction():
    try:
        with open(module+"_Correction.py", "r") as correction :
            ligne="Voici un ou des exemples de corrections possibles"
            send_msg("Exemple(s) de correction", ligne)
            ligne="-------------------------------------------------"
            send_msg("Exemple(s) de correction", ligne)
            lignes=correction.read().split("\n")
            for ligne in lignes:
                send_msg("Exemple(s) de correction", ligne)
    except:
        pass



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    afficher_correction()
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(*inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
