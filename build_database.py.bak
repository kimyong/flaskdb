import os
from datetime import datetime
from config import db
from models import Person, Note, Address

# Data to initialize database with
PEOPLE = [
    {
        "fname": "Doug",
        "mname": "",
        "lname": "Farrell",
        "date_of_birth": "10-May-1980",
        "mobile_number": "+65-82520816",
        "gender":"M",
        "customer_number": "SG1024682067",
        "country_of_birth":"US"
        "country_of_residence":"SG",
        "customer_segment":"Retail",
        "notes": [
            ("Cool, a mini-blogging application!", "2019-01-06 22:17:54"),
            ("This could be useful", "2019-01-08 22:17:54"),
            ("Well, sort of useful", "2019-03-06 22:17:54"),
        ],
        "addresses": [
            ("Residence", "Pickering Street", "10-231", "", "", "SG", "231245", "", "Singapore", "2019-04-06 22:18:00"),
            ("Office", "Changi Business Park", "04-31", "", "", "SG", "470878", "", "Singapore", "2019-04-06 22:17:54"),
        ],
    },
    {
        "fname": "Kent",
        "mname": ""
        "lname": "Brockman",
        "date_of_birth": "10-May-1981",
        "mobile_number": "+65-82522216",
        "gender":"M",
        "customer_number": "TH1027582067",
        "country_of_birth":"HK"
        "country_of_residence":"SG",
        "customer_segment":"Retail",
        "notes": [
            (
                "I'm going to make really profound observations",
                "2019-01-07 22:17:54",
            ),
            (
                "Maybe they'll be more obvious than I thought",
                "2019-02-06 22:17:54",
            ),
        ],
        "addresses": [
            ("Residence", "Dunlop Street", "15-231", "", "", "SG", "431245", "", "Singapore", "2019-04-06 22:18:00"),
            ("Office", "Changi Business Park", "04-31", "", "", "SG", "470878", "", "Singapore", "2019-04-06 22:17:54"),
        ],
    },
    {
        "fname": "Bunny",
        "mname": ""
        "lname": "Easter",
        "date_of_birth": "10-May-1956",
        "mobile_number": "+65-9520816",
        "gender":"M",
        "customer_number": "CA1024682067",
        "country_of_birth":"CA"
        "country_of_residence":"SG",
        "customer_segment":"Retail",
        "notes": [
            ("Has anyone seen my Easter eggs?", "2019-01-07 22:47:54"),
            ("I'm really late delivering these!", "2019-04-06 22:17:54"),
        ],
        "addresses": [
            ("Residence", "Coleman Street", "231A", "", "", "SG", "239245", "", "Singapore", "2019-04-06 22:18:00"),
            ("Office", "Changi Business Park", "04-31", "", "", "SG", "470878", "", "Singapore", "2019-04-06 22:17:54"),
        ],
    },
]

# Delete database file if it exists currently
if os.path.exists("people.db"):
    os.remove("people.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person.get("lname"), fname=person.get("fname"))

    # Add the notes for the person
    for note in person.get("notes"):
        content, timestamp = note
        p.notes.append(
            Note(
                content=content,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            )
        )
    db.session.add(p)

#db.session.commit()

#for person in PEOPLE:
#    p = Person(lname=person.get("lname"), fname=person.get("fname"))

    # Add the notes for the person
    for address in person.get("addresses"):
        addr_type, addr_line1, addr_line2, addr_line3, addr_line4, country_code, zip_code, state, city, timestamp = address 
        p.addresses.append(
            Address(
                addr_type = addr_type,
                addr_line1 = addr_line1,
                addr_line2 = addr_line2,
                addr_line3 = addr_line3,
                addr_line4 = addr_line4,
                country_code = country_code,
                zip_code = zip_code,
                state = state,
                city = city,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            )
        )
    db.session.add(p)

db.session.commit()
