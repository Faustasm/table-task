import sys
from entity_utils import load_entity
from entities import Database, Table, Column
import os


def read_table_data(file_name):
    table_data = list()
    with open(file_name, "r") as file:
        rows = [row for row in file.readlines() if row != "\n"]
        for row_idx in range(len(rows)):
            row = rows[row_idx]
            columns = [
                column.strip().strip("\n").strip("\t") for column in row.split("|")
            ]
            if row_idx == 0:
                table_data.append(columns)
                continue
            for column_idx in range(len(columns)):
                column = columns[column_idx]
                if column and column_idx == 0:
                    table_data.append(load_entity(columns[0], columns[2], "database"))
                    break
                elif column and column_idx == 1:
                    table_data.append(load_entity(columns[1], columns[3], "table"))
                    break
                elif column and column_idx == 2:
                    dtype = load_entity(columns[3])
                    table_data.append(load_entity(columns[2], columns[4], dtype))
                    break

    return table_data

if __name__ == "__main__":
    file_name = sys.argv[1]
    table_data = read_table_data(file_name)
    header = table_data[0]
    database_column_width = max(
        max([len(data.name) for data in table_data if isinstance(data, Database)]),
        len(header[0]),
    )
    table_column_width = max(
        max([len(data.name) for data in table_data if isinstance(data, Table)]),
        len(header[1]),
    )
    column_column_width = max(
        max([len(data.name) for data in table_data if isinstance(data, Column)]),
        len(header[2]),
    )
    type_column_width = max(
        max([len(data.dtype.name) for data in table_data if isinstance(data, Column)]),
        len(header[3]),
    )
    title_column_width = max(
        max(
            [
                len(data.title)
                for data in table_data
                if isinstance(data, Database | Table | Column)
            ]
        ),
        len(header[4]),
    )

    print(
        "{}|{}|{}|{}|{}".format(
            header[0] + " " * (database_column_width - len(header[0])),
            header[1] + " " * (table_column_width - len(header[1])),
            header[2] + " " * (column_column_width - len(header[2])),
            header[3] + " " * (type_column_width - len(header[3])),
            header[4] + " " * (title_column_width - len(header[4])),
        )
    )

    for item in table_data:
        if isinstance(item, Database | Table | Column):
            print(
                item.present_as_row(
                    database_column_width,
                    table_column_width,
                    column_column_width,
                    type_column_width,
                    title_column_width,
                )
            )
