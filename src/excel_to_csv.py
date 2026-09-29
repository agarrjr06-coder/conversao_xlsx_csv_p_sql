"""Conversão de arquivos Excel para CSV.

O script recebe um arquivo .xlsx, cria a pasta de saída quando necessário
e gera um CSV em UTF-8 pronto para uso em etapas posteriores de ETL, BI
ou carga em banco de dados.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import pandas as pd


DEFAULT_OUTPUT_NAME = "faturamento_atualizado.csv"


def convert_excel_to_csv(
    input_file: Path,
    output_dir: Path,
    output_name: str = DEFAULT_OUTPUT_NAME,
) -> Path:
    """Converte um arquivo Excel para CSV e retorna o caminho gerado."""

    if not input_file.exists():
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {input_file}")

    if input_file.suffix.lower() != ".xlsx":
        raise ValueError("O arquivo de entrada deve estar no formato .xlsx")

    if not output_name.lower().endswith(".csv"):
        output_name = f"{output_name}.csv"

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / output_name

    start = time.perf_counter()

    print(f"Lendo arquivo: {input_file}")
    dataframe = pd.read_excel(input_file, engine="openpyxl")

    print(f"Linhas carregadas: {len(dataframe):,}")
    print(f"Gerando CSV: {output_file}")

    dataframe.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig",
    )

    elapsed = time.perf_counter() - start
    print(f"Conversão concluída em {elapsed:.2f} segundos.")

    return output_file


def parse_args() -> argparse.Namespace:
    """Lê os argumentos informados na linha de comando."""

    parser = argparse.ArgumentParser(
        description="Converte uma planilha Excel (.xlsx) para CSV."
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Caminho do arquivo Excel de entrada.",
    )
    parser.add_argument(
        "output_dir",
        type=Path,
        help="Pasta onde o CSV será salvo.",
    )
    parser.add_argument(
        "--output-name",
        default=DEFAULT_OUTPUT_NAME,
        help=f"Nome do CSV gerado. Padrão: {DEFAULT_OUTPUT_NAME}",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    convert_excel_to_csv(
        input_file=args.input_file,
        output_dir=args.output_dir,
        output_name=args.output_name,
    )


if __name__ == "__main__":
    main()
