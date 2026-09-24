users = [
    {
        "name": "Alice Smith",
        "age": 34,
        "email": "alice.smith@example.com",
        "date_of_birth": "15-March-1992",
    },
    {
        "name": "John Doe",
        "age": 42,
        "email": "john.doe@example.com",
        "date_of_birth": "22-July-1984",
    },
    {
        "name": "Elena Rostova",
        "age": 25,
        "email": "elena.rostova@example.com",
        "date_of_birth": "10-November-2001",
    },
    {
        "name": "Marcus Chen",
        "age": 56,
        "email": "marcus.chen@example.com",
        "date_of_birth": "04-February-1970",
    },
    {
        "name": "Fatima Al-Fassi",
        "age": 29,
        "email": "fatima.alfassi@example.com",
        "date_of_birth": "19-August-1997",
    },
    {
        "name": "Liam O'Connor",
        "age": 61,
        "email": "liam.oconnor@example.com",
        "date_of_birth": "30-January-1965",
    },
    {
        "name": "Sofia Rossi",
        "age": 38,
        "email": "sofia.rossi@example.com",
        "date_of_birth": "12-June-1988",
    },
    {
        "name": "Kenji Sato",
        "age": 47,
        "email": "kenji.sato@example.com",
        "date_of_birth": "05-October-1979",
    },
    {
        "name": "Chloe Dubois",
        "age": 22,
        "email": "chloe.dubois@example.com",
        "date_of_birth": "14-April-2004",
    },
    {
        "name": "Carlos Gomez",
        "age": 51,
        "email": "carlos.gomez@example.com",
        "date_of_birth": "28-September-1974",
    },
    {
        "name": "Amina Bello",
        "age": 33,
        "email": "amina.bello@example.com",
        "date_of_birth": "03-December-1993",
    },
    {
        "name": "Lucas Weber",
        "age": 40,
        "email": "lucas.weber@example.com",
        "date_of_birth": "17-May-1986",
    },
    {
        "name": "Priya Sharma",
        "age": 27,
        "email": "priya.sharma@example.com",
        "date_of_birth": "21-August-1999",
    },
    {
        "name": "David Miller",
        "age": 68,
        "email": "david.miller@example.com",
        "date_of_birth": "09-January-1958",
    },
    {
        "name": "Zara Khan",
        "age": 24,
        "email": "zara.khan@example.com",
        "date_of_birth": "11-July-2002",
    },
    {
        "name": "Oliver Twist",
        "age": 76,
        "email": "oliver.twist@example.com",
        "date_of_birth": "25-March-1950",
    },
    {
        "name": "Mei Lin",
        "age": 31,
        "email": "mei.lin@example.com",
        "date_of_birth": "08-October-1995",
    },
    {
        "name": "Gabriel Silva",
        "age": 44,
        "email": "gabriel.silva@example.com",
        "date_of_birth": "16-February-1982",
    },
    {
        "name": "Hannah Abbott",
        "age": 20,
        "email": "hannah.abbott@example.com",
        "date_of_birth": "29-June-2006",
    },
    {
        "name": "Dmitri Ivanov",
        "age": 54,
        "email": "dmitri.ivanov@example.com",
        "date_of_birth": "02-November-1972",
    },
    {
        "name": "Aisha Mohamed",
        "age": 36,
        "email": "aisha.mohamed@example.com",
        "date_of_birth": "13-April-1990",
    },
    {
        "name": "Noah van Dijk",
        "age": 26,
        "email": "noah.vandijk@example.com",
        "date_of_birth": "18-September-2000",
    },
    {
        "name": "Yuki Tanaka",
        "age": 49,
        "email": "yuki.tanaka@example.com",
        "date_of_birth": "07-May-1977",
    },
    {
        "name": "Grace Hopper",
        "age": 85,
        "email": "grace.hopper@example.com",
        "date_of_birth": "09-December-1941",
    },
    {
        "name": "Mateo Fernandez",
        "age": 35,
        "email": "mateo.fernandez@example.com",
        "date_of_birth": "24-January-1991",
    },
]

for user in users :
    if (int(user["date_of_birth"][-4:]) > 2000):
        print(user["name"], user["date_of_birth"])
