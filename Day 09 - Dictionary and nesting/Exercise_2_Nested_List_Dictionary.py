country_capitals = {
    "United States": "Washington D.C.",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
    "China": "Beijing",
    "Japan": "Tokyo"
}

travel_log = {
    "United States" : ["New York", "Miami", "Key West", "San Francisco"]
}
print(travel_log["United States"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log_updated = \
    {
    "India" : [
            {
                "Lived in Cities" : ["Ichalkaranji", "Jaysingpur", "Hyderabad", "Pune"],
                "Years" : [5, 16, 1.5, 3]
            },
            {
                "Visited Cities" : ["Mumbai", "Chennai", "Bangalore / Mangalore"],
                "Days" : [3, 2, 5]
            }
        ],
    "United States" :
        [
            {
                "Lived in Cities" : ["Middle Town, CT", "North Wales, PA", "San Mateo, CA", "Raleigh, NC", "Dublin, Ca",
                                     "Pleasanton, CA"],
                "Years" : [.25, 3, .25, .25, 1.5, 9]
            },
            {
                "Visited Cities" : ["New York City", "New Jersey Cities", "Niagara Falls, PA", "Washington, DC","Miami, FL", "Key West, FL",
                                    "Seattle, WA", "San Diago, CA", "Yosemite, CA", "Lake Tahoe, CA", "Texas Cities"],
                "Days":[5, 5, 5, 5, 2, 1, 15, 5, 4, 3, 10]
            }
        ]
    }

print("I lived in these cities in India")
for city, years in zip(travel_log_updated["India"][0]["Lived in Cities"], travel_log_updated["India"][0]["Years"]):
    print(f"{city} :  {years}")

print("I have lived in following cities in United States")
for city in travel_log_updated["United States"][0]["Lived in Cities"]:
    print(city)

total_us = sum(travel_log_updated["United States"][0]["Years"])
print(f"Total years lived in United States : {total_us}")

total_india = sum(travel_log_updated["India"][0]["Years"])
print(f"Total years lived in India : {total_india}")

print(total_us+total_india)
