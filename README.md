##Cloner le projet
git clone https://github.com/promise-temi/ocr_facture.git

##Accéder au répertoire du projet
cd ocr_facture/backend

##Assurez-vous d’être dans le même dossier que le fichier Dockerfile.
Prérequis
	•	Docker Desktop doit être installé sur votre machine.

##Construction de l’image Docker
Dans votre terminal, exécutez la commande suivante :
docker build -t django-ocr .

##Lancement du conteneur
Une fois l’image construite, lancez le conteneur avec la commande :
docker run -p 8000:8000 django-ocr

##Accéder à l’application
Ouvrez votre navigateur et rendez-vous à l’adresse suivante :
http://127.0.0.1:8000/add-invoice-page/

##Pour vous connecter voici les identifiants
id: super_user
mdp : password

##Acceder à l'interface d'administration à l'url : 
http://127.0.0.1:8000/admin/

##Pour vous connecter voici les identifiants
id: super_user
mdp : password

##Pour réccuperer des factures depuis la base pour tester l'application: 
1. Rendez vous à la base du projet
2. Dans votre terminal entrez cd ocr_facture/backend/modules
3. Puis entrez python get_all_facture_image.py
4. Vous pourrez retrouver les factures dans assets/images (toujour dans le dossier modules)
4. Factultatif : si il n'y a pas assez de factures pour vous, dans get_all_facture_image.py vous pouvez ajouter des années années en plus, comme 2019 dans les paramètre en plus de 2018.
