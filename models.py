from datetime import datetime
from config import db, ma
from marshmallow import fields


class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    mname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    date_of_birth = db.Column(db.String(32))
    mobile_number = db.Column(db.String(32))
    gender = db.Column(db.String(1))
    customer_number = db.Column(db.String(32))
    country_of_birth = db.Column(db.String(2))
    country_of_residence = db.Column(db.String(2))
    customer_segment = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    addresses = db.relationship(
        "Address",
        backref="person",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Address.timestamp)",
    )

class Address(db.Model):
    __tablename__ = "address"
    addr_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"))
    addr_type = db.Column(db.String(32), nullable=False)
    addr_line1 = db.Column(db.String(32), nullable=False)
    addr_line2 = db.Column(db.String(32), nullable=True)
    addr_line3 = db.Column(db.String(32), nullable=True)
    addr_line4 = db.Column(db.String(32), nullable=True)
    country_code = db.Column(db.String(2), nullable=False )
    zip_code = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(32), nullable=True)
    city = db.Column(db.String(32), nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PersonSchema(ma.ModelSchema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    class Meta:
        model = Person
        sqla_session = db.session

    addresses = fields.Nested("PersonAddressSchema", default=[], many=True)

class PersonAddressSchema(ma.ModelSchema):

    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    addr_id = fields.Int()
    person_id = fields.Int()
    addr_type = fields.Str()
    addr_line1 = fields.Str()
    addr_line2 = fields.Str()
    addr_line3 = fields.Str()
    addr_line4 = fields.Str()
    country_code = fields.Str()
    zip_code = fields.Int()
    state = fields.Str()
    city = fields.Str()
    timestamp = fields.Str()


class AddressSchema(ma.ModelSchema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    class Meta:
        model = Address
        sqla_session = db.session

    person = fields.Nested("AddressPersonSchema", default=None)

class AddressPersonSchema(ma.ModelSchema):

    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    person_id = fields.Int()
    lname = fields.Str()
    fname = fields.Str()
    timestamp = fields.Str()

