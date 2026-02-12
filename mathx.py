#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  mathx.py
 #
 #  File Description:
 #      This Python script, mathx.py, contains Python functions for math calculations. 
 #      Here is the list:
 #
 #  return_regression_model_equation_coefficients
 #  return_polynomial_line_series
 #  return_equation_as_text
 #  return_r_squared_value
 #
 #  is_perfect_square
 #  calculate_closest_factors
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  03/04/2024      Initial Development                     Nicholas J. George
 #  02/10/2026      Abbreviated variable names              Nicholas J. George
 #
 #******************************************************************************************/

import math

import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'mathx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  return_regression_model_equation_coefficients
 #
 #  Function Description:
 #      This function returns the coefficients for a regression equation using x-y series.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the series holding the x values.
 #  series  y_series        The parameter is the series holding the y values.
 #  integer degree_int      This parameter is the degree of the polynomial.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_regression_model_equation_coefficients \
        (x_series, 
         y_series,
         degree_int):

    equation_list = np.poly1d(np.polyfit(x_series, y_series, degree_int))

    return equation_list


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  return_polynomial_line_series
 #
 #  Function Description:
 #      This function returns a polynomial line as an np array.
 #
 #
 #  Return Type: np array
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the series holding the x values.
 #  series  y_series        The parameter is the series holding the y values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_polynomial_line_series \
        (x_series, 
         y_series):

    sample_number_int = abs(int((x_series.max() - y_series.min()) / 2))

    return np.linspace(x_series.min(), x_series.max(), sample_number_int)


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  return_equation_as_text
 #
 #  Function Description:
 #      This function returns the model equation as a string.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    model_equation_list
 #                          The parameter is a list of coefficients for a polynomial.
 #  integer coefficient_precision_int
 #                          The parameter is the precision of the equation's coefficients.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_equation_as_text \
        (model_equation_list,
         coefficient_precision_int = 4):

    degree_int = len(model_equation_list)


    for index, term in enumerate(model_equation_list):

        temp_eqn = str(round(float(term), coefficient_precision_int))

        if degree_int > 1:

            temp_eqn = temp_eqn + 'x' + '^' + str(degree_int)

        elif degree_int == 1:

            temp_eqn = temp_eqn + 'x'

        if degree_int == len(model_equation_list):

            final_eqn = temp_eqn

        else:

            final_eqn = final_eqn + ' + ' + temp_eqn

        degree_int -= 1


    final_eqn = 'y = ' + final_eqn


    return final_eqn


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  return_r_squared_value
 #
 #  Function Description:
 #      This function returns the r-squared value from x-y series.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the series holding the x values.
 #  series  y_series        The parameter is the series holding the y values.
 #  integer degree_int      This parameter is the degree of the polynomial.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_r_squared_value \
        (x_series, 
         y_series, 
         degree_int):

    coefficients_flt_nparray = np.polyfit(x_series, y_series, degree_int)

    pPoly1D = np.poly1d(coefficients_flt_nparray)


    yhatList = pPoly1D(x_series)

    ybar_flt = y_series.sum() / len(y_series)


    ssreg_flt = ((yhatList - ybar_flt) ** 2).sum()

    sstot_flt = ((y_series - ybar_flt) ** 2).sum()


    return ssreg_flt / sstot_flt


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  is_perfect_square
 #
 #  Function Description:
 #      This function indicates whether the input is a perfect square.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer positive_int    The parameter is the input integer.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def is_perfect_square(positive_int):

    positive_int = int(positive_int)


    if positive_int < 0:

        return False

    elif positive_int >= 0 and positive_int <= 1:

        return True


    x_int = positive_int // 2

    seen = set([x_int])


    while x_int * x_int != positive_int:

        x_int = (x_int + (positive_int // x_int)) // 2

        if x_int in seen: 

            return False

        seen.add(x_int)


    return True


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  calculate_closest_factors
 #
 #  Function Description:
 #      This function calculates the closest factors of an integer.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer positive_int    The parameter is the input integer.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #  02/10/2026          Abbreviated variable names                  Nicholas J. George
 #
 #******************************************************************************************/

def calculate_closest_factors(positive_int):

    positive_int = int(positive_int)

    if positive_int <= 0:

        return [0, 0]


    a_int, b_int, i_int = 1, positive_int, 0


    while a_int < b_int:

        i_int += 1

        if positive_int % i_int == 0:

            a_int = i_int

            b_int = positive_int // a_int


    if positive_int > 2 and a_int > b_int:

        a_int, b_int = b_int, a_int


    return [b_int, a_int]


# In[ ]:




