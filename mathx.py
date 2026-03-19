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
 #  rtn_regr_model_eqn_coef
 #  rtn_poly_line_array
 #  rtn_eqn_as_text
 #  rtn_r_sqr
 #
 #  is_perf_sqr
 #  calc_clst_factors
 #  calc_rows_and_cols
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #  02/24/2026          Upgraded Module                             Nicholas J. George
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
 #  Function Name:  rtn_regr_model_eqn_coef
 #
 #  Function Description:
 #      This function returns the coefficients for a regression equation using x-y series.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          x_array          The parameter is the array holding the x values.
 #  array          y_array          The parameter is the array holding the y values.
 #  integer        degree_int       This parameter is the degree of the polynomial.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_regr_model_eqn_coef(x_array, y_array, degree_int):

    return np.poly1d(np.polyfit(x_array, y_array, degree_int))


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_poly_line_array
 #
 #  Function Description:
 #      This function returns a polynomial line as an array.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          x_array          The parameter is the array holding the x values.
 #  array          y_array          The parameter is the array holding the y values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_poly_line_array(x_array, y_array):

    return np.linspace(x_array.min(), x_array.max(), abs(int((x_array.max() - y_array.min()) / 2)))


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_eqn_as_text
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          model_eqn_array  The parameter is a array of coefficients for a 
 #                                  polynomial.
 #  integer        coef_prec_int    The parameter is the precision of the equation's 
 #                                  coefficients.
 # 
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_eqn_as_text(model_eqn_array, coef_prec_int):

    degree_int = len(model_eqn_array)


    for idx, term in enumerate(model_eqn_array):

        temp_eqn = str(round(float(term), coef_prec_int))

        if degree_int > 1:

            temp_eqn = temp_eqn + 'x' + '^' + str(degree_int)

        elif degree_int == 1:

            temp_eqn += 'x'


        if degree_int == len(model_eqn_array):

            final_eqn = temp_eqn

        else:

            final_eqn = final_eqn + ' + ' + temp_eqn

        degree_int -= 1


    return 'y = ' + final_eqn


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_r_sqr
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         x_array          The parameter is the array holding the x values.
 #  series         y_array          The parameter is the array holding the y values.
 #  integer        degree_int       The parameter is the degree of the polynomial.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_r_sqr(x_array, y_array, degree_int):

    coef_flt_array = np.polyfit(x_array, y_array, degree_int)

    pPoly1D = np.poly1d(coef_flt_array)


    yhatArray = pPoly1D(x_array)

    ybar_flt = np.sum(y_array) / len(y_array)


    ssreg_flt = np.sum(((yhatArray - ybar_flt) ** 2))

    sstot_flt = np.sum(((y_array - ybar_flt) ** 2))


    return ssreg_flt / sstot_flt


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  is_perf_sqr
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
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def is_perf_sqr(input_obj):

    input_int = int(abs(input_obj))

    if input_int == 0 or input_int == 1: return True


    x_int = input_int // 2

    seen = set([x_int])


    while x_int * x_int != input_int:

        x_int = (x_int + (input_int // x_int)) // 2

        if x_int in seen: return False

        seen.add(x_int)


    return True


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  calc_clst_factors
 #
 #  Function Description:
 #      This function calculates and returns the two closest factors of an integer.
 #
 #
 #  Return Type: integer, integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  integer        positive_int     The parameter is the input integer.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_clst_factors(positive_int):

    c = int(abs(positive_int))

    a, b, i = 1, c, 0


    while a < b:

        i += 1

        if c % i == 0:

            a = i

            b = c // a


    return b, a


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  calc_rows_and_cols
 #
 #  Function Description:
 #      The function returns the number of rows and columns based on the number of plots.
 #
 #
 #  Return Type: int, int
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the multichart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_rows_and_cols(chart_dict):

    return calc_clst_factors(chart_dict['figure']['nplots'])


# In[ ]:




