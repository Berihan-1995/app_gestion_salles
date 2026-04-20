import json

# Ce fichier fait lire et écrire les salles dans le fichier JSON
import mysql.connector
import json
from models.salle import Salle


class DataSalle:

    def get_connection(self):
        """
        Lit config.json et retourne une connexion MySQL
        """
        with open("data/config.json", "r") as f:
            config = json.load(f)

        return mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

    def insert_salle(self, salle: Salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO salle (code, description, categorie, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.description, salle.categorie, salle.capacite)

        cursor.execute(sql, values)
        conn.commit()

        cursor.close()
        conn.close()

    def update_salle(self, salle: Salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = "UPDATE salle SET description=%s, categorie=%s, capacite=%s WHERE code=%s"
        values = (salle.description, salle.categorie, salle.capacite, salle.code)

        cursor.execute(sql, values)
        conn.commit()

        cursor.close()
        conn.close()

    def delete_salle(self, code: str):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = "DELETE FROM salle WHERE code=%s"
        cursor.execute(sql, (code,))
        conn.commit()

        cursor.close()
        conn.close()

    def get_salle(self, code: str):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = "SELECT code, description, categorie, capacite FROM salle WHERE code=%s"
        cursor.execute(sql, (code,))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:
            return Salle(row[0], row[1], row[2], row[3])
        return None

    def get_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = "SELECT code, description, categorie, capacite FROM salle"
        cursor.execute(sql)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        liste = []
        for r in rows:
            liste.append(Salle(r[0], r[1], r[2], r[3]))

        return liste
