import PyPDF2

input_pdf = "G.K 1 (2014).pdf"
output_pdf = "output.pdf"

with open(input_pdf, "rb") as input_file, open(output_pdf, "wb") as output_file:
    pdf_reader = PyPDF2.PdfReader(input_file)
    pdf_writer = PyPDF2.PdfWriter()

    for page_number in range(len(pdf_reader.pages)):
        if (page_number + 1) % 2 == 0:  # Keep even pages
            pdf_writer.add_page(pdf_reader.pages[page_number])

    pdf_writer.write(output_file)
