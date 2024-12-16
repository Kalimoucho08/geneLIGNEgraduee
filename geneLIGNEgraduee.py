import tkinter as tk
import random
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

class BandGenerator:
    def __init__(self, main_root):
        self.main_root = main_root
        self.main_root.title("Générateur de Bandes")
        
        # Entrée pour le nombre de bandes
        self.num_bands_label = tk.Label(main_root, text="Nombre de bandes :", font=("Helvetica", 12))
        self.num_bands_label.pack(pady=5)
        self.num_bands_entry = tk.Entry(main_root)
        self.num_bands_entry.pack(pady=5)

        # Entrée pour la taille des bandes
        self.band_size_label = tk.Label(main_root, text="Taille des bandes :", font=("Helvetica", 12))
        self.band_size_label.pack(pady=5)
        self.band_size_entry = tk.Entry(main_root)
        self.band_size_entry.pack(pady=5)

        # Entrée pour le nombre de cercles rouges
        self.num_circles_label = tk.Label(main_root, text="Nombre de cercles rouges par bande :", font=("Helvetica", 12))
        self.num_circles_label.pack(pady=5)
        self.num_circles_entry = tk.Entry(main_root)
        self.num_circles_entry.pack(pady=5)

        # Bouton pour générer les bandes et cercles
        self.generate_button = tk.Button(main_root, text="Générer PDF", command=self.generate_pdf)
        self.generate_button.pack(pady=20)

    def validate_entries(self):
        try:
            num_bands = int(self.num_bands_entry.get() or "0")
            band_size = int(self.band_size_entry.get() or "0")
            num_circles = int(self.num_circles_entry.get() or "0")
            if num_bands <= 0 or band_size <= 0 or num_circles < 0:
                raise ValueError("Les valeurs doivent être positives.")
            return num_bands, band_size, num_circles
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))
            return None

    def generate_pdf(self):
        validation_result = self.validate_entries()
        if validation_result is None:
            return

        num_bands, band_size, num_circles = validation_result
        pdf_buffer = BytesIO()
        c = canvas.Canvas(pdf_buffer, pagesize=letter)
        
        width, height = letter
        margin = 50
        
        y_position = height - margin  # Position de départ en haut de la page
        
        for band in range(num_bands):
            if y_position < margin + 100:  # Si la position y est trop basse, ajouter une nouvelle page
                c.showPage()
                y_position = height - margin  # Réinitialiser la position y

            # Dessiner la bande numérique avec une longueur correspondant à la largeur de la page
            
            y_position -= 20

            # Ligne de graduation correspondant à la largeur de la page
            c.line(margin, y_position, width - margin, y_position)

            circle_positions = []
            while len(circle_positions) < num_circles:
                pos = random.randint(1, band_size - 1)  # Éviter les bords
                if pos % 5 != 0 and pos not in circle_positions:  # Éviter les multiples de 5 et les doublons
                    circle_positions.append(pos)

            for i in range(0, band_size + 1):
                x = margin + (i / band_size) * (width - 2 * margin)
                if i % 5 == 0:
                    c.line(x, y_position - 10, x, y_position + 8)  # Graduation longue
                    c.drawCentredString(x, y_position - 20, str(i))  # Afficher le numéro
                else:
                    c.line(x, y_position - 5, x, y_position + 4)  # Graduation courte

                if i in circle_positions:  # Placer un cercle rouge si nécessaire
                    c.setStrokeColorRGB(1, 0, 0)  # Couleur rouge pour les cercles
                    c.circle(x, y_position, 5)      # Dessiner le cercle rouge
                    c.setStrokeColorRGB(0, 0, 0)    # Revenir à la couleur noire

            y_position -= 50

        c.save()
        
        pdf_buffer.seek(0)
        pdf_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        
        if pdf_file_path:
            with open(pdf_file_path, 'wb') as f:
                f.write(pdf_buffer.getvalue())
            messagebox.showinfo("Succès", "PDF enregistré avec succès.")

if __name__ == "__main__":
    main_root = tk.Tk()
    app = BandGenerator(main_root)
    main_root.mainloop()
