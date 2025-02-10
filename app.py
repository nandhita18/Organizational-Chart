from flask import Flask,jsonify, render_template
import json

app = Flask(__name__)

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Load the data once at the start and store it in a global variable
data = load_json_data('data/data.json')


# # Organizational data
# data = [
#    {
#     "key": 1,
#     "name": "Christopher Taylor",
#     "position": "Sr.Analyst",
#     "parent": 86
#   },
#   {
#     "key": 2,
#     "name": "Dominique Lucero",
#     "position": "CTO",
#     "parent": 179
#   },
#   {
#     "key": 3,
#     "name": "Tiffany Brown",
#     "position": "Manager",
#     "parent": 378
#   },
#   {
#     "key": 4,
#     "name": "Robert Baldwin",
#     "position": "VP",
#     "parent": 360
#   },
#   {
#     "key": 5,
#     "name": "Katie Russell",
#     "position": "CTO",
#     "parent": 50
#   },
#   {
#     "key": 6,
#     "name": "Teresa Miller",
#     "position": "GM",
#     "parent": 444
#   },
#   {
#     "key": 7,
#     "name": "The board",
#     "position": "Board of Directors",
#     "parent": None
#   },
#   {
#     "key": 8,
#     "name": "Caroline Miller",
#     "position": "Executive",
#     "parent": 289
#   },
#   {
#     "key": 9,
#     "name": "David Galloway",
#     "position": "President",
#     "parent": 60
#   },
#   {
#     "key": 10,
#     "name": "Andrea Anderson",
#     "position": "GCPEO",
#     "parent": 497
#   },
#   {
#     "key": 11,
#     "name": "Barbara Ford",
#     "position": "Sr.Analyst",
#     "parent": 3
#   },
#   {
#     "key": 12,
#     "name": "Diana Humphrey",
#     "position": "Deputy.GM",
#     "parent": 486
#   },
#   {
#     "key": 13,
#     "name": "Joshua Brady",
#     "position": "GM",
#     "parent": 318
#   },
#   {
#     "key": 14,
#     "name": "James Day",
#     "position": "Manager",
#     "parent": 435
#   },
#   {
#     "key": 15,
#     "name": "Angel Dean",
#     "position": "Sr.VP",
#     "parent": 38
#   },
#   {
#     "key": 16,
#     "name": "Rachel Chaney",
#     "position": "GCPEO",
#     "parent": 328
#   },
#   {
#     "key": 18,
#     "name": "Tara Diaz",
#     "position": "Manager",
#     "parent": 270
#   },
#   {
#     "key": 19,
#     "name": "Anthony Gibson",
#     "position": "Analyst",
#     "parent": 1
#   },
#   {
#     "key": 20,
#     "name": "Briana Carter",
#     "position": "GCFO",
#     "parent": 316
#   },
#   {
#     "key": 22,
#     "name": "Jessica Olson",
#     "position": "Sr.Manager",
#     "parent": 226
#   },
#   {
#     "key": 24,
#     "name": "James Ewing",
#     "position": "Sr.GM",
#     "parent": 417
#   },
#   {
#     "key": 25,
#     "name": "Ashley Chaney",
#     "position": "GCFO",
#     "parent": 94
#   },
#   {
#     "key": 26,
#     "name": "Nancy Garner",
#     "position": "Sr.GM",
#     "parent": 490
#   },
#   {
#     "key": 27,
#     "name": "James Moore",
#     "position": "GCPEO",
#     "parent": 218
#   },
#   {
#     "key": 28,
#     "name": "Cassandra Kerr",
#     "position": "CMO",
#     "parent": 497
#   },
#   {
#     "key": 29,
#     "name": "Kathy Dean",
#     "position": "CTO",
#     "parent": 74
#   },
#   {
#     "key": 30,
#     "name": "Amanda Cruz",
#     "position": "CMO",
#     "parent": 162
#   },
#   {
#     "key": 31,
#     "name": "Kristen Davis",
#     "position": "Sr.VP",
#     "parent": 330
#   },
#   {
#     "key": 32,
#     "name": "Joshua Patel",
#     "position": "GCCO",
#     "parent": 186
#   },
#   {
#     "key": 33,
#     "name": "Adam Watkins",
#     "position": "GCCO",
#     "parent": 170
#   },
#   {
#     "key": 34,
#     "name": "Natalie Hayes",
#     "position": "GCPEO",
#     "parent": 357
#   },
#   {
#     "key": 35,
#     "name": "Kellie Fisher",
#     "position": "Analyst",
#     "parent": 124
#   },
#   {
#     "key": 36,
#     "name": "Rebecca Ward",
#     "position": "GM",
#     "parent": 471
#   },
#   {
#     "key": 37,
#     "name": "Michael Soto",
#     "position": "Manager",
#     "parent": 39
#   },
#   {
#     "key": 38,
#     "name": "Jasmine Townsend",
#     "position": "President",
#     "parent": 50
#   },
#   {
#     "key": 39,
#     "name": "Diane Scott",
#     "position": "Sr.Manager",
#     "parent": 307
#   },
#   {
#     "key": 40,
#     "name": "Diamond Banks",
#     "position": "GCCO",
#     "parent": 316
#   },
#   {
#     "key": 41,
#     "name": "Tiffany Callahan",
#     "position": "Executive",
#     "parent": 551
#   },
#   {
#     "key": 42,
#     "name": "Michael Williams",
#     "position": "Associate VP",
#     "parent": 154
#   },
#   {
#     "key": 43,
#     "name": "Patricia Bonilla",
#     "position": "GM",
#     "parent": 24
#   },
#   {
#     "key": 44,
#     "name": "Bradley Fisher",
#     "position": "Executive",
#     "parent": 513
#   },
#   {
#     "key": 45,
#     "name": "Catherine Silva",
#     "position": "CTO",
#     "parent": 478
#   },
#   {
#     "key": 46,
#     "name": "Jennifer Alvarado",
#     "position": "COO",
#     "parent": 128
#   },
#   {
#     "key": 47,
#     "name": "John Wilson",
#     "position": "GCPEO",
#     "parent": 478
#   },
#   {
#     "key": 48,
#     "name": "Kathy Freeman",
#     "position": "Sr.VP",
#     "parent": 364
#   },
#   {
#     "key": 49,
#     "name": "Mary Pena",
#     "position": "COO",
#     "parent": 316
#   },
#   {
#     "key": 50,
#     "name": "Charles Palmer",
#     "position": "CEO",
#     "parent": 553
#   },
#   {
#     "key": 51,
#     "name": "Alexander Chavez",
#     "position": "GCPEO",
#     "parent": 186
#   },
#   {
#     "key": 53,
#     "name": "Jaime Kim",
#     "position": "COO",
#     "parent": 479
#   },
#   {
#     "key": 54,
#     "name": "Jennifer Waters",
#     "position": "President",
#     "parent": 218
#   },
#   {
#     "key": 55,
#     "name": "Brandon Kramer",
#     "position": "Analyst",
#     "parent": 88
#   },
#   {
#     "key": 56,
#     "name": "Kaitlyn Bond",
#     "position": "Manager",
#     "parent": 82
#   },
#   {
#     "key": 57,
#     "name": "Lindsay Allen",
#     "position": "President",
#     "parent": 479
#   },
#   {
#     "key": 58,
#     "name": "Christine Graham",
#     "position": "President",
#     "parent": 413
#   },
#   {
#     "key": 60,
#     "name": "William Perez",
#     "position": "CEO",
#     "parent": 298
#   },
#   {
#     "key": 61,
#     "name": "Richard Wise",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 62,
#     "name": "Nicole Clark",
#     "position": "CTO",
#     "parent": 362
#   },
#   {
#     "key": 63,
#     "name": "Ian Lewis",
#     "position": "Manager",
#     "parent": 428
#   },
#   {
#     "key": 64,
#     "name": "Samuel Graham",
#     "position": "Manager",
#     "parent": 428
#   },
#   {
#     "key": 65,
#     "name": "Wendy Ramirez",
#     "position": "COO",
#     "parent": 170
#   },
#   {
#     "key": 66,
#     "name": "Brian Johnson",
#     "position": "Executive",
#     "parent": 280
#   },
#   {
#     "key": 67,
#     "name": "John Cruz",
#     "position": "Sr.VP",
#     "parent": 165
#   },
#   {
#     "key": 68,
#     "name": "Christopher Moreno",
#     "position": "Sr.Executive",
#     "parent": 102
#   },
#   {
#     "key": 69,
#     "name": "Angela Carter",
#     "position": "GCPEO",
#     "parent": 170
#   },
#   {
#     "key": 70,
#     "name": "Danielle Murphy",
#     "position": "Sr.VP",
#     "parent": 40
#   },
#   {
#     "key": 71,
#     "name": "Carrie Edwards",
#     "position": "Analyst",
#     "parent": 445
#   },
#   {
#     "key": 72,
#     "name": "Michael Smith",
#     "position": "CMO",
#     "parent": 422
#   },
#   {
#     "key": 73,
#     "name": "Laura Adams",
#     "position": "CTO",
#     "parent": 444
#   },
#   {
#     "key": 74,
#     "name": "Felicia Griffin",
#     "position": "CEO",
#     "parent": 137
#   },
#   {
#     "key": 75,
#     "name": "Troy Douglas",
#     "position": "VP",
#     "parent": 309
#   },
#   {
#     "key": 76,
#     "name": "Lydia Wright",
#     "position": "Sr.VP",
#     "parent": 119
#   },
#   {
#     "key": 77,
#     "name": "Ryan Thomas",
#     "position": "COO",
#     "parent": 169
#   },
#   {
#     "key": 78,
#     "name": "Charles Castro",
#     "position": "Deputy.GM",
#     "parent": 267
#   },
#   {
#     "key": 79,
#     "name": "Rebecca Marquez",
#     "position": "Sr.Analyst",
#     "parent": 135
#   },
#   {
#     "key": 80,
#     "name": "Jessica Austin",
#     "position": "Sr.Analyst",
#     "parent": 102
#   },
#   {
#     "key": 82,
#     "name": "Melanie Torres",
#     "position": "Sr.Manager",
#     "parent": 353
#   },
#   {
#     "key": 84,
#     "name": "Arthur Rodriguez",
#     "position": "Associate VP",
#     "parent": 228
#   },
#   {
#     "key": 85,
#     "name": "Dawn Evans",
#     "position": "President",
#     "parent": 422
#   },
#   {
#     "key": 86,
#     "name": "Jonathan Thornton",
#     "position": "Manager",
#     "parent": 435
#   },
#   {
#     "key": 87,
#     "name": "Joshua Rodriguez",
#     "position": "Deputy.GM",
#     "parent": 312
#   },
#   {
#     "key": 88,
#     "name": "Valerie Hoover",
#     "position": "Sr.Analyst",
#     "parent": 86
#   },
#   {
#     "key": 89,
#     "name": "Susan Dixon",
#     "position": "Sr.GM",
#     "parent": 120
#   },
#   {
#     "key": 90,
#     "name": "Kenneth Wiggins",
#     "position": "GCCO",
#     "parent": 179
#   },
#   {
#     "key": 91,
#     "name": "Aaron Murphy",
#     "position": "COO",
#     "parent": 170
#   },
#   {
#     "key": 92,
#     "name": "Sarah Faulkner",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 93,
#     "name": "Jennifer Christensen",
#     "position": "CEO",
#     "parent": 61
#   },
#   {
#     "key": 94,
#     "name": "James Huynh",
#     "position": "CEO",
#     "parent": 122
#   },
#   {
#     "key": 95,
#     "name": "William Graham",
#     "position": "CEO",
#     "parent": 262
#   },
#   {
#     "key": 96,
#     "name": "Caitlin Mcdonald",
#     "position": "CEO",
#     "parent": 92
#   },
#   {
#     "key": 97,
#     "name": "Susan Davis",
#     "position": "VP",
#     "parent": 182
#   },
#   {
#     "key": 98,
#     "name": "Linda Jackson",
#     "position": "CTO",
#     "parent": 497
#   },
#   {
#     "key": 99,
#     "name": "John Avila",
#     "position": "COO",
#     "parent": 218
#   },
#   {
#     "key": 100,
#     "name": "Cynthia Guzman",
#     "position": "VP",
#     "parent": 182
#   },
#   {
#     "key": 101,
#     "name": "Michael Cole",
#     "position": "Manager",
#     "parent": 188
#   },
#   {
#     "key": 102,
#     "name": "Marc Morales",
#     "position": "Manager",
#     "parent": 554
#   },
#   {
#     "key": 103,
#     "name": "Tiffany Bryant",
#     "position": "Sr.Manager",
#     "parent": 402
#   },
#   {
#     "key": 104,
#     "name": "Amy Gilbert",
#     "position": "Manager",
#     "parent": 403
#   },
#   {
#     "key": 105,
#     "name": "Danielle Ward",
#     "position": "VP",
#     "parent": 360
#   },
#   {
#     "key": 106,
#     "name": "Beth Daniels",
#     "position": "GCCO",
#     "parent": 362
#   },
#   {
#     "key": 107,
#     "name": "Angel Long",
#     "position": "VP",
#     "parent": 58
#   },
#   {
#     "key": 108,
#     "name": "Mr. Matthew Jennings",
#     "position": "CMO",
#     "parent": 413
#   },
#   {
#     "key": 109,
#     "name": "Anthony Henry",
#     "position": "CTO",
#     "parent": 328
#   },
#   {
#     "key": 110,
#     "name": "William Baker",
#     "position": "GCFO",
#     "parent": 50
#   },
#   {
#     "key": 111,
#     "name": "James Haynes",
#     "position": "GCFO",
#     "parent": 457
#   },
#   {
#     "key": 112,
#     "name": "Joshua Campbell",
#     "position": "Sr.Executive",
#     "parent": 63
#   },
#   {
#     "key": 113,
#     "name": "Jessica Wright",
#     "position": "Deputy.GM",
#     "parent": 388
#   },
#   {
#     "key": 114,
#     "name": "James Rodriguez",
#     "position": "President",
#     "parent": 50
#   },
#   {
#     "key": 115,
#     "name": "Stephen Mitchell",
#     "position": "COO",
#     "parent": 230
#   },
#   {
#     "key": 116,
#     "name": "Warren Collins",
#     "position": "CEO",
#     "parent": 553
#   },
#   {
#     "key": 117,
#     "name": "Natalie Lee",
#     "position": "GCPEO",
#     "parent": 128
#   },
#   {
#     "key": 118,
#     "name": "Jared Cline",
#     "position": "GCCO",
#     "parent": 316
#   },
#   {
#     "key": 119,
#     "name": "Brian Jones",
#     "position": "President",
#     "parent": 128
#   },
#   {
#     "key": 120,
#     "name": "Brian Berger",
#     "position": "VP",
#     "parent": 182
#   },
#   {
#     "key": 121,
#     "name": "Joshua Jenkins",
#     "position": "GCCO",
#     "parent": 96
#   },
#   {
#     "key": 122,
#     "name": "Jackson Brewer",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 123,
#     "name": "Brent Johnson",
#     "position": "Executive",
#     "parent": 356
#   },
#   {
#     "key": 124,
#     "name": "Lori Ramirez",
#     "position": "Sr.Analyst",
#     "parent": 104
#   },
#   {
#     "key": 125,
#     "name": "Michael Mccormick",
#     "position": "Executive",
#     "parent": 551
#   },
#   {
#     "key": 126,
#     "name": "Jeffrey Lewis",
#     "position": "Sr.Manager",
#     "parent": 87
#   },
#   {
#     "key": 127,
#     "name": "Larry Vega",
#     "position": "Executive",
#     "parent": 508
#   },
#   {
#     "key": 128,
#     "name": "Jennifer Clark",
#     "position": "CEO",
#     "parent": 553
#   },
#   {
#     "key": 129,
#     "name": "Stephanie Howe",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 130,
#     "name": "Vanessa Li",
#     "position": "Executive",
#     "parent": 356
#   },
#   {
#     "key": 131,
#     "name": "Timothy Vega",
#     "position": "Sr.Executive",
#     "parent": 477
#   },
#   {
#     "key": 132,
#     "name": "Edward Perry",
#     "position": "Executive",
#     "parent": 491
#   },
#   {
#     "key": 133,
#     "name": "Lucas Jones",
#     "position": "Executive",
#     "parent": 448
#   },
#   {
#     "key": 134,
#     "name": "Wanda Taylor",
#     "position": "President",
#     "parent": 230
#   },
#   {
#     "key": 135,
#     "name": "Christopher Fisher",
#     "position": "Manager",
#     "parent": 319
#   },
#   {
#     "key": 136,
#     "name": "Mark Nichols",
#     "position": "President",
#     "parent": 96
#   },
#   {
#     "key": 137,
#     "name": "Misty Williams",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 139,
#     "name": "Mrs. Vanessa Moody",
#     "position": "Sr.Manager",
#     "parent": 12
#   },
#   {
#     "key": 140,
#     "name": "Erika Gordon",
#     "position": "Executive",
#     "parent": 491
#   },
#   {
#     "key": 141,
#     "name": "Nicole Black",
#     "position": "GCFO",
#     "parent": 509
#   },
#   {
#     "key": 142,
#     "name": "Gary Johnson",
#     "position": "Executive",
#     "parent": 131
#   },
#   {
#     "key": 143,
#     "name": "Lisa Davis",
#     "position": "Manager",
#     "parent": 188
#   },
#   {
#     "key": 144,
#     "name": "Robert Salazar",
#     "position": "GCCO",
#     "parent": 479
#   },
#   {
#     "key": 145,
#     "name": "Thomas Osborne",
#     "position": "President",
#     "parent": 60
#   },
#   {
#     "key": 146,
#     "name": "John Frank",
#     "position": "VP",
#     "parent": 136
#   },
#   {
#     "key": 147,
#     "name": "Andrew Woods",
#     "position": "GCFO",
#     "parent": 95
#   },
#   {
#     "key": 148,
#     "name": "Shannon Fuentes",
#     "position": "Sr.VP",
#     "parent": 501
#   },
#   {
#     "key": 149,
#     "name": "James Ruiz",
#     "position": "CTO",
#     "parent": 230
#   },
#   {
#     "key": 151,
#     "name": "Heather Williams",
#     "position": "Sr.VP",
#     "parent": 182
#   },
#   {
#     "key": 152,
#     "name": "Ethan Barber",
#     "position": "Executive",
#     "parent": 508
#   },
#   {
#     "key": 153,
#     "name": "Heidi Williams",
#     "position": "COO",
#     "parent": 230
#   },
#   {
#     "key": 154,
#     "name": "Donna Holmes",
#     "position": "GM",
#     "parent": 50
#   },
#   {
#     "key": 155,
#     "name": "Kevin Crawford",
#     "position": "Manager",
#     "parent": 319
#   },
#   {
#     "key": 156,
#     "name": "Tara Jones",
#     "position": "GCFO",
#     "parent": 497
#   },
#   {
#     "key": 157,
#     "name": "Katrina Watkins",
#     "position": "VP",
#     "parent": 399
#   },
#   {
#     "key": 158,
#     "name": "Veronica Mcmillan",
#     "position": "VP",
#     "parent": 290
#   },
#   {
#     "key": 159,
#     "name": "Charles Haney",
#     "position": "Sr.GM",
#     "parent": 75
#   },
#   {
#     "key": 160,
#     "name": "Keith Ward",
#     "position": "Executive",
#     "parent": 280
#   },
#   {
#     "key": 161,
#     "name": "Michelle Washington",
#     "position": "Analyst",
#     "parent": 495
#   },
#   {
#     "key": 162,
#     "name": "Erin Reid",
#     "position": "CEO",
#     "parent": 509
#   },
#   {
#     "key": 163,
#     "name": "Anna Hubbard",
#     "position": "CMO",
#     "parent": 362
#   },
#   {
#     "key": 164,
#     "name": "Lindsay Mitchell",
#     "position": "Executive",
#     "parent": 280
#   },
#   {
#     "key": 165,
#     "name": "Kim Martinez",
#     "position": "President",
#     "parent": 186
#   },
#   {
#     "key": 167,
#     "name": "James Burke PhD",
#     "position": "CTO",
#     "parent": 316
#   },
#   {
#     "key": 168,
#     "name": "Marie Greene",
#     "position": "COO",
#     "parent": 549
#   },
#   {
#     "key": 169,
#     "name": "Angela Anderson",
#     "position": "CEO",
#     "parent": 129
#   },
#   {
#     "key": 170,
#     "name": "Jose Bond",
#     "position": "CEO",
#     "parent": 509
#   },
#   {
#     "key": 171,
#     "name": "Janet Shelton",
#     "position": "Analyst",
#     "parent": 433
#   },
#   {
#     "key": 172,
#     "name": "Cassidy Cunningham",
#     "position": "Analyst",
#     "parent": 450
#   },
#   {
#     "key": 173,
#     "name": "Kimberly Clark",
#     "position": "Manager",
#     "parent": 378
#   },
#   {
#     "key": 174,
#     "name": "Beverly Edwards",
#     "position": "COO",
#     "parent": 95
#   },
#   {
#     "key": 175,
#     "name": "Julia Walker",
#     "position": "Manager",
#     "parent": 435
#   },
#   {
#     "key": 176,
#     "name": "Laura Daniel",
#     "position": "Sr.GM",
#     "parent": 65
#   },
#   {
#     "key": 177,
#     "name": "Claire Wiley",
#     "position": "GCCO",
#     "parent": 60
#   },
#   {
#     "key": 178,
#     "name": "David Hurst",
#     "position": "President",
#     "parent": 413
#   },
#   {
#     "key": 179,
#     "name": "Christopher Ross",
#     "position": "CEO",
#     "parent": 376
#   },
#   {
#     "key": 180,
#     "name": "Amanda Johnson",
#     "position": "CTO",
#     "parent": 357
#   },
#   {
#     "key": 182,
#     "name": "David Harrington",
#     "position": "President",
#     "parent": 60
#   },
#   {
#     "key": 183,
#     "name": "Julie Cook",
#     "position": "Sr.GM",
#     "parent": 91
#   },
#   {
#     "key": 184,
#     "name": "Michael Castro",
#     "position": "Deputy.GM",
#     "parent": 13
#   },
#   {
#     "key": 185,
#     "name": "Sarah Gray",
#     "position": "Sr.Analyst",
#     "parent": 477
#   },
#   {
#     "key": 186,
#     "name": "Anthony Howell",
#     "position": "CEO",
#     "parent": 137
#   },
#   {
#     "key": 187,
#     "name": "Wendy Knapp",
#     "position": "President",
#     "parent": 60
#   },
#   {
#     "key": 188,
#     "name": "Austin Weaver",
#     "position": "Sr.Manager",
#     "parent": 353
#   },
#   {
#     "key": 189,
#     "name": "David Schneider",
#     "position": "Sr.VP",
#     "parent": 25
#   },
#   {
#     "key": 190,
#     "name": "Brandon Wolfe",
#     "position": "Sr.GM",
#     "parent": 532
#   },
#   {
#     "key": 191,
#     "name": "Kyle Holmes",
#     "position": "Deputy.GM",
#     "parent": 204
#   },
#   {
#     "key": 192,
#     "name": "Angel Castillo",
#     "position": "President",
#     "parent": 93
#   },
#   {
#     "key": 193,
#     "name": "April Bowen",
#     "position": "VP",
#     "parent": 496
#   },
#   {
#     "key": 194,
#     "name": "Emily Wilcox",
#     "position": "Sr.Manager",
#     "parent": 434
#   },
#   {
#     "key": 195,
#     "name": "Jason Williams",
#     "position": "Associate VP",
#     "parent": 243
#   },
#   {
#     "key": 196,
#     "name": "David Huang",
#     "position": "Analyst",
#     "parent": 433
#   },
#   {
#     "key": 197,
#     "name": "Tammy Villarreal",
#     "position": "Associate VP",
#     "parent": 312
#   },
#   {
#     "key": 198,
#     "name": "Amanda Lin",
#     "position": "Deputy.GM",
#     "parent": 329
#   },
#   {
#     "key": 199,
#     "name": "Justin Becker",
#     "position": "GCFO",
#     "parent": 549
#   },
#   {
#     "key": 200,
#     "name": "Vanessa Soto",
#     "position": "GCPEO",
#     "parent": 422
#   },
#   {
#     "key": 201,
#     "name": "Diamond Steele",
#     "position": "VP",
#     "parent": 134
#   },
#   {
#     "key": 202,
#     "name": "Vanessa Wallace",
#     "position": "Associate VP",
#     "parent": 486
#   },
#   {
#     "key": 203,
#     "name": "Janice Mcbride DVM",
#     "position": "GCPEO",
#     "parent": 230
#   },
#   {
#     "key": 204,
#     "name": "Colleen Doyle",
#     "position": "GM",
#     "parent": 242
#   },
#   {
#     "key": 206,
#     "name": "Sean Fowler",
#     "position": "Sr.VP",
#     "parent": 239
#   },
#   {
#     "key": 207,
#     "name": "Casey Le",
#     "position": "Associate VP",
#     "parent": 312
#   },
#   {
#     "key": 208,
#     "name": "Brittany Reed",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 209,
#     "name": "David Lewis",
#     "position": "President",
#     "parent": 497
#   },
#   {
#     "key": 210,
#     "name": "Mr. Calvin Kane DVM",
#     "position": "Sr.GM",
#     "parent": 53
#   },
#   {
#     "key": 211,
#     "name": "Derrick Thompson",
#     "position": "Analyst",
#     "parent": 291
#   },
#   {
#     "key": 212,
#     "name": "Erika Johnson",
#     "position": "GCCO",
#     "parent": 96
#   },
#   {
#     "key": 213,
#     "name": "Stacy Jackson",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 214,
#     "name": "Daniel Martinez",
#     "position": "GCFO",
#     "parent": 549
#   },
#   {
#     "key": 215,
#     "name": "Joshua Randall",
#     "position": "COO",
#     "parent": 93
#   },
#   {
#     "key": 216,
#     "name": "Rodney Cox",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 217,
#     "name": "Douglas Montoya",
#     "position": "Sr.Executive",
#     "parent": 483
#   },
#   {
#     "key": 218,
#     "name": "Crystal Callahan",
#     "position": "CEO",
#     "parent": 122
#   },
#   {
#     "key": 219,
#     "name": "Alison Garcia",
#     "position": "Associate VP",
#     "parent": 329
#   },
#   {
#     "key": 220,
#     "name": "Abigail Parrish",
#     "position": "CEO",
#     "parent": 137
#   },
#   {
#     "key": 221,
#     "name": "Christopher Holmes",
#     "position": "CTO",
#     "parent": 169
#   },
#   {
#     "key": 222,
#     "name": "Megan Cabrera",
#     "position": "GCPEO",
#     "parent": 413
#   },
#   {
#     "key": 223,
#     "name": "Richard Lyons",
#     "position": "CTO",
#     "parent": 74
#   },
#   {
#     "key": 224,
#     "name": "Carol Burke",
#     "position": "Sr.Analyst",
#     "parent": 321
#   },
#   {
#     "key": 225,
#     "name": "Kenneth Donaldson",
#     "position": "Sr.VP",
#     "parent": 535
#   },
#   {
#     "key": 226,
#     "name": "James Evans",
#     "position": "Deputy.GM",
#     "parent": 329
#   },
#   {
#     "key": 227,
#     "name": "Nicholas Tucker",
#     "position": "Executive",
#     "parent": 7
#   },
#   {
#     "key": 228,
#     "name": "Susan Padilla",
#     "position": "GM",
#     "parent": 242
#   },
#   {
#     "key": 229,
#     "name": "Megan Scott",
#     "position": "Deputy.GM",
#     "parent": 243
#   },
#   {
#     "key": 230,
#     "name": "Mrs. Leslie Jacobs MD",
#     "position": "CEO",
#     "parent": 262
#   },
#   {
#     "key": 231,
#     "name": "Lisa Arellano",
#     "position": "GCPEO",
#     "parent": 220
#   },
#   {
#     "key": 232,
#     "name": "Michael Mccullough",
#     "position": "GCFO",
#     "parent": 96
#   },
#   {
#     "key": 233,
#     "name": "Eric Pollard",
#     "position": "Analyst",
#     "parent": 526
#   },
#   {
#     "key": 234,
#     "name": "Ricardo Vargas",
#     "position": "GCCO",
#     "parent": 74
#   },
#   {
#     "key": 235,
#     "name": "William Freeman",
#     "position": "VP",
#     "parent": 165
#   },
#   {
#     "key": 236,
#     "name": "David Dunn",
#     "position": "GCFO",
#     "parent": 390
#   },
#   {
#     "key": 237,
#     "name": "Nathan Morales",
#     "position": "CTO",
#     "parent": 413
#   },
#   {
#     "key": 238,
#     "name": "Thomas Johnson",
#     "position": "Analyst",
#     "parent": 305
#   },
#   {
#     "key": 239,
#     "name": "William Hanson",
#     "position": "President",
#     "parent": 128
#   },
#   {
#     "key": 240,
#     "name": "Mrs. Heather Johns",
#     "position": "Deputy.GM",
#     "parent": 36
#   },
#   {
#     "key": 241,
#     "name": "Micheal Phillips",
#     "position": "Sr.VP",
#     "parent": 58
#   },
#   {
#     "key": 242,
#     "name": "Regina Clark",
#     "position": "Sr.GM",
#     "parent": 97
#   },
#   {
#     "key": 243,
#     "name": "Christopher Mosley MD",
#     "position": "GM",
#     "parent": 176
#   },
#   {
#     "key": 245,
#     "name": "David Flynn",
#     "position": "Sr.GM",
#     "parent": 97
#   },
#   {
#     "key": 246,
#     "name": "Jennifer Arnold",
#     "position": "GCCO",
#     "parent": 169
#   },
#   {
#     "key": 247,
#     "name": "John Humphrey",
#     "position": "Sr.VP",
#     "parent": 209
#   },
#   {
#     "key": 249,
#     "name": "Matthew Patterson",
#     "position": "Executive",
#     "parent": 448
#   },
#   {
#     "key": 250,
#     "name": "Taylor Barnett",
#     "position": "Manager",
#     "parent": 194
#   },
#   {
#     "key": 251,
#     "name": "Stacey Diaz",
#     "position": "COO",
#     "parent": 162
#   },
#   {
#     "key": 252,
#     "name": "Gina Ware",
#     "position": "Executive",
#     "parent": 487
#   },
#   {
#     "key": 253,
#     "name": "Emily Mora",
#     "position": "Sr.GM",
#     "parent": 153
#   },
#   {
#     "key": 254,
#     "name": "Ryan Stokes",
#     "position": "Manager",
#     "parent": 139
#   },
#   {
#     "key": 255,
#     "name": "Chad Olson",
#     "position": "GCCO",
#     "parent": 116
#   },
#   {
#     "key": 257,
#     "name": "Sara Smith",
#     "position": "Executive",
#     "parent": 356
#   },
#   {
#     "key": 258,
#     "name": "Jacob Frank",
#     "position": "CTO",
#     "parent": 186
#   },
#   {
#     "key": 259,
#     "name": "Mrs. Meghan Wells",
#     "position": "GCFO",
#     "parent": 339
#   },
#   {
#     "key": 260,
#     "name": "Sarah James",
#     "position": "GCFO",
#     "parent": 208
#   },
#   {
#     "key": 261,
#     "name": "Anna Young",
#     "position": "Deputy.GM",
#     "parent": 432
#   },
#   {
#     "key": 262,
#     "name": "Aaron Gray",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 263,
#     "name": "Debra Henry",
#     "position": "CTO",
#     "parent": 179
#   },
#   {
#     "key": 264,
#     "name": "Melissa Whitaker",
#     "position": "GCCO",
#     "parent": 362
#   },
#   {
#     "key": 265,
#     "name": "Thomas Huang",
#     "position": "CMO",
#     "parent": 316
#   },
#   {
#     "key": 266,
#     "name": "Collin Harrison",
#     "position": "CMO",
#     "parent": 60
#   },
#   {
#     "key": 267,
#     "name": "Michelle Murray",
#     "position": "GM",
#     "parent": 317
#   },
#   {
#     "key": 268,
#     "name": "Jack Roberts",
#     "position": "Executive",
#     "parent": 335
#   },
#   {
#     "key": 270,
#     "name": "Alexandra Martinez",
#     "position": "Sr.Manager",
#     "parent": 521
#   },
#   {
#     "key": 271,
#     "name": "Shawn Turner",
#     "position": "Associate VP",
#     "parent": 482
#   },
#   {
#     "key": 272,
#     "name": "Michael Smith",
#     "position": "COO",
#     "parent": 50
#   },
#   {
#     "key": 274,
#     "name": "John Hood",
#     "position": "CTO",
#     "parent": 479
#   },
#   {
#     "key": 275,
#     "name": "Christina Walsh",
#     "position": "Sr.VP",
#     "parent": 437
#   },
#   {
#     "key": 276,
#     "name": "John Delacruz",
#     "position": "Executive",
#     "parent": 448
#   },
#   {
#     "key": 277,
#     "name": "Rhonda Richardson",
#     "position": "Sr.Analyst",
#     "parent": 37
#   },
#   {
#     "key": 278,
#     "name": "Theresa Baker",
#     "position": "Executive",
#     "parent": 131
#   },
#   {
#     "key": 279,
#     "name": "Allison Ross",
#     "position": "CMO",
#     "parent": 220
#   },
#   {
#     "key": 280,
#     "name": "James Lucero",
#     "position": "Sr.Executive",
#     "parent": 14
#   },
#   {
#     "key": 281,
#     "name": "Kristopher Schultz",
#     "position": "COO",
#     "parent": 74
#   },
#   {
#     "key": 282,
#     "name": "Christopher Massey",
#     "position": "Deputy.GM",
#     "parent": 204
#   },
#   {
#     "key": 283,
#     "name": "Margaret Cain",
#     "position": "CTO",
#     "parent": 74
#   },
#   {
#     "key": 284,
#     "name": "Brandi Miller",
#     "position": "Sr.VP",
#     "parent": 431
#   },
#   {
#     "key": 285,
#     "name": "Justin Lopez",
#     "position": "Sr.Analyst",
#     "parent": 104
#   },
#   {
#     "key": 286,
#     "name": "Amber Martin",
#     "position": "Sr.VP",
#     "parent": 134
#   },
#   {
#     "key": 287,
#     "name": "Courtney Holt",
#     "position": "GM",
#     "parent": 24
#   },
#   {
#     "key": 288,
#     "name": "Amy Conner",
#     "position": "President",
#     "parent": 478
#   },
#   {
#     "key": 289,
#     "name": "Tina Dalton",
#     "position": "Sr.Executive",
#     "parent": 477
#   },
#   {
#     "key": 290,
#     "name": "Mr. Alan Johnston",
#     "position": "President",
#     "parent": 497
#   },
#   {
#     "key": 291,
#     "name": "Mark Fernandez",
#     "position": "Sr.Analyst",
#     "parent": 135
#   },
#   {
#     "key": 292,
#     "name": "Joseph Gallagher",
#     "position": "GCPEO",
#     "parent": 479
#   },
#   {
#     "key": 293,
#     "name": "Danny Jones",
#     "position": "GCPEO",
#     "parent": 479
#   },
#   {
#     "key": 294,
#     "name": "Jocelyn Orr",
#     "position": "GCPEO",
#     "parent": 95
#   },
#   {
#     "key": 295,
#     "name": "Connie Giles",
#     "position": "GCPEO",
#     "parent": 94
#   },
#   {
#     "key": 296,
#     "name": "Joel Lang",
#     "position": "GCPEO",
#     "parent": 116
#   },
#   {
#     "key": 297,
#     "name": "Jessica Juarez",
#     "position": "Sr.VP",
#     "parent": 212
#   },
#   {
#     "key": 298,
#     "name": "Kimberly Kim",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 299,
#     "name": "Allison Rose",
#     "position": "GM",
#     "parent": 557
#   },
#   {
#     "key": 300,
#     "name": "Daniel Black",
#     "position": "GCCO",
#     "parent": 549
#   },
#   {
#     "key": 301,
#     "name": "John Reeves",
#     "position": "COO",
#     "parent": 50
#   },
#   {
#     "key": 302,
#     "name": "Nathan Lee",
#     "position": "Sr.Executive",
#     "parent": 306
#   },
#   {
#     "key": 303,
#     "name": "Cheryl Myers",
#     "position": "CTO",
#     "parent": 94
#   },
#   {
#     "key": 304,
#     "name": "Desiree Hall",
#     "position": "Sr.Analyst",
#     "parent": 175
#   },
#   {
#     "key": 305,
#     "name": "Jeffrey Zamora",
#     "position": "Sr.Analyst",
#     "parent": 104
#   },
#   {
#     "key": 306,
#     "name": "Mark Yang",
#     "position": "Manager",
#     "parent": 22
#   },
#   {
#     "key": 307,
#     "name": "Molly Copeland",
#     "position": "Deputy.GM",
#     "parent": 504
#   },
#   {
#     "key": 308,
#     "name": "David Salazar",
#     "position": "GCCO",
#     "parent": 93
#   },
#   {
#     "key": 309,
#     "name": "Sarah Smith",
#     "position": "President",
#     "parent": 74
#   },
#   {
#     "key": 310,
#     "name": "Kim Meza",
#     "position": "CMO",
#     "parent": 362
#   },
#   {
#     "key": 311,
#     "name": "Mr. Richard Hall",
#     "position": "Associate VP",
#     "parent": 13
#   },
#   {
#     "key": 312,
#     "name": "Jacob Brown",
#     "position": "GM",
#     "parent": 186
#   },
#   {
#     "key": 313,
#     "name": "Edgar Bush",
#     "position": "COO",
#     "parent": 96
#   },
#   {
#     "key": 314,
#     "name": "Jenny Huynh",
#     "position": "Sr.GM",
#     "parent": 370
#   },
#   {
#     "key": 315,
#     "name": "Michael Blackwell",
#     "position": "CMO",
#     "parent": 444
#   },
#   {
#     "key": 316,
#     "name": "Kathy Hines",
#     "position": "CEO",
#     "parent": 390
#   },
#   {
#     "key": 317,
#     "name": "Kayla Gomez",
#     "position": "Sr.GM",
#     "parent": 523
#   },
#   {
#     "key": 318,
#     "name": "Barbara Hansen",
#     "position": "Sr.GM",
#     "parent": 120
#   },
#   {
#     "key": 319,
#     "name": "Gina Griffith",
#     "position": "Sr.Manager",
#     "parent": 191
#   },
#   {
#     "key": 320,
#     "name": "Aaron Morrison",
#     "position": "GCPEO",
#     "parent": 93
#   },
#   {
#     "key": 321,
#     "name": "Heather Barnett",
#     "position": "Manager",
#     "parent": 403
#   },
#   {
#     "key": 322,
#     "name": "Mike Johnson",
#     "position": "Analyst",
#     "parent": 88
#   },
#   {
#     "key": 323,
#     "name": "Loretta Martin",
#     "position": "Sr.GM",
#     "parent": 480
#   },
#   {
#     "key": 324,
#     "name": "David Velasquez",
#     "position": "Sr.Analyst",
#     "parent": 173
#   },
#   {
#     "key": 325,
#     "name": "Kimberly Walker",
#     "position": "Deputy.GM",
#     "parent": 388
#   },
#   {
#     "key": 326,
#     "name": "Chad Yu",
#     "position": "Executive",
#     "parent": 358
#   },
#   {
#     "key": 327,
#     "name": "Cristian Thomas",
#     "position": "Analyst",
#     "parent": 224
#   },
#   {
#     "key": 328,
#     "name": "Nicholas Novak",
#     "position": "CEO",
#     "parent": 122
#   },
#   {
#     "key": 329,
#     "name": "Dillon Hunt",
#     "position": "GM",
#     "parent": 26
#   },
#   {
#     "key": 330,
#     "name": "Taylor Gonzalez MD",
#     "position": "GCCO",
#     "parent": 116
#   },
#   {
#     "key": 331,
#     "name": "Anna Hendricks",
#     "position": "Sr.VP",
#     "parent": 424
#   },
#   {
#     "key": 332,
#     "name": "Linda Johnson",
#     "position": "COO",
#     "parent": 74
#   },
#   {
#     "key": 333,
#     "name": "Andre Turner",
#     "position": "Sr.Analyst",
#     "parent": 477
#   },
#   {
#     "key": 334,
#     "name": "Heather Hoover",
#     "position": "Sr.VP",
#     "parent": 111
#   },
#   {
#     "key": 335,
#     "name": "Linda Anderson",
#     "position": "Sr.Executive",
#     "parent": 464
#   },
#   {
#     "key": 337,
#     "name": "Sabrina Thomas",
#     "position": "Deputy.GM",
#     "parent": 299
#   },
#   {
#     "key": 338,
#     "name": "Antonio Hughes",
#     "position": "GCPEO",
#     "parent": 169
#   },
#   {
#     "key": 339,
#     "name": "Jimmy Day",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 340,
#     "name": "Christine Saunders",
#     "position": "CMO",
#     "parent": 128
#   },
#   {
#     "key": 341,
#     "name": "Jared Turner",
#     "position": "COO",
#     "parent": 186
#   },
#   {
#     "key": 342,
#     "name": "Gregory Dalton",
#     "position": "GCCO",
#     "parent": 170
#   },
#   {
#     "key": 343,
#     "name": "Michael Wagner",
#     "position": "GCCO",
#     "parent": 170
#   },
#   {
#     "key": 344,
#     "name": "Angela Hughes",
#     "position": "Sr.VP",
#     "parent": 182
#   },
#   {
#     "key": 346,
#     "name": "Bianca Jackson",
#     "position": "GCPEO",
#     "parent": 179
#   },
#   {
#     "key": 347,
#     "name": "Keith Russo",
#     "position": "Executive",
#     "parent": 358
#   },
#   {
#     "key": 348,
#     "name": "Meagan Murphy",
#     "position": "GCCO",
#     "parent": 93
#   },
#   {
#     "key": 349,
#     "name": "Anthony Reilly",
#     "position": "Analyst",
#     "parent": 411
#   },
#   {
#     "key": 350,
#     "name": "Ricky Mejia",
#     "position": "GCPEO",
#     "parent": 74
#   },
#   {
#     "key": 351,
#     "name": "Cynthia Perry",
#     "position": "GCPEO",
#     "parent": 74
#   },
#   {
#     "key": 352,
#     "name": "Chloe King",
#     "position": "Sr.Analyst",
#     "parent": 18
#   },
#   {
#     "key": 353,
#     "name": "Scott Klein",
#     "position": "Deputy.GM",
#     "parent": 388
#   },
#   {
#     "key": 354,
#     "name": "Michael Gonzalez",
#     "position": "VP",
#     "parent": 178
#   },
#   {
#     "key": 355,
#     "name": "Hannah Barajas",
#     "position": "GM",
#     "parent": 362
#   },
#   {
#     "key": 356,
#     "name": "Kenneth Brown",
#     "position": "Sr.Executive",
#     "parent": 449
#   },
#   {
#     "key": 357,
#     "name": "Jacob Jones",
#     "position": "CEO",
#     "parent": 216
#   },
#   {
#     "key": 358,
#     "name": "Scott Mann",
#     "position": "Sr.Executive",
#     "parent": 155
#   },
#   {
#     "key": 359,
#     "name": "Brandy Wiley",
#     "position": "GCCO",
#     "parent": 186
#   },
#   {
#     "key": 360,
#     "name": "Teresa Adams",
#     "position": "President",
#     "parent": 316
#   },
#   {
#     "key": 361,
#     "name": "Brittany Manning",
#     "position": "CMO",
#     "parent": 230
#   },
#   {
#     "key": 362,
#     "name": "Savannah Mills",
#     "position": "CEO",
#     "parent": 509
#   },
#   {
#     "key": 363,
#     "name": "Gina Page",
#     "position": "Analyst",
#     "parent": 519
#   },
#   {
#     "key": 364,
#     "name": "Sandra Williams",
#     "position": "GCFO",
#     "parent": 213
#   },
#   {
#     "key": 365,
#     "name": "Kayla Powell",
#     "position": "Analyst",
#     "parent": 285
#   },
#   {
#     "key": 366,
#     "name": "Tracey Roberts",
#     "position": "Sr.Analyst",
#     "parent": 306
#   },
#   {
#     "key": 367,
#     "name": "Michael Lee",
#     "position": "GCCO",
#     "parent": 128
#   },
#   {
#     "key": 368,
#     "name": "Matthew Doyle",
#     "position": "Sr.VP",
#     "parent": 290
#   },
#   {
#     "key": 369,
#     "name": "Melinda Walker",
#     "position": "Executive",
#     "parent": 112
#   },
#   {
#     "key": 370,
#     "name": "Dr. Taylor Lee",
#     "position": "VP",
#     "parent": 309
#   },
#   {
#     "key": 371,
#     "name": "Timothy Wood",
#     "position": "President",
#     "parent": 94
#   },
#   {
#     "key": 372,
#     "name": "Melissa Martinez",
#     "position": "Manager",
#     "parent": 270
#   },
#   {
#     "key": 373,
#     "name": "Tamara Perry",
#     "position": "Analyst",
#     "parent": 285
#   },
#   {
#     "key": 374,
#     "name": "Jonathan Harris",
#     "position": "GCFO",
#     "parent": 137
#   },
#   {
#     "key": 376,
#     "name": "Tiffany Leblanc",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 377,
#     "name": "Sarah Mills",
#     "position": "Analyst",
#     "parent": 459
#   },
#   {
#     "key": 378,
#     "name": "Rebekah Kirk",
#     "position": "Sr.Manager",
#     "parent": 521
#   },
#   {
#     "key": 379,
#     "name": "Gregg Long",
#     "position": "CTO",
#     "parent": 478
#   },
#   {
#     "key": 380,
#     "name": "Danielle Acosta",
#     "position": "CMO",
#     "parent": 413
#   },
#   {
#     "key": 381,
#     "name": "Joseph Cole",
#     "position": "COO",
#     "parent": 230
#   },
#   {
#     "key": 382,
#     "name": "Shelley Jones",
#     "position": "Deputy.GM",
#     "parent": 267
#   },
#   {
#     "key": 383,
#     "name": "Meghan Bell",
#     "position": "Sr.VP",
#     "parent": 239
#   },
#   {
#     "key": 384,
#     "name": "Daniel Vincent",
#     "position": "Analyst",
#     "parent": 79
#   },
#   {
#     "key": 385,
#     "name": "Gregory Walker",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 386,
#     "name": "Matthew Short",
#     "position": "CTO",
#     "parent": 218
#   },
#   {
#     "key": 387,
#     "name": "April Lee",
#     "position": "VP",
#     "parent": 54
#   },
#   {
#     "key": 388,
#     "name": "Katherine Henderson",
#     "position": "GM",
#     "parent": 420
#   },
#   {
#     "key": 389,
#     "name": "Stephanie Pitts",
#     "position": "Analyst",
#     "parent": 450
#   },
#   {
#     "key": 390,
#     "name": "Christopher Hammond",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 391,
#     "name": "Alexander Barnes",
#     "position": "Sr.GM",
#     "parent": 503
#   },
#   {
#     "key": 392,
#     "name": "Sean Kennedy",
#     "position": "GM",
#     "parent": 210
#   },
#   {
#     "key": 393,
#     "name": "William Jones",
#     "position": "COO",
#     "parent": 220
#   },
#   {
#     "key": 394,
#     "name": "Todd Perez",
#     "position": "Sr.VP",
#     "parent": 178
#   },
#   {
#     "key": 395,
#     "name": "Patrick Nolan",
#     "position": "GCFO",
#     "parent": 96
#   },
#   {
#     "key": 396,
#     "name": "Timothy Hansen",
#     "position": "Executive",
#     "parent": 112
#   },
#   {
#     "key": 397,
#     "name": "Johnny Miller",
#     "position": "VP",
#     "parent": 309
#   },
#   {
#     "key": 398,
#     "name": "Paul Allen",
#     "position": "GCPEO",
#     "parent": 50
#   },
#   {
#     "key": 399,
#     "name": "Tyler Miller",
#     "position": "President",
#     "parent": 169
#   },
#   {
#     "key": 400,
#     "name": "Joseph Lee",
#     "position": "Analyst",
#     "parent": 79
#   },
#   {
#     "key": 401,
#     "name": "Cassandra Adams",
#     "position": "Analyst",
#     "parent": 526
#   },
#   {
#     "key": 402,
#     "name": "Anthony Kelly",
#     "position": "Deputy.GM",
#     "parent": 299
#   },
#   {
#     "key": 403,
#     "name": "Stephanie Smith",
#     "position": "Sr.Manager",
#     "parent": 325
#   },
#   {
#     "key": 404,
#     "name": "Jon Taylor",
#     "position": "CTO",
#     "parent": 230
#   },
#   {
#     "key": 405,
#     "name": "Monique Obrien",
#     "position": "GCFO",
#     "parent": 316
#   },
#   {
#     "key": 406,
#     "name": "Jason Young",
#     "position": "GCFO",
#     "parent": 186
#   },
#   {
#     "key": 407,
#     "name": "Ronnie Thompson",
#     "position": "Sr.VP",
#     "parent": 512
#   },
#   {
#     "key": 408,
#     "name": "Daniel Hughes",
#     "position": "CMO",
#     "parent": 218
#   },
#   {
#     "key": 409,
#     "name": "Adam Combs",
#     "position": "CTO",
#     "parent": 95
#   },
#   {
#     "key": 410,
#     "name": "Carolyn Whitehead",
#     "position": "GCCO",
#     "parent": 186
#   },
#   {
#     "key": 411,
#     "name": "Bradley Gardner",
#     "position": "Sr.Analyst",
#     "parent": 64
#   },
#   {
#     "key": 412,
#     "name": "Rebecca Ward",
#     "position": "Sr.GM",
#     "parent": 430
#   },
#   {
#     "key": 413,
#     "name": "Alexis Perry",
#     "position": "CEO",
#     "parent": 129
#   },
#   {
#     "key": 414,
#     "name": "Shawn Allen",
#     "position": "COO",
#     "parent": 478
#   },
#   {
#     "key": 415,
#     "name": "Joseph Marshall",
#     "position": "Deputy.GM",
#     "parent": 392
#   },
#   {
#     "key": 416,
#     "name": "Christian Barton",
#     "position": "GCCO",
#     "parent": 116
#   },
#   {
#     "key": 417,
#     "name": "Eric Wilson",
#     "position": "COO",
#     "parent": 422
#   },
#   {
#     "key": 418,
#     "name": "Ryan Campos",
#     "position": "Executive",
#     "parent": 112
#   },
#   {
#     "key": 419,
#     "name": "Kerry Clark",
#     "position": "Sr.Analyst",
#     "parent": 101
#   },
#   {
#     "key": 420,
#     "name": "Sharon Cooper",
#     "position": "Sr.GM",
#     "parent": 53
#   },
#   {
#     "key": 422,
#     "name": "Ricardo Bailey",
#     "position": "CEO",
#     "parent": 339
#   },
#   {
#     "key": 423,
#     "name": "Michelle Mccormick",
#     "position": "GCCO",
#     "parent": 94
#   },
#   {
#     "key": 424,
#     "name": "Katie Miller",
#     "position": "GCFO",
#     "parent": 362
#   },
#   {
#     "key": 425,
#     "name": "Matthew Long",
#     "position": "Associate VP",
#     "parent": 267
#   },
#   {
#     "key": 426,
#     "name": "Carmen Griffin",
#     "position": "Associate VP",
#     "parent": 36
#   },
#   {
#     "key": 428,
#     "name": "Laura Hatfield",
#     "position": "Sr.Manager",
#     "parent": 240
#   },
#   {
#     "key": 429,
#     "name": "Kristy Faulkner",
#     "position": "CMO",
#     "parent": 93
#   },
#   {
#     "key": 430,
#     "name": "Kimberly Woodward",
#     "position": "VP",
#     "parent": 57
#   },
#   {
#     "key": 431,
#     "name": "Christopher Elliott",
#     "position": "GCCO",
#     "parent": 497
#   },
#   {
#     "key": 432,
#     "name": "Stephanie Davis",
#     "position": "GM",
#     "parent": 183
#   },
#   {
#     "key": 433,
#     "name": "Michael Hall",
#     "position": "Sr.Analyst",
#     "parent": 155
#   },
#   {
#     "key": 434,
#     "name": "Brian Martinez",
#     "position": "Deputy.GM",
#     "parent": 329
#   },
#   {
#     "key": 435,
#     "name": "Mark Rodriguez",
#     "position": "Sr.Manager",
#     "parent": 337
#   },
#   {
#     "key": 436,
#     "name": "Christina King",
#     "position": "COO",
#     "parent": 170
#   },
#   {
#     "key": 437,
#     "name": "Laura Floyd",
#     "position": "GCCO",
#     "parent": 128
#   },
#   {
#     "key": 438,
#     "name": "Benjamin Pena",
#     "position": "Deputy.GM",
#     "parent": 432
#   },
#   {
#     "key": 439,
#     "name": "Scott Anderson",
#     "position": "Analyst",
#     "parent": 526
#   },
#   {
#     "key": 440,
#     "name": "Russell Phillips",
#     "position": "GM",
#     "parent": 179
#   },
#   {
#     "key": 441,
#     "name": "Tracy Sanchez",
#     "position": "VP",
#     "parent": 178
#   },
#   {
#     "key": 442,
#     "name": "John Jackson",
#     "position": "Manager",
#     "parent": 39
#   },
#   {
#     "key": 443,
#     "name": "Jeffrey Andrews",
#     "position": "GCCO",
#     "parent": 50
#   },
#   {
#     "key": 444,
#     "name": "Alicia Lynn",
#     "position": "CEO",
#     "parent": 216
#   },
#   {
#     "key": 445,
#     "name": "Jennifer Allen",
#     "position": "Sr.Analyst",
#     "parent": 135
#   },
#   {
#     "key": 446,
#     "name": "Rebecca Hughes",
#     "position": "Executive",
#     "parent": 448
#   },

#   {
#     "key": 448,
#     "name": "Elizabeth Richardson",
#     "position": "Sr.Executive",
#     "parent": 516
#   },
#   {
#     "key": 449,
#     "name": "Michael Davis",
#     "position": "Manager",
#     "parent": 522
#   },
#   {
#     "key": 450,
#     "name": "Douglas Hughes",
#     "position": "Sr.Analyst",
#     "parent": 306
#   },
#   {
#     "key": 451,
#     "name": "Amanda Hawkins",
#     "position": "CMO",
#     "parent": 479
#   },
#   {
#     "key": 452,
#     "name": "Veronica Holt",
#     "position": "Associate VP",
#     "parent": 355
#   },
#   {
#     "key": 453,
#     "name": "Andrew Byrd",
#     "position": "CTO",
#     "parent": 444
#   },
#   {
#     "key": 454,
#     "name": "Sarah Hudson",
#     "position": "GCFO",
#     "parent": 61
#   },
#   {
#     "key": 455,
#     "name": "Benjamin Harris",
#     "position": "Analyst",
#     "parent": 304
#   },
#   {
#     "key": 456,
#     "name": "Sandra Golden",
#     "position": "COO",
#     "parent": 220
#   },
#   {
#     "key": 457,
#     "name": "Deborah Dawson",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 458,
#     "name": "Tracy Marquez",
#     "position": "Sr.VP",
#     "parent": 395
#   },
#   {
#     "key": 459,
#     "name": "Julia Gilbert",
#     "position": "Sr.Analyst",
#     "parent": 555
#   },
#   {
#     "key": 460,
#     "name": "James Villegas",
#     "position": "Associate VP",
#     "parent": 13
#   },
#   {
#     "key": 461,
#     "name": "Gabriel Smith",
#     "position": "Associate VP",
#     "parent": 486
#   },
#   {
#     "key": 462,
#     "name": "Matthew Stewart",
#     "position": "Sr.Analyst",
#     "parent": 250
#   },
#   {
#     "key": 463,
#     "name": "Ashley Garrett",
#     "position": "Analyst",
#     "parent": 304
#   },
#   {
#     "key": 464,
#     "name": "Kristin Allen",
#     "position": "Manager",
#     "parent": 188
#   },
#   {
#     "key": 465,
#     "name": "Anthony Hernandez",
#     "position": "Sr.VP",
#     "parent": 110
#   },
#   {
#     "key": 466,
#     "name": "Charles Fuentes",
#     "position": "Executive",
#     "parent": 448
#   },
#   {
#     "key": 467,
#     "name": "Franklin Thomas",
#     "position": "GCFO",
#     "parent": 129
#   },
#   {
#     "key": 468,
#     "name": "Juan Perez",
#     "position": "Sr.Executive",
#     "parent": 306
#   },
#   {
#     "key": 469,
#     "name": "Howard Hansen",
#     "position": "GCPEO",
#     "parent": 478
#   },
#   {
#     "key": 470,
#     "name": "Sarah Lopez",
#     "position": "Sr.VP",
#     "parent": 367
#   },
#   {
#     "key": 471,
#     "name": "Leslie Dyer",
#     "position": "Sr.GM",
#     "parent": 332
#   },
#   {
#     "key": 472,
#     "name": "Mark Morgan",
#     "position": "Manager",
#     "parent": 543
#   },
#   {
#     "key": 473,
#     "name": "John Lang",
#     "position": "Analyst",
#     "parent": 366
#   },
#   {
#     "key": 474,
#     "name": "Steven Cox",
#     "position": "Deputy.GM",
#     "parent": 287
#   },
#   {
#     "key": 475,
#     "name": "Jeff Case",
#     "position": "Analyst",
#     "parent": 526
#   },
#   {
#     "key": 476,
#     "name": "Robert Owens",
#     "position": "Sr.Manager",
#     "parent": 337
#   },
#   {
#     "key": 477,
#     "name": "Mary Wong",
#     "position": "Manager",
#     "parent": 22
#   },
#   {
#     "key": 478,
#     "name": "Elizabeth Wong",
#     "position": "CEO",
#     "parent": 213
#   },
#   {
#     "key": 479,
#     "name": "Latoya Rice",
#     "position": "CEO",
#     "parent": 385
#   },
#   {
#     "key": 480,
#     "name": "Mallory Decker MD",
#     "position": "COO",
#     "parent": 128
#   },
#   {
#     "key": 481,
#     "name": "Tammy Wright",
#     "position": "CTO",
#     "parent": 422
#   },
#   {
#     "key": 482,
#     "name": "Andrew Jenkins",
#     "position": "GM",
#     "parent": 253
#   },
#   {
#     "key": 483,
#     "name": "Karen Cox",
#     "position": "Manager",
#     "parent": 39
#   },
#   {
#     "key": 484,
#     "name": "Kimberly Mitchell",
#     "position": "GCCO",
#     "parent": 328
#   },
#   {
#     "key": 485,
#     "name": "Tiffany Glenn",
#     "position": "GCCO",
#     "parent": 218
#   },
#   {
#     "key": 486,
#     "name": "Shane Hampton",
#     "position": "GM",
#     "parent": 412
#   },
#   {
#     "key": 487,
#     "name": "Dorothy Mcgee",
#     "position": "Sr.Executive",
#     "parent": 483
#   },
#   {
#     "key": 488,
#     "name": "Tiffany Lewis",
#     "position": "GCCO",
#     "parent": 74
#   },
#   {
#     "key": 489,
#     "name": "Ann Smith",
#     "position": "GCFO",
#     "parent": 94
#   },
#   {
#     "key": 490,
#     "name": "Maria Armstrong",
#     "position": "VP",
#     "parent": 58
#   },
#   {
#     "key": 491,
#     "name": "Nathan Phillips",
#     "position": "Sr.Executive",
#     "parent": 14
#   },
#   {
#     "key": 492,
#     "name": "Jasmine Porter",
#     "position": "VP",
#     "parent": 288
#   },
#   {
#     "key": 493,
#     "name": "Abigail Moore",
#     "position": "Deputy.GM",
#     "parent": 482
#   },
#   {
#     "key": 494,
#     "name": "Maria Harrison",
#     "position": "GCCO",
#     "parent": 179
#   },
#   {
#     "key": 495,
#     "name": "Bradley Wagner",
#     "position": "Sr.Analyst",
#     "parent": 321
#   },
#   {
#     "key": 496,
#     "name": "Anthony Hines",
#     "position": "President",
#     "parent": 128
#   },
#   {
#     "key": 497,
#     "name": "Evan Newman",
#     "position": "CEO",
#     "parent": 137
#   },
#   {
#     "key": 498,
#     "name": "Yvonne Freeman",
#     "position": "Manager",
#     "parent": 126
#   },
#   {
#     "key": 499,
#     "name": "Chad Ferguson",
#     "position": "Deputy.GM",
#     "parent": 13
#   },
#   {
#     "key": 500,
#     "name": "Maria Smith",
#     "position": "COO",
#     "parent": 218
#   },
#   {
#     "key": 501,
#     "name": "Robert Mccall",
#     "position": "President",
#     "parent": 497
#   },
#   {
#     "key": 502,
#     "name": "Robert Simpson",
#     "position": "President",
#     "parent": 444
#   },
#   {
#     "key": 503,
#     "name": "Michael Nash",
#     "position": "VP",
#     "parent": 187
#   },
#   {
#     "key": 504,
#     "name": "Mr. Gary Stephens",
#     "position": "GM",
#     "parent": 186
#   },
#   {
#     "key": 505,
#     "name": "Louis Randall",
#     "position": "Sr.VP",
#     "parent": 212
#   },
#   {
#     "key": 506,
#     "name": "Anthony Martinez",
#     "position": "CTO",
#     "parent": 328
#   },
#   {
#     "key": 507,
#     "name": "Katherine Hopkins",
#     "position": "COO",
#     "parent": 497
#   },
#   {
#     "key": 508,
#     "name": "Christopher Ward",
#     "position": "Sr.Executive",
#     "parent": 516
#   },
#   {
#     "key": 509,
#     "name": "Mia Buckley",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 510,
#     "name": "Miss Patricia York MD",
#     "position": "Sr.Analyst",
#     "parent": 102
#   },
#   {
#     "key": 511,
#     "name": "Kelli Hernandez",
#     "position": "Sr.GM",
#     "parent": 441
#   },
#   {
#     "key": 512,
#     "name": "Cindy Cross",
#     "position": "President",
#     "parent": 230
#   },
#   {
#     "key": 513,
#     "name": "Amy Williams",
#     "position": "Sr.Executive",
#     "parent": 372
#   },
#   {
#     "key": 514,
#     "name": "Ms. Angela James",
#     "position": "Sr.VP",
#     "parent": 405
#   },
#   {
#     "key": 515,
#     "name": "Christopher Scott",
#     "position": "GCPEO",
#     "parent": 328
#   },
#   {
#     "key": 516,
#     "name": "Kathy Bowen",
#     "position": "Manager",
#     "parent": 543
#   },
#   {
#     "key": 517,
#     "name": "Taylor Ellison",
#     "position": "CTO",
#     "parent": 94
#   },
#   {
#     "key": 518,
#     "name": "Mary Guzman",
#     "position": "Associate VP",
#     "parent": 243
#   },
#   {
#     "key": 519,
#     "name": "Jeffrey Wong DVM",
#     "position": "Sr.Analyst",
#     "parent": 143
#   },
#   {
#     "key": 520,
#     "name": "Shelby Kelley",
#     "position": "GCPEO",
#     "parent": 422
#   },
#   {
#     "key": 521,
#     "name": "Laura Hughes",
#     "position": "Deputy.GM",
#     "parent": 204
#   },
#   {
#     "key": 522,
#     "name": "Eric Steele",
#     "position": "Sr.Manager",
#     "parent": 474
#   },
#   {
#     "key": 523,
#     "name": "Alexa Johnson",
#     "position": "COO",
#     "parent": 50
#   },
#   {
#     "key": 524,
#     "name": "Faith Ramos",
#     "position": "Associate VP",
#     "parent": 267
#   },
#   {
#     "key": 525,
#     "name": "Steven Adams",
#     "position": "GCFO",
#     "parent": 216
#   },
#   {
#     "key": 526,
#     "name": "William Mercer",
#     "position": "Sr.Analyst",
#     "parent": 254
#   },
#   {
#     "key": 527,
#     "name": "Tina Cruz",
#     "position": "Manager",
#     "parent": 378
#   },
#   {
#     "key": 528,
#     "name": "William Park",
#     "position": "CMO",
#     "parent": 116
#   },
#   {
#     "key": 529,
#     "name": "Kenneth Salazar",
#     "position": "Associate VP",
#     "parent": 388
#   },
#   {
#     "key": 530,
#     "name": "Brandy Moore",
#     "position": "CTO",
#     "parent": 497
#   },
#   {
#     "key": 531,
#     "name": "Jack Moore",
#     "position": "GM",
#     "parent": 245
#   },
#   {
#     "key": 532,
#     "name": "Christina Hays",
#     "position": "VP",
#     "parent": 134
#   },
#   {
#     "key": 533,
#     "name": "Diane Munoz",
#     "position": "CTO",
#     "parent": 74
#   },
#   {
#     "key": 534,
#     "name": "Jill Torres",
#     "position": "GCPEO",
#     "parent": 116
#   },
#   {
#     "key": 535,
#     "name": "Deborah Gregory",
#     "position": "GCFO",
#     "parent": 170
#   },
#   {
#     "key": 536,
#     "name": "Colin Robertson",
#     "position": "GCFO",
#     "parent": 547
#   },
#   {
#     "key": 537,
#     "name": "Morgan Beck",
#     "position": "VP",
#     "parent": 290
#   },
#   {
#     "key": 538,
#     "name": "Caitlin Gonzales",
#     "position": "Deputy.GM",
#     "parent": 329
#   },
#   {
#     "key": 539,
#     "name": "William Hayes",
#     "position": "Analyst",
#     "parent": 285
#   },
#   {
#     "key": 540,
#     "name": "Gabriel Thomas",
#     "position": "Sr.VP",
#     "parent": 290
#   },
#   {
#     "key": 541,
#     "name": "Charles Perkins",
#     "position": "GCPEO",
#     "parent": 549
#   },
#   {
#     "key": 542,
#     "name": "Ryan Gonzalez",
#     "position": "GCPEO",
#     "parent": 95
#   },
#   {
#     "key": 543,
#     "name": "Charles Sullivan",
#     "position": "Sr.Manager",
#     "parent": 353
#   },
#   {
#     "key": 544,
#     "name": "Fernando Gonzalez",
#     "position": "VP",
#     "parent": 209
#   },
#   {
#     "key": 545,
#     "name": "Jesus Smith",
#     "position": "Deputy.GM",
#     "parent": 243
#   },
#   {
#     "key": 546,
#     "name": "Cory Bell",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 547,
#     "name": "Gene Johnson",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 548,
#     "name": "Rachel Fletcher",
#     "position": "COO",
#     "parent": 362
#   },
#   {
#     "key": 549,
#     "name": "Joshua Garcia",
#     "position": "CEO",
#     "parent": 298
#   },
#   {
#     "key": 550,
#     "name": "Diana Gonzales",
#     "position": "Executive",
#     "parent": 468
#   },
#   {
#     "key": 551,
#     "name": "Samantha Holt",
#     "position": "Sr.Executive",
#     "parent": 143
#   },
#   {
#     "key": 552,
#     "name": "Margaret Gibson",
#     "position": "GCFO",
#     "parent": 262
#   },
#   {
#     "key": 553,
#     "name": "Victor Baker",
#     "position": "GCEO",
#     "parent": 7
#   },
#   {
#     "key": 554,
#     "name": "Charlotte Harris",
#     "position": "Sr.Manager",
#     "parent": 198
#   },
#   {
#     "key": 555,
#     "name": "Kara Jones",
#     "position": "Manager",
#     "parent": 139
#   },
#   {
#     "key": 556,
#     "name": "Elizabeth Smith",
#     "position": "Sr.Executive",
#     "parent": 372
#   },
#   {
#     "key": 557,
#     "name": "Craig Andrews",
#     "position": "Sr.GM",
#     "parent": 158
#   },
#   {
#     "key": 558,
#     "name": "Courtney Norton",
#     "position": "Analyst",
#     "parent": 291
#   },
#   {
#     "key": 8,
#     "name": "Caroline Miller",
#     "position": "Executive",
#     "parent": 2
#   },
#   {
#     "key": 8,
#     "name": "Caroline Miller",
#     "position": "Executive",
#     "parent": 10
#   },
#   {
#     "key": 8,
#     "name": "Caroline Miller",
#     "position": "Executive",
#     "parent": 15
#   },
#   {
#     "key": 8,
#     "name": "Caroline Miller",
#     "position": "Executive",
#     "parent": 28
#   },
#   {
#     "key": 8,
#     "name": "Caroline Miller",
#     "position": "Executive",
#     "parent": 42
#   }
# ]
  
# Set parent key to "" if it's None
for node in data:
    if node["parent"] is None:
        node["parent"] = ""  
      
# Flask app
def get_children_count(parent_id):
    return len([node for node in data if node["parent"] == parent_id])
  
# fetch children of a parent node
@app.route('/api/get-children/<int:parent_id>', methods=['GET'])
def get_children(parent_id):
    children = [node for node in data if node["parent"] == parent_id]
 
    # Add childCount to parent node
    for child in children:
        child["childCount"] = get_children_count(child["key"])
        
    return jsonify(children)
        
# fetch top-level nodes
@app.route('/api/get-top-level', methods=['GET'])
def get_top_level():
    top_level_nodes = [node for node in data if node["parent"] == ""]
    
    # Add childCount to top-level nodes
    for node in top_level_nodes:
        node["childCount"] = get_children_count(node["key"])

    return jsonify(top_level_nodes)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
