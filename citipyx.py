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
 #  set_config_dict
 #  get_config_dict
 #  set_weather_dict
 #  get_weather_dict
 #
 #  rtn_city_names_array
 #  rtn_weather_df
 #  rtn_city_weather_styler
 #
 #  set_vacation_temp_rng
 #  set_vacation_humid_rng
 #  set_vacation_cloud_rng
 #  set_vacation_wind_speed_rng
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
import pandasx

import requests

import datetime as dt
import numpy as np
import pandas as pd

from citipy import citipy

from weather_api_keys import weather_api_key, geoapify_key

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'citipyx.py'


# In[3]:


config_dict \
    = {'data': {'weathermap_url': 'http://api.openweathermap.org',
                'geoapify_url': 'https://api.geoapify.com/v2/places',
                'datafile': './resources/cities_weather.csv'},
       'highlight': {'cols': ['temperature', 'humidity', 
                              'cloudiness', 'wind_speed'],
                     'max': 'lime',
                     'min': 'yellow'},
       'vac_loc': {'search_radius': 10000,
                   'result_limit': 20,
                   'lang_desig': 'en'},
       'params': { 'index': 'city_id',
                   'units': 'imperial',
                   'city_set': 50,
                   'city_count': 3000},
       'search_cat': ['accommodation.hotel',
                      'catering.restaurant',
                      'tourism.attraction'],
       'styler_fmt': {'city': pandasx.fmt_dict['text'],
                      'longitude': pandasx.fmt_dict['flt'],
                      'latitude': pandasx.fmt_dict['flt'],
                      'temperature': pandasx.fmt_dict['tmpf_flt'],
                      'humidity': pandasx.fmt_dict['pct_int'],
                      'cloudiness': pandasx.fmt_dict['pct_int'],
                      'wind_speed': pandasx.fmt_dict['flt'],
                      'country': pandasx.fmt_dict['text']},
       'weather': {'min_temp': 0,
                   'max_temp': 120,
                   'min_humid': 0,
                   'max_humid': 100,
                   'min_cloud': 0,
                   'max_cloud': 100,
                   'min_wind_speed': 0,
                   'max_wind_speed': 100}}


# In[4]:


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


# In[5]:


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


# In[6]:


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


# In[7]:


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


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_city_names_array
 #
 #  Function Description:
 #      This function returns a numpy array of cities from the API, citypy.
 #
 #
 #  Return Type: array
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

def rtn_city_names_array():

    cities_array = np.array([], dtype = str)


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


    for coords_tuple in lat_lng_flt_tuple_list:

        city_name \
            = citipy.nearest_city \
                (coords_tuple[0], 
                 coords_tuple[1]) \
                    .city_name

        if city_name not in cities_array:

            cities_array \
                = np.append(cities_array, city_name)


    return cities_array


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_weather_df
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
 #  array   cities_array    This parameter is a numpy array of city names.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_weather_df \
        (cities_array):

    query_url \
        = f"{config_dict['data']['weathermap_url']}/data/2.5/weather?appid=" \
          + f"{weather_api_key}&units={config_dict['params']['units']}&q="


    city_weather_dict_list = []

    record_count_int = 0

    set_of_cities_count_int = 1


    logx.print_and_log_text('\nCITY WEATHER DATA RETRIEVAL BEGINS...\n')


    for idx, city_name in enumerate(cities_array):

        if idx % config_dict['params']['city_set'] == 0 \
           and idx >= config_dict['params']['city_set']:

            record_count_int = 0

            set_of_cities_count_int += 1


        logx.print_and_log_text \
            (f'\nProcessing record #{record_count_int + 1} ' \
             + f'of set {set_of_cities_count_int} for city, {city_name}.')


        city_url = query_url + city_name

        record_count_int += 1


        try:

            city_weather_dict = requests.get(city_url).json()

            city_weather_dict_list.append \
                ({'city': city_name, 
                  'latitude': city_weather_dict['coord']['lat'], 
                  'longitude': city_weather_dict['coord']['lon'], 
                  'temperature': city_weather_dict['main']['temp'],
                  'humidity': city_weather_dict['main']['humidity'],
                  'cloudiness': city_weather_dict['clouds']['all'],
                  'wind_speed': city_weather_dict['wind']['speed'],
                  'country': city_weather_dict['sys']['country'],
                  'date_time': dt.datetime.fromtimestamp(city_weather_dict['dt'])})

        except:

            logx.print_and_log_text \
                (f'\nThe script did not find the city, {city_name}. Skipping...')


    logx.print_and_log_text('\nCITY WEATHER DATA RETRIEVAL IS COMPLETE.') 


    city_weather_df =  pd.DataFrame(city_weather_dict_list)

    city_weather_df.index.name = config_dict['params']['index']


    return city_weather_df


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_city_weather_styler
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
 #  string  caption         The parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_city_weather_styler \
        (input_df,
         caption):

    temp_df = input_df.copy()

    return \
        temp_df \
            .style \
            .set_caption(caption) \
            .set_table_styles(pandasx.style_dict['table_styles']) \
            .set_properties(**pandasx.style_dict['properties']) \
            .format(config_dict['styler_fmt']) \
            .highlight_max \
                (subset = config_dict['highlight']['cols'],
                 color = config_dict['highlight']['max']) \
            .highlight_min \
                (subset = config_dict['highlight']['cols'],
                 color = config_dict['highlight']['min']) \
            .hide()


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_temp_rng
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
 #  integer min_temp_int    The parameter is the minimum vacation maximum temperature.
 #  integer max_temp_int    The parameter is the maximum vacation maximum temperature.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/11/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_vacation_temp_rng \
        (min_temp_int,
         max_temp_int):

    global config_dict


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


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_humid_rng
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

