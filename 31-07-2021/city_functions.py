def city_country(city_name, country_name, population=""):
    formatted_city = city_name.title() + ", " + country_name.title()
    if population:
        formatted_city += " - population " + population
    return(formatted_city)
