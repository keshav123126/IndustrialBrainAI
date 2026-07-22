import fitz


class DocumentProcessor:

    def extract_text(self, file_path: str):

        pdf = fitz.open(file_path)

        text = ""

        total_pages = len(pdf)

        for page in pdf:

            text += page.get_text()

        pdf.close()

        return {
            "text": text,
            "pages": total_pages
        }


document_processor = DocumentProcessor()