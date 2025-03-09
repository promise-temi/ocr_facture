const getListFromFile = require('./getData'); // ✅ Import avec `require()`
const getTextFromLink

(async () => {
    try {
        let facturesList = await getListFromFile('../data/factures_links.txt'); // ✅ Appel de la fonction
        console.log("Liste des factures :", facturesList);

    } catch (error) {
        console.error("Impossible de récupérer la liste :", error);
    }
})();





 
