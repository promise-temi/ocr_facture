function getListFromFile(file){
    const fs = require('fs').promises; // Utilisation de `fs.promises` pour `async/await`

    async function getFacturesList(file) {
        try {
            let data = await fs.readFile(file, 'utf8'); // Lire le fichier en texte
            let jsonString = data.replace(/'/g, '"'); // ✅ Remplacer les apostrophes par des guillemets
            let facturesArray = JSON.parse(jsonString); // ✅ Convertir en tableau

            return facturesArray;
        } catch (err) {
            console.error("Erreur lors de la lecture ou du parsing du fichier :", err);
        }
    }

    // Utilisation
    (async () => {
        let facturesList = await getFacturesList('factures_links.txt');
        console.log("Liste des factures :", facturesList);
        return facturesList
    })();
}