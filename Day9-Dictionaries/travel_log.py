travel_log=[{
    "country":"France",
    "Visits":12,
    "cities":["Paris","Lille","Dijoin"]
},
{
    "country":"Germany",
    "visits":5,
    "cities":["Berlin","Hamburg","Stuttgart"]
}]

def travel(country_1,visits_1,cities_1):
    travis={}
    travis["Country"]=country_1
    travis["Visits"]=visits_1
    travis["cities"]=cities_1
    travel_log.append(travis)

travel(country_1="Russia",visits_1=2,cities_1=["Moscow","Saint Petersbugh"])  
print(travel_log)      