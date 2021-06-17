import PyPDF2

with open('twopage.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # print(reader.numPages)
    page = reader.getPage(1)
    print(page.rotateCounterClockwise(90))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('twist.pdf', "wb") as new_file:
        writer.write(new_file)

