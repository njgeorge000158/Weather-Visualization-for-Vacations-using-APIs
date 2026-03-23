[vacationsFigure44RestaurantLocations.html](https://github.com/user-attachments/files/26195067/vacationsFigure44RestaurantLocations.html)![weather](https://github.com/njgeorge000158/Weather-Visualization-for-Vacations-from-APIs/assets/137228821/7a04bda6-ff8b-47df-b255-568d7c2076ab)

----

# **WeatherPy and VacationPy: From Global Climate Data to Personalized Vacation Recommendations**

----

## **Overview**

This project consists of two interconnected Jupyter Notebooks that work in sequence to transform raw global weather data into a curated list of vacation destinations filtered against user-defined climate preferences.

## **WeatherPy: Global Weather Visualization**

The first notebook, `weather.ipynb`, retrieves and visualizes current weather conditions for over 500 cities across the globe. The results are compiled and exported to `cities_weather.csv`, stored in the `resources` folder, which serves as the foundation for the second stage of the analysis.

## **VacationPy: Destination Selection**

The second notebook, `vacations.ipynb`, reads `cities_weather.csv` as its input and applies a set of specified weather conditions to filter the global dataset down to a shortlist of candidate vacation destinations. By pairing weather data with mapping and location tools, the notebook identifies and visualizes the cities that best match the desired climate criteria — transforming a dataset of hundreds of cities into a targeted and personalized set of recommendations.

---

<img width="1360" height="1070" alt="Screenshot 2026-03-23 at 1 58 57 PM" src="https://github.com/user-attachments/assets/38db4a60-d186-4a46-bf9e-d5731f5dcaa3" />

<img width="1469" height="563" alt="vacationsTable53TouristAttractionLocations" src="https://github.com/user-attachments/assets/7e594815-f9e9-481d-a582-dcc5972b1691" />



<img width="898" alt="Screenshot 2024-04-20 at 3 44 09 PM" src="https://github.com/njgeorge000158/Weather-Visualization-for-Vacations-using-APIs/assets/137228821/6c8ffabb-c4b3-4fbf-9b9f-45503b43b478">

<img width="1095" alt="Screenshot 2024-04-20 at 3 34 27 PM" src="https://github.com/njgeorge000158/Weather-Visualization-for-Vacations-using-APIs/assets/137228821/84f93882-03bd-46bb-b4ea-abf8b94b2eb8">

---

## **Workflow Summary**

The two notebooks form a deliberate and clean analytical pipeline: WeatherPy collects and structures the data, and VacationPy consumes and acts on it. The CSV file serves as the handoff point between the two stages, keeping the workflows modular, transparent, and easy to reproduce or adapt for different weather preferences.

----

## Copyright

Nicholas J. George © 2023. All Rights Reserved.
