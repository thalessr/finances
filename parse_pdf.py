import pymupdf4llm
import pathlib

pdf_path = pathlib.Path("docs/financas_corporativas.pdf")

pdf_text = pymupdf4llm.to_markdown(pdf_path, pages=range(0,134))

pathlib.Path("docs/financas_corporativas.md").write_text(pdf_text)