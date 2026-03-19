#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  dtypesx.py
 #
 #  File Description:
 #      This Python script, dtypesx.py, contains generic Python functions 
 #      for manipulating datatypes, dates, and times.  Here is the list:
 # 
 #  cnv_data_to_array
 #  cnv_to_pct_chg
 #  cnv_dts_idxs_to_date
 #
 #  rtn_data_obj_size
 #  rtn_rows_with_unq_idxs
 #  rtn_date_idxs
 #
 #  rtn_prior_date
 #  rtn_future_date
 #
 #  rtn_norm_date_idx
 #  rtn_norm_series_list_df
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #  02/18/2026          Upgraded Module                             Nicholas J. George
 #
 #******************************************************************************************/

import datetime as dt
import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'dtypesx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  cnv_data_to_array
 #
 #  Function Description:
 #      This function takes an input object and returns it as a numpy array if it
 #      is an array, Series, list, or tuple. Otherwise, the function returns None.
 #
 #
 #  Return Type: array or none
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is a input obj.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def cnv_data_to_array(input_obj):

    if isinstance(input_obj, np.ndarray): return input_obj

    elif isinstance(input_obj, pd.Series): return input_obj.to_numpy()

    elif isinstance(input_obj, list): return np.array(input_obj)

    elif isinstance(input_obj, tuple): return np.array(input_obj)

    else: return None


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  cnv_to_pct_chg
 #
 #  Function Description:
 #      This function receives a series of numbers, converts its values to percent
 #      change values, and returns the new series to the caller.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is input series.
 #  integer        round_int        The parameter is the place to round the results.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George           
 #
 #******************************************************************************************/

def cnv_to_pct_chg \
        (input_series,
         round_int = 2):

    input_array = input_series.to_numpy()

    temp_array = input_array * 0.0


    for i, ele in enumerate(input_array):

        if i > 0 and input_array[i - 1] != 0.0:

            temp_array[i] = ((ele - input_array[i - 1]) / input_array[i - 1]) * 100


    final_series = pd.Series(temp_array, index = input_series.index)

    final_series = final_series.drop(final_series.index[0])

    if round_int >= 0: final_series = final_series.round(round_int)


    return final_series


# In[5]:


#******************************************************************************************
 #
 #  Function Name:  cnv_dts_idxs_to_date
 #
 #  Function Description:
 #      This function receives a series with timestamp indices, converts them 
 #      into dates, and returns them as an array.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def cnv_dts_idxs_to_date(input_series):

    dates_array = np.array([], dtype = 'datetime64[D]')


    for ts in input_series.index.to_numpy():

        tmp_ts = pd.Timestamp(ts)

        tmp_ts.to_pydatetime()

        dates_array = np.append(dates_array, tmp_ts.date())


    return dates_array


# In[6]:


#******************************************************************************************
 #
 #  Function Name:  rtn_data_obj_size
 #
 #  Function Description:
 #      This function receives a list or dataframe and returns its length.
 #
 #
 #  Return Type: integer or none
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_data_obj_size(input_obj):

    if isinstance(input_obj, list) or isinstance(input_obj, np.ndarray): return len(input_obj[0])

    elif isinstance(input_obj, dict): return len(next(iter(input_obj.values())))

    elif isinstance(input_obj, pd.DataFrame): return len(input_obj.columns)

    else: return None


# In[7]:


#******************************************************************************************
 #
 #  Function Name:  rtn_rows_with_unq_idxs
 #
 #  Function Description:
 #      This function receives a series and removes all redundant rows with the same index
 #      but leaves the row with the last instance of an index.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_rows_with_unq_idxs(input_series):

    tmp_series = input_series.dropna()

    last_idx_int = len(tmp_series) - 1

    idx_array = values_array = np.array([], dtype = int)


    for idx, row in enumerate(tmp_series):

        if idx < last_idx_int: cmp_date = (tmp_series.index[idx + 1]).date()

        elif idx == last_idx_int: cmp_date = (tmp_series.index[idx - 1]).date()


        if (tmp_series.index[idx]).date() != cmp_date:

            idx_array = np.append(idx_array, tmp_series.index[idx])

            values_array = np.append(values_array, tmp_series.iloc[idx])


    final_series = pd.Series(values_array, index = idx_array)

    return final_series


# In[8]:


#******************************************************************************************
 #
 #  Function Name:  rtn_date_idxs
 #
 #  Function Description:
 #      This function receives a series with timestamps for indices, converts those
 #      timestamps to dates, and returns the new series.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_date_idxs(input_series):

    values_array = input_series.to_numpy()

    dates_array = cnv_dts_idxs_to_date(input_series)


    return pd.Series(values_array, index = dates_array, name = input_series.name)


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_prior_date
 #
 #  Function Description:
 #      This function returns the prior date based on the number of days.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         date             The parameter is the date.
 #  integer        days_int         The parameter is the number of days
 #  string         date_fmt         The parameter is the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_prior_date \
        (date, 
         days_int = 365, 
         date_fmt = '%Y-%m-%d'):

    curr_date = dt.datetime.strptime(date, date_fmt)

    tmp_date = curr_date.date() - dt.timedelta(days = days_int)

    prior_date = dt.datetime.strftime(tmp_date, date_fmt)


    return prior_date


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_future_date
 #
 #  Function Description:
 #      This function returns the future date based on the number of days.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         date             The parameter is the date.
 #  integer        days_int         The parameter is the number of days
 #  string         date_fmt         The parameter is the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_future_date \
        (date, 
         days_int, 
         date_fmt = '%Y-%m-%d'):

    curr_date = dt.datetime.strptime(date, date_fmt)

    tmp_date = curr_date.date() + dt.timedelta(days = days_int)

    future_date = dt.datetime.strftime(tmp_date, date_fmt)


    return future_date


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_norm_date_idx
 #
 #  Function Description:
 #      This function returns a series list where the all the series possess 
 #      a common index.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           input_list       The parameter is the unsorted input series list 
 #                                  of date strings with the format, yyyy-mm-dd.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_norm_date_idx(input_list):

    sorted_list = sorted(input_list, key = len)


    for idx, series in enumerate(sorted_list):

        curr_list = series.index.tolist()

        new_list = [ele[5:] for ele in curr_list]


        if idx >= 1: tmp_list = [ele for ele in tmp_list if ele in new_list]

        else: tmp_list = new_list 


    return tmp_list


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_norm_series_list_df
 #
 #  Function Description:
 #      This function returns a dataframe from a series list normalized 
 #      from a common index with a date string format, yyyy-mm-dd.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           input_list       The parameter is a input series list.
 #  list           omit_list        The parameter is the omitted series indices list.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_norm_series_list_df \
        (input_list,
         omit_list = None):

    curr_list = input_list.copy()


    if omit_list is not None: 

        curr_list = [x for i, x in enumerate(curr_list) if i not in omit_list]


    norm_idx_list = rtn_norm_date_idx(curr_list)

    norm_list = []


    for idx, series in enumerate(curr_list):

        idx_list = [x[5:] for x in curr_list[idx].index.tolist()]

        curr_list[idx] = curr_list[idx].set_axis(idx_list)


        temp_list = []

        for j, x in enumerate(curr_list[idx]):

            if str(curr_list[idx].index[j]) in norm_idx_list: temp_list.append(x)


        norm_series = pd.Series(temp_list, index = norm_idx_list)

        norm_series.name = curr_list[idx].name


        norm_list.append(norm_series)


    return pd.DataFrame(norm_list).transpose()


# In[ ]:




