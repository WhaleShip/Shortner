from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

from database.session_manager import SessionManager, get_session


def get_conn_engine():
    return SessionManager().engine


convention = {
    "all_column_names": lambda constraint, table: "_".join(
        [str(column.name) for column in constraint.columns.values()]
    ),
    "ix": "ix__%(table_name)s__%(all_column_names)s",
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": ("fk__%(table_name)s__%(all_column_names)s__" "%(referred_table_name)s"),
    "pk": "pk__%(table_name)s",
}

metadata = MetaData(naming_convention=convention)
BaseDeclarativeModel = declarative_base(metadata=metadata)


__all__ = [
    "get_session",
    "get_conn_engine",
    "BaseDeclarativeModel",
]
