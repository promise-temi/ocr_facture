import { createWorker } from 'tesseract.js';
getTextFromLink('https://projetocrstorageacc.blob.core.windows.net/invoices-2018/FAC_2018_0048-220.png?sv=2019-12-12&ss=b&srt=sco&sp=rl&se=2026-01-01T00:00:00Z&st=2025-01-01T00:00:00Z&spr=https&sig=%2BjCi7n8g%2F3849Rprey27XzHMoZN9zdVfDw6CifS6Y1U%3D')
async function getTextFromLink(link){
    const worker = await createWorker('eng');
    const ret = await worker.recognize(link);
    console.log(ret.data.text.split('\n'));
    await worker.terminate();
}

module.exports = getTextFromLink;