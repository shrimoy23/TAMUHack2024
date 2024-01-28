import json
parser_schema = {
        "initial_airport" : "The three letter geocode of the airport that is closest to my location.",
        "final_airport" : "The three letter geocode of the airport that is closest to the location I am traveling to.",
        "leave_date" : "The date in which the travelers will leave in the format mm-dd.",
        "arrive_date" : "The date in which the travelers will arrive in the format mm-dd.",
        "seat_quality" : "The seat quality as one of the 4 choices: Economy, Premium Economy, Business, First",
        "activities" : "A singular string consisting of 2 or 3 activities that you will suggest for me based on my initial activity interests.",
        "restaurants" : "A singular string consisting of 2 or 3 restaurants you will suggest for me based on my initial food interests"
    }