#!/usr/bin/env python
# coding: utf-8

# In[1]:


 #*******************************************************************************************
 #
 #  File Name:  citipyx.py 
 #
 #  File Description:
 #      This Python script, citipyx.py, provides constants and functions for 
 #      finding and processing geographical locations. 
 #      Here is the list:
 #
 #  set_weathermap_url
 #  set_geoapify_url
 #  set_datafile
 #  set_index
 #  set_units
 #  set_city_set
 #  set_city_count
 #  set_search_cat
 #  set_temp_range
 #  set_humid_range
 #  set_cloud_range
 #  set_wind_speed_range
 #  set_config_dict
 #  set_weather_dict
 #
 #  get_config_dict
 #  get_weather_dict
 #
 #  return_city_names_list
 #  return_weather_df
 #  return_city_weather_styler
 #
 #  set_vacation_temp_range
 #  set_vacation_humid_range
 #  set_vacation_cloud_range
 #  set_vacation_wind_speed_range
 #
 #  search_category_rename
 #  finalize_vacation_df
 #  update_location_vacation_df
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  02/11/2026      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import logx
import requests

from citipy import citipy
from weather_api_keys import weather_api_key
from weather_api_keys import geoapify_key

from datetime import datetime
import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'citipyx.py'


# In[3]:


config_dict \
    = {'data': {'weathermap_url': 'http://api.openweathermap.org',
                'geoapify_url': 'https://api.geoapify.com/v2/places',
                'datafile': './resources/cities_weather.csv'},
       'params': { 'index': 'city_id',
                   'units': 'imperial',
                   'city_set': 50,
                   'city_count': 3000},
       'search_cat': ['accommodation.hotel',
                      'catering.restaurant',
                      'tourism.attraction'],
       'weather': {'min_temp': 0,
                   'max_temp': 120,
                   'min_humid': 0,
                   'max_humid': 100,
                   'min_cloud': 0,
                   'max_cloud': 100,
                   'min_wind_speed': 0,
                   'max_wind_speed': 100}}

ranges_dict \
    = {'temp': [config_dict['weather']['min_temp'], config_dict['weather']['max_temp']],
       'humid': [config_dict['weather']['min_humid'], config_dict['weather']['max_humid']],
       'cloud': [config_dict['weather']['min_cloud'], config_dict['weather']['max_cloud']],
       'wind_speed': [config_dict['weather']['min_wind_speed'], config_dict['weather']['max_wind_speed']]}


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  set_weathermap_url
 #
 #  Function Description:
 #      This function sets the weathermap url in the configuration dictionary.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  url             The parameter is the new url.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_weathermap_url(url):

    global config_dict

    config_dict['data']['weathermap_url'] = url


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  set_geoapify_url
 #
 #  Function Description:
 #      This function sets the geoapify url in the configuration dictionary.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  url             The parameter is the new url.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_geoapify_url(url):

    global config_dict

    config_dict['data']['geoapify_url'] = url


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  set_datafile
 #
 #  Function Description:
 #      This function sets the data file path in the configuration dictionary.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  datafile        The parameter is the new data file path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_datafile(datafile):

    global config_dict

    config_dict['data']['datafile'] = datafile


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  set_index
 #
 #  Function Description:
 #      This function sets the name of the city dataframe index name in the configuration 
 #      dictionary.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  index           The parameter is the new index name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_index(index):

    global config_dict

    config_dict['params']['index'] = index


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  set_units
 #
 #  Function Description:
 #      This function sets the type of units returned from the open weathermap url.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  units           The parameter is the new type of units.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_units(units):

    global config_dict

    config_dict['params']['units'] = units


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  set_city_set
 #
 #  Function Description:
 #      This function sets the number of cities in a single set.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  city_set        The parameter is new number of cities in a single set.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_city_set(city_set):

    global config_dict

    config_dict['params']['city_set'] = city_set


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  set_city_count
 #
 #  Function Description:
 #      This function sets the total number of cities.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  city_count      The parameter is the new total number of cities.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_city_count(city_count):

    global config_dict

    config_dict['params']['city_count'] = city_count


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  set_search_cat
 #
 #  Function Description:
 #      This function sets the list of acceptable search categories.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string list
 #          search_cat_list The parameter is the list of new search categories.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_city_count(search_cat_list):

    global config_dict

    config_dict['search_cat'] = search_cat_list


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  set_temp_range
 #
 #  Function Description:
 #      This function sets the temperature range.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_range     The parameter is a new list of the minimum and maximum 
 #                          temperatures.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_temp_range(input_range):

    global config_dict

    config_dict['weather']['min_temp'] = input_range[0]

    config_dict['weather']['max_temp'] = input_range[1]


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  set_humid_range
 #
 #  Function Description:
 #      This function sets the humidity percentage range.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_range     The parameter is a new list of the minimum and maximum 
 #                          temperatures for humidities.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_humid_range(input_range):

    global config_dict

    config_dict['weather']['min_humid'] = input_range[0]

    config_dict['weather']['max_humid'] = input_range[1]


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  set_cloud_range
 #
 #  Function Description:
 #      This function sets the cloudiness percentage range.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_range     The parameter is a new list of the minimum and maximum 
 #                          percentages for cloudiness.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_cloud_range(input_range):

    global config_dict

    config_dict['weather']['min_cloud'] = input_range[0]

    config_dict['weather']['max_cloud'] = input_range[1]


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  set_wind_speed_range
 #
 #  Function Description:
 #      This function sets the wind speed range.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_range     The parameter is a new list of the minimum and maximum 
 #                          speeds in mph for wind speeds.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_wind_speed_range(input_range):

    global config_dict

    config_dict['weather']['min_wind_speed'] = input_range[0]

    config_dict['weather']['max_wind_speed'] = input_range[1]


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  set_config_dict
 #
 #  Function Description:
 #      This function sets the configuration dictionary.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_range     The parameter is a new configuration dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_config_dict(input_dict):

    global config_dict

    config_dict = input_dict


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  set_weather_dict
 #
 #  Function Description:
 #      This function sets the weather dictionary.
 #
 #
 #  Return Type: none
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_range     The parameter is a new weather dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_weather_dict(input_dict):

    global config_dict

    config_dict['weather'] = input_dict


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  get_config_dict
 #
 #  Function Description:
 #      This function returns the configuration dictionary.
 #
 #
 #  Return Type: dict
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_config_dict():

    return config_dict


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  get_weather_dict
 #
 #  Function Description:
 #      This function returns the weather dictionary.
 #
 #
 #  Return Type: dict
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_weather_dict():

    return config_dict['weather']


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  return_city_names_list
 #
 #  Function Description:
 #      This function returns a list of cities from the API, citypy.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_city_names_list():

    cities_list = []


    lat_rng_flt_tuple = (-90.0, 90.0)

    lng_rng_flt_tuple = (-180.0, 180.0)


    random_lat_flt_array \
        = np.random.uniform \
            (lat_rng_flt_tuple[0], 
             lng_rng_flt_tuple[1], 
             size = config_dict['params']['city_count'])

    random_lng_flt_array \
        = np.random.uniform \
            (lng_rng_flt_tuple[0], 
             lng_rng_flt_tuple[1], 
             size = config_dict['params']['city_count'])


    lat_lng_flt_tuple_list \
        = zip(random_lat_flt_array, random_lng_flt_array)


    for lat_lng_flt_tuple in lat_lng_flt_tuple_list:

        city_name \
            = citipy.nearest_city \
                (lat_lng_flt_tuple[0], 
                 lat_lng_flt_tuple[1]) \
                    .city_name

        if city_name not in cities_list:

            cities_list.append(city_name)


    return cities_list


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  return_weather_df
 #
 #  Function Description:
 #      This function returns weather information from the open weathermap website 
 #      using the requests module and a list of cities.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string list
 #          cities_list     This parameter is a list of city names.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_weather_df(cities_list):

    query_url \
        = f"{config_dict['data']['weathermap_url']}/data/2.5/weather?appid=" \
          + f"{weather_api_key}&units={config_dict['params']['units']}&q="


    city_weather_dict_list = []

    record_count_int = 0

    set_of_cities_count_int = 1


    logx.print_and_log_text('\nCITY WEATHER DATA RETRIEVAL BEGINS...\n')


    for index, city_name in enumerate(cities_list):

        if index % config_dict['params']['city_set']== 0 \
           and index >= config_dict['params']['city_set']:

            record_count_int = 0

            set_of_cities_count_int += 1


        logx.print_and_log_text \
            (f'\nProcessing record #{record_count_int + 1} ' \
             + f'of set {set_of_cities_count_int} for city, {city_name}.')


        city_url = query_url + city_name

        record_count_int += 1


        try:

            city_weather_dict = requests.get(city_url).json()


            city_lat_flt = city_weather_dict['coord']['lat']

            city_lng_flt = city_weather_dict['coord']['lon']

            city_temp_flt = city_weather_dict['main']['temp']

            city_humid_int = city_weather_dict['main']['humidity']

            city_clouds_int = city_weather_dict['clouds']['all']

            city_wind_speed_flt = city_weather_dict['wind']['speed']

            city_country = city_weather_dict['sys']['country']

            city_datetime = datetime.fromtimestamp(city_weather_dict['dt'])


            city_weather_dict_list.append \
                ({'city': city_name, 
                  'latitude': city_lat_flt, 
                  'longitude': city_lng_flt, 
                  'temperature': city_temp_flt,
                  'humidity': city_humid_int,
                  'cloudiness': city_clouds_int,
                  'wind_speed': city_wind_speed_flt,
                  'country': city_country,
                  'date_time': city_datetime})

        except:

            logx.print_and_log_text \
                (f'\nThe script did not find the city, {city_name}. Skipping...')


    logx.print_and_log_text('\nCITY WEATHER DATA RETRIEVAL IS COMPLETE.') 


    city_weather_df =  pd.DataFrame(city_weather_dict_list)

    city_weather_df.index.name = config_dict['params']['index']


    return city_weather_df


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  return_city_weather_styler
 #
 #  Function Description:
 #      This function receives a city weather dataframe, formats a copy of it 
 #      as a styler, and returns it to the caller.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_df        The parameter is the input dataframe.
 #  string  caption          The parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_city_weather_styler \
        (input_df,
         caption):

    temp_df = input_df.copy()

    return \
        temp_df \
            .style \
            .set_caption(caption) \
            .set_table_styles \
                ([{'selector': 'caption', 
                   'props': [('color', 'black'), 
                             ('font-size', '20px'),
                             ('font-style', 'bold'),
                             ('text-align', 'center')]}]) \
            .set_properties \
                (**{'text-align': 'center',
                    'border': '1.3px solid red',
                    'color': 'blue'}) \
            .format \
                ({'city': pandasx.GENERAL_TEXT_FORMAT,
                  'longitude': pandasx.FLOAT_FORMAT,
                  'latitude': pandasx.FLOAT_FORMAT,
                  'temperature': pandasx.TEMPERATURE_flt_FORMAT,
                  'humidity': pandasx.PERCENT_int_FORMAT,
                  'cloudiness': pandasx.PERCENT_int_FORMAT,
                  'wind_speed': pandasx.FLOAT_FORMAT,
                  'country': pandasx.GENERAL_TEXT_FORMAT}) \
            .highlight_max \
                (subset = ['temperature', 'humidity', 'cloudiness', 'wind_speed'],
                 color = 'lime') \
            .highlight_min \
                (subset = ['temperature', 'humidity', 'cloudiness', 'wind_speed'],
                 color = 'yellow') \
            .hide()


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_temp_range
 #
 #  Function Description:
 #      This subroutine sets the vacation temperature range in Fahrenheit.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer min_temp_int
 #                          The parameter is the minimum vacation maximum temperature.
 #  integer max_temp_int
 #                          The parameter is the maximum vacation maximum temperature.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_vacation_temp_range \
        (min_temp_int,
         max_temp_int):

    global config_dict

    global ranges_dict


    min_temp_int = int(min_temp_int)

    max_temp_int = int(max_temp_int)


    if min_temp_int < config_dict['weather']['min_temp']:

        min_temp_int = config_dict['weather']['min_temp']

    if max_temp_int > config_dict['weather']['max_temp']:

        max_temp_int = config_dict['weather']['max_temp']

    if min_temp_int > max_temp_int:

        min_temp_int, max_temp_int \
            = max_temp_int, min_temp_int


    config_dict['weather']['min_temp'] = min_temp_int

    config_dict['weather']['max_temp'] = max_temp_int

    ranges_dict['temp'] = [min_temp_int, max_temp_int]


# In[24]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_humid_range
 #
 #  Function Description:
 #      This function sets the vacation humidity range.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer min_humid_int   The parameter is the minimum vacation humidity.
 #  integer max_humid_int   The parameter is the maximum vacation humidity.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_vacation_humid_range \
        (min_humid_int,
         max_humid_int):

    global config_dict

    global ranges_dict


    min_humid_int = int(min_humid_int)

    max_humid_int = int(max_humid_int)


    if min_humid_int < config_dict['weather']['min_humid']:

        min_humid_int = config_dict['weather']['min_humid']

    if max_humid_int > config_dict['weather']['max_humid']:

        max_humid_int = config_dict['weather']['max_humid']

    if min_humid_int > max_humid_int:

        min_humid_int, max_humid_int \
            = max_humid_int, min_humid_int


    config_dict['weather']['min_humid'] = min_humid_int

    config_dict['weather']['max_humid'] = max_humid_int

    ranges_dict['humid'] = [min_humid_int, max_humid_int]


# In[25]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_cloud_range
 #
 #  Function Description:
 #      This function sets the vacation cloudiness range.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer min_cloud_int   The parameter is the minimum vacation cloudiness.
 #  integer max_cloud_int   The parameter is the maximum vacation cloudiness.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_vacation_cloud_range \
        (min_cloud_int,
         max_cloud_int):

    global config_dict

    global ranges_dict


    min_cloud_int = int(min_cloud_int)

    max_cloud_int = int(max_cloud_int)


    if min_cloud_int < config_dict['weather']['min_cloud']:

        min_cloud_int = config_dict['weather']['min_cloud']

    if max_cloud_int > config_dict['weather']['max_cloud']:

        max_cloud_int = config_dict['weather']['max_cloud']

    if min_cloud_int > max_cloud_int:

        min_cloud_int, max_cloud_int \
            = max_cloud_int, min_cloud_int


    config_dict['weather']['min_cloud'] = min_cloud_int

    config_dict['weather']['max_cloud'] = max_cloud_int

    ranges_dict['cloud'] = [min_cloud_int, max_cloud_int]


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_wind_speed_range
 #
 #  Function Description:
 #      This function sets the vacation wind speed range.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer min_wind_speed_int
 #                          The parameter is the minimum vacation wind speed.
 #  integer max_wind_speed_int
 #                          The parameter is the maximum vacation wind speed.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_vacation_wind_speed_range \
        (min_wind_speed_int,
         max_wind_speed_int):

    global config_dict

    global ranges_dict


    min_wind_speed_int = int(min_wind_speed_int)

    max_wind_speed_int = int(max_wind_speed_int)


    if min_wind_speed_int < config_dict['weather']['min_wind_speed']:

        min_wind_speed_int = config_dict['weather']['min_wind_speed']

    if max_wind_speed_int > config_dict['weather']['max_wind_speed']:

        max_wind_speed_int = config_dict['weather']['max_wind_speed']

    if min_wind_speed_int > max_wind_speed_int:

        min_wind_speed_int, max_wind_speed_int \
            = max_wind_speed_int, min_wind_speed_int


    config_dict['weather']['min_wind_speed'] = min_wind_speed_int

    config_dict['weather']['max_wind_speed'] = max_wind_speed_int

    ranges_dict['wind_speed'] = [min_wind_speed_int, max_wind_speed_int]


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  search_category_rename
 #
 #  Function Description:
 #      This function verifies and renames the search category for a column name.
 #
 #
 #  Return Type: string, bool
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  search_category The parameter is a search category.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/12/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def search_category_rename(search_category):

    new_category_name = ''

    found_bool = False


    for cat in config_dict['search_cat']:

        if search_category == config_dict['search_cat'][len(config_dict['search_cat'])-1]:

            new_category_name = search_category.replace('.', ' ')

        else:

            new_category_name = search_category.rsplit('.', 1)[1]


        found_bool = True


    return new_category_name, found_bool


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  finalize_vacation_df
 #
 #  Function Description:
 #      This function finalizes and returns the vacation dataframe with the location 
 #      information.
 #
 #
 #  Return Type: string, bool
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_df        The parameter is a input dataframe.
 #  string  column_name     The parameter is the new column name.
 #  list    city_name_list  The parameter is the list of city names.
 #  list    location_name_list
 #                          The parameter is the list of location names.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/12/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def finalize_vacation_df \
        (input_df,
         column_name,
         city_name_list,
         location_name_list):

    new_df \
        = input_df.apply \
            (lambda x: x[input_df['city'].isin(city_name_list)])

    new_df.reset_index(drop = True, inplace = True)

    new_df[column_name] = pd.Series(location_name_list)    


    return new_df     


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  update_location_vacation_df
 #
 #  Function Description:
 #      This function takes a dataframe of vacation data, populates the location name 
 #      column, and returns the updated dataframe to the caller.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_df        The parameter is the input dataframe.
 #  string  column_name     The parameter is the location column name in the dataframe.
 #  string  search_category The parameter is a search category.
 #  integer search_radius_int  
 #                          The parameter is the search radius in feet.
 #  integer result_limit_int   
 #                          The parameter is a limit on the number of results.
 #  string  lang_desig      The parameter is the language designation for the search.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def update_location_vacation_df \
        (input_df,
         column_name,
         search_category = 'accommodation.hotel',
         search_radius_int = 10000,
         result_limit_int = 20,
         lang_desig = 'en'):

    params_dict \
        = {'categories': [search_category],
           'filter': '',
           'bias': '',
           'limit': result_limit_int,
           'lang': lang_desig,
           'apiKey': geoapify_key}


    category_name, found_bool = search_category_rename(search_category)


    if found_bool == False:

        return input_df


    logx.print_and_log_text(f'STARTING {category_name.upper()} SEARCH...\n\n')


    city_name_list = []

    location_name_list = []


    for index, row in input_df.iterrows():

        longitude_flt = input_df.at[index, 'longitude']

        latitude_flt = input_df.at[index, 'latitude']


        params_dict['filter'] \
            = f'circle:{longitude_flt},{latitude_flt},{search_radius_int}'

        params_dict['bias'] \
            = f'proximity:{longitude_flt},{latitude_flt}'


        response_dict \
            = requests.get \
                (url = config_dict['data']['geoapify_url'], 
                 params = params_dict) \
                    .json()

        if len(response_dict['features']) <= 0:

            continue


        for index, location in enumerate(response_dict['features']):

            try:

                location_name = location['properties']['name']

                location_name_list.append(location_name)

                logx.print_and_log_text \
                    (f'Located the following {category_name}...' \
                     + f'{location_name} ' \
                     + f"in {input_df.at[index, 'city']}, " \
                     + f"{input_df.at[index, 'country']}\n\n")

                break

            except:

                continue

        city_name_list.append(row['city'])


    new_df \
        = finalize_vacation_df \
            (input_df,
             column_name,
             city_name_list,
             location_name_list)

    logx.print_and_log_text(f'{category_name.upper()} SEARCH COMPLETE...\n\n')


    return new_df


# In[ ]:




