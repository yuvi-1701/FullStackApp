from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: int

    # Using a declared_attr to give a default table name of the class
    # name in lowercase. This makes it easier to query and reference
    # the table names in the code.
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # Using __repr__ to give a string representation of the model.
    # This is useful for debugging and logging.
    def __repr__(self):
        items = [f"{k}={v}" for k, v in self.__dict__.items() if not k.startswith("_")]
        return f"<{self.__class__.__name__} {' '.join(items)}>"