def set_vacation_humid_rng \
        (min_humid_int,
         max_humid_int):

    global config_dict


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


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_cloud_rng
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

def set_vacation_cloud_rng \
        (min_cloud_int,
         max_cloud_int):

    global config_dict

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


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_wind_speed_rng
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

def set_vacation_wind_speed_rng \
        (min_wind_speed_int,
         max_wind_speed_int):

    global config_dict


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


# In[15]:


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

def search_category_rename \
        (search_category):

    new_category_name = ''

    found_bool = False


    for cat in config_dict['search_cat']:

        if search_category == \
            config_dict['search_cat'][len(config_dict['search_cat']) - 1 ]:

            new_category_name = search_category.replace('.', ' ')

        else:

            new_category_name = search_category.rsplit('.', 1)[1]


        found_bool = True


    return new_category_name, found_bool


# In[16]:


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
 #  array   city_name_array The parameter is a numpy array of city names.
 #  array   loc_name_array  The parameter is a numpy array of location names.
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
         city_name_array,
         loc_name_array):

    new_df \
        = input_df.apply \
            (lambda x: x[input_df['city'].isin(city_name_array)])

    new_df.reset_index(drop = True, inplace = True)

    new_df[column_name] = pd.Series(loc_name_array)    


    return new_df     


# In[17]:


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
         search_category = 'accommodation.hotel'):

    params_dict \
        = {'categories': [search_category],
           'filter': '',
           'bias': '',
           'limit': config_dict['vac_loc']['result_limit'],
           'lang': config_dict['vac_loc']['lang_desig'],
           'apiKey': geoapify_key}


    category_name, found_bool = search_category_rename(search_category)


    if found_bool == False:

        return input_df


    logx.print_and_log_text(f'STARTING {category_name.upper()} SEARCH...\n\n')


    city_name_array = np.array([], dtype = str)

    loc_name_array = np.array([], dtype = str)


    for i, row in input_df.iterrows():

        longitude_flt = input_df.at[i, 'longitude']

        latitude_flt = input_df.at[i, 'latitude']


        params_dict['filter'] \
            = f"circle:{longitude_flt},{latitude_flt},{config_dict['vac_loc']['search_radius']}"

        params_dict['bias'] \
            = f'proximity:{longitude_flt},{latitude_flt}'


        response_dict \
            = requests.get \
                (url = config_dict['data']['geoapify_url'], 
                 params = params_dict).json()

        if len(response_dict['features']) <= 0:

            continue


        for j, location in enumerate(response_dict['features']):

            try:

                location_name = location['properties']['name']

                loc_name_array = np.append(loc_name_array, location_name)

                logx.print_and_log_text \
                    (f'Located the following {category_name}...' \
                     + f'{location_name} ' \
                     + f"in {input_df.at[j, 'city']}, " \
                     + f"{input_df.at[j, 'country']}\n\n")

                break

            except:

                continue

        city_name_array = np.append(city_name_array, row['city'])


    new_df \
        = finalize_vacation_df \
            (input_df,
             column_name,
             city_name_array,
             loc_name_array)

    logx.print_and_log_text(f'{category_name.upper()} SEARCH COMPLETE...\n\n')


    return new_df


# In[ ]:




