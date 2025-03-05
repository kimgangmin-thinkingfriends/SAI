from sqlalchemy.inspection import inspect


def row_to_dict(row) -> dict:
    return {key: getattr(row, key) for key in inspect(row).attrs.keys()}
