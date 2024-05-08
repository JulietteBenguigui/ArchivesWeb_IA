# Un script pour vérifier la validité de l'ensemble des "seeds" des collectes IA de la BnF et de l'IIPC.


import csv
import requests

def check_link_validity(link):
    try:
        response = requests.head(link)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def main(csv_file):
    valid_links = 0
    total_links = 0
    
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        
        for row in reader:
            link = row[0]  # Assuming link is in the first column
            total_links += 1
            if check_link_validity(link):
                valid_links += 1
                
    if total_links == 0:
        print("Le fichier CSV est vide.")
        return
    
    validity_percentage = (valid_links / total_links) * 100
    print(f"Nombre total de liens : {total_links}")
    print(f"Nombre de liens valides : {valid_links}")
    print(f"Pourcentage de liens valides : {validity_percentage:.2f}%")

if __name__ == "__main__":
    csv_file = "all_seeds.csv"  # Remplace 'nom_du_fichier.csv' par le chemin de ton fichier CSV
    main(csv_file)
