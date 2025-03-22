from docxtpl import DocxTemplate


# charge le modèle
doc = DocxTemplate("modele.docx")

contexte = {
        "id" : "FAC/2018/0001",
        "date" : "2018-10-13",
        "nom" : "Carol Potter",
        "adresse" : "ashley38@example.org",
        "city": "Address 405 Adrian Crest Suite 095",
        "state" : "MN",
        "postal_code" : "36094",
        "total" : "1146.84"
    }


def make_invoice_pdf(id, date, nom, address, city, state, postal_code, total):
    # definir les variables
    contexte = {
        "id" : id,
        "date" : date,
        "nom":nom,
        "adresse":address,
        "city": city,
        "state" : state,
        "postal_code" : postal_code,
        "total" : total
    }

    # 3) On “render” le document avec ce contexte
    doc.render(contexte)
    doc.save("document_rempli.docx")

make_invoice_pdf()

