from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


object = Tk()
object.title("Interface d'accueil")
lalargeur = object.winfo_screenwidth()
lahauteur = object.winfo_screenheight()
object.minsize(lalargeur , lahauteur)

conn = sqlite3.connect("banque.db")
cur = conn.cursor()

## ------------------------- creation d'un table
##cur.execute("CREATE TABLE  compte (id INTEGER PRIMARY KEY AUTOINCREMENT , codeCompte TEXT , solde TEXT , nom TEXT , prenom TEXT, typeCompte TEXT , montant TEXT)")
##conn.commit()
#conn.close()




codeCompte = StringVar()
solde = StringVar()
nom = StringVar()
prenom = StringVar()
typeCompte = StringVar()
montant = StringVar()

def annuler():
    codeCompte.set("")
    solde.set("")
    nom.set("")
    prenom.set("")
    typeCompte.set("")
    montant.set("")

def creationCompte():
    codeCompter = codeCompte.get()
    solder = solde.get()
    nomr = nom.get()
    prenomr = prenom.get()
    typeCompter = typeCompte.get()
    montantr = montant.get()

    if codeCompter == "" and solder == "" and nomr == "" and prenomr == "" and typeCompter == "" and montantr == "":
        messagebox.showerror("Erreurr","Veuillez saisir tout les champs")
    else:



        req = "INSERT INTO compte(codeCompte,solde,nom,prenom,typeCompte,montant) VALUES(?,?,?,?,?,?)"
        cur.execute(req, (codeCompter,solder, nomr, prenomr, typeCompter, montantr))
        conn.commit()
        annuler()
        messagebox.showinfo("Creation", "Comte crée avec succès")



# """"""""""""""""""""""""""" stoque
titreStock = Label(object , text = "Gestion d'une banque" , font=("times new roman",30) , bg="grey")
titreStock.pack(side=TOP , fill=X)


# """"
def fonctionNouveauCompte():
    for widget in frameCenter.winfo_children():
        widget.destroy()

    titre  = Label(frameCenter , text="Creation d'un compte" , font=("times new roman",20) , bg="blue")
    titre.pack(fill=X, side=TOP)

    codeComptelabel = Label(frameCenter , text="Code Compte" , font=("times new roman",20))
    codeComptelabel.place(x= 250, y=70)
    codeCompteEntry = Entry(frameCenter , font=("times new roman",20), textvariable=codeCompte)
    codeCompteEntry.place(x= 500, y=70, width=350)

    soldelabel = Label(frameCenter, text="Solde", font=("times new roman", 20))
    soldelabel.place(x=250, y=140)
    soldeEntry = Entry(frameCenter, font=("times new roman", 20), textvariable=solde)
    soldeEntry.place(x=500, y=140, width=350)

    nomlabel = Label(frameCenter, text="Nom", font=("times new roman", 20))
    nomlabel.place(x=250, y=210)
    nomEntry = Entry(frameCenter, font=("times new roman", 20), textvariable=nom)
    nomEntry.place(x=500, y=210, width=350)

    prenomlabel = Label(frameCenter, text="Prenom", font=("times new roman", 20))
    prenomlabel.place(x=250, y=280)
    prenomEntry = Entry(frameCenter, font=("times new roman", 20), textvariable=prenom)
    prenomEntry.place(x=500, y=280, width=350)

    typeComptelabel = Label(frameCenter, text="Type Compte", font=("times new roman", 20))
    typeComptelabel.place(x=250, y=350)
    typeCompteEntry = ttk.Combobox(frameCenter, values=["Compte courant","Compte epargne"], font=("times new roman", 20) , textvariable=typeCompte)
    typeCompteEntry.place(x=500, y=350, width=350)

    montantlabel = Label(frameCenter, text="Montant decouvert", font=("times new roman", 20))
    montantlabel.place(x=250, y=420)
    montantEntry = Entry(frameCenter,  font=("times new roman", 20), textvariable=montant)
    montantEntry.place(x=500, y=420, width=350)

    bouttonAnnuler = Button(frameCenter, text="Annuler", bg="red", font=("times new roman", 20), command=annuler)
    bouttonAnnuler.place(x=500, y= 500, width=150)

    bouttonCree = Button(frameCenter, text="Crée", bg="blue", font=("times new roman", 20), command=creationCompte)
    bouttonCree.place(x=700, y=500, width=150)


