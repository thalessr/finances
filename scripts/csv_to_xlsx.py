#!/usr/bin/env python3
"""
Converte um CSV para XLSX (usa pandas).
Uso: python3 scripts/csv_to_xlsx.py input.csv output.xlsx
"""
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 3:
        print("Uso: python3 scripts/csv_to_xlsx.py input.csv output.xlsx", file=sys.stderr)
        sys.exit(1)
    input_csv = Path(sys.argv[1])
    output_xlsx = Path(sys.argv[2])

    try:
        import pandas as pd
    except Exception as e:
        print("pandas não encontrado:", e, file=sys.stderr)
        sys.exit(2)

    df = pd.read_csv(input_csv)
    df.to_excel(output_xlsx, index=False)
    print(f"Escrito: {output_xlsx}")

if __name__ == "__main__":
    main()

