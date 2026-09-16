from ogma.document import create_document, add_title_page, add_standard_sections
from ogma.references import add_references_section
from ogma.figures import add_figure, FigureCounter

doc = create_document()
fig_counter = FigureCounter()

add_title_page(
    doc,
    title="The Impact of X on Y",
    name="John Doe",
    student_num="123456789",
    course="CK121 Psychology & Computing",
    university="University College Cork",
    module_code="AB1234",
    lecturer="Dr. Jane Doe",
    date="August 28th, 2026",
)

add_figure(
    doc,
    fig_counter,
    image_path = "/Users/davidfield/PycharmProjects/ogma/p1.png",
    title = "X and Y of X and Y",
    note = "Data collected from N=150 participants"
)

add_figure(
    doc,
    fig_counter,
    image_path = "/Users/davidfield/PycharmProjects/ogma/p1.png",
    title = "X and Y of X and Y",
    note = "Data collected from N=150 participants"
)

add_figure(
    doc,
    fig_counter,
    image_path = "/Users/davidfield/PycharmProjects/ogma/p1.png",
    title = "X and Y of X and Y",
    note = "Data collected from N=150 participants"
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

doc.save("examples/text_output10.docx")