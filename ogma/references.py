from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph
from docx.shared import Inches

def format_reference_parts(ref):
    """
    This function returns a list of (text, italic tuples representing the reference.
    """
    authors = ref["authors"]
    if len(authors) == 1:
        author_str = authors[0]
    elif len(authors) == 2:
        author_str = f"{authors[0]}, & {authors[-1]}"
    else:
        author_str = ", ".join(authors[:-1]) + f", & {authors[-1]}"

    parts = [
        (f"{author_str} ", False),
        (f"({ref['year']}. ", False),
        (f"{ref['title']}, ", False)
    ]

    if "source" in ref:

        source_str = ref["source"]
        if "volume" in ref:
            volume_part = f", {ref["volume"]}"
            parts.append((source_str, True))
            parts.append((volume_part, True))
            if "issue" in ref:
                parts.append((f"({ref["issue"]})", False))
        else:
            parts.append((source_str, True))

        if "pages" in ref:
            parts.append((f", {ref["pages"]}", False))

        parts.append((".", False))

    if "doi" in ref:
        parts.append((f" https://doi.org/{ref["doi"]}", False))

    return parts

def sort_references(references):
    return sorted(references, key=lambda r: r["authors"][0].lower())

def _insert_paragraph_after(paragraph):
    """
    This function creates a new paragraph immediately after the given one
    """
    new_para = OxmlElement("w:p")
    paragraph._p.addnext(new_para)
    return Paragraph(new_para, paragraph._parent)

def find_heading_paragraph(doc, heading_text):
    for para in doc.paragraphs:
        if para.text.strip() == heading_text:
            return para
    return None

def add_references_section(doc, references):
    heading_para = find_heading_paragraph(doc, "References")
    if heading_para is None:
        raise ValueError("Could not find a 'References' heading - make sure to call add_standard_sections")

    sorted_references = sort_references(references)

    anchor = heading_para
    for ref in sorted_references:
        anchor = _insert_paragraph_after(anchor)
        anchor.paragraph_format.left_indent = Inches(0.5)
        anchor.paragraph_format.first_line_indent = Inches(-0.5)

        for text, italic in format_reference_parts(ref):
            run = anchor.add_run(text)
            run.italic = italic