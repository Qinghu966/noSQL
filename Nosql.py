
import pymongo as pymongo

client = pymongo.MongoClient(
        "mongodb+srv://Qinghua:Ye19960711@cluster0.9wrnz.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
countries = db.countries
continents = db.continents

def print_hi(name):
    print(f'Hi, {name}')

def connectedbd():
    print(db.list_collection_names())

    for country in countries.find():
        print(country['name'])

# 1/ Get all the country where a letter or word given is in the name
def getCountriesByLetter(name):
    query = {
        "name": {
            "$regex": name,
            "$options": "i"
        }
    }
    result = countries.find(query)
    for country in result:
        print(country['name'])

# 3/ Send the list of continents with the number of countries
def getContinentsWithCountriesNumber():
    result = continents.aggregate([{'$project': {'name': 1,
                                                 'NumberOfCountries': {'$size': '$countries'}}}])
    for continent in result:
        print(continent['name'])
        print(continent['NumberOfCountries'])

# 4/ Gets till the 4th country under specified continent ordered by name
def getFourCountries(continent_name):
    query1 = {
            "name": {"$regex": continent_name, "$options": "i"},
    }
    result1 = continents.find_one(query1)
    print("Continent :"+result1['name'])
    print("List of the first four countries:")
    query2 = {"_id": {"$in": result1['countries']}}
    result2 = countries.find(query2).sort("name").limit(4)
    for country in result2:
        print(country['name'])

# 6/ Gets all countries ordered by population in ascending order
def orderByPopulation():
    result = countries.find().sort("population", 1)
    for country in result:
        print(country['name'])

# 7/ Gets countries where population is greater than 100000 and including u in the country name
def populationIsGreaterThan():
    query = {
    "population": {"$gt": 100000},
    "name": {"$regex": "u", "$options": "i"},
    }
    result = countries.find(query)
    for country in result:
        print(country['name'])

if __name__ == '__main__':
    print_hi('PyCharm')
    # connectedbd()
    # getCountriesByLetter("fi")
    #getContinentsWithCountriesNumber()
    #getFourCountries("Europe")
    # orderByPopulation()
    #populationIsGreaterThan()