def fonctionCompteCourant():
    for widget in frameCenter.winfo_children():
        widget.destroy()

    titre = Label(frameCenter, text="Liste de tout les comtes Courant", font=("times new roman", 20), bg="blue")
    titre.pack(fill=X, side=TOP)


def fonctionCompteEpargne():
    for widget in frameCenter.winfo_children():
        widget.destroy()

    titre = Label(frameCenter, text="Liste de tout les comtes Epargne", font=("times new roman", 20), bg="blue")
    titre.pack(fill=X, side=TOP)


def fonctionCompte():
    for widget in frameCenter.winfo_children():
        widget.destroy()

    titre = Label(frameCenter, text="Liste de tout les comtes", font=("times new roman", 20), bg="blue")
    titre.pack(fill=X, side=TOP)

    montableau = ttk.Treeview(frameCenter, columns=(1, 2, 3, 4, 5, 6,7), height=1000, show="headings")
    montableau.heading(1, text="ID")
    montableau.heading(2, text="Code du Compte")
    montableau.heading(3, text="Solde")
    montableau.heading(4, text="Nom")
    montableau.heading(5, text="Prenom")
    montableau.heading(6, text="Type compte")
    montableau.heading(7, text="Montant decouvert")

    montableau.column(1, width=100)
    montableau.column(2, width=100)
    montableau.column(3, width=200)
    montableau.column(4, width=225)
    montableau.column(5, width=300)
    montableau.column(6, width=300)

    req = "SELECT * FROM compte"
    cur.execute(req)

    for a in cur.fetchall():
        montableau.insert("", END, values=a)

    montableau.place(x=5, y=50)


def fonctionOperation():
    for widget in frameCenter.winfo_children():
        widget.destroy()

    titre = Label(frameCenter, text="Liste des operations", font=("times new roman", 20), bg="blue")
    titre.pack(fill=X, side=TOP)

def fonctionConsultation():
    for widget in frameCenter.winfo_children():
        widget.destroy()

    ajout  = Button(frameCenter , text="Ajout" , font=("times new roman",20) , bg="blue")
    ajout.place(x = 0 , y = 5 , width=230)









#"""""""""""""""""""""""""""""""" le dasboad """
dasbord = Frame(object , relief= GROOVE , bd=10)
dasbord.place(x = 0, y = 0 , width = 250 , height = lahauteur)

titredasbord = Label(dasbord , text="Banque" , font=("times new roman",30) , bg="grey")
titredasbord.pack(side=TOP , fill=X)

produit  = Button(dasbord , text="Nouveau Compte" , font=("times new roman",20) , bg="blue" , command=fonctionNouveauCompte )
produit.place(x = 0 , y = 70 , width=230)

fournisseur  = Button(dasbord , text="Compte Courant" , font=("times new roman",20) , bg="blue", command=fonctionCompteCourant)
fournisseur.place(x = 0 , y = 140 , width=230)

categorie  = Button(dasbord , text="Compte Epargne" , font=("times new roman",20) , bg="blue" , command= fonctionCompteEpargne)
categorie.place(x = 0 , y = 210 , width=230)

produit  = Button(dasbord , text="Liste Compte" , font=("times new roman",20) , bg="blue" , command=fonctionCompte )
produit.place(x = 0 , y = 280 , width=230)

fournisseur  = Button(dasbord , text="Operation" , font=("times new roman",20) , bg="blue", command=fonctionOperation)
fournisseur.place(x = 0 , y = 350 , width=230)

categorie  = Button(dasbord , text="Consultation" , font=("times new roman",20) , bg="blue" , command= fonctionConsultation)
categorie.place(x = 0 , y = 420 , width=230)



categorie  = Button(dasbord , text="Deconnexion" , font=("times new roman",20) , bg="red" , command=quit)
categorie.place(x = 0 , y = 720 , width=230)



# """"""""""""""""""""""""""" frame du centre
frameCenter = Frame(object , relief= GROOVE , bd=10)
frameCenter.place(x = 250 , y = 55 , height= lahauteur - 50 , width= lalargeur - 250)








object.mainloop()
