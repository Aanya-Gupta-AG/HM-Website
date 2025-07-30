## Part 1 Code Updated

import csv
import requests

class CountryYear:
    def __init__(self, name, country_iso3, year, life_expectancy, gdp_per_capita, population, ref_pop, access_to_elec, prim_schl_enrollment, prim_complete_rate, fert_rate):
        ## Required indicators
        self.name = str(name)
        self.country_iso3 = str(country_iso3)
        self.year = int(year)
        self.life_expectancy = float(life_expectancy)
        self.gdp_per_capita = float(gdp_per_capita)
        self.population = int(population)
        ## My indicators
        self.ref_pop = ref_pop
        self.access_to_elec = access_to_elec
        self.prim_schl_enrollment = prim_schl_enrollment
        self.prim_complete_rate = prim_complete_rate
        self.fert_rate = fert_rate

    def __str__(self):
        return f"{self.name},{self.country_iso3},{self.year},{self.life_expectancy},{self.gdp_per_capita},{self.population},{self.ref_pop},{self.access_to_elec},{self.prim_schl_enrollment},{self.prim_complete_rate},{self.fert_rate}"

    @staticmethod
    def get_world_bank_data(indicator, countries, years):
        data = {country: {year: "" for year in years} for country in countries}
        for country in countries:
            for year in years:
                url = f"http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?date={year}&format=json"
                response = requests.get(url)
                if response.status_code == 200:
                    try:
                        record = response.json()[1][0] 
                        if "value" in record:
                            data[country][year] = record["value"] 
                    except (IndexError, TypeError):
                        pass

        return data

    @classmethod
    def def_cont_yr_objects(cls, countries, years):
        indicators = {
            "life_expectancy": "SP.DYN.LE00.IN",
            "gdp_per_capita": "NY.GDP.PCAP.CD",
            "population": "SP.POP.TOTL",
            "ref_pop": "SM.POP.REFG",
            "access_to_elec": "EG.ELC.ACCS.ZS",
            "prim_schl_enrollment": "SE.PRM.ENRR",
            "prim_complete_rate": "SE.PRM.CMPT.ZS",
            "fert_rate": "SP.ADO.TFRT",
        }

        data_tot = {key: cls.get_world_bank_data(indicator, countries, years) for key, indicator in indicators.items()} ## Source for this line: Chat GPT
                                                                                                                        ## Explanation: This line pairs the indicator name with its API code and creates keys to access the data (based on the indicator) in a new dictionary.

        country_year_objects = []
        for country in countries:
            for year in years:
                country_year = cls(
                    name = country,
                    country_iso3 = country,
                    year = year,
                    life_expectancy = data_tot["life_expectancy"].get(country, {}).get(year, ""), ## Source for this line: https://stackoverflow.com/questions/25833613/safe-method-to-get-value-of-nested-dictionary 
                                                                                                  ## Explanation: This lines pulls data from the nested dictionary created above (returns empty if not possible), and I followed the same structure throughout. 
                    gdp_per_capita = data_tot["gdp_per_capita"].get(country, {}).get(year, ""),
                    population = data_tot["population"].get(country, {}).get(year, ""),
                    ref_pop = data_tot["ref_pop"].get(country, {}).get(year, ""),
                    access_to_elec = data_tot["access_to_elec"].get(country, {}).get(year, ""),
                    prim_schl_enrollment = data_tot["prim_schl_enrollment"].get(country, {}).get(year, ""),
                    prim_complete_rate = data_tot["prim_complete_rate"].get(country, {}).get(year, ""),
                    fert_rate = data_tot["fert_rate"].get(country, {}).get(year, "")
                )
                country_year_objects.append(country_year)
        return country_year_objects

    @staticmethod
    def save_to_csv(country_year_objects, filename):
        headers = ["name", "country_iso3", "year", "life_expectancy", "gdp_per_capita", "population", "ref_pop",
                   "access_to_elec", "prim_schl_enrollment", "prim_complete_rate", "fert_rate"]
        with open(filename, "w") as file:
            writer = csv.writer(file) ## Source for this line: https://www.geeksforgeeks.org/writing-csv-files-in-python/ 
                                      ## Explanation: I used the website to learn about the writer function. 
            writer.writerow(headers)
            for obj in country_year_objects:
                writer.writerow([
                    obj.name, obj.country_iso3, obj.year, obj.life_expectancy, obj.gdp_per_capita, obj.population,
                    obj.ref_pop, obj.access_to_elec, obj.prim_schl_enrollment, obj.prim_complete_rate, obj.fert_rate
                ])

if __name__ == "__main__":
    countries = ["USA", "IND", "NGA", "BGD", "ARG", "KEN", "PAN", "CRI", "SEN"]
    years = range(2000, 2017)
    country_year_data = CountryYear.def_cont_yr_objects(countries, years)
    CountryYear.save_to_csv(country_year_data, "LAB2_AG.csv")
