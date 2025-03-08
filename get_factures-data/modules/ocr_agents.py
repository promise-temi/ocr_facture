import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

def main():
    use_azure_ocr()

# azure ocr
def use_azure_ocr(image_url):
    try:
        endpoint = os.environ["VISION_ENDPOINT"]
        key = os.environ["VISION_KEY"]
    except KeyError:
        raise EnvironmentError("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'. Set them before running this sample.")

    # Création du client d'analyse d'image
    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    # Appel synchronisé pour analyser l'image depuis son URL
    result = client.analyze_from_url(
        image_url=image_url,  # Correction ici : utiliser image_url au lieu de 'im'
        visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
        gender_neutral_caption=True,  # Optionnel (la valeur par défaut est False)
    )

    output = {}

    # Traitement du résultat de la légende (caption)
    if result.caption is not None:
        output["caption"] = {
            "text": result.caption.text,
            "confidence": result.caption.confidence
        }

    # Traitement du résultat OCR (lecture)
    if result.read is not None:
        read_lines = []
        # Itérer sur chaque bloc de texte détecté
        for block in result.read.blocks:
            for line in block.lines:
                line_info = {
                    "text": line.text,
                    "bounding_box": line.bounding_polygon,
                    "words": []
                }
                # Itérer sur chaque mot de la ligne
                for word in line.words:
                    line_info["words"].append({
                        "text": word.text,
                        "bounding_box": word.bounding_polygon,
                        "confidence": word.confidence
                    })
                read_lines.append(line_info)
        output["read"] = read_lines

    return output

if __name__ == "__main__":
    main()