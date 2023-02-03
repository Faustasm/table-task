class Node:
    name: str
    title: str


class Database(Node):
    def present_as_row(
        self,
        database_column_width,
        table_column_width,
        column_column_width,
        type_column_width,
        title_column_width,
    ):
        return "{}|{}|{}".format(
            self.name
            + " "
            * (
                database_column_width
                + table_column_width
                + column_column_width
                - len(self.name)
                + 2
            ),
            " " * type_column_width,
            self.title + " " * (title_column_width - len(self.title)),
        )


class Table(Node):
    def present_as_row(
        self,
        database_column_width,
        table_column_width,
        column_column_width,
        type_column_width,
        title_column_width,
    ):
        return "{}|{}|{}|{}".format(
            " " * database_column_width,
            self.name
            + " " * (table_column_width + column_column_width - len(self.name) + 1),
            " " * type_column_width,
            self.title + " " * (title_column_width - len(self.title)),
        )


class DataType:
    name: str


class Integer(DataType):
    pass


class String(DataType):
    pass


class Column(Node):
    dtype: DataType

    def present_as_row(
        self,
        database_column_width,
        table_column_width,
        column_column_width,
        type_column_width,
        title_column_width,
    ):
        return "{}|{}|{}|{}|{}".format(
            " " * database_column_width,
            " " * table_column_width,
            self.name + " " * (column_column_width - len(self.name)),
            self.dtype.name + " " * (type_column_width - len(self.dtype.name)),
            self.title + " " * (title_column_width - len(self.title)),
        )
