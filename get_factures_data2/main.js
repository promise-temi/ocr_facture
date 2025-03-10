// Import des librairies et modules
const fs = require('fs');
const path = require('path');
const { createWorker } = require('tesseract.js');

// Chemin du dossier des images 
let directoryPath = path.join(__dirname, 'data', 'images');

// lIRE les fichiers dans le dossier
let files = fs.readdirSync(directoryPath); // Lire les fichiers dans le dossier


console.log("Liste des fichiers :", files);

// Fonction OCR pour extraire du texte depuis une image grace a easy ocr
async function getTextFromImg(imgPath) {
    const worker = await createWorker('eng'); // Initialiser le moteur OCR
    const ret = await worker.recognize(imgPath); // Lecture de l'image
    await worker.terminate(); // Fermer le moteur
    return ret.data.text.split('\n'); // Retourner le texte sous forme de tableau
}

// Fonction principale pour traiter toutes les images 
async function processImages() {
    let textList = [];

    for (let facture of files) {
        let imgPath = path.join(directoryPath, facture); // Construire le chemin complet de l'image
        console.log(`Traitement de : ${imgPath}`);
        
        try {
            let text = await getTextFromImg(imgPath); // Récupérer le texte
            console.log("Texte extrait :", text);

            textList.push({ 'facture': facture, 'text': text });
        } catch (error) {
            console.error(`Erreur avec l'image ${facture} :`, error);
        }
    }

    // Convertir en JSON
    let jsonContent = JSON.stringify(textList, null, 2);

    // Sauvegarder le fichier JSON
    try {
        await fs.promises.writeFile("data/resultats.json", jsonContent, "utf8");
        console.log("Résultats enregistrés dans data/resultats.json");
    } catch (err) {
        console.error("Erreur d'écriture du fichier JSON :", err);
    }
}

// Exécuter la fonction principale
processImages();
