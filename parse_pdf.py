import pymupdf4llm
import pathlib

pdf_path = pathlib.Path("documentacao/i8429en.pdf")

pdf_text = pymupdf4llm.to_markdown(pdf_path, pages=range(0,227))

pathlib.Path("documentacao/livros/i8429en.mdc").write_text(pdf_text)