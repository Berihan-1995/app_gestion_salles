import customtkinter as ctk
from tkinter import messagebox, ttk
from models.salle import Salle
from services.service_salle import ServiceSalle

class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x600")

        self.service_salle = ServiceSalle()

        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        self.lblCode = ctk.CTkLabel(self.cadreInfo, text="Code :")
        self.lblCode.grid(row=0, column=0, padx=5, pady=5)
        self.entCode = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entCode.grid(row=0, column=1, padx=5, pady=5)

        self.lblDesc = ctk.CTkLabel(self.cadreInfo, text="Description :")
        self.lblDesc.grid(row=1, column=0, padx=5, pady=5)
        self.entDesc = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entDesc.grid(row=1, column=1, padx=5, pady=5)

        self.lblCat = ctk.CTkLabel(self.cadreInfo, text="Catégorie :")
        self.lblCat.grid(row=2, column=0, padx=5, pady=5)
        self.entCat = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entCat.grid(row=2, column=1, padx=5, pady=5)

        self.lblCap = ctk.CTkLabel(self.cadreInfo, text="Capacité :")
        self.lblCap.grid(row=3, column=0, padx=5, pady=5)
        self.entCap = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entCap.grid(row=3, column=1, padx=5, pady=5)

        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10)

        self.btnAjouter = ctk.CTkButton(self.cadreActions, text="Ajouter", command=self.ajouter_salle)
        self.btnAjouter.grid(row=0, column=0, padx=10, pady=10)

        self.btnModifier = ctk.CTkButton(self.cadreActions, text="Modifier", command=self.modifier_salle)
        self.btnModifier.grid(row=0, column=1, padx=10, pady=10)

        self.btnSupprimer = ctk.CTkButton(self.cadreActions, text="Supprimer", command=self.supprimer_salle)
        self.btnSupprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btnRechercher = ctk.CTkButton(self.cadreActions, text="Rechercher", command=self.rechercher_salle)
        self.btnRechercher.grid(row=0, column=3, padx=10, pady=10)

        self.cadreList = ctk.CTkFrame(self, corner_radius=10)
        self.cadreList.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )

        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")

        self.treeList.column("code", width=80)
        self.treeList.column("description", width=200)
        self.treeList.column("categorie", width=120)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(fill="both", expand=True, padx=10, pady=10)

        self.lister_salles()

    def ajouter_salle(self):
        code = self.entCode.get()
        desc = self.entDesc.get()
        cat = self.entCat.get()
        cap = self.entCap.get()

        try:
            cap = int(cap)
        except:
            messagebox.showerror("Erreur", "La capacité doit être un nombre.")
            return

        salle = Salle(code, desc, cat, cap)
        ok, msg = self.service_salle.ajouter_salle(salle)

        if ok:
            messagebox.showinfo("Succès", msg)
            self.lister_salles()
        else:
            messagebox.showerror("Erreur", msg)

    def modifier_salle(self):
        code = self.entCode.get()
        desc = self.entDesc.get()
        cat = self.entCat.get()
        cap = self.entCap.get()

        try:
            cap = int(cap)
        except:
            messagebox.showerror("Erreur", "La capacité doit être un nombre.")
            return

        salle = Salle(code, desc, cat, cap)
        ok, msg = self.service_salle.modifier_salle(salle)

        if ok:
            messagebox.showinfo("Succès", msg)
            self.lister_salles()
        else:
            messagebox.showerror("Erreur", msg)

    def supprimer_salle(self):
        code = self.entCode.get()
        ok, msg = self.service_salle.supprimer_salle(code)
        messagebox.showinfo("Information", msg)
        self.lister_salles()

    def rechercher_salle(self):
        code = self.entCode.get()
        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.entDesc.delete(0, "end")
            self.entCat.delete(0, "end")
            self.entCap.delete(0, "end")

            self.entDesc.insert(0, salle.description)
            self.entCat.insert(0, salle.categorie)
            self.entCap.insert(0, salle.capacite)
        else:
            messagebox.showerror("Erreur", "Salle introuvable.")

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))
