from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
<<<<<<< HEAD
class Base(object):
=======
class Base:
>>>>>>> upstream/master
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
<<<<<<< HEAD

=======
>>>>>>> upstream/master
