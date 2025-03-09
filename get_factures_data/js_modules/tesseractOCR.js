const { createWorker } = require('tesseract.js'); // ✅ Utiliser require() au lieu de import

async function getTextFromLink(link) {
    const worker = await createWorker('eng');
    const ret = await worker.recognize(link);
    // console.log(ret.data.text.split('\n'));
    await worker.terminate();
    return ret.data.text.split('\n')
}

module.exports = getTextFromLink; // ✅ Export correct en CommonJS
