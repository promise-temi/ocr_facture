const getListFromFile = require('./js_modules/getData'); // ✅ Import avec `require()`
const getTextFromLink = require('./js_modules/tesseractOCR');
const fs = require('fs').promises;

(async () => {
    try { 
        let facturesList = await getListFromFile('data/factures_links.txt'); // ✅ Appel de la fonction
        console.log("Liste des factures :", facturesList);
        textList = []
        for (let i = 0; i < facturesList.length; i++) {
            let facture = facturesList[i]; // ✅ Prendre l'élément `i` et non toujours `0`
            let text = await getTextFromLink(facture);
            console.log('this is it');
            console.log(text);
            textList.push({'facture':facture, 'text':text})
        }

        //  Convertir la liste en JSON
        let jsonContent = JSON.stringify(textList, null, 2);

        //  Enregistrer dans un fichier JSON
        await fs.writeFile("data/resultats.json", jsonContent, "utf8");
        console.log(" Résultats enregistrés dans resultats.json");
    } catch (error) {
        console.error("Impossible de récupérer la liste :", error);
    }
})();





 
