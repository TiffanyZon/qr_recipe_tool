from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem,
)
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.platypus import Image


def create_pdf_recipe(
    filename: str,
    title: str,
    cred: str,
    ingrediens: list[dict],
    step: list[str],
    portion: str,
    time: str,
):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title=title,
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    h_style = styles["Heading2"]
    meta_style = ParagraphStyle(
        "Meta",
        parent=styles["Normal"],
        spaceAfter=10,
    )

    ing_section_style = ParagraphStyle(
        "IngSection",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        spaceBefore=6,
        spaceAfter=3,
    )

    story = []

    story.insert(0, Image("hemkop_logo.png", width=10 * cm, height=2 * cm))

    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 5))

    story.append(Paragraph(cred))
    story.append(Spacer(1, 2))

    meta_parts = []

    if portion:
        meta_parts.append(f"Portioner: {portion}")
    if time:
        meta_parts.append(f"Tid: {time}")
    if meta_parts:
        story.append(Paragraph(" | ".join(meta_parts), meta_style))

    story.append(Spacer(1, 8))

    story.append(Paragraph("Ingredienser", h_style))
    if ingrediens:
        for section in ingrediens:
            title = section.get("title")
            items = section.get("items", [])

            if title:
                story.append(Paragraph(title, ing_section_style))

            story.append(
                ListFlowable(
                    [ListItem(Paragraph(i, styles["Normal"])) for i in items],
                    bulletType="bullet",
                    leftIndent=18,
                )
            )
    else:
        story.append(Paragraph("• (fyll i ingredienser här)", styles["Normal"]))

    story.append(Spacer(1, 10))

    story.append(Paragraph("Steg", h_style))
    if step:
        step_list = ListFlowable(
            [ListItem(Paragraph(s, styles["Normal"])) for s in step],
            bulletType="1",
            start="1",
            leftIndent=18,
        )
        story.append(step_list)
    else:
        story.append(Paragraph(""))

    story.append(Spacer(1, 25))

    qr = Image("qrcode.png", width=5 * cm, height=5 * cm)

    text_block = [
        Paragraph(
            "Scanna QR kod för att komma till receptet på Hemköp.se.",
            styles["Normal"],
        ),
        Spacer(1, 6),
        Paragraph(
            "<b>Lycka till och smaklig spis!</b>",
            styles["Normal"],
        ),
    ]

    table_data = [[text_block, qr]]

    table = Table(
        table_data,
        colWidths=[10 * cm, 4 * cm],
    )

    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )

    story.append(table)

    doc.build(story)


if __name__ == "__main__":
    create_pdf_recipe(
        "recept.pdf",
        title="Asia tofu med hoisin och vitlök",
        cred="Recept från Hemköp.se",
        ingrediens=[
            {
                "title": None,
                "items": [
                    "400 g tofu",
                    "2 dl hoisinsås",
                    "4 msk ljus soja",
                    "1 msk riven ingefära",
                    "4 st vitlöksklyftor",
                    "1 st röd chili",
                    "2 tsk sesamolja",
                    "2 dl majsstärkelse",
                    "1 dl matolja att steka i",
                    "4 st strimlade salladslökar",
                ],
            },
            {
                "title": "Wokade Grönsaker",
                "items": [
                    "1 st broccoli skuren i bitar",
                    "200 g strimlad vitkål",
                    "2 st skivade morötter",
                ],
            },
            {
                "title": "Till Servering",
                "items": ["4 port jasminris", "1 st lime"],
            },
        ],
        step=[
            "Ta ut tofun ur förpackningen och lägg en tyngd ovanpå. Låt tofun vattna ur ca 20 min. Torka av med hushållspapper.",
            "Blanda samman hoisinsås, soja, ingefära, vitlök, chili och sesamolja.",
            "Skär tofun i bitar, lägg i såsen och låt marinera ca 15 min. Ta upp bitarna och vänd i majsstärkelse.",
            "Stek tofun krispig i olja och vänd försiktigt. Strössla över salladslök.",
            "Woka grönsakerna snabbt i het panna. Vänd med resterande sås och smaka av med salt och peppar. Servera grönsakerna med tofu, kokt jasminris och limeklyftor.",
        ],
        portion="4",
        time="30 min",
    )
