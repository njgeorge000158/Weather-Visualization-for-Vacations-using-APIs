#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  matplotlibx.py
 #
 #  File Description:
 #      The Python script, matplotlibx.py, contains generic Python functions
 #      for matplotlib charts and processing.  Here is the list:
 #
 #  display_linear_regression_line
 #  display_regression_line
 #
 #  display_line_chart_from_xy_series
 #  display_line_chart_from_df
 #  display_stacked_line_subplots
 #
 #  display_boxplots_from_series_list
 #  display_boxplot_from_df
 #
 #  display_bar_chart_from_series
 #  display_bar_chart_from_df
 #  
 #  display_scatter_plot_from_xy_series
 #  display_multiple_scatter_plots_from_xy_series_list
 #
 #  display_pie_chart_from_series
 #  display_multiple_pie_charts_from_df
 #
 #  display_histogram_from_series
 #  display_histograms_from_series_list
 #  display_multiple_histograms_from_df
 #
 #  display_plot_from_series
 #  display_plots_from_series_list
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/18/2023      Initial Development                     Nicholas J. George
 #  02/10/2026      Abbreviated variable names              Nicholas J. George
 #
 #******************************************************************************************/

import logx
import mathx

import math

import matplotlib.pyplot as plt
import pandas as pd

from scipy import stats

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'matplotlibx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  display_linear_regression_line
 #
 #  Function Description:
 #      The function displays a linear regression line.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the x-axis series.
 #  series  y_series        The parameter is the y-axis series.
 #  float   x_coord_flt     The parameter is the x-coordinate of the text.   
 #  float   y_coord_flt     The parameter is the y-coordinate of the text.  
 #  string  line_color      The parameter is the line color.
 #  string  line_width_flt  The parameter is the line type.
 #  float   alpha_flt       The parameter is the alpha (transparency) value.  
 #  integer coef_precision_int
 #                          The parameter is the equation coefficient precision. 
 #  float   font_size_flt The parameter is the equation's font size. 
 #  string  font_weight     The parameter is the equation's font weight.
 #  string  font_color      The parameter is the equation's font color.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_linear_regression_line \
        (x_series,
         y_series,
         x_coord_flt,
         y_coord_flt,
         line_color = 'red',
         line_width_flt = 3.0,
         alpha_flt = 1.0,
         coef_precision_int = 4,
         font_size_flt = 16.0,
         font_weight = 'bold',
         font_color = 'blue'):

    (slope, intercept, rvalue, pvalue, stderr) = stats.linregress(x_series, y_series)

    linear_regression_series = (x_series * slope) + intercept

    r_squared_flt = rvalue * rvalue


    plt.plot \
        (x_series,
         linear_regression_series,
         color = line_color,
         linewidth = line_width_flt,
         alpha = alpha_flt)

    linear_equation \
        = 'y = ' + str(round(slope, coef_precision_int)) \
          + 'x + ' + str(round(intercept, coef_precision_int))

    plt.annotate \
        (linear_equation,
         (x_coord_flt, y_coord_flt),
         fontsize = font_size_flt,
         fontweight = font_weight,
         color = font_color)   


    logx.print_and_log_text('r-value:     {:.4f}'.format(rvalue))

    logx.print_and_log_text('r-squared:   {:.4f}\n'.format(r_squared_flt))


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  display_polynomial_regression_line
 #
 #  Function Description:
 #      The function displays a single line chart from an x and y series and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the x-axis series.
 #  series  y_series        The parameter is the y-axis series.
 #  float   x_coord_flt     The parameter is the x-coordinate of the text.   
 #  float   y_coord_flt     The parameter is the y-coordinate of the text.
 #  integer degree_int      The parameter is the regression polynomial degree.
 #  string  line_color      The parameter is the line color.
 #  string  line_width_flt  The parameter is the line type.
 #  float   alpha_flt       The parameter is the alpha (transparency) value.  
 #  integer coef_precision_int
 #                          The parameter is the equation coefficient precision. 
 #  float   font_size_flt   The parameter is the equation's font size. 
 #  string  font_weight     The parameter is the equation's font weight.
 #  string  font_color      The parameter is the equation's font color.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_polynomial_regression_line \
        (x_series,
         y_series,
         x_coord_flt,
         y_coord_flt,
         degree_int,
         line_color = 'red',
         line_width_flt = 3.0,
         alpha_flt = 1.0,
         coef_precision_int = 4,
         font_size_flt = 16.0,
         font_weight = 'bold',
         font_color = 'blue'):

    model_equation_list \
        = mathx.return_regression_model_equation_coefficients \
            (x_series, y_series, degree_int)

    polynomial_line_series = mathx.return_polynomial_line_series(x_series, y_series)

    plt.plot \
        (polynomial_line_series, 
         model_equation_list(polynomial_line_series),
         color = line_color,
         linewidth = line_width_flt,
         alpha = alpha_flt)


    equation_label = mathx.return_equation_as_text(model_equation_list)

    plt.annotate \
        (equation_label,
         (x_coord_flt, y_coord_flt),
          fontsize = font_size_flt,
          fontweight = font_weight,
          color = font_color)


    r_squared_flt = mathx.return_r_squared_value(x_series, y_series, degree_int)

    r_value_flt = math.sqrt(r_squared_flt)


    logx.print_and_log_text('r-value:     {:.4f}'.format(r_value_flt))

    logx.print_and_log_text('r-squared:   {:.4f}'.format(r_squared_flt))


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  display_line_chart_from_xy_series
 #
 #  Function Description:
 #      The function displays a single line chart from an x and y series and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the x-axis series.
 #  series  y_series        The parameter is the y-axis series.
 #  string  title           The parameter is the chart title.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  string  line_color      The parameter is the line color.
 #  string  line_type
 #                          The parameter is the line type.
 #  float   alpha_flt       The parameter is the alpha (transparency) value.
 #  string  fill_style      The parameter is the line fills style.
 #  float   line_width_flt  The parameter is the line width.       
 #  string  marker          The parameter is the marker type.
 #  string  marker_face_color
 #                          The parameter is the marker face color.
 #  string  marker_edge_color
 #                          The parameter is the marker edge color.
 #  float   marker_size_flt The parameter is the marker size.
 #  float   marker_edge_width_flt
 #                          The parameter is the marker edge width. 
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   xlabel_font_size_flt
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_flt  The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_flt
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_flt  The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_flt
 #                          The parameter is the x-axis tick font size. 
 #  float   yticks_font_size_flt
 #                          The parameter is the y-axis tick font size. 
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_line_chart_from_xy_series \
        (x_series,
         y_series,
         title,
         xlabel,
         ylabel,
         line_color = 'darkslategray',
         line_type = 'solid',
         alpha_flt = 1.0,
         fill_style = 'full',
         line_width_flt = 3.0,
         marker = 'o',
         marker_face_color = 'red',
         marker_edge_color = 'black',
         marker_size_flt = 10.0,
         marker_edge_width_flt = 1.0,
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 20.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xticks_font_size_flt = 14.0,
         xticks_rotation_flt = 0.0,
         yticks_font_size_flt = 14.0,
         yticks_rotation_flt = 0.0,
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    plt.figure(figsize = (figure_width_flt, figure_length_flt))

    plt.plot \
        (x_series,
         y_series,
         alpha = alpha_flt,
         color = line_color,
         fillstyle = fill_style,
         linewidth = line_width_flt,
         marker = marker,
         markerfacecolor = marker_face_color,
         markeredgecolor = marker_edge_color,
         markersize = marker_size_flt,
         markeredgewidth = marker_edge_width_flt,
         linestyle = line_type)

    plt.title \
        (title,
         fontdict = {'fontsize': title_font_size_flt, 
                     'fontstyle': title_font_style},
         pad = title_pad_flt)

    plt.xlabel \
        (xlabel,
         fontdict = {'fontsize': xlabel_font_size_flt,
                     'fontstyle': xlabel_font_style},
         labelpad = xlabel_pad_flt)

    plt.ylabel \
        (ylabel,
         fontdict = {'fontsize': ylabel_font_size_flt,
                     'fontstyle': ylabel_font_style},
         labelpad = ylabel_pad_flt)

    plt.xticks(fontsize = xticks_font_size_flt, rotation = xticks_rotation_flt)

    plt.yticks(fontsize = yticks_font_size_flt, rotation = yticks_rotation_flt)


    plt.grid()

    logx.save_plot_image(title)

    plt.show()


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  display_line_chart_from_df
 #
 #  Function Description:
 #      The function displays a chart from a dataframe and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe  
 #          input_df        The parameter is the input dataframe.
 #  string  title           The parameter is the chart title.
 #  list    colors_list
 #                          The parameter is the list of colors for the subplots.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  float   alpha_flt       The parameter is the alpha (transparency) value.
 #  string  fill_style      The parameter is the line fills style.
 #  float   line_width_flt  The parameter is the line width.       
 #  string  marker          The parameter is the marker type.
 #  string  marker_face_color
 #                          The parameter is the marker face color.
 #  string  marker_edge_color
 #                          The parameter is the marker edge color.
 #  float   marker_edge_width_flt
 #                          The parameter is the marker size.
 #  boolean grid_bool       The parameter indicates whether the chart displays a grid.
 #  boolean display_legend_bool
 #                          The parameter indicates whether the legend will be present.
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   xlabel_font_size_flt
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_flt  The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_flt
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_flt  The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_flt
 #                          The parameter is the subplot's x-tick label's font size.
 #  float   xticks_rotation_flt
 #                          The parameter is the subplot's x-tick label's rotation in degrees.
 #  float   yticks_font_size_flt
 #                          The parameter is the subplot's y-tick label's font size.
 #  float   yticks_rotation_flt
 #                          The parameter is the subplot's y-tick label's rotation in degrees.
 #  string  legend_loc      The parameter is the legend's general location.
 #  float   legend_font_size_flt
 #                          The parameter is legend's font size.
 #  tuple   legend_bbox_to_anchor_flt_tuple
 #                          The parameter is the legend's xy-coordinates. 
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_line_chart_from_df \
        (input_df,
         title,
         colors_list,
         xlabel = None,
         ylabel = None,
         alpha_flt = 0.8,
         fill_style = 'full',
         line_width_flt = 3.0,
         marker = 'o',
         marker_face_color = 'red',
         marker_edge_color = 'black',
         marker_size_flt = 0.0,
         marker_edge_width_flt = 1.0,
         grid_bool = True,
         display_legend_bool = False,
         title_font_size_flt = 16.0,
         title_font_style = 'normal',
         title_pad_flt = 10.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xticks_font_size_flt = 14.0,
         xticks_rotation_flt = 90.0,
         yticks_font_size_flt = 14.0,
         yticks_rotation_flt = 0.0,
         legend_loc = 'center right',
         legend_font_size_flt = 14.0,
         legend_bbox_to_anchor_flt_tuple = (1.5, 0.5),
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    plt.figure(figsize = (figure_width_flt, figure_length_flt))

    input_df \
        .plot.line \
            (label = [],
             color = colors_list,
             alpha = alpha_flt,
             marker = marker,
             markerfacecolor = marker_face_color,
             markeredgecolor = marker_edge_color ,
             markersize = marker_size_flt,
             grid = grid_bool,
             legend = display_legend_bool)

    plt.title \
        (title,
         fontdict = {'fontsize': title_font_size_flt, 
                     'fontstyle': title_font_style},
         pad = title_pad_flt)

    if xlabel != None:

        plt.xlabel \
            (xlabel,
             fontdict = {'fontsize': xlabel_font_size_flt,
                         'fontstyle': xlabel_font_style},
             labelpad = xlabel_pad_flt)

    if ylabel != None:

        plt.ylabel \
            (ylabel,
             fontdict = {'fontsize': ylabel_font_size_flt,
                         'fontstyle': ylabel_font_style},
             labelpad = ylabel_pad_flt)

    plt.xticks(fontsize = xticks_font_size_flt, rotation = xticks_rotation_flt)

    plt.yticks(fontsize = yticks_font_size_flt, rotation = yticks_rotation_flt)

    if display_legend_bool == True:

        plt.legend \
            (loc = legend_loc,
             fontsize = legend_font_size_flt,
             bbox_to_anchor = legend_bbox_to_anchor_flt_tuple)


    logx.save_plot_image(title)

    plt.show()


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  display_stacked_line_subplots
 #
 #  Function Description:
 #      The function receives a dictionary of series and formatting parameters 
 #      for the display of stacked line subplots.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dictionary
 #          input_frame_dict
 #                          The parameter is the input dictionary of plot series
 #  string  suptitle        The parameter is the chart title.
 #  list    colors_list     The parameter is the list of colors for the subplots.
 #  string  supxlabel       The parameter is the title for the figure's x-axis.
 #  string  supylabel       The parameter is the title for the figure's y-axis.
 #  string  xlabel          The parameter is the title for the plot's x-axis.
 #  string  ylabel          The parameter is the title for the plot's y-axis.
 #  boolean first_ylabel_pad_bool
 #                          The parameter indicates whether the first subplot 
 #                          should have a different pad value.
 #  float   first_ylabel_pad_flt
 #                          The parameter is first subplot pad value.
 #  boolean ylabel_default_bool
 #                          The parameter indicates whether the y label will 
 #                          have the default value.
 #  boolean display_legend_bool
 #                          The parameter indicates whether the legend will be present.
 #  string  legend_loc      The parameter is the legend's general location.
 #  float   legend_font_size_flt
 #                          The parameter is legend's font size.
 #  tuple   legend_bbox_to_anchor_flt_tuple
 #                          The parameter is the legend's xy-coordinates. 
 #  float   suptitle_x_flt  The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_flt  The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_flt
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_weight
 #                          The parameter is the figure title's font weight.
 #  float   supxlabel_x_flt The parameter is the figure's x-axis label's 
 #                          x-coordinate padding.
 #  float   supxlabel_y_flt The parameter is the figure's x-axis label's 
 #                          y-coordinate padding.
 #  float   supxlabel_font_size_flt
 #                          The parameter is the figure's x-axis label's font size.
 #  string  supxlabel_font_weight
 #                          The parameter is the figure's x-axis label's font weight.
 #  float   supylabel_x_flt The parameter is the figure's y-axis label's 
 #                          x-coordinate padding.
 #  float   supylabel_y_flt The parameter is the figure's y-axis label's 
 #                          y-coordinate padding.
 #  float   supylabel_font_size_flt
 #                          The parameter is the figure's y-axis label's font size.
 #  string  supylabel_font_weight
 #                          The parameter is the figure's y-axis label's font weight.
 #  float   xlabel_pad_flt  The parameter is the subplot's x-axis label's padding.
 #  float   xlabel_font_size_flt
 #                          The parameter is the subplot's x-axis label's font size.
 #  string  xlabel_loc      The parameter is the subplot's x-axis label's general location.
 #  string  xlabel_font_weight
 #                          The parameter is the subplot's x-axis label's font weight.
 #  float   ylabel_pad_flt  The parameter is the subplot's y-axis label's padding.
 #  float   ylabel_font_size_flt
 #                          The parameter is the subplot's y-axis label's font size.
 #  string  ylabel_loc      The parameter is the subplot's y-axis label's general location.
 #  string  ylabel_font_weight
 #                          The parameter is the subplot's y-axis label's font weight.
 #  float   xtick_label_size_flt
 #                          The parameter is the subplot's x-tick label's font size.
 #  float   xtick_label_rotation_flt
 #                          The parameter is the subplot's x-tick label's rotation in degrees.
 #  float   ytick_label_size_flt
 #                          The parameter is the subplot's y-tick label's font size.
 #  float   ytick_label_rotation_flt
 #                          The parameter is the subplot's y-tick label's rotation in degrees.
 #  float   subplot_width_space_flt
 #                          The parameter is the width of the space between subplots.
 #  float   subplot_height_space_flt
 #                          The parameter is the width of the space between subplots.
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/  

def display_stacked_line_subplots \
        (input_frame_dict,
         suptitle,
         colors_list,
         supxlabel = None,
         supylabel = None,
         xlabel = None,
         ylabel = None,
         first_ylabel_pad_bool = False,
         first_ylabel_pad_flt = 4.0,
         ylabel_default_bool = True,
         display_legend_bool = True,
         legend_loc = 'center right',
         legend_font_size_flt = 14.0,
         legend_bbox_to_anchor_flt_tuple = (1.12, 0.5),
         suptitle_x_flt = 0.5,  
         suptitle_y_flt = 1.0,  
         suptitle_font_size_flt = 20.0,
         suptitle_font_weight = 'normal',
         supxlabel_x_flt = 0.5,  
         supxlabel_y_flt = -0.15,
         supxlabel_font_size_flt = 16.0,
         supxlabel_font_weight = 'normal',
         supylabel_x_flt = 0.0,  
         supylabel_y_flt = 0.5,  
         supylabel_font_size_flt = 16.0,
         supylabel_font_weight = 'normal',
         xlabel_pad_flt = 4.0,
         xlabel_font_size_flt = 16.0,
         xlabel_loc = 'center',
         xlabel_font_weight = 'normal',
         ylabel_pad_flt = 4.0,
         ylabel_font_size_flt = 16.0,
         ylabel_loc = 'center',
         ylabel_font_weight = 'normal',
         xtick_label_size_flt = 14.0,
         xtick_label_rotation_flt = 90.0,
         ytick_label_size_flt = 14.0,
         ytick_label_rotation_flt = 0.0,
         subplot_width_space_flt = None,
         subplot_height_space_flt = None,
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    input_df = pd.DataFrame(input_frame_dict)

    subplot_count_int = len(input_df.keys())


    if xlabel == None:

        xlabel = ''


    fig, axs \
        = plt.subplots \
            (subplot_count_int, figsize = (figure_width_flt, figure_length_flt))

    fig.suptitle \
        (suptitle,
         x = suptitle_x_flt,
         y = suptitle_y_flt,
         fontsize = suptitle_font_size_flt, 
         fontweight = suptitle_font_weight)

    if supxlabel != None:

        fig.supxlabel \
            (supxlabel,
             x = supxlabel_x_flt,
             y = supxlabel_y_flt,
             fontsize = supxlabel_font_size_flt, 
             fontweight = supxlabel_font_weight)

    if supylabel != None:

        fig.supylabel \
            (supylabel,
             x = supylabel_x_flt,
             y = supylabel_y_flt,
             fontsize = supylabel_font_size_flt, 
             fontweight = supylabel_font_weight)


    legend_line_plot_list = []

    legend_line_names_list = []


    for index, subplot in enumerate(axs):

        line_subplot, \
            = subplot.plot \
                (input_df.iloc[:,index], color = colors_list[index])

        legend_line_plot_list.append(line_subplot)

        legend_line_names_list.append(input_df.iloc[:,index].name)

        subplot.grid()


        if index == (subplot_count_int - 1):

            subplot.set_xlabel \
                (xlabel, 
                 labelpad = xlabel_pad_flt, 
                 fontsize = xlabel_font_size_flt, 
                 loc = xlabel_loc, 
                 fontweight = xlabel_font_weight)

        else:

            subplot.set_xticklabels(labels = [])


        if ylabel == None:

            ylabel = input_df.iloc[:,index].name


        if index == 0 and first_ylabel_pad_bool == True:

            subplot.set_ylabel \
                (ylabel, 
                 labelpad = first_ylabel_pad_flt, 
                 fontsize = ylabel_font_size_flt, 
                 loc = ylabel_loc, 
                 fontweight = ylabel_font_weight)

        else:

            subplot.set_ylabel \
                (ylabel, 
                 labelpad = ylabel_pad_flt, 
                 fontsize = ylabel_font_size_flt, 
                 loc = ylabel_loc, 
                 fontweight = ylabel_font_weight)


        subplot.tick_params \
            (axis = 'x', 
             labelrotation = xtick_label_rotation_flt, 
             labelsize = xtick_label_size_flt)

        subplot.tick_params \
            (axis = 'y', 
             labelrotation = ytick_label_rotation_flt, 
             labelsize = ytick_label_size_flt)


    if display_legend_bool == True:

        fig.legend \
            (legend_line_plot_list, 
             legend_line_names_list, 
             loc = legend_loc,
             fontsize = legend_font_size_flt,
             bbox_to_anchor = legend_bbox_to_anchor_flt_tuple)


    plt.subplots_adjust \
        (wspace = subplot_width_space_flt, 
         hspace = subplot_height_space_flt)


    logx.save_plot_image(suptitle)

    plt.show()


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  display_boxplots_from_series_list
 #
 #  Function Description:
 #      The function displays a box plot from a list of series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_series_list
 #                          The parameter is the input series list.
 #  list    xticks_label_list
 #                          The parameter is the list of a-axis tick labels.
 #  string  title           The parameter is the chart title.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  float   box_widths_flt  The parameter is the width of boxes in the chart.    
 #  boolean mean_line_bool  The parameter indicates whether the mean lines are present.
 #  boolean show_means_bool The parameter indicates whether the means are present.
 #  boolean vertical_bool   The parameter indicates whether the boxplot is vertical.
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   xlabel_font_size_flt
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_flt  The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_flt
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_flt  The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_flt
 #                          The parameter is the x-axis tick font size. 
 #  float   xticks_rotation_flt
 #                          The parameter is the x-axis tick rotation in degrees.
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_boxplots_from_series_list \
        (input_series_list,
         xticks_label_list,
         title,
         xlabel = '',
         ylabel = '',
         box_widths_flt = 0.45,
         mean_line_bool = True,
         show_means_bool = True,
         vertical_bool = True,
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 20.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xticks_font_size_flt = 14.0,
         xticks_rotation_flt = 0.0,
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    fig1, axs = plt.subplots(figsize = (figure_width_flt, figure_length_flt))

    axs.boxplot \
        (input_series_list,
         vert = vertical_bool,
         widths = box_widths_flt,
         meanline = mean_line_bool, 
         showmeans = show_means_bool)

    axs.set_title \
        (title,
         fontdict = {'fontsize': title_font_size_flt, 
                     'fontstyle': title_font_style},
         pad = title_pad_flt)

    axs.set_xlabel \
        (xlabel,
         fontdict = {'fontsize': xlabel_font_size_flt, 
                     'fontstyle': xlabel_font_style},
         labelpad = xlabel_pad_flt)

    axs.set_ylabel \
        (ylabel,
         fontdict = {'fontsize': ylabel_font_size_flt, 
                     'fontstyle': ylabel_font_style},
         labelpad = ylabel_pad_flt)


    ticks_index_int_list = []

    for index, regimen in enumerate(xticks_label_list):

        ticks_index_int_list.append(index + 1)


    axs.set_xticks \
        (ticks_index_int_list, 
         xticks_label_list,
         fontsize = xticks_font_size_flt,
         rotation = xticks_rotation_flt)


    if vertical_bool == True:

        plt.grid(axis = 'y')

    else:

        plt.grid(axis = 'x')


    logx.save_plot_image(title)

    plt.show()


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  display_boxplot_from_df
 #
 #  Function Description:
 #      The function displays a box plot from a dataframe.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    input_df        The parameter is the input dataframe.
 #  string  x_column        The parameter is the dataframe column with the x-variable data.
 #  string  y_column        The parameter is the dataframe column with the y-variable data.
 #  string  suptitle        The parameter is the figure title.
 #  string  title           The parameter is the chart title.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  float   box_widths_flt  The parameter is the width of boxes in the chart.    
 #  boolean mean_line_bool  The parameter indicates whether the mean lines are present.
 #  boolean show_means_bool The parameter indicates whether the means are present.
 #  boolean vertical_bool   The parameter indicates whether the boxplot is vertical.
 #  boolean grid_bool       The parameter indicates whether the boxplot displays a grid.
 #  float   suptitle_x_flt  The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_flt  The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_flt
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_weight
 #                          The parameter is the figure title's font weight.
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   xlabel_font_size_flt
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_flt  The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_flt
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_flt  The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_flt
 #                          The parameter is the x-axis tick font size. 
 #  float   xticks_rotation_flt
 #                          The parameter is the x-axis tick rotation in degrees. 
 #  float   yticks_font_size_flt
 #                          The parameter is the y-axis tick font size. 
 #  float   yticks_rotation_flt
 #                          The parameter is the y-axis tick rotation in degrees. 
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_boxplot_from_df \
        (input_df,
         x_column,
         y_column,
         suptitle = '',
         title = '',
         xlabel = '',
         ylabel = '',
         box_widths_flt = 0.45,
         mean_line_bool = True,
         show_means_bool = True,
         vertical_bool = True,
         grid_bool = True,
         suptitle_x_flt = 0.5,  
         suptitle_y_flt = 1.01, 
         suptitle_font_size_flt = 20.0,
         suptitle_font_style = 'normal',
         title_font_size_flt = 16.0,
         title_font_style = 'normal',
         title_pad_flt = 10.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xticks_font_size_flt = 14.0,
         xticks_rotation_flt = 90.0,
         yticks_font_size_flt = 14.0,
         yticks_rotation_flt = 0.0,
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):


    box_plot_axes \
        = input_df \
            .boxplot \
                (by = x_column,
                 column = [y_column], 
                 fontsize = xticks_font_size_flt,
                 widths = box_widths_flt,
                 meanline = mean_line_bool,
                 showmeans = show_means_bool,
                 vert = vertical_bool,
                 grid = grid_bool,
                 figsize = (figure_width_flt, figure_length_flt))

    plt.suptitle \
        (suptitle,
         x = suptitle_x_flt,
         y = suptitle_y_flt,
         fontsize = suptitle_font_size_flt, 
         fontstyle = suptitle_font_style)

    plt.title \
        (title,
         fontdict = {'fontsize': title_font_size_flt, 
                     'fontstyle': title_font_style},
         pad = title_pad_flt)

    plt.xlabel \
        (xlabel,
         fontdict = {'fontsize': xlabel_font_size_flt, 
                     'fontstyle': xlabel_font_style},
         labelpad = xlabel_pad_flt)

    plt.ylabel \
        (ylabel,
         fontdict = {'fontsize': ylabel_font_size_flt, 
                     'fontstyle': ylabel_font_style},
         labelpad = ylabel_pad_flt)


    plt.xticks(fontsize = xticks_font_size_flt, rotation = xticks_rotation_flt)

    plt.yticks(fontsize = yticks_font_size_flt, rotation = yticks_rotation_flt)


    logx.save_plot_image(suptitle)

    plt.show()


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  display_bar_chart_from_series
 #
 #  Function Description:
 #      The function displays a bar chart from a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    The parameter is the input series.
 #  string  title           The parameter is the chart title.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel           The parameter is the y-axis label.
 #  list    bar_colors_list The parameter is the list of bar chart bar colors.
 #  boolean horizontal_bool The parameter indicates whether the bar chart is horizontal.
 #  string  bar_align       The parameter is bar alignment.
 #  string  edge_color      The parameter is the bar edge color.
 #  float   line_width_flt  The parameter is the bar line width.       
 #  float   alpha_flt       The parameter is the bar transparency level (0-1.0).
 #  float   bar_width_flt   The parameter is the bar width.
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   xlabel_font_size_flt
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_flt  The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_flt
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_flt  The parameter is the y-axis space pad value. 
 #  float  xtick_label_rotation_flt
 #                          The parameter is the x-axis tick rotation. 
 #  float  xtick_font_size_flt
 #                          The parameter is the x-axis tick font size.
 #  float  ytick_label_rotation_flt
 #                          The parameter is the y-axis tick rotation. 
 #  float  ytick_font_size_flt
 #                          The parameter is the y-axis tick font size. 
 #  float  figure_width_flt The parameter is the figure width. 
 #  float  figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_bar_chart_from_series \
        (input_series,
         title,
         xlabel,
         ylabel,
         bar_colors_list,
         horizontal_bool = False,
         bar_align = 'center',
         edge_color = 'black',
         line_width_flt = 1.5,
         bar_width_flt = 0.5,
         alpha_flt = 1.0,
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 20.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xtick_label_rotation_flt = 80.0,
         xtick_font_size_flt = 14.0,
         ytick_label_rotation_flt = 0.0,
         ytick_font_size_flt = 14.0,        
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    plt.figure(figsize = (figure_width_flt, figure_length_flt))


    if horizontal_bool == False:

        plt.bar \
            (input_series.keys(),
             input_series,
             align = bar_align,
             color = bar_colors_list,
             edgecolor = edge_color,
             linewidth = line_width_flt,
             alpha = alpha_flt,
             width = bar_width_flt)

    else:

        plt.barh \
            (input_series.keys(),
             input_series,
             align = bar_align,
             color = bar_colors_list,
             edgecolor = edge_color,
             linewidth = line_width_flt,
             alpha = alpha_flt)


    plt.title \
        (title,
         fontdict = {'fontsize': title_font_size_flt, 
                     'fontstyle': title_font_style},
         pad = title_pad_flt)


    plt.xlabel \
        (xlabel,
         fontdict = {'fontsize': xlabel_font_size_flt, 
                     'fontstyle': xlabel_font_style},
         labelpad = xlabel_pad_flt)

    plt.ylabel \
        (ylabel,
         fontdict = {'fontsize': ylabel_font_size_flt, 
                     'fontstyle': ylabel_font_style},
         labelpad = ylabel_pad_flt)


    plt.xticks \
        (rotation = xtick_label_rotation_flt,
         fontsize = xtick_font_size_flt)

    plt.yticks \
        (rotation = ytick_label_rotation_flt,
         fontsize = ytick_font_size_flt)


    plt.grid(axis = 'y')


    logx.save_plot_image(title)

    plt.show()


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  display_bar_chart_from_df
 #
 #  Function Description:
 #      The function displays a bar chart from a dataframe.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_df        The parameter is the input dataframe.
 #  string  title           The parameter is the chart title.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  list    bar_colors_list
 #                          The parameter is the list of bar colors.
 #  boolean stacked_bool    The parameter indicates whether the bar chart is stacked.
 #  boolean legend_bool     The parameter indicates whether the legend is present.
 #  tuple   legend_bbox_to_anchor_flt_tuple
 #                          The parameter is the legend's xy-coordinates. 
 #  string  bar_align       The parameter is bar alignment.
 #  string  edge_color      The parameter is the bar edge color.
 #  float   line_width_flt  The parameter is the bar line width.       
 #  float   alpha_flt       The parameter is the bar transparency level (0-1.0).
 #  float   bar_width_flt   The parameter is the bar width.
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   xlabel_font_size_flt
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_flt  The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_flt
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_flt  The parameter is the y-axis space pad value. 
 #  float   xtick_label_rotation_flt
 #                          The parameter is the x-axis tick rotation. 
 #  float   xtick_font_size_flt
 #                          The parameter is the x-axis tick font size.
 #  float   ytick_label_rotation_flt
 #                          The parameter is the y-axis tick rotation. 
 #  float   ytick_font_size_flt
 #                          The parameter is the y-axis tick font size. 
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_bar_chart_from_df \
        (input_df,
         title,
         xlabel,
         ylabel,
         bar_colors_list,
         stacked_bool = False,
         legend_bool = False,
         legend_bbox_to_anchor_flt_tuple = (1.1, 1.05),
         bar_align = 'center',
         edge_color = 'black',
         line_width_flt = 1.5,
         bar_width_flt = 0.5,
         alpha_flt = 1.0,
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 20.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xtick_label_rotation_flt = 80.0,
         xtick_font_size_flt = 14.0,
         ytick_label_rotation_flt = 0.0,
         ytick_font_size_flt = 14.0,
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    input_df.plot.bar \
        (stacked = stacked_bool,
         align = bar_align,
         color = bar_colors_list,
         edgecolor = edge_color,
         linewidth = line_width_flt,
         alpha = alpha_flt,
         width = bar_width_flt, 
         legend = legend_bool,
         figsize = (figure_width_flt, figure_length_flt))

    if legend_bool == True:

        plt.legend \
            (bbox_to_anchor \
                 = (legend_bbox_to_anchor_flt_tuple[0], 
                    legend_bbox_to_anchor_flt_tuple[1]))


    plt.title \
        (title,
         fontdict = {'fontsize': title_font_size_flt, 
                     'fontstyle': title_font_style},
         pad = title_pad_flt)

    plt.xlabel \
        (xlabel,
         fontdict = {'fontsize': xlabel_font_size_flt,
                     'fontstyle': xlabel_font_style},
         labelpad = xlabel_pad_flt)

    plt.ylabel \
        (ylabel,
         fontdict = {'fontsize': ylabel_font_size_flt,
                     'fontstyle': ylabel_font_style},
         labelpad = ylabel_pad_flt)

    plt.xticks \
        (rotation = xtick_label_rotation_flt,
         fontsize = xtick_font_size_flt)

    plt.yticks \
        (rotation = ytick_label_rotation_flt,
         fontsize = ytick_font_size_flt)


    plt.grid(axis = 'y')

    logx.save_plot_image(title)

    plt.show()


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  display_scatter_plot_from_xy_series
 #
 #  Function Description:
 #      The function displays a scatter plot from x-y series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series        The parameter is the x-axis series.
 #  series  y_series        The parameter is the y-axis series.
 #  string  title           The parameter is the chart title.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  integer degree_int      The parameter is the degree of the regression line polynomial.
 #  float   equation_x_coord_flt
 #                          The parameter is the equation's x-coordinate.  
 #  float   equation_y_coord_flt
 #                          The parameter is the equation's y-coordinate.  
 #  string  marker_shape    The parameter is marker shape.
 #  float   marker_size_flt The parameter is the marker size.       
 #  string  marker_color    The parameter is the marker color.
 #  float   line_width_flt  The parameter is line width of the scatter points.
 #  string  edge_colors     The parameter is the edge color for the scatter points.
 #  float   alpha_flt       The parameter is the bar transparency level (0-1.0).
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   xlabel_font_size_flt
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_flt  The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_flt
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_flt  The parameter is the y-axis space pad value. 
 #  float   xtick_label_rotation_flt
 #                          The parameter is the x-axis tick rotation. 
 #  float   xtick_font_size_flt
 #                          The parameter is the x-axis tick font size.
 #  float   ytick_label_rotation_flt
 #                          The parameter is the y-axis tick rotation. 
 #  float   ytick_font_size_flt
 #                          The parameter is the y-axis tick font size. 
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_scatter_plot_from_xy_series \
        (x_series, 
         y_series, 
         title,
         xlabel,
         ylabel,
         degree_int = 0,
         equation_x_coord_flt = 0.0,
         equation_y_coord_flt = 0.0,
         marker_shape = 'o',
         marker_size_flt = 80.0,
         marker_color = 'lime',
         line_width_flt = 1.5,
         edge_colors = 'black',
         alpha_flt = 0.8,
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 20.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xtick_label_rotation_flt = 0.0,
         xtick_font_size_flt = 14.0,
         ytick_label_rotation_flt = 0.0,
         ytick_font_size_flt = 14.0,        
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    plt.figure(figsize = (figure_width_flt, figure_length_flt))

    plt.scatter \
        (x_series, 
         y_series, 
         marker = marker_shape,
         s = marker_size_flt,
         color = marker_color, 
         linewidth = line_width_flt,
         edgecolors = edge_colors,
         alpha = alpha_flt)

    plt.title \
        (title, 
         fontdict = {'fontsize': title_font_size_flt, 
                     'fontstyle': title_font_style},
         pad = title_pad_flt)

    plt.xlabel \
        (xlabel,
         fontdict = {'fontsize': xlabel_font_size_flt, 
                     'fontstyle': xlabel_font_style},
         labelpad = xlabel_pad_flt)

    plt.ylabel \
        (ylabel,
         fontdict = {'fontsize': ylabel_font_size_flt, 
                     'fontstyle': ylabel_font_style},
         labelpad = ylabel_pad_flt)

    plt.xticks \
        (rotation = xtick_label_rotation_flt,
         fontsize = xtick_font_size_flt)

    plt.yticks \
        (rotation = ytick_label_rotation_flt,
         fontsize = ytick_font_size_flt)

    plt.grid()


    if degree_int == 1:

        display_linear_regression_line \
            (x_series, y_series,
             equation_x_coord_flt,
             equation_y_coord_flt)

    elif degree_int > 1:

        display_polynomial_regression_line \
            (x_series, y_series,
             equation_x_coord_flt,
             equation_y_coord_flt,
             degree_int)


    logx.save_plot_image(title)

    plt.show()


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  display_multiple_scatter_plots_from_xy_series_list
 #
 #  Function Description:
 #      The function displays multiple scatter plots from x-y series lists.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  x_series_list   The parameter is the x-axis series list.
 #  series  y_series_list   The parameter is the y-axis series list.
 #  string  titles_list     The parameter is the chart title list.
 #  string  suptitle        The parameter is the figure title.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  integer degree_int      The parameter is the degree of the regression line polynomial.
 #  float   equation_x_coord_flt_list
 #                          The parameter is the list of equation's x-coordinates.  
 #  float   equation_y_coord_flt_list
 #                          The parameter is the list of equation's y-coordinate.  
 #  string  marker_shape    The parameter is marker shape.
 #  float   marker_size_flt The parameter is the marker size.       
 #  string  marker_color    The parameter is the marker color.
 #  float   line_width_flt  The parameter is line width of the scatter points.
 #  string  edge_colors     The parameter is the edge color for the scatter points.
 #  float   alpha_flt       The parameter is the bar transparency level (0-1.0).
 #  float   suptitle_font_size_flt
 #                          The parameter is the figure title font size. 
 #  string  suptitle_font_style
 #                          The parameter is the figure title font style.
 #  float   suptitle_pad_flt
 #                          The parameter is the figure title space pad value. 
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   xlabel_font_size_flt
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_flt  The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_flt
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_flt  The parameter is the y-axis space pad value. 
 #  float   xtick_label_rotation_flt
 #                          The parameter is the x-axis tick rotation. 
 #  float   xtick_font_size_flt
 #                          The parameter is the x-axis tick font size.
 #  float   ytick_label_rotation_flt
 #                          The parameter is the y-axis tick rotation. 
 #  float   ytick_font_size_flt
 #                          The parameter is the y-axis tick font size. 
 #  float   tight_layout_pad_flt
 #                          The parameter is the figure tight layout padding. 
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_multiple_scatter_plots_from_xy_series_list \
        (x_series_list,
         y_series_list,
         titles_list,
         suptitle,
         xlabel,
         ylabel,
         degree_int = 0,
         equation_x_coord_flt_list = 0.0,
         equation_y_coord_flt_list = 0.0,
         marker_shape = 'o',
         marker_size_flt = 80.0,
         marker_color = 'lime',
         line_width_flt = 1.5,
         edge_colors = 'black',
         alpha_flt = 0.8,
         suptitle_font_size_flt = 20.0,
         suptitle_font_weight = 'normal',
         suptitle_pad_flt = 1.0,         
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 20.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xtick_label_rotation_flt = 0.0,
         xtick_font_size_flt = 14.0,
         ytick_label_rotation_flt = 0.0,
         ytick_font_size_flt = 14.0,
         tight_layout_pad_flt = 3.0,
         figure_width_flt = 15.0,
         figure_length_flt = 5.5181):

    scatter_plot_count_int = len(x_series_list)

    if scatter_plot_count_int != len(y_series_list):

        logx.print_and_log_text \
            ('The function, display_multiple_scatter_plots_from_xy_series_list, '
              + f'in source file, {CONSTANT_LOCAL_FILE_NAME},'
              + f'with the caption, {suptitle},'
              + 'was unable to display scatter plots '
              + 'because the number of x and y series did not match.')


    plt.subplots(figsize = (figure_width_flt, figure_length_flt))

    plt.clf()


    x_length_int, y_length_int \
        = mathx.calculate_closest_factors(scatter_plot_count_int)


    for index in range(0, scatter_plot_count_int):

        plt.subplot(x_length_int, y_length_int, index + 1)

        plt.scatter \
            (x_series_list[index], 
             y_series_list[index], 
             marker = marker_shape,
             s = marker_size_flt,
             color = marker_color, 
             linewidth = line_width_flt,
             edgecolors = edge_colors,
             alpha = alpha_flt)

        plt.title \
            (titles_list[index], 
             fontdict = {'fontsize': title_font_size_flt, 
                         'fontstyle': title_font_style},
             pad = title_pad_flt)

        plt.xlabel \
            (xlabel,
             fontdict = {'fontsize': xlabel_font_size_flt, 
                        'fontstyle': xlabel_font_style},
             labelpad = xlabel_pad_flt)

        plt.ylabel \
            (ylabel,
             fontdict = {'fontsize': ylabel_font_size_flt, 
                         'fontstyle': ylabel_font_style},
             labelpad = ylabel_pad_flt)

        plt.xticks \
            (rotation = xtick_label_rotation_flt,
             fontsize = xtick_font_size_flt)

        plt.yticks \
            (rotation = ytick_label_rotation_flt,
             fontsize = ytick_font_size_flt)

        plt.grid()


        if degree_int == 1:

            logx.print_and_log_text(titles_list[index] + ':')

            display_linear_regression_line \
                (x_series_list[index],
                 y_series_list[index],
                 equation_x_coord_flt_list[index],
                 equation_y_coord_flt_list[index])

        elif degree_int > 1:

            logx.print_and_log_text(titles_list[index] + ':')

            display_polynomial_regression_line \
                (x_series_list[index],
                 y_series_list[index],
                 equation_x_coord_flt_list[index],
                 equation_y_coord_flt_list[index],
                 degree_int)

        plt.tight_layout(pad = tight_layout_pad_flt)

        plt.suptitle \
            (suptitle, 
             fontsize = suptitle_font_size_flt,
             fontweight = suptitle_font_weight,
             y = suptitle_pad_flt)

        logx.save_plot_image(suptitle)

        plt.show()


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  display_pie_chart_from_series
 #
 #  Function Description:
 #      The function displays a pie chart from a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    The parameter is the input series.
 #  string  title           The parameter is the figure title.
 #  list    colors_list     The parameter is the list of pie wedge colors.
 #  tuple   explode_flt_tuple   
 #                          The parameter is the degree of separation for each pie wedge.
 #  boolean shadow_bool     The parameter indicates whether the pie chart is shadowed.
 #  float   pct_distance_flt
 #                          The parameter is the percent distance between pie wedges.  
 #  float   start_angle_flt The parameter is the pie chart's start angle.
 #  string  auto_pct        The parameter is percent format for pie wedges.
 #  float   label_distance_flt
 #                          The parameter is the label's distance from the center.
 #  float   chart_font_size_flt
 #                          The parameter is the chart text font size.       
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_pie_chart_from_series \
        (input_series,
         title,
         colors_list,
         explode_flt_tuple,
         shadow_bool = True,
         pct_distance_flt = 0.75,
         start_angle_flt = 45.0,
         auto_pct = '%1.1f%%',
         label_distance_flt = 1.1,
         chart_font_size_flt = 14.0,
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 5.0,
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    temp_series = input_series.copy()

    temp_series.rename(None, inplace = True)


    plt.figure(figsize = (figure_width_flt, figure_length_flt))

    plt.pie \
        (temp_series,
         labels = temp_series.index, 
         colors = colors_list,   
         explode = explode_flt_tuple, 
         shadow = shadow_bool,
         pctdistance = pct_distance_flt,
         startangle = start_angle_flt,
         autopct = auto_pct,
         labeldistance = label_distance_flt,
         textprops = {'fontsize': chart_font_size_flt})

    plt.title \
        (title,
         fontdict = {'fontsize': title_font_size_flt, 
                     'fontstyle': title_font_style},
         pad = title_pad_flt)   


    logx.save_plot_image(title)

    plt.show()


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  display_multiple_pie_charts_from_df
 #
 #  Function Description:
 #      The function receives a dataframe and formatting parameters for the display
 #      of multiple pie charts.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_df        The parameter is the input dataframe
 #  string  suptitle        The parameter is the chart title.
 #  list    colors_list     The parameter is the list of pie wedge colors.
 #  tuple   explode_flt_tuple   
 #                          The parameter is the degree of separation for each pie wedge.
 #  boolean shadow_bool     The parameter indicates whether the pie chart is shadowed.
 #  float   pct_distance_flt
 #                          The parameter is the percent distance between pie wedges.  
 #  float   start_angle_flt The parameter is the pie chart's start angle.
 #  string  auto_pct        The parameter is percent format for pie wedges.
 #  float   label_distance_flt
 #                          The parameter is the label's distance from the center.
 #  float   chart_font_size_flt
 #                          The parameter is the chart text font size.  
 #  float   suptitle_x_flt  The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_flt  The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_flt
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_weight
 #                          The parameter is the figure title's font weight.
 #  string  titles_list     The parameter is the list of chart titles.
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   title_y_flt     The parameter is the title's y-axis displacement.
 #  string  xlabel          The parameter is the subplot's x-axis label.
 #  float   xlabel_pad_flt  The parameter is the subplot's x-axis label's padding.
 #  float   xlabel_font_size_flt
 #                          The parameter is the subplot's x-axis label's font size.
 #  string  xlabel_loc      The parameter is the subplot's x-axis label's general location.
 #  string  xlabel_font_weight
 #                          The parameter is the subplot's x-axis label's font weight.
 #  string  ylabel          The parameter is the subplot's y-axis label.
 #  float   ylabel_pad_flt  The parameter is the subplot's y-axis label's padding.
 #  float   ylabel_font_size_flt
 #                          The parameter is the subplot's y-axis label's font size.
 #  string  ylabel_loc      The parameter is the subplot's y-axis label's general location.
 #  string  ylabel_font_weight
 #                          The parameter is the subplot's y-axis label's font weight.
 #  float   subplot_width_space_flt
 #                          The parameter is the width of the space between subplots.
 #  float   subplot_height_space_flt
 #                          The parameter is the width of the space between subplots.
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/  

def display_multiple_pie_charts_from_df \
        (input_df,
         suptitle,
         colors_list,
         explode_flt_tuple,
         shadow_bool = True,
         pct_distance_flt = 0.75,
         start_angle_flt = 45.0,
         auto_pct = '%1.1f%%',
         label_distance_flt = 1.2,
         chart_font_size_flt = 12.0,
         suptitle_x_flt = 0.5,  
         suptitle_y_flt = 0.9,  
         suptitle_font_size_flt = 20.0,
         suptitle_font_weight = 'normal',
         titles_list = [],
         title_font_size_flt = 18.0,
         title_font_style = 'normal',
         title_pad_flt = 5.0,
         title_y_flt = 1.05,
         xlabel = '',
         xlabel_pad_flt = 4.0,
         xlabel_font_size_flt = 16.0,
         xlabel_loc = 'center',
         xlabel_font_weight = 'normal',
         ylabel = '',
         ylabel_pad_flt = 4.0,
         ylabel_font_size_flt = 16.0,
         ylabel_loc = 'center',
         ylabel_font_weight = 'normal',
         subplot_width_space_flt = 1.1,
         subplot_height_space_flt = None,
         figure_width_flt = 15.0,
         figure_length_flt = 5.5181):

    chart_count_int = len(input_df.columns)

    row_count_int, column_count_int \
        = mathx.calculate_closest_factors(chart_count_int)

    index = 0


    fig, axs \
        = plt.subplots \
            (nrows = row_count_int, ncols = column_count_int,
             figsize = (figure_width_flt, figure_length_flt),
             tight_layout = True)

    fig.suptitle \
        (suptitle,
         x = suptitle_x_flt,
         y = suptitle_y_flt,
         fontsize = suptitle_font_size_flt, 
         fontweight = suptitle_font_weight)


    for row in range(row_count_int):
        for column in range(column_count_int):

            input_df.iloc[:, index].plot.pie \
                (ax = axs[index],
                 colors = colors_list, 
                 shadow = shadow_bool,
                 pctdistance = pct_distance_flt,
                 startangle = start_angle_flt, 
                 autopct = auto_pct,
                 labeldistance = label_distance_flt,
                 textprops = {'fontsize': chart_font_size_flt},
                 subplots = True)


            if len(titles_list) <= 0:

                title = input_df.iloc[:, index].name

            else:

                title = titles_list[index]


            axs[index].set_title \
                (title,
                 fontdict = {'fontsize': title_font_size_flt, 
                             'fontstyle': title_font_style},
                 pad = title_pad_flt,
                 y = title_y_flt)


            axs[index].set_xlabel \
                (xlabel, 
                 labelpad = xlabel_pad_flt, 
                 fontsize = xlabel_font_size_flt, 
                 loc = xlabel_loc, 
                 fontweight = xlabel_font_weight)

            axs[index].set_ylabel \
                (ylabel, 
                 labelpad = ylabel_pad_flt, 
                 fontsize = ylabel_font_size_flt, 
                 loc = ylabel_loc, 
                 fontweight = ylabel_font_weight)


            index += 1


    plt.subplots_adjust \
        (wspace = subplot_width_space_flt, 
         hspace = subplot_height_space_flt)


    logx.save_plot_image(suptitle)

    plt.show()


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  display_histogram_from_series
 #
 #  Function Description:
 #      The function displays a histogram from a series and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    The parameter is the input series.
 #  string  title           The parameter is the chart title.
 #  list    color           The parameter is the color of the histogram.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  integer bins_count_int  The parameter is the number of histogram bins.
 #  float   alpha_flt       The parameter is the alpha (transparency) value.
 #  boolean grid_bool       The parameter indicates whether the boxplot displays a grid.
 #  string  fill_style      The parameter is the line fills style.
 #  float   line_width_flt  The parameter is the line width around a histogram box.       
 #  string  edge_color      The parameter is the histogram box edge color.
 #  boolean display_legend_bool
 #                          The parameter indicates whether the legend will be present.
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   xlabel_font_size_flt
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_flt  The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_flt
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_flt  The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_flt
 #                          The parameter is the subplot's x-tick label's font size.
 #  float   xticks_rotation_flt
 #                          The parameter is the subplot's x-tick label's rotation in degrees.
 #  float   yticks_font_size_flt
 #                          The parameter is the subplot's y-tick label's font size.
 #  float   yticks_rotation_flt
 #                          The parameter is the subplot's y-tick label's rotation in degrees.
 #  string  legend_loc      The parameter is the legend's general location.
 #  float   legend_font_size_flt
 #                          The parameter is legend's font size.
 #  tuple   legend_bbox_to_anchor_flt_tuple
 #                          The parameter is the legend's xy-coordinates. 
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_histogram_from_series \
        (input_series,
         title,
         color,
         xlabel = None,
         ylabel = None,
         bins_count_int = 20,
         alpha_flt = 1.0,
         grid_bool = True,
         line_width_flt = 1.5,
         edge_color = 'black',
         display_legend_bool = False,
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 20.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xticks_font_size_flt = 14.0,
         xticks_rotation_flt = 90.0,
         yticks_font_size_flt = 14.0,
         yticks_rotation_flt = 0.0,
         legend_loc = 'center right',
         legend_font_size_flt = 14.0,
         legend_bbox_to_anchor_flt_tuple = (1.5, 0.5),
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    input_series \
        .plot.hist \
            (bins = bins_count_int, 
             alpha = alpha_flt, 
             color = color, 
             linewidth = line_width_flt, 
             edgecolor = edge_color, 
             legend = display_legend_bool,
             figsize = (figure_width_flt, figure_length_flt))


    plt.title \
        (title,
         fontdict = {'fontsize': title_font_size_flt, 
                     'fontstyle': title_font_style},
         pad = title_pad_flt)


    if xlabel != None:

        plt.xlabel \
            (xlabel,
             fontdict = {'fontsize': xlabel_font_size_flt,
                         'fontstyle': xlabel_font_style},
             labelpad = xlabel_pad_flt)

    if ylabel != None:

        plt.ylabel \
            (ylabel,
             fontdict = {'fontsize': ylabel_font_size_flt,
                         'fontstyle': ylabel_font_style},
             labelpad = ylabel_pad_flt)


    plt.xticks(fontsize = xticks_font_size_flt, rotation = xticks_rotation_flt)

    plt.yticks(fontsize = yticks_font_size_flt, rotation = yticks_rotation_flt)


    if display_legend_bool == True:

        plt.legend \
            (loc = legend_loc,
             fontsize = legend_font_size_flt,
             bbox_to_anchor = legend_bbox_to_anchor_flt_tuple)


    logx.save_plot_image(title)


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  display_histograms_from_series_list
 #
 #  Function Description:
 #      The function receives a series list and formatting parameters for the display
 #      of multiple histograms in a single figure.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    The parameter is the input dataframe
 #  string  suptitle        The parameter is the chart title.
 #  string  supxlabel       The parameter is the title for the figure's x-axis.
 #  string  supylabel       The parameter is the title for the figure's y-axis.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  list    color           The parameter is the histogram color.
 #  boolean reverse_dimensions_bool 
 #                          The parameter indicates whether the histograms share the x-axis.
 #  boolean share_x_bool    The parameter indicates whether the histograms share the x-axis.
 #  boolean share_y_bool    The parameter indicates whether the histograms share the y-axis.
 #  boolean tight_layout_bool  
 #                          The parameter indicates whether the figure has a tight layout.
 #  integer bins_count_int  The parameter is the number of histogram bins.
 #  float   alpha_flt       The parameter is the alpha (transparency) value.
 #  boolean grid_bool       The parameter indicates whether the boxplot displays a grid.
 #  float   line_width_flt  The parameter is the line width around a histogram box.       
 #  string  edge_color      The parameter is the histogram box edge color.
 #  float   suptitle_x_flt  The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_flt  The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_flt
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_style
 #                          The parameter is the figure title's font style.
 #  float   supxlabel_x_flt The parameter is the figure's x-axis label's 
 #                          x-coordinate padding.
 #  float   supxlabel_y_flt The parameter is the figure's x-axis label's 
 #                          y-coordinate padding.
 #  float   supxlabel_font_size_flt
 #                          The parameter is the figure's x-axis label's font size.
 #  string  supxlabel_font_style
 #                          The parameter is the figure's x-axis label's font style.
 #  float   supylabel_x_flt The parameter is the figure's y-axis label's 
 #                          x-coordinate padding.
 #  float   supylabel_y_flt The parameter is the figure's y-axis label's 
 #                          y-coordinate padding.
 #  float   supylabel_font_size_flt
 #                          The parameter is the figure's y-axis label's font size.
 #  string  supylabel_font_style
 #                          The parameter is the figure's y-axis label's font style.
 #  string  titles_list     The parameter is the list of chart titles.
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   title_y_flt     The parameter is the title's y-axis displacement.
 #  string  xlabel          The parameter is the subplot's x-axis label.
 #  float   xlabel_pad_flt  The parameter is the subplot's x-axis label's padding.
 #  float   xlabel_font_size_flt
 #                          The parameter is the subplot's x-axis label's font size.
 #  string  xlabel_loc      The parameter is the subplot's x-axis label's general location.
 #  string  xlabel_font_style
 #                          The parameter is the subplot's x-axis label's font style.
 #  string  ylabel          The parameter is the subplot's y-axis label.
 #  float   ylabel_pad_flt  The parameter is the subplot's y-axis label's padding.
 #  float   ylabel_font_size_flt
 #                          The parameter is the subplot's y-axis label's font size.
 #  string  ylabel_loc      The parameter is the subplot's y-axis label's general location.
 #  string  ylabel_font_style
 #                          The parameter is the subplot's y-axis label's font style.
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/  

def display_histograms_from_series_list \
        (input_series_list,
         suptitle,
         supxlabel = None,
         supylabel = None,
         xlabel = '',
         ylabel = '',
         color = 'firebrick',
         reverse_dimensions_bool = True,
         share_x_bool = True,
         share_y_bool = True,
         tight_layout_bool = True,
         bins_count_int = 20,
         alpha_flt = 1.0,
         grid_bool = True,
         line_width_flt = 1.5,
         edge_color = 'black',
         suptitle_x_flt = 0.5,  
         suptitle_y_flt = 0.9,  
         suptitle_font_size_flt = 20.0,
         suptitle_font_weight = 'normal',
         supxlabel_x_flt = 0.5,  
         supxlabel_y_flt = 0.0,  
         supxlabel_font_size_flt = 16.0,
         supxlabel_font_weight = 'normal',
         supylabel_x_flt = 0.0,  
         supylabel_y_flt = 0.5,  
         supylabel_font_size_flt = 16.0,
         supylabel_font_weight = 'normal',
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 20.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         tight_layout_flt = 3.0,
         figure_width_flt = 15.0,
         figure_length_flt = 7.5):

    chart_count_int = len(input_series_list)

    colors_list = [color] * chart_count_int


    row_count_int, column_count_int \
        = mathx.calculate_closest_factors(chart_count_int)

    if reverse_dimensions_bool == True:

        row_count_int, column_count_int = column_count_int, row_count_int       


    fig, axs \
        = plt.subplots \
            (row_count_int, 
             column_count_int, 
             figsize = (figure_width_flt, figure_length_flt),
             sharex = share_x_bool,
             sharey = share_y_bool, 
             tight_layout = tight_layout_bool)


    plt.clf()


    fig.suptitle \
        (suptitle,
         x = suptitle_x_flt,
         y = suptitle_y_flt,
         fontsize = suptitle_font_size_flt, 
         fontweight = suptitle_font_weight)


    for index in range(chart_count_int):

        plt.subplot(row_count_int, column_count_int, index + 1)


        input_series_list[index] \
            .plot.hist \
                (bins = bins_count_int, 
                 alpha = alpha_flt,
                 grid = grid_bool,
                 color = colors_list[index], 
                 linewidth = line_width_flt, 
                 edgecolor = edge_color,
                 legend = False)


        plt.title \
            (input_series_list[index].name,
             fontdict = {'fontsize': title_font_size_flt, 
                         'fontstyle': title_font_style},
             pad = title_pad_flt)


        plt.xlabel \
            (xlabel,
             fontdict = {'fontsize': xlabel_font_size_flt,
                         'fontstyle': xlabel_font_style},
             labelpad = xlabel_pad_flt)

        plt.ylabel \
            (ylabel,
             fontdict = {'fontsize': ylabel_font_size_flt,
                         'fontstyle': ylabel_font_style},
             labelpad = ylabel_pad_flt)


        plt.tight_layout(pad = 3.0)


    if supxlabel != None:

        fig.supxlabel \
            (supxlabel,
             x = supxlabel_x_flt,
             y = supxlabel_y_flt,
             fontsize = supxlabel_font_size_flt, 
             fontweight = supxlabel_font_weight)

    if supylabel != None:

            fig.supylabel \
                (supylabel,
                 x = supylabel_x_flt,
                 y = supylabel_y_flt,
                 fontsize = supylabel_font_size_flt, 
                 fontweight = supylabel_font_weight)


    logx.save_plot_image(suptitle)

    plt.show()


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  display_multiple_histograms_from_df
 #
 #  Function Description:
 #      The function receives a dataframe and formatting parameters for the display
 #      of multiple histograms.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_df        The parameter is the input dataframe
 #  string  suptitle        The parameter is the chart title.
 #  list    colors_list     The parameter is the list of histogram colors.
 #  string  supxlabel       The parameter is the title for the figure's x-axis.
 #  string  supylabel       The parameter is the title for the figure's y-axis.
 #  boolean share_x_bool    The parameter indicates whether the histograms share the x-axis.
 #  boolean share_y_bool    The parameter indicates whether the histograms share the y-axis.
 #  boolean tight_layout_bool  
 #                          The parameter indicates whether the figure has a tight layout.
 #  integer bins_count_int  The parameter is the number of histogram bins.
 #  float   alpha_flt       The parameter is the alpha (transparency) value.
 #  boolean grid_bool       The parameter indicates whether the boxplot displays a grid.
 #  float   suptitle_x_flt  The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_flt  The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_flt
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_weight
 #                          The parameter is the figure title's font weight.
 #  float   supxlabel_x_flt The parameter is the figure's x-axis label's 
 #                          x-coordinate padding.
 #  float   supxlabel_y_flt The parameter is the figure's x-axis label's 
 #                          y-coordinate padding.
 #  float   supxlabel_font_size_flt
 #                          The parameter is the figure's x-axis label's font size.
 #  string  supxlabel_font_weight
 #                          The parameter is the figure's x-axis label's font weight.
 #  float   supylabel_x_flt The parameter is the figure's y-axis label's 
 #                          x-coordinate padding.
 #  float   supylabel_y_flt The parameter is the figure's y-axis label's 
 #                          y-coordinate padding.
 #  float   supylabel_font_size_flt
 #                          The parameter is the figure's y-axis label's font size.
 #  string  supylabel_font_weight
 #                          The parameter is the figure's y-axis label's font weight.
 #  string  titles_list     The parameter is the list of chart titles.
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   title_y_flt     The parameter is the title's y-axis displacement.
 #  string  xlabel          The parameter is the subplot's x-axis label.
 #  float   xlabel_pad_flt  The parameter is the subplot's x-axis label's padding.
 #  float   xlabel_font_size_flt
 #                          The parameter is the subplot's x-axis label's font size.
 #  string  xlabel_loc      The parameter is the subplot's x-axis label's general location.
 #  string  xlabel_font_weight
 #                          The parameter is the subplot's x-axis label's font weight.
 #  string  ylabel          The parameter is the subplot's y-axis label.
 #  float   ylabel_pad_flt  The parameter is the subplot's y-axis label's padding.
 #  float   ylabel_font_size_flt
 #                          The parameter is the subplot's y-axis label's font size.
 #  string  ylabel_loc      The parameter is the subplot's y-axis label's general location.
 #  string  ylabel_font_weight
 #                          The parameter is the subplot's y-axis label's font weight.
 #  float   xtick_label_size_flt
 #                          The parameter is the subplot's x-tick label's font size.
 #  float   xtick_label_rotation_flt
 #                          The parameter is the subplot's x-tick label's rotation in degrees.
 #  float   ytick_label_size_flt
 #                          The parameter is the subplot's y-tick label's font size.
 #  float   ytick_label_rotation_flt
 #                          The parameter is the subplot's y-tick label's rotation in degrees.
 #  float   subplot_width_space_flt
 #                          The parameter is the width of the space between subplots.
 #  float   subplot_height_space_flt
 #                          The parameter is the width of the space between subplots.
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/  

def display_multiple_histograms_from_df \
        (input_df,
         suptitle,
         colors_list,
         supxlabel = None,
         supylabel = None,
         share_x_bool = False,
         share_y_bool = True,
         tight_layout_bool = True,
         bins_count_int = 20,
         alpha_flt = 0.8,
         grid_bool = True,
         suptitle_x_flt = 0.5,  
         suptitle_y_flt = 1.0,  
         suptitle_font_size_flt = 20.0,
         suptitle_font_weight = 'normal',
         supxlabel_x_flt = 0.5,  
         supxlabel_y_flt = 0.0,  
         supxlabel_font_size_flt = 16.0,
         supxlabel_font_weight = 'normal',
         supylabel_x_flt = 0.0,  
         supylabel_y_flt = 0.5,  
         supylabel_font_size_flt = 16.0,
         supylabel_font_weight = 'normal',
         titles_list = [],
         title_font_size_flt = 18.0,
         title_font_style = 'normal',
         title_pad_flt = 5.0,
         title_y_flt = 1.05,
         xlabel = '',
         xlabel_pad_flt = 4.0,
         xlabel_font_size_flt = 16.0,
         xlabel_loc = 'center',
         xlabel_font_weight = 'normal',
         ylabel = '',
         ylabel_pad_flt = 4.0,
         ylabel_font_size_flt = 16.0,
         ylabel_loc = 'center',
         ylabel_font_weight = 'normal',
         xtick_label_size_flt = 14.0,
         xtick_label_rotation_flt = 0.0,
         ytick_label_size_flt = 14.0,
         ytick_label_rotation_flt = 0.0,
         subplot_width_space_flt = 1.1,
         subplot_height_space_flt = None,
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    chart_count_int = len(input_df.columns)

    row_count_int, column_count_int \
        = mathx.calculate_closest_factors(chart_count_int)

    index = 0


    fig, axs \
        = plt.subplots \
            (nrows = row_count_int, ncols = column_count_int,
             figsize = (figure_width_flt, figure_length_flt),
             sharex = share_x_bool,
             sharey = share_y_bool, 
             tight_layout = tight_layout_bool)

    fig.suptitle \
        (suptitle,
         x = suptitle_x_flt,
         y = suptitle_y_flt,
         fontsize = suptitle_font_size_flt, 
         fontweight = suptitle_font_weight)


    ax = axs.ravel()


    for row in range(row_count_int):
        for column in range(column_count_int):

            input_df.iloc[:, index].hist \
                (ax = ax[index],
                 color = colors_list[index], 
                 bins = bins_count_int,
                 alpha = alpha_flt,
                 grid = grid_bool)


            if len(titles_list) <= 0:

                title = input_df.keys()[index]

            else:

                title = titles_list[index]


            ax[index].set_title \
                (title,
                 fontdict = {'fontsize': title_font_size_flt, 
                             'fontstyle': title_font_style},
                 pad = title_pad_flt,
                 y = title_y_flt)

            ax[index].set_xlabel \
                (xlabel, 
                 labelpad = xlabel_pad_flt, 
                 fontsize = xlabel_font_size_flt, 
                 loc = xlabel_loc, 
                 fontweight = xlabel_font_weight)

            ax[index].set_ylabel \
                (ylabel, 
                 labelpad = ylabel_pad_flt, 
                 fontsize = ylabel_font_size_flt, 
                 loc = ylabel_loc, 
                 fontweight = ylabel_font_weight)

            ax[index].tick_params \
                (axis = 'x', 
                 labelrotation = xtick_label_rotation_flt, 
                 labelsize = xtick_label_size_flt)

            ax[index].tick_params \
                (axis = 'y', 
                 labelrotation = ytick_label_rotation_flt, 
                 labelsize = ytick_label_size_flt)

            index += 1


    if supxlabel != None:

        fig.supxlabel \
            (supxlabel,
             x = supxlabel_x_flt,
             y = supxlabel_y_flt,
             fontsize = supxlabel_font_size_flt, 
             fontweight = supxlabel_font_weight)

    if supylabel != None:

            fig.supylabel \
                (supylabel,
                 x = supylabel_x_flt,
                 y = supylabel_y_flt,
                 fontsize = supylabel_font_size_flt, 
                 fontweight = supylabel_font_weight)


    plt.subplots_adjust \
        (wspace = subplot_width_space_flt, 
         hspace = subplot_height_space_flt)


    logx.save_plot_image(suptitle)

    plt.show()


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  display_plot_from_series
 #
 #  Function Description:
 #      The function displays a plot from a series and criteria.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    The parameter is the input series.
 #  string  title           The parameter is the chart title.
 #  list    color           The parameter is the color of the histogram.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  float   alpha_flt       The parameter is the alpha (transparency) value.
 #  boolean grid_bool       The parameter indicates whether the boxplot displays a grid.
 #  boolean display_legend_bool
 #                          The parameter indicates whether the legend will be present.
 #  nparray display_legend_bool
 #                          The parameter is the positions of peaks in the graph.
 #  string  peaks_marker_size_flt
 #                          The parameter is the size of the peaks markers.
 #  float   peaks_label_y_offset_flt
 #                          The parameter is the y-axis offset of the label
 #                          from the peaks marker. 
 #  list   peaks_color_list The parameter is the peaks marker and label colors. 
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   xlabel_font_size_flt
 #                          The parameter is the x-axis font size. 
 #  string  xlabel_font_style
 #                          The parameter is the x-axis font style.
 #  float   xlabel_pad_flt  The parameter is the x-axis space pad value. 
 #  float   ylabel_font_size_flt
 #                          The parameter is the y-axis font size. 
 #  string  ylabel_font_style
 #                          The parameter is the y-axis font style.
 #  float   ylabel_pad_flt  The parameter is the y-axis space pad value. 
 #  float   xticks_font_size_flt
 #                          The parameter is the subplot's x-tick label's font size.
 #  float   xticks_rotation_flt
 #                          The parameter is the subplot's x-tick label's rotation in degrees.
 #  float   yticks_font_size_flt
 #                          The parameter is the subplot's y-tick label's font size.
 #  float   yticks_rotation_flt
 #                          The parameter is the subplot's y-tick label's rotation in degrees.
 #  string  legend_loc      The parameter is the legend's general location.
 #  float   legend_font_size_flt
 #                          The parameter is legend's font size.
 #  tuple   legend_bbox_to_anchor_flt_tuple
 #                          The parameter is the legend's xy-coordinates. 
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def display_plot_from_series \
        (input_series,
         title,
         color,
         xlabel = None,
         ylabel = None,
         alpha_flt = 1.0,
         grid_bool = True,
         display_legend_bool = False,
         peaks_nparray = [],
         peaks_marker_size_flt = 15.0,
         peaks_font_size_flt = 12.0,
         peaks_label_y_offset_flt = 5.0,
         peaks_color_list = ['red', 'blue'],
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 20.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xticks_font_size_flt = 14.0,
         xticks_rotation_flt = 90.0,
         yticks_font_size_flt = 14.0,
         yticks_rotation_flt = 0.0,
         legend_loc = 'center right',
         legend_font_size_flt = 14.0,
         legend_bbox_to_anchor_flt_tuple = (1.5, 0.5),
         figure_width_flt = 9.708,
         figure_length_flt = 6.0):

    plt.figure(figsize = (figure_width_flt, figure_length_flt))

    plt.clf()


    input_series \
        .plot \
            (color = color,
             alpha = alpha_flt,
             grid = grid_bool,
             legend = display_legend_bool)

    if len(peaks_nparray) > 0:

        plt.plot \
            (input_series.index[peaks_nparray], 
             input_series.iloc[peaks_nparray], 
             'x', 
             markersize = peaks_marker_size_flt, 
             color = peaks_color_list[0])

        for i, j in zip(input_series.index[peaks_nparray], input_series.iloc[peaks_nparray]):

            y_coord_flt = j + peaks_label_y_offset_flt

            plt.annotate \
                (i, xy = (i, y_coord_flt), 
                 size = peaks_font_size_flt, 
                 color = peaks_color_list[1])


    plt.title \
        (title,
         fontdict = {'fontsize': title_font_size_flt, 
                     'fontstyle': title_font_style},
         pad = title_pad_flt)


    if xlabel != None:

        plt.xlabel \
            (xlabel,
             fontdict = {'fontsize': xlabel_font_size_flt,
                         'fontstyle': xlabel_font_style},
             labelpad = xlabel_pad_flt)

    if ylabel != None:

        plt.ylabel \
            (ylabel,
             fontdict = {'fontsize': ylabel_font_size_flt,
                         'fontstyle': ylabel_font_style},
             labelpad = ylabel_pad_flt)


    plt.xticks(fontsize = xticks_font_size_flt, rotation = xticks_rotation_flt)

    plt.yticks(fontsize = yticks_font_size_flt, rotation = yticks_rotation_flt)


    if display_legend_bool == True:

        plt.legend \
            (loc = legend_loc,
             fontsize = legend_font_size_flt,
             bbox_to_anchor = legend_bbox_to_anchor_flt_tuple)


    logx.save_plot_image(title)


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  display_plots_from_series_list
 #
 #  Function Description:
 #      The function receives a series list and formatting parameters for the display
 #      of plots in a single figure.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  input_series    The parameter is the input dataframe
 #  string  suptitle        The parameter is the chart title.
 #  string  supxlabel       The parameter is the title for the figure's x-axis.
 #  string  supylabel       The parameter is the title for the figure's y-axis.
 #  string  xlabel          The parameter is the x-axis label.
 #  string  ylabel          The parameter is the y-axis label.
 #  list    color           The parameter is the histogram color.
 #  boolean reverse_dimensions_bool 
 #                          The parameter indicates whether the histograms share the x-axis.
 #  boolean share_x_bool    The parameter indicates whether the histograms share the x-axis.
 #  boolean share_y_bool    The parameter indicates whether the histograms share the y-axis.
 #  boolean tight_layout_bool  
 #                          The parameter indicates whether the figure has a tight layout.
 #  float   alpha_flt       The parameter is the alpha (transparency) value.
 #  boolean grid_bool       The parameter indicates whether the boxplot displays a grid.
 #  float   suptitle_x_flt  The parameter is the figure title's x-coordinate padding.
 #  float   suptitle_y_flt  The parameter is the figure title's y-coordinate padding.
 #  float   suptitle_font_size_flt
 #                          The parameter is the figure title's font size.
 #  string  suptitle_font_style
 #                          The parameter is the figure title's font style.
 #  float   supxlabel_x_flt The parameter is the figure's x-axis label's 
 #                          x-coordinate padding.
 #  float   supxlabel_y_flt The parameter is the figure's x-axis label's 
 #                          y-coordinate padding.
 #  float   supxlabel_font_size_flt
 #                          The parameter is the figure's x-axis label's font size.
 #  string  supxlabel_font_style
 #                          The parameter is the figure's x-axis label's font style.
 #  float   supylabel_x_flt The parameter is the figure's y-axis label's 
 #                          x-coordinate padding.
 #  float   supylabel_y_flt The parameter is the figure's y-axis label's 
 #                          y-coordinate padding.
 #  float   supylabel_font_size_flt
 #                          The parameter is the figure's y-axis label's font size.
 #  string  supylabel_font_style
 #                          The parameter is the figure's y-axis label's font style.
 #  string  titles_list     The parameter is the list of chart titles.
 #  float   title_font_size_flt
 #                          The parameter is the title font size. 
 #  string  title_font_style
 #                          The parameter is the title font style.
 #  float   title_pad_flt   The parameter is the title space pad value. 
 #  float   title_y_flt     The parameter is the title's y-axis displacement.
 #  string  xlabel          The parameter is the subplot's x-axis label.
 #  float   xlabel_pad_flt  The parameter is the subplot's x-axis label's padding.
 #  float   xlabel_font_size_flt
 #                          The parameter is the subplot's x-axis label's font size.
 #  string  xlabel_loc      The parameter is the subplot's x-axis label's general location.
 #  string  xlabel_font_style
 #                          The parameter is the subplot's x-axis label's font style.
 #  string  ylabel          The parameter is the subplot's y-axis label.
 #  float   ylabel_pad_flt  The parameter is the subplot's y-axis label's padding.
 #  float   ylabel_font_size_flt
 #                          The parameter is the subplot's y-axis label's font size.
 #  string  ylabel_loc      The parameter is the subplot's y-axis label's general location.
 #  string  ylabel_font_style
 #                          The parameter is the subplot's y-axis label's font style.
 #  float   figure_width_flt
 #                          The parameter is the figure width. 
 #  float   figure_length_flt
 #                          The parameter is the figure length. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/  

def display_plots_from_series_list \
        (input_series_list,
         suptitle,
         supxlabel = None,
         supylabel = None,
         xlabel = '',
         ylabel = '',
         color = 'darkgreen',
         reverse_dimensions_bool = True,
         share_x_bool = True,
         share_y_bool = True,
         tight_layout_bool = True,
         alpha_flt = 1.0,
         grid_bool = True,
         suptitle_x_flt = 0.5,  
         suptitle_y_flt = 0.9,  
         suptitle_font_size_flt = 20.0,
         suptitle_font_weight = 'normal',
         supxlabel_x_flt = 0.5,  
         supxlabel_y_flt = 0.0,  
         supxlabel_font_size_flt = 16.0,
         supxlabel_font_weight = 'normal',
         supylabel_x_flt = 0.0,  
         supylabel_y_flt = 0.5,  
         supylabel_font_size_flt = 16.0,
         supylabel_font_weight = 'normal',
         title_font_size_flt = 20.0,
         title_font_style = 'normal',
         title_pad_flt = 20.0,
         xlabel_font_size_flt = 16.0,
         xlabel_font_style = 'normal',
         xlabel_pad_flt = 10.0,
         ylabel_font_size_flt = 16.0,
         ylabel_font_style = 'normal',
         ylabel_pad_flt = 10.0,
         xticks_font_size_flt = 14.0,
         xticks_rotation_flt = 90.0,
         yticks_font_size_flt = 14.0,
         yticks_rotation_flt = 0.0,
         tight_layout_flt = 3.0,
         figure_width_flt = 15.0,
         figure_length_flt = 10.0):

    chart_count_int = len(input_series_list)

    colors_list = [color] * chart_count_int


    row_count_int, column_count_int \
        = mathx.calculate_closest_factors(chart_count_int)

    if reverse_dimensions_bool == True:

        row_count_int, column_count_int = column_count_int, row_count_int       


    fig, axs \
        = plt.subplots \
            (row_count_int, 
             column_count_int, 
             figsize = (figure_width_flt, figure_length_flt),
             sharex = share_x_bool,
             sharey = share_y_bool, 
             tight_layout = tight_layout_bool)


    plt.clf()


    fig.suptitle \
        (suptitle,
         x = suptitle_x_flt,
         y = suptitle_y_flt,
         fontsize = suptitle_font_size_flt, 
         fontweight = suptitle_font_weight)


    for index in range(chart_count_int):

        plt.subplot(row_count_int, column_count_int, index + 1)


        input_series_list[index] \
            .plot \
                (color = colors_list[index], 
                 alpha = alpha_flt, 
                 grid = grid_bool,
                 legend = False)


        plt.title \
            (input_series_list[index].name,
             fontdict = {'fontsize': title_font_size_flt, 
                         'fontstyle': title_font_style},
             pad = title_pad_flt)


        plt.xlabel \
            (xlabel,
             fontdict = {'fontsize': xlabel_font_size_flt,
                         'fontstyle': xlabel_font_style},
             labelpad = xlabel_pad_flt)

        plt.ylabel \
            (ylabel,
             fontdict = {'fontsize': ylabel_font_size_flt,
                         'fontstyle': ylabel_font_style},
             labelpad = ylabel_pad_flt)

        plt.xticks(fontsize = xticks_font_size_flt, rotation = xticks_rotation_flt)

        plt.yticks(fontsize = yticks_font_size_flt, rotation = yticks_rotation_flt)


        plt.tight_layout(pad = 3.0)


    if supxlabel != None:

        fig.supxlabel \
            (supxlabel,
             x = supxlabel_x_flt,
             y = supxlabel_y_flt,
             fontsize = supxlabel_font_size_flt, 
             fontweight = supxlabel_font_weight)

    if supylabel != None:

            fig.supylabel \
                (supylabel,
                 x = supylabel_x_flt,
                 y = supylabel_y_flt,
                 fontsize = supylabel_font_size_flt, 
                 fontweight = supylabel_font_weight)


    logx.save_plot_image(suptitle)

    plt.show()


# In[ ]:




