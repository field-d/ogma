from ogma.document import create_document, add_title_page, add_standard_sections
from ogma.references import add_references_section

doc = create_document()

add_title_page(
    doc,
    title="The Impact of X on Y",
    name="David Field",
    student_num="124706055",
    course="BA Psychology & Computing",
    university="University College Cork",
    module_code="AP2051",
    lecturer="Dr. Didier Ching",
    date="August 28th, 2026",
)

references = [
    {
        "authors": ["Smith, J.", "Doe, A."],
        "year": 2021,
        "title": "The psychology of x",
        "source": "Journal of Science",
        "volume": "12",
        "issue": "3",
        "pages": "45-67",
        "doi": "10.1234/jbs.2021.001",
    },
{
        "authors": ["Smith, J.", "Doe, A."],
        "year": 2021,
        "title": "The psychology of x",
        "source": "Journal of Science",
        "volume": "12",
        "issue": "3",
        "pages": "45-67",
        "doi": "10.1234/jbs.2021.001",
    },
{
        "authors": ["Smith, J.", "Doe, A."],
        "year": 2021,
        "title": "The psychology of x",
        "source": "Journal of Science",
        "volume": "12",
        "issue": "3",
        "pages": "45-67",
        "doi": "10.1234/jbs.2021.001",
    }

]


add_standard_sections(doc)
add_references_section(doc, references)

doc.save("examples/text_output6.docx")