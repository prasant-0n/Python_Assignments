# create a list using names of 10 cities and pincodes. Combinethem all to convert it into string using join with delimiter “: ”. Modify the names of
# cities by adding state-cities in the string. Finally split it to have the information in list in the format state-city-pincode
# Input data
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Bengaluru",
          "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow"]
pincodes = [110001, 400001, 600001, 700001,
            560001, 500001, 411001, 380001, 302001, 226001]

# Combine city names and pincodes using a colon delimiter
city_data_str = ":".join(
    [f"{city}-{pincode}" for city, pincode in zip(cities, pincodes)])

# Modify city names by adding state-cities
state_cities = {
    "Delhi": "Delhi-NCR",
    "Mumbai": "Maharashtra-Mumbai",
    "Chennai": "Tamil Nadu-Chennai",
    "Kolkata": "West Bengal-Kolkata",
    "Bengaluru": "Karnataka-Bengaluru",
    "Hyderabad": "Telangana-Hyderabad",
    "Pune": "Maharashtra-Pune",
    "Ahmedabad": "Gujarat-Ahmedabad",
    "Jaipur": "Rajasthan-Jaipur",
    "Lucknow": "Uttar Pradesh-Lucknow"
}

# Split the city data string into a list and modify city names
city_data_list = []
for city_data in city_data_str.split(":"):
    city, pincode = city_data.split("-")
    state_city = state_cities[city]
    city_data_list.append(f"{state_city}-{pincode}")

# Print the final result
print(city_data_list)
