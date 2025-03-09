const fs = require('fs').promises; // ✅ Utilisation de CommonJS avec `require()`

async function getListFromFile(file) {
    try {
        let data = await fs.readFile(file, 'utf8'); // ✅ Lire le fichier
        let jsonString = data.replace(/'/g, '"'); // ✅ Remplacer les apostrophes par des guillemets
        let facturesArray = JSON.parse(jsonString); // ✅ Convertir en tableau

        return facturesArray;
    } catch (err) {
        console.error("Erreur lors de la lecture ou du parsing du fichier :", err);
        throw err;
    }
}

module.exports = getListFromFile; // ✅ Exporter avec CommonJS
