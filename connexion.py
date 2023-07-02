from cgitb import text
from tkinter import *
import sqlite3
from subprocess import call
from tkinter import messagebox

notreObjet = Tk()
notreObjet.title("GESTION D'UNE BANQUE")
largeur = notreObjet.winfo_screenwidth()
hauteur = notreObjet.winfo_screenheight()
notreObjet.minsize(largeur,hauteur)

conn = sqlite3.connect("banque.db")
cur = conn.cursor()



def Connexion():

    surnom=inputNomUtilisateur.get()
    mdp=inputMotPass.get()

    if surnom == "" and mdp == "":
        notreObjet.destroy()
        call(["python", "index.py"])
    else:
        inputMotPass("0", "end")
        inputNomUtilisateur("0", "end")

    """" 
    conn = cur.execute("select * from connexion where id = 1")
    a = conn.fetchall()

    if(surnom=="" and mdp==""):
        messagebox.showerror("ERREUR","Veuillez remplir les champs")
        inputMotPass("0", "end")
        inputNomUtilisateur("0", "end")
    elif(surnom== a[0][1] and mdp==a[0][2]):
        notreObjet.destroy()
        call(["python","Index.py"])
    else:
        messagebox.showerror("ERREUR","Nom utilisateur ou mot de passe incorrect")
    """




titreConnexion = Label(notreObjet , text="Connexion" , bg="green",relief=SUNKEN , font=("times new roman",20), fg="black" )
titreConnexion.pack(side=TOP , fill=X)


labelNomUtilisateur = Label(notreObjet , text="Nom d'utilisateur" , font=("times new roman",20))
labelNomUtilisateur.place(x = 450 , y= 130)

inputNomUtilisateur = Entry(notreObjet,font = ("times new roman",20))
inputNomUtilisateur.place(x=700 , y=130)


labelMotPass = Label(notreObjet , text="Mot de Passe" , font=("times new roman",20))
labelMotPass.place(x = 450 , y= 200)

inputMotPass = Entry(notreObjet,font = ("times new roman",20), show="*")
inputMotPass.place(x=700 , y=200)

buttonConnexion = Button(notreObjet,text="Connexion",font=("times new roman",20), bg="skyblue", fg="white",command=Connexion)
buttonConnexion.place(x=575 , y=270, width=250)















notreObjet.mainloop()