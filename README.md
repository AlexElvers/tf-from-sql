# TF from SQL

## Installation

Install Poetry for dependency management: https://python-poetry.org/docs/

Create virtual environment and install dependencies:

```bash
python -m venv env
. env/bin/activate
poetry install
```

## Usage

Create and initialize SQLite database:

```bash
python -m tf_from_sql init-db 
```

Show data:

```bash
python -m tf_from_sql show-data
```
