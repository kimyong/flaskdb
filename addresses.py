"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Person, Address, AddressSchema


def read_all():
    """
    This function responds to a request for /api/people/notes
    with the complete list of notes, sorted by note timestamp

    :return:                json list of all notes for all people
    """
    # Query the database for all the notes
    addresses = Address.query.order_by(db.desc(Address.timestamp)).all()

    # Serialize the list of notes from our data
    address_schema = AddressSchema(many=True, exclude=["person.addresses"])
    data = address_schema.dump(addresses).data
    return data


def read_one(person_id, address_id):
    """
    This function responds to a request for
    /api/people/{person_id}/notes/{note_id}
    with one matching note for the associated person

    :param person_id:       Id of person the note is related to
    :param note_id:         Id of the note
    :return:                json string of note contents
    """
    # Query the database for the note
    address = (
        Address.query.join(Person, Person.person_id == Address.person_id)
        .filter(Person.person_id == person_id)
        .filter(Address.addr_id == address_id)
        .one_or_none()
    )

    # Was a note found?
    if address is not None:
        address_schema = AddressSchema()
        data = address_schema.dump(address).data
        return data

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Address not found for Id: {address_id}")


def create(person_id, address):
    """
    This function creates a new note related to the passed in person id.

    :param person_id:       Id of the person the note is related to
    :param note:            The JSON containing the note data
    :return:                201 on success
    """
    # get the parent person
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    # Was a person found?
    if person is None:
        abort(404, f"Person not found for Id: {person_id}")

    # Create a note schema instance
    schema = AddressSchema()
    new_address = schema.load(address, session=db.session).data

    # Add the note to the person and database
    person.addresses.append(new_address)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_address).data

    return data, 201


def update(person_id, address_id, address):
    """
    This function updates an existing note related to the passed in
    person id.

    :param person_id:       Id of the person the note is related to
    :param note_id:         Id of the note to update
    :param content:            The JSON containing the note data
    :return:                200 on success
    """
    update_address = (
        Address.query.filter(Person.person_id == person_id)
        .filter(Address.addr_id == address_id)
        .one_or_none()
    )

    # Did we find an existing note?
    if update_address is not None:

        # turn the passed in note into a db object
        schema = AddressSchema()
        update = schema.load(address, session=db.session).data

        # Set the id's to the note we want to update
        update.person_id = update_address.person_id
        update.addr_id = update_address.addr_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated note in the response
        data = schema.dump(update_address).data

        return data, 200

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Address not found for Id: {address_id}")


def delete(person_id, address_id):
    """
    This function deletes a note from the note structure

    :param person_id:   Id of the person the note is related to
    :param note_id:     Id of the note to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the note requested
    address = (
        Address.query.filter(Person.person_id == person_id)
        .filter(Address.addr_id == address_id)
        .one_or_none()
    )

    # did we find a note?
    if address is not None:
        db.session.delete(address)
        db.session.commit()
        return make_response(
        ("Address deleted", 200)
        )


    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Address not found for Id: {address_id}")
