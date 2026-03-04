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
 #  get_xylabels
 #  set_xylabels
 #  get_bar_chart_xylabels
 #  set_bar_chart_xylabels
 #  get_boxplot_chart_xylabels
 #  set_boxplot_chart_xylabels
 #  get_histogram_chart_xylabels
 #  set_histogram_chart_xylabels
 #  get_line_chart_xylabels
 #  set_line_chart_xylabels
 #  get_pie_chart_xylabels
 #  set_pie_chart_xylabels
 #  get_plot_chart_xylabels
 #  set_plot_chart_xylabels
 #  get_scatterplot_chart_xylabels
 #  set_scatterplot_chart_xylabels
 #  get_scatterplot_multichart_xylabels
 #  set_scatterplot_multichart_xylabels
 #
 #  get_regr_line_dict
 #  set_regr_line_dict
 #  get_regr_degree
 #  set_regr_degree
 #  get_regr_eqn_coords
 #  set_regr_eqn_coords
 #
 #  get_bar_chart_dict
 #  set_bar_chart_dict
 #  get_bar_chart_colors
 #  set_bar_chart_colors
 #
 #  get_boxplot_chart_dict
 #  set_boxplot_chart_dict
 #
 #  get_histogram_chart_dict
 #  set_histogram_chart_dict
 #
 #  get_line_chart_dict
 #  set_line_chart_dict
 #
 #  get_pie_chart_dict
 #  set_pie_chart_dict
 #  get_pie_chart_colors
 #  set_pie_chart_colors
 #  get_pie_chart_explode
 #  set_pie_chart_explode
 #
 #  get_plot_chart_dict
 #  set_plot_chart_dict
 #
 #  get_scatterplot_chart_dict
 #  set_scatterplot_chart_dict
 #
 #  get_scatterplot_multichart_dict
 #  set_scatterplot_multichart_dict
 #
 #  proc_boxplot_chart_input
 #  proc_bar_chart_input
 #  proc_line_chart_input
 #  proc_pie_chart_input
 #  proc_plot_chart_input
 #  proc_scatterplot_chart_input
 #  proc_scatterplot_multichart_input
 #  proc_chart_input
 #
 #  linear_regr_line
 #  regr_line
 #
 #  plot_subplots
 #  plot_subplot
 #
 #  plot_figsize
 #  plot_title_axes
 #  plot_limits
 #  plot_ticks
 #  plot_legend
 #  plot_regr_line
 #  plot_peaks
 #  plot_suptitle_axes
 #  plot_tight_layout
 #
 #  plot_bar_chart_series
 #  plot_bar_chart_df
 #  plot_bar_chart
 #  plot_boxplot_chart
 #  plot_histogram_chart
 #  plot_line_chart
 #  plot_pie_chart
 #  plot_plot_chart
 #  plot_scatterplot_chart
 #
 #  boxplot_chart
 #  bar_chart
 #  histogram_chart
 #  line_chart
 #  pie_chart
 #  plot_chart
 #  scatterplot_chart
 #
 #  scatterplot_multichart
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #  02/24/2026          Upgraded Module                             Nicholas J. George
 #
 #******************************************************************************************/

import logx
import dtypesx
import mathx

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from enum import Enum, auto
from scipy import stats

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'matplotlibx.py'


# In[3]:


class chart_enum(Enum):

    BAR = auto()

    BOXPLOT = auto()

    HISTOGRAM = auto()

    LINE = auto()

    PIE = auto()

    PLOT = auto()

    SCATTER = auto()

    MULTISCATTER = auto()


# In[4]:


regr_line_dict \
    = {'degree': 0,
       'eqn_x_coord': 0.0,
       'eqn_y_coord': 0.0,
       'linecolor': 'red',
       'linewidth': 3.0,
       'alpha': 1.0,
       'coef_prec': 4,
       'fontsize': 16.0,
       'fontweight': 'bold',
       'fontcolor': 'blue'}


# In[5]:


bar_chart_dict \
    = {'params': {'horizontal': False,
                  'stacked': False,
                  'align': 'center',
                  'color': None,
                  'edgecolor': 'black',
                  'linewidth': 1.5,
                  'tick_label': None,
                  'log': False,
                  'alpha': 1.0},
       'vertical': {'width': 0.5,
                    'bottom': 0},
       'horizontal': {'height': 0.5,
                      'left': 0},
       'title': {'text': None,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'pad': 20.0},
       'xlabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'ylabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'xlim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 90.0},
       'yticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'y'},
       'legend': {'display': False,
                  'loc': 'center right',
                  'fontsize': 14.0,
                  'bbox_to_anchor': (1.5, 0.5)},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[6]:


boxplot_chart_dict \
    = {'params': {'notch': False, 
                  'vert': True, 
                  'orientation': 'vertical', 
                  'whis': 1.5, 
                  'widths': 0.45, 
                  'patch_artist': False, 
                  'autorange': False, 
                  'meanline': True,
                  'showmeans': True},
       'title': {'text': None,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'pad': 20.0},
       'xlabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'ylabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'xlim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 90.0},
       'yticks': {'display': False,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'y'},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[7]:


histogram_chart_dict \
    = {'params': {'bins': 10,
                  'range': None,
                  'density': False,
                  'weights': None,
                  'cumulative': False,
                  'bottom': 0,
                  'histtype': 'bar',
                  'align': 'mid',
                  'orientation': 'vertical',
                  'rwidth': None,
                  'log': False,
                  'color': None,
                  'label': None,
                  'stacked': False,
                  'edgecolor': 'black',
                  'color': 'white',
                  'linewidth': 1.5,
                  'alpha': 1.0},
       'title': {'text': None,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'pad': 20.0},
       'xlabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'ylabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'xlim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 90.0},
       'yticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': False,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': False,
                  'loc': 'center right',
                  'fontsize': 14.0,
                  'bbox_to_anchor': (1.5, 0.5)},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[8]:


line_chart_dict \
    = {'line': {'color': 'darkslategray',
                'linestyle': 'solid',
                'fillstyle': 'full',
                'linewidth': 3.0,
                'alpha': 1.0},
       'marker': {'shape': 'o',
                  'color': 'red',
                  'edgecolor': 'black',
                  'size': 10.0,
                  'edgewidth': 1.0},
       'params': {'logx': False,
                  'logy': False,
                  'loglog': False,
                  'stacked': False,
                  'use_index': True},
       'title': {'text': None,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'pad': 20.0},
       'xlabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'ylabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'xlim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'yticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': False,
                  'loc': 'center right',
                  'fontsize': 14.0,
                  'bbox_to_anchor': (1.5, 0.5)},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[9]:


pie_chart_dict \
    = {'params': {'explode': None,
                  'colors': None,
                  'hatch': None,
                  'autopct': '%1.1f%%',
                  'pctdistance': 0.6,
                  'labeldistance': 1.1,
                  'shadow': True,
                  'startangle': 45.0,
                  'radius': 1.0,
                  'counterclock': True,
                  'wedgeprops': None,
                  'textprops': {'fontsize': 14.0,
                                'fontstyle': 'normal'},
                  'center': (0, 0),
                  'frame': False,
                  'rotatelabels': False,
                  'normalize': True},
       'title': {'text': None,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'pad': 20.0},
       'xlabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'ylabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'legend': {'display': False,
                  'loc': 'center right',
                  'fontsize': 14.0,
                  'bbox_to_anchor': (1.5, 0.5)},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[10]:


plot_chart_dict \
    = {'params': {'scalex': True, 
                  'scaley': True,
                  'color': None,
                  'alpha': 1.0},
       'peaks': {'display': False,
                 'array': [],
                 'markersize': 15.0,
                 'fontsize': 12.0,
                 'y_offset': 5.0,
                 'color': np.array(['red', 'blue'])},
       'title': {'text': None,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'pad': 20.0},
       'xlabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'ylabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'xlim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 90.0},
       'yticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': False,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': False,
                  'loc': 'center right',
                  'fontsize': 14.0,
                  'bbox_to_anchor': (1.5, 0.5)},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[11]:


scatterplot_chart_dict \
    = {'marker': {'shape': 'o',
                  'size': 80.0,
                  'color': 'lime',
                  'linewidth': 1.5,
                  'edgecolors': 'black',
                  'alpha': 0.8},
       'title': {'text': None,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'pad': 20.0},
       'xlabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'ylabel': {'text': None,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'pad': 10.0},
       'xlim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 90.0},
       'yticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[12]:


scatterplot_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'normal',
                                       'size': 20.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.01,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'normal',
                                        'size': 16.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.5,
                     'y': 0.01,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'normal',
                                        'size': 16.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  get_xylabels
 #
 #  Function Description:
 #      The function retrieves the chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_xylabels(chart_type):

    if chart_type == chart_enum.BAR.value:

        return \
            bar_chart_dict['xlabel']['text'], \
            bar_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.BOXPLOT.value:

        return \
            boxplot_chart_dict['xlabel']['text'], \
            boxplot_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.HISTOGRAM.value:

        return \
            histogram_chart_dict['xlabel']['text'], \
            histogram_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.LINE.value:

        return \
            line_chart_dict['xlabel']['text'], \
            line_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.PIE.value:

        return \
            pie_chart_dict['xlabel']['text'], \
            pie_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.PLOT.value:

        return \
            plot_chart_dict['xlabel']['text'], \
            plot_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.SCATTER.value:

        return \
            scatterplot_chart_dict['xlabel']['text'], \
            scatterplot_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.MULTISCATTER.value:

        return \
            scatterplot_multichart_dict['xlabel']['text'], \
            scatterplot_multichart_dict['ylabel']['text']

    else: return None, None


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  set_xylabels
 #
 #  Function Description:
 #      The function sets the chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_xylabels \
        (xlabel,
         ylabel,
         chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['xlabel']['text'] = xlabel
        bar_chart_dict['ylabel']['text'] = ylabel

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['xlabel']['text'] = xlabel
        boxplot_chart_dict['ylabel']['text'] = ylabel

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['xlabel']['text'] = xlabel
        histogram_chart_dict['ylabel']['text'] = ylabel

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['xlabel']['text'] = xlabel
        line_chart_dict['ylabel']['text'] = ylabel

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['xlabel']['text'] = xlabel
        pie_chart_dict['ylabel']['text'] = ylabel

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['xlabel']['text'] = xlabel
        plot_chart_dict['ylabel']['text'] = ylabel

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['xlabel']['text'] = xlabel
        scatterplot_chart_dict['ylabel']['text'] = ylabel

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['xlabel']['text'] = xlabel
        scatterplot_multichart_dict['ylabel']['text'] = ylabel


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_xylabels
 #
 #  Function Description:
 #      The function retrieves the bar chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_xylabels():

    return get_xylabels(chart_enum.BAR.value)


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_xylabels
 #
 #  Function Description:
 #      The function sets the bar chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_xylabels \
        (xlabel, 
         ylabel):

    set_xylabels(xlabel, ylabel, chart_enum.BAR.value)


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  get_boxplot_chart_xylabels
 #
 #  Function Description:
 #      The function retrieves the boxplot chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_boxplot_chart_xylabels():

    return get_xylabels(chart_enum.BOXPLOT.value)


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  set_boxplot_chart_xylabels
 #
 #  Function Description:
 #      The function sets the boxplot chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_boxplot_chart_xylabels \
        (xlabel, 
         ylabel):

    set_xylabels(xlabel, ylabel, chart_enum.BOXPLOT.value)


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  get_histogram_chart_xylabels
 #
 #  Function Description:
 #      The function retrieves the histogram chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_histogram_chart_xylabels():

    return get_xylabels(chart_enum.HISTOGRAM.value)


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  set_histogram_chart_xylabels
 #
 #  Function Description:
 #      The function sets the histogram chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_histogram_chart_xylabels \
        (xlabel, 
         ylabel):

    set_xylabels(xlabel, ylabel, chart_enum.HISTOGRAM.value)


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  get_line_chart_xylabels
 #
 #  Function Description:
 #      The function retrieves the line chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_line_chart_xylabels():

    return get_xylabels(chart_enum.LINE.value)


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  set_line_chart_xylabels
 #
 #  Function Description:
 #      The function sets the line chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_line_chart_xylabels \
        (xlabel, 
         ylabel):

    set_xylabels(xlabel, ylabel, chart_enum.LINE.value)


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  get_pie_chart_xylabels
 #
 #  Function Description:
 #      The function retrieves the pie chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_pie_chart_xylabels():

    return get_xylabels(chart_enum.PIE.value)


# In[24]:


#*******************************************************************************************
 #
 #  Function Name:  set_pie_chart_xylabels
 #
 #  Function Description:
 #      The function sets the pie chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_pie_chart_xylabels \
        (xlabel, 
         ylabel):

    set_xylabels(xlabel, ylabel, chart_enum.PIE.value)


# In[25]:


#*******************************************************************************************
 #
 #  Function Name:  get_plot_chart_xylabels
 #
 #  Function Description:
 #      The function retrieves the plot chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_plot_chart_xylabels():

    return get_xylabels(chart_enum.PLOT.value)


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  set_plot_chart_xylabels
 #
 #  Function Description:
 #      The function sets the plot chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_plot_chart_xylabels \
        (xlabel, 
         ylabel):

    set_xylabels(xlabel, ylabel, chart_enum.PLOT.value)


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  get_scatterplot_chart_xylabels
 #
 #  Function Description:
 #      The function retrieves the scatter plot chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_scatterplot_chart_xylabels():

    return get_xylabels(chart_enum.SCATTER.value)


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  set_scatterplot_chart_xylabels
 #
 #  Function Description:
 #      The function sets the scatter plot chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_scatterplot_chart_xylabels \
        (xlabel, 
         ylabel):

    set_xylabels(xlabel, ylabel, chart_enum.SCATTER.value)


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  get_scatterplot_multichart_xylabels
 #
 #  Function Description:
 #      The function retrieves the scatter plot multichart's x-axis label and y-axis label.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_scatterplot_multichart_xylabels():

    return get_xylabels(chart_enum.MULTISCATTER.value)


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  set_scatterplot_multichart_xylabels
 #
 #  Function Description:
 #      The function sets the scatter plot multichart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_scatterplot_multichart_xylabels \
        (xlabel, 
         ylabel):

    set_xylabels(xlabel, ylabel, chart_enum.MULTISCATTER.value)


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  get_regr_line_dict
 #
 #  Function Description:
 #      The function retrieves the global regression line dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_regr_line_dict():

    return regr_line_dict


# In[32]:


#*******************************************************************************************
 #
 #  Function Name:  set_regr_line_dict
 #
 #  Function Description:
 #      The function sets the global regression line dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated regression line
 #                                  dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_regr_line_dict(upd_dict):

    global regr_line_dict

    regr_line_dict = upd_dict


# In[33]:


#*******************************************************************************************
 #
 #  Function Name:  get_regr_degree
 #
 #  Function Description:
 #      The function retrieves the regression line degree.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_regr_degree():

    return regr_line_dict['degree']


# In[34]:


#*******************************************************************************************
 #
 #  Function Name:  set_regr_degree
 #
 #  Function Description:
 #      The function sets the regression line degree.
 #
 #
 #  Return Type: n/a
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

def set_regr_degree(input_obj):

    global regr_line_dict

    if isinstance(input_obj, int) == True:

        regr_line_dict['degree'] = [abs(input_obj)]

    elif isinstance(input_obj, float) == True:

        regr_line_dict['degree'] = [int(abs(input_obj))]

    elif isinstance(input_obj, list) == True:

        regr_line_dict['degree'] = np.array(input_obj)

    elif isinstance(input_obj, np.ndarray) == True:

        regr_line_dict['degree'] = input_obj

    elif isinstance(input_obj, pd.Series) == True:

        regr_line_dict['degree'] = input_obj.to_numpy()


# In[35]:


#*******************************************************************************************
 #
 #  Function Name:  get_regr_line_dict
 #
 #  Function Description:
 #      The function retrieves the regression equations x-axis and y-axis coordinates.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_regr_eqn_coords():

    return regr_line_dict['eqn_x_coord'], regr_line_dict['eqn_y_coord']


# In[36]:


#*******************************************************************************************
 #
 #  Function Name:  set_regr_eqn_coords
 #
 #  Function Description:
 #      The function sets the regression equations x-axis and y-axis coordinates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         x_crd_obj        The parameter is the regression equation's
 #                                  x-coordinate.
 #  object         y_crd_obj        The parameter is the regression equation's
 #                                  y-coordinate.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_regr_eqn_coords(x_crd_obj, y_crd_obj):

    global regr_line_dict


    if isinstance(x_crd_obj, int) == True \
        or isinstance(x_crd_obj, float) == True:

        regr_line_dict['eqn_x_coord'] = [x_crd_obj]

    elif isinstance(x_crd_obj, list) == True:

        regr_line_dict['eqn_x_coord'] = x_crd_obj


    if isinstance(y_crd_obj, int) == True \
        or isinstance(y_crd_obj, float) == True:

        regr_line_dict['eqn_y_coord'] = [y_crd_obj]

    elif isinstance(y_crd_obj, list) == True:

        regr_line_dict['eqn_y_coord'] = y_crd_obj  


# In[37]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_dict
 #
 #  Function Description:
 #      The function retrieves the global bar chart dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_dict():

    return bar_chart_dict


# In[38]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_dict
 #
 #  Function Description:
 #      The function sets the global bar chart dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated bar chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_dict(upd_dict):

    global bar_chart_dict

    bar_chart_dict = upd_dict


# In[39]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_colors
 #
 #  Function Description:
 #      The function retrieves the bar chart face colors.
 #
 #
 #  Return Type: string or list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_colors():

    return bar_chart_dict['params']['color']


# In[40]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_colors
 #
 #  Function Description:
 #      The function sets the bar chart face colors.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         upd_obj          The parameter is the updated group of bar chart 
 #                                  colors.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_colors(upd_obj):

    global bar_chart_dict

    bar_chart_dict['params']['color'] \
        = dtypesx.cnv_data_to_array(upd_obj)


# In[41]:


#*******************************************************************************************
 #
 #  Function Name:  get_boxplot_chart_dict
 #
 #  Function Description:
 #      The function retrieves the global boxplot chart dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_boxplot_chart_dict():

    return boxplot_chart_dict


# In[42]:


#*******************************************************************************************
 #
 #  Function Name:  set_boxplot_chart_dict
 #
 #  Function Description:
 #      The function sets the global boxplot chart dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated boxplot chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_boxplot_chart_dict(upd_dict):

    global boxplot_chart_dict

    boxplot_chart_dict = upd_dict


# In[43]:


#*******************************************************************************************
 #
 #  Function Name:  get_histogram_chart_dict
 #
 #  Function Description:
 #      The function retrieves the global histogram chart dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_histogram_chart_dict():

    return histogram_chart_dict


# In[44]:


#*******************************************************************************************
 #
 #  Function Name:  set_histogram_chart_dict
 #
 #  Function Description:
 #      The function sets the global histogram chart dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated histogram chart 
 #                                  dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_histogram_chart_dict(upd_dict):

    global histogram_chart_dict

    histogram_chart_dict = upd_dict


# In[45]:


#*******************************************************************************************
 #
 #  Function Name:  get_line_chart_dict
 #
 #  Function Description:
 #      The function retrieves the global line chart dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_line_chart_dict():

    return line_chart_dict


# In[46]:


#*******************************************************************************************
 #
 #  Function Name:  set_line_chart_dict
 #
 #  Function Description:
 #      The function sets the global line chart dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated line chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_line_chart_dict(upd_dict):

    global line_chart_dict

    line_chart_dict = upd_dict


# In[47]:


#*******************************************************************************************
 #
 #  Function Name:  get_pie_chart_dict
 #
 #  Function Description:
 #      The function retrieves the global pie chart dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_pie_chart_dict():

    return pie_chart_dict


# In[48]:


#*******************************************************************************************
 #
 #  Function Name:  set_pie_chart_dict
 #
 #  Function Description:
 #      The function sets the global line chart dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated pie chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_pie_chart_dict(upd_dict):

    global pie_chart_dict

    pie_chart_dict = upd_dict


# In[49]:


#*******************************************************************************************
 #
 #  Function Name:  get_pie_chart_colors
 #
 #  Function Description:
 #      The function retrieves the pie chart colors.
 #
 #
 #  Return Type: array, list, or tuple
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_pie_chart_colors():

    return pie_chart_dict['params']['colors']


# In[50]:


#*******************************************************************************************
 #
 #  Function Name:  set_pie_chart_colors
 #
 #  Function Description:
 #      The function sets the pie chart colors.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         upd_obj          The parameter is the updated group of pie chart 
 #                                  colors.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_pie_chart_colors(upd_obj):

    global pie_chart_dict

    pie_chart_dict['params']['colors'] \
        = dtypesx.cnv_data_to_array(upd_obj)


# In[51]:


#*******************************************************************************************
 #
 #  Function Name:  get_pie_chart_explode
 #
 #  Function Description:
 #      The function retrieves the pie chart explode values.
 #
 #
 #  Return Type: array, list, or tuple
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_pie_chart_explode():

    return pie_chart_dict['params']['explode']


# In[52]:


#*******************************************************************************************
 #
 #  Function Name:  set_pie_chart_explode
 #
 #  Function Description:
 #      The function sets the pie chart explode values.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         upd_obj          The parameter is the updated group of pie chart 
 #                                  explode values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_pie_chart_explode(upd_obj):

    global pie_chart_dict

    pie_chart_dict['params']['explode'] \
        = dtypesx.cnv_data_to_array(upd_obj)


# In[53]:


#*******************************************************************************************
 #
 #  Function Name:  get_plot_chart_dict
 #
 #  Function Description:
 #      The function retrieves the global plot chart dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_plot_chart_dict():

    return plot_chart_dict


# In[54]:


#*******************************************************************************************
 #
 #  Function Name:  set_plot_chart_dict
 #
 #  Function Description:
 #      The function sets the global plot chart dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated plot chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_plot_chart_dict(upd_dict):

    global plot_chart_dict

    plot_chart_dict = upd_dict


# In[55]:


#*******************************************************************************************
 #
 #  Function Name:  get_scatterplot_chart_dict
 #
 #  Function Description:
 #      The function retrieves the global scatterplot chart dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_scatterplot_chart_dict():

    return scatterplot_chart_dict


# In[56]:


#*******************************************************************************************
 #
 #  Function Name:  set_scatterplot_chart_dict
 #
 #  Function Description:
 #      The function sets the global scatterplot chart dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated scatterplot chart 
 #                                  dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_scatterplot_chart_dict(upd_dict):

    global scatterplot_chart_dict

    scatterplot_chart_dict = upd_dict


# In[57]:


#*******************************************************************************************
 #
 #  Function Name:  get_scatterplot_multichart_dict
 #
 #  Function Description:
 #      The function retrieves the global scatterplot multichart dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_scatterplot_multichart_dict():

    return scatterplot_multichart_dict


# In[58]:


#*******************************************************************************************
 #
 #  Function Name:  set_scatterplot_multichart_dict
 #
 #  Function Description:
 #      The function sets the global scatterplot multichart dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated scatterplot multichart 
 #                                  dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_scatterplot_multichart_dict(upd_dict):

    global scatterplot_multichart_dict

    scatterplot_multichart_dict = upd_dict


# In[59]:


#*******************************************************************************************
 #
 #  Function Name:  proc_bar_chart_input
 #
 #  Function Description:
 #      The function takes input for a bar chart and processes it for display. If the
 #      input is a Series or Dataframe, the function returns it unchanged. If the input
 #      is a Series dictionary, Series list, or Series array, the function converts
 #      the data to a Dataframe and returns it. Otherwise, the function returns None.
 #
 #
 #  Return Type: series / dataframe
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

def proc_bar_chart_input(input_obj):

    if isinstance(input_obj, pd.Series) \
        or isinstance(input_obj, pd.DataFrame):

        return input_obj

    elif isinstance(input_obj, dict) \
        or isinstance(input_obj, list) \
        or isinstance(input_obj, np.ndarray):

        return pd.DataFrame(input_obj)

    else: return None


# In[60]:


#*******************************************************************************************
 #
 #  Function Name:  proc_boxplot_chart_input
 #
 #  Function Description:
 #      The function takes input for a boxplot chart and processes it for display. If
 #      the input is a Series list [data, labels] or a DataFrame, the function retrieves 
 #      and returns the data and labels. Otherwise, the function returns None for both 
 #      the data and labels.
 #
 #
 #  Return Type: series, array
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

def proc_boxplot_chart_input(input_obj):

    if isinstance(input_obj, list) \
        and len(input_obj) >= 2:

        data = input_obj[0]

        labels = np.array(input_obj[1])

    elif isinstance(input_obj, pd.DataFrame):

        data \
            = [group[boxplot_chart_dict['params']['y_col']].values \
               for _, group in input_obj.groupby(boxplot_chart_dict['params']['x_col'])]

        labels \
            = np.array([name for name, _ in input_obj \
                    .groupby(boxplot_chart_dict['params']['x_col'])])

    else: data, labels = None, None


    return data, labels


# In[61]:


#*******************************************************************************************
 #
 #  Function Name:  proc_line_chart_input
 #
 #  Function Description:
 #      The function takes input for a bar chart and processes it for display. If the
 #      input is a Series or Dataframe, the function returns it unchanged. If the input
 #      is a Series list or Series array, the function converts the data to a Series 
 #      and returns it. Otherwise, the function returns None.
 #
 #
 #  Return Type: series / dataframe
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

def proc_line_chart_input(input_obj):

    if isinstance(input_obj, pd.Series) \
        or isinstance(input_obj, pd.DataFrame):

        return input_obj

    elif (isinstance(input_obj, list) \
          or isinstance(input_obj, np.ndarray)) \
            and len(input_obj) >= 2:

        index = dtypesx.cnv_data_to_array(input_obj[0])

        data = dtypesx.cnv_data_to_array(input_obj[1])

        input_series = pd.Series(data, index = index)

        return input_series

    else: return None


# In[62]:


#*******************************************************************************************
 #
 #  Function Name:  proc_pie_chart_input
 #
 #  Function Description:
 #      The function takes input for a pie chart and processes it for display. If the
 #      input is a Series, Series list, Series tuple, or Series array, the function 
 #      retrieves and returns the data and labels. Otherwise, the function returns None 
 #      for both the data and labels.
 #
 #
 #  Return Type: array, array
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

def proc_pie_chart_input(input_obj):

    if isinstance(input_obj, pd.Series):

        data = input_obj.to_numpy()

        labels = input_obj.index.to_numpy()

    elif isinstance(input_obj, list) \
            or isinstance(input_obj, tuple) \
            or isinstance(input_obj, np.ndarray):

        data = dtypesx.cnv_data_to_array(input_obj[0])

        labels = dtypesx.cnv_data_to_array(input_obj[1])

    else: data, labels = None, None


    return data, labels


# In[63]:


#*******************************************************************************************
 #
 #  Function Name:  proc_plot_chart_input
 #
 #  Function Description:
 #      The function takes input for a plot chart and processes it for display. If the
 #      input is a Series, Series list, Series tuple, or Series array, the function 
 #      retrieves and returns the x-axis and y-axis data as a Series. Otherwise, the 
 #      function returns None.
 #
 #
 #  Return Type: series
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

def proc_plot_chart_input(input_obj):

    if isinstance(input_obj, pd.Series):

        temp_obj = input_obj

    elif isinstance(input_obj, list) \
            or isinstance(input_obj, tuple) \
            or isinstance(input_obj, np.ndarray):

        index = dtypesx.cnv_data_to_array(input_obj[0])

        data = dtypesx.cnv_data_to_array(input_obj[1])

        temp_obj = pd.Series(data, index = index)

    else: temp_obj = None


    return temp_obj


# In[64]:


#*******************************************************************************************
 #
 #  Function Name:  proc_scatterplot_chart_input
 #
 #  Function Description:
 #      The function takes input for a scatterplot chart and processes it for display. 
 #      If the input is a Series, Series list, Series tuple, or Series array, the 
 #      function retrieves and returns the x-axis and y-axis data. Otherwise, the 
 #      function returns None for both data.
 #
 #
 #  Return Type: array, array
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

def proc_scatterplot_chart_input(input_obj):

    if (isinstance(input_obj, list) \
            or isinstance(input_obj, np.ndarray)\
            or isinstance(input_obj, tuple)) \
                and len(input_obj) >= 2:

        x_array = dtypesx.cnv_data_to_array(input_obj[0])

        y_array = dtypesx.cnv_data_to_array(input_obj[1])

    elif isinstance(input_obj, pd.Series):

        y_array = input_obj.index.to_numpy()

        x_array = input_obj.to_numpy()

    else: x_array, y_array = None, None


    return x_array, y_array


# In[65]:


#*******************************************************************************************
 #
 #  Function Name:  proc_scatterplot_multichart_input
 #
 #  Function Description:
 #      The function takes input for a scatterplot multichart and processes it for 
 #      display. If the input is a list of Series lists or DataFrame, the function
 #      retrieves and returns the x-axis and y-axis data. Otherwise, the function
 #      returns None for both data.
 #
 #
 #  Return Type: list, list
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

def proc_scatterplot_multichart_input(input_obj):

    if isinstance(input_obj, list):

        return input_obj[0], input_obj[1]

    elif isinstance(input_obj, pd.DataFrame):

        x_list = []

        y_list = []

        for idx in range(len(input_obj.columns)):

            x_list.append(pd.Series(list(input_obj.index)))

            y_list.append(input_obj.iloc[:, idx])

        return x_list, y_list

    else: return None, None


# In[66]:


#*******************************************************************************************
 #
 #  Function Name:  proc_chart_input
 #
 #  Function Description:
 #      The function takes input for a chart and processes it for display.
 #
 #
 #  Return Type: series / dataframe / series, array / array, array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  enueration     chart_enum_value The parameter indicates the chart type.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def proc_chart_input \
        (input_obj,
         chart_enum_value):

    if chart_enum_value == chart_enum.LINE.value:

        return proc_line_chart_input(input_obj)

    elif chart_enum_value == chart_enum.BOXPLOT.value:

        return proc_boxplot_chart_input(input_obj)

    elif chart_enum_value == chart_enum.BAR.value:

        return proc_bar_chart_input(input_obj)

    elif chart_enum_value == chart_enum.SCATTER.value:

        return proc_scatterplot_chart_input(input_obj)

    elif chart_enum_value == chart_enum.PIE.value:

        return proc_pie_chart_input(input_obj)

    elif chart_enum_value == chart_enum.HISTOGRAM.value:

        return dtypesx.cnv_data_to_array(input_obj)

    elif chart_enum_value == chart_enum.PLOT.value:

        return proc_plot_chart_input(input_obj)

    elif chart_enum_value == chart_enum.MULTISCATTER.value:

        return proc_scatterplot_multichart_input(input_obj)


# In[67]:


#*******************************************************************************************
 #
 #  Function Name:  linear_regr_line
 #
 #  Function Description:
 #      The function displays a linear regression line on a chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         x_obj            The parameter is the x-axis data.
 #  object         y_obj            The parameter is the y-axis data.
 #  float          x_coord_flt      The parameter is the x-coordinate of the text.   
 #  float          y_coord_flt      The parameter is the y-coordinate of the text.  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def linear_regr_line \
        (x_obj,
         y_obj,
         x_coord_flt,
         y_coord_flt):

    x_array = dtypesx.cnv_data_to_array(x_obj)

    y_array = dtypesx.cnv_data_to_array(y_obj)


    (slope, intercept, rvalue, pvalue, stderr) \
        = stats.linregress(x_array, y_array)

    linear_regr_array \
        = (x_array * slope) + intercept


    plt.plot \
        (x_array,
         linear_regr_array,
         color = regr_line_dict['linecolor'],
         linewidth = regr_line_dict['linewidth'],
         alpha = regr_line_dict['alpha'])

    linear_eqn \
        = 'y = ' + str(round(slope, regr_line_dict['coef_prec'])) \
          + 'x + ' + str(round(intercept, regr_line_dict['coef_prec']))

    plt.annotate \
        (linear_eqn,
         (x_coord_flt, y_coord_flt),
         fontsize = regr_line_dict['fontsize'],
         fontweight = regr_line_dict['fontweight'],
         color = regr_line_dict['fontcolor'])   


    logx.print_and_log_text('r-value:     {:.4f}'.format(rvalue))

    logx.print_and_log_text('r-squared:   {:.4f}\n'.format(rvalue*rvalue))


# In[68]:


#*******************************************************************************************
 #
 #  Function Name:  regr_line
 #
 #  Function Description:
 #      The function displays a regression line on a chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         x_obj            The parameter is the x-axis data.
 #  object         y_obj            The parameter is the y-axis data.
 #  float          x_coord_flt      The parameter is the x-coordinate of the text.   
 #  float          y_coord_flt      The parameter is the y-coordinate of the text.
 #  integer        degree_int       The parameter is the regression polynomial degree.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def regr_line \
        (x_obj,
         y_obj,
         x_coord_flt,
         y_coord_flt,
         degree_int = 1):

    if degree_int <= 1:

        linear_regr_line \
            (x_obj, y_obj,
             x_coord_flt,
             y_coord_flt)

        return


    x_array = dtypesx.cnv_data_to_array(x_obj)

    y_array = dtypesx.cnv_data_to_array(y_obj)


    model_eqn_array \
        = mathx.rtn_regr_model_eqn_coef \
            (x_array, y_array, degree_int)

    poly_line_array \
        = mathx.rtn_poly_line_array \
            (x_array, y_array)


    plt.plot \
        (poly_line_array, 
         model_eqn_array(poly_line_array),
         color = regr_line_dict['linecolor'],
         linewidth = regr_line_dict['linewidth'],
         alpha = regr_line_dict['alpha'])

    eqn_lbl \
        = mathx.rtn_eqn_as_text \
            (model_eqn_array,
             regr_line_dict['coef_prec'])

    plt.annotate \
        (eqn_lbl,
         (x_coord_flt, y_coord_flt),
         fontsize = regr_line_dict['fontsize'],
         fontweight = regr_line_dict['fontweight'],
         color = regr_line_dict['fontcolor'])


    r_sqr_flt \
        = mathx.rtn_r_sqr \
            (x_array, y_array, degree_int)


    logx.print_and_log_text('r-value:     {:.4f}'.format(math.sqrt(r_sqr_flt)))

    logx.print_and_log_text('r-squared:   {:.4f}'.format(r_sqr_flt))


# In[69]:


#*******************************************************************************************
 #
 #  Function Name:  plot_subplots
 #
 #  Function Description:
 #      The function plots the figure subplots for the multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_subplots(chart_dict):

    return \
        plt.subplots \
            (figsize 
                 = (chart_dict['figure']['width'], 
                    chart_dict['figure']['length']),
             nrows = chart_dict['figure']['nrows'], 
             ncols = chart_dict['figure']['ncols'],
             sharex = chart_dict['figure']['sharex'],
             sharey = chart_dict['figure']['sharey'])


# In[70]:


#*******************************************************************************************
 #
 #  Function Name:  plot_subplot
 #
 #  Function Description:
 #      The function plots the figure subplot in the multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  integer        idx              The parameter is the plot index minus one.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_subplot(chart_dict, idx):

    plt.subplot \
        (chart_dict['figure']['nrows'], 
         chart_dict['figure']['ncols'], 
         idx + 1)


# In[71]:


#*******************************************************************************************
 #
 #  Function Name:  plot_figsize
 #
 #  Function Description:
 #      The function plots the figure dimensions.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_figsize(chart_dict):

    plt.figure \
        (figsize \
            = (chart_dict['figure']['width'], 
               chart_dict['figure']['length']))


# In[72]:


#*******************************************************************************************
 #
 #  Function Name:  plot_title_axes
 #
 #  Function Description:
 #      The function plots the chart's title, x-axis label, and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  integer        idx              The parameter is the plot index.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_title_axes \
        (chart_dict,
         idx = 0):

    if chart_dict['title']['text'][idx] != None:

        plt.title \
            (chart_dict['title']['text'][idx],
             fontdict = {'fontsize': chart_dict['title']['fontsize'], 
                         'fontstyle': chart_dict['title']['fontstyle']},
             pad = chart_dict['title']['pad'])


    if chart_dict['xlabel']['text'] != None:

        plt.xlabel \
            (chart_dict['xlabel']['text'],
             fontdict = {'fontsize': chart_dict['xlabel']['fontsize'],
                         'fontstyle': chart_dict['xlabel']['fontstyle']},
             labelpad = chart_dict['xlabel']['pad'])

    if chart_dict['ylabel']['text'] != None:

        plt.ylabel \
            (chart_dict['ylabel']['text'],
             fontdict = {'fontsize': chart_dict['ylabel']['fontsize'],
                         'fontstyle': chart_dict['ylabel']['fontstyle']},
             labelpad = chart_dict['ylabel']['pad'])


# In[73]:


#*******************************************************************************************
 #
 #  Function Name:  plot_limits
 #
 #  Function Description:
 #      The function sets the x-axis and y-axis limits.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_limits(chart_dict):

    if chart_dict['xlim']['display'] == True:

        if chart_dict['xlim']['mode'] == 'set':

            plt.xlim \
                (chart_dict['xlim']['set']['min'], 
                 chart_dict['xlim']['set']['max'])
        else:

            plt.xlim(left = chart_dict['xlim']['adjust']['left'])

            plt.xlim(right = chart_dict['xlim']['adjust']['right'])


    if chart_dict['ylim']['display'] == True:

        if chart_dict['ylim']['mode'] == 'set':

            plt.xlim \
                (chart_dict['ylim']['set']['min'], 
                 chart_dict['ylim']['set']['max'])
        else:

            plt.xlim(left = chart_dict['ylim']['adjust']['left'])

            plt.xlim(right = chart_dict['ylim']['adjust']['right']) 


# In[74]:


#*******************************************************************************************
 #
 #  Function Name:  plot_ticks
 #
 #  Function Description:
 #      The function plots the x-axis and y-axis ticks and chart grid.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  array          tick_lbls_array  The optional parameter is the tick labels.
 #  boolean        boxplot_bool     The optional parameter indicates whether the chart 
 #                                  is a boxplot.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_ticks \
        (chart_dict,
         tick_lbls_array = np.array([], dtype = str),
         boxplot_bool = False):

    if boxplot_bool == False:

        if chart_dict['xticks']['display'] == True:

            plt.xticks \
                (fontsize = chart_dict['xticks']['fontsize'], 
                 rotation = chart_dict['xticks']['rotation'])

    else:

        if chart_dict['xticks']['display'] == True:

            ticks_idx_array = np.array([], dtype = int)

            for idx, lbl in enumerate(tick_lbls_array):

                ticks_idx_array = np.append(ticks_idx_array, idx + 1)


            plt.xticks \
                (ticks_idx_array, 
                 tick_lbls_array,
                 fontsize = boxplot_chart_dict['xticks']['fontsize'], 
                 rotation = boxplot_chart_dict['xticks']['rotation'])


    if boxplot_chart_dict['yticks']['display'] == True:

        plt.yticks \
            (fontsize = boxplot_chart_dict['yticks']['fontsize'], 
             rotation = boxplot_chart_dict['yticks']['rotation'])


    if chart_dict['grid']['display'] == True:

        plt.grid \
            (visible = chart_dict['grid']['visible'],
             which = chart_dict['grid']['which'],
             axis =  chart_dict['grid']['axis'])   


# In[75]:


#*******************************************************************************************
 #
 #  Function Name:  plot_legend
 #
 #  Function Description:
 #      The function plots the chart's legend.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_legend(chart_dict):

    if chart_dict['legend']['display'] == True:

        plt.legend \
            (loc = chart_dict['legend']['loc'],
             fontsize = chart_dict['legend']['fontsize'],
             bbox_to_anchor = chart_dict['legend']['bbox_to_anchor'])


# In[76]:


#*******************************************************************************************
 #
 #  Function Name:  plot_regr_line
 #
 #  Function Description:
 #      The function plots the chart's regression line.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          x_array          The parameter is the x-coordinates.
 #  array          y_array          The parameter is the y-coordinates.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  integer        idx              The parameter is the plot index.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_regr_line \
        (x_array, 
         y_array, 
         chart_dict,
         idx = 0):

    if chart_dict['degree'][idx] >= 1:

        regr_line \
            (x_array, y_array,
             chart_dict['eqn_x_coord'][idx],
             chart_dict['eqn_y_coord'][idx],
             chart_dict['degree'][idx])


# In[77]:


#*******************************************************************************************
 #
 #  Function Name:  plot_peaks
 #
 #  Function Description:
 #      The function plots the chart's labels for line peaks from a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_peaks \
        (input_series, 
         chart_dict):

    if chart_dict['peaks']['display'] == True:

        x_array \
            = dtypesx.cnv_data_to_array \
                (list(input_series.index[chart_dict['peaks']['array']]))

        y_array \
            = dtypesx.cnv_data_to_array \
                (list(input_series.iloc[chart_dict['peaks']['array']]))


        plt.plot \
            (x_array, y_array, 'x', 
             markersize = chart_dict['peaks']['markersize'], 
             color = chart_dict['peaks']['color'][0]) 


        for i, j in zip(x_array, y_array):

            y_coord_flt = j + emp_obj.iloc[chart_dict['peaks']['y_offset']]

            plt.annotate \
                (i, xy = (i, y_coord_flt), 
                 size = chart_dict['peaks']['fontsize'], 
                 color = chart_dict['peaks']['color'][1])


# In[78]:


#*******************************************************************************************
 #
 #  Function Name:  plot_suptitle_axes
 #
 #  Function Description:
 #      The function plots the chart's suptitle, supx-axis label, and supy-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         figure           The parameter is the matplotlib figure object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_suptitle_axes \
        (figure,
         chart_dict):

    if chart_dict['suptitle']['text'] != None:

        figure.suptitle \
            (t = chart_dict['suptitle']['text'], 
             x = chart_dict['suptitle']['x'],
             y = chart_dict['suptitle']['y'],
             horizontalalignment = chart_dict['suptitle']['horizontalalignment'],
             verticalalignment = chart_dict['suptitle']['verticalalignment'],
             fontproperties = chart_dict['suptitle']['fontproperties'])

    if chart_dict['supxlabel']['text'] != None:

        figure.suptitle \
            (t = chart_dict['supxlabel']['text'], 
             x = chart_dict['supxlabel']['x'],
             y = chart_dict['supxlabel']['y'],
             horizontalalignment = chart_dict['supxlabel']['horizontalalignment'],
             verticalalignment = chart_dict['supxlabel']['verticalalignment'],
             fontproperties = chart_dict['supxlabel']['fontproperties'])

    if chart_dict['supylabel']['text'] != None:

        figure.suptitle \
            (t = chart_dict['supylabel']['text'], 
             x = chart_dict['supylabel']['x'],
             y = chart_dict['supylabel']['y'],
             horizontalalignment = chart_dict['supylabel']['horizontalalignment'],
             verticalalignment = chart_dict['supylabel']['verticalalignment'],
             fontproperties = chart_dict['supylabel']['fontproperties'])


# In[79]:


#*******************************************************************************************
 #
 #  Function Name:  plot_tight_layout
 #
 #  Function Description:
 #      The function sets the tight layout parameters for a multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_tight_layout(chart_dict):

    if chart_dict['tight_layout']['display'] == True:

        plt.tight_layout \
            (pad = chart_dict['tight_layout']['pad'],
             h_pad = chart_dict['tight_layout']['h_pad'],
             w_pad = chart_dict['tight_layout']['w_pad'],
             rect = chart_dict['tight_layout']['rect'])


# In[80]:


#*******************************************************************************************
 #
 #  Function Name:  plot_bar_chart_series
 #
 #  Function Description:
 #      The function plots a bar chart from a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_bar_chart_series \
    (input_series,
     chart_dict):

    if chart_dict['params']['horizontal'] == False:

        plt.bar \
            (input_series.keys(),
             input_series,
             width = chart_dict['vertical']['width'],
             bottom = chart_dict['vertical']['bottom'],
             align = chart_dict['params']['align'],
             color = chart_dict['params']['color'],
             edgecolor = chart_dict['params']['edgecolor'],
             linewidth = chart_dict['params']['linewidth'],
             tick_label = chart_dict['params']['tick_label'],
             log = chart_dict['params']['log'],
             alpha = chart_dict['params']['alpha'])

    else:

        plt.barh \
            (input_series.keys(),
             input_series,
             height = chart_dict['horizontal']['height'],
             left = chart_dict['horizontal']['left'],
             align = chart_dict['params']['align'],
             color = chart_dict['params']['color'],
             edgecolor = chart_dict['params']['edgecolor'],
             linewidth = chart_dict['params']['linewidth'],
             tick_label = chart_dict['params']['tick_label'],
             log = chart_dict['params']['log'],
             alpha = chart_dict['params']['alpha'])


# In[81]:


#*******************************************************************************************
 #
 #  Function Name:  plot_bar_chart_df
 #
 #  Function Description:
 #      The function plots a bar chart from a Dataframe.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input DataFrame.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_bar_chart_df \
    (input_df,
     chart_dict):

    if chart_dict['params']['horizontal'] == True:

        input_df \
            .plot.barh \
                (height = chart_dict['horizontal']['height'],
                 left = chart_dict['horizontal']['left'],
                 stacked = chart_dict['params']['stacked'],
                 align = chart_dict['params']['align'],
                 color = chart_dict['params']['color'],
                 edgecolor = chart_dict['params']['edgecolor'],
                 linewidth = chart_dict['params']['linewidth'],
                 tick_label = chart_dict['params']['tick_label'],
                 log = chart_dict['params']['log'],
                 alpha = chart_dict['params']['alpha'])

    else:

        input_df \
            .plot.bar \
                (width = chart_dict['vertical']['width'],
                 bottom = chart_dict['vertical']['bottom'],
                 stacked = chart_dict['params']['stacked'],
                 align = chart_dict['params']['align'],
                 color = chart_dict['params']['color'],
                 edgecolor = chart_dict['params']['edgecolor'],
                 linewidth = chart_dict['params']['linewidth'],
                 tick_label = chart_dict['params']['tick_label'],
                 log = chart_dict['params']['log'],
                 alpha = chart_dict['params']['alpha'])



# In[82]:


#*******************************************************************************************
 #
 #  Function Name:  plot_bar_chart
 #
 #  Function Description:
 #      The function plots a bar chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_bar_chart \
    (input_obj,
     chart_dict):

    if isinstance(input_obj, pd.Series):

        plot_bar_chart_series(input_obj, chart_dict)

    elif isinstance(input_obj, pd.DataFrame):

        plot_bar_chart_df(input_obj, chart_dict)


# In[83]:


#*******************************************************************************************
 #
 #  Function Name:  plot_boxplot_chart
 #
 #  Function Description:
 #      The function plots a boxplot chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           data_list        The parameter is the series list.
 #  array          tick_lbls_array  The parameter is the tick labels array.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_boxplot_chart \
        (data_list, 
         tick_lbls_array,
         chart_dict):

    plt.boxplot \
        (x = data_list,
         notch = chart_dict['params']['notch'], 
         vert = chart_dict['params']['vert'], 
         orientation = chart_dict['params']['orientation'], 
         whis = chart_dict['params']['whis'], 
         widths = chart_dict['params']['widths'], 
         patch_artist = chart_dict['params']['patch_artist'], 
         autorange = chart_dict['params']['autorange'], 
         meanline = chart_dict['params']['meanline'],
         showmeans = chart_dict['params']['showmeans'])


# In[84]:


#*******************************************************************************************
 #
 #  Function Name:  plot_histogram_chart
 #
 #  Function Description:
 #      The function plots a histogram chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the data array.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_histogram_chart \
        (data_array,
         chart_dict):

    plt.hist \
        (data_array,
         bins = chart_dict['params']['bins'],
         range = chart_dict['params']['range'],
         density = chart_dict['params']['density'],
         weights = chart_dict['params']['weights'],
         cumulative = chart_dict['params']['cumulative'],
         bottom = chart_dict['params']['bottom'],
         histtype = chart_dict['params']['histtype'],
         align = chart_dict['params']['align'],
         orientation = chart_dict['params']['orientation'],
         rwidth = chart_dict['params']['rwidth'],
         log = chart_dict['params']['log'],
         color = chart_dict['params']['color'],
         label = chart_dict['params']['label'],
         stacked = chart_dict['params']['stacked'],
         edgecolor = chart_dict['params']['edgecolor'],
         facecolor = chart_dict['params']['color'],
         linewidth = chart_dict['params']['linewidth'],
         alpha = chart_dict['params']['alpha'])


# In[85]:


#*******************************************************************************************
 #
 #  Function Name:  plot_line_chart
 #
 #  Function Description:
 #      The function plots a line chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_line_chart \
        (input_obj,
         chart_dict):

    input_obj \
        .plot \
        .line \
            (color = chart_dict['line']['color'],
             linestyle = chart_dict['line']['linestyle'],
             fillstyle = chart_dict['line']['fillstyle'],
             linewidth = chart_dict['line']['linewidth'],
             alpha = chart_dict['line']['alpha'],
             marker = chart_dict['marker']['shape'],
             markerfacecolor = chart_dict['marker']['color'],
             markeredgecolor = chart_dict['marker']['edgecolor'],
             markersize = chart_dict['marker']['size'],
             markeredgewidth = chart_dict['marker']['edgewidth'],
             logx = chart_dict['params']['logx'],
             logy = chart_dict['params']['logy'],
             loglog = chart_dict['params']['loglog'],
             stacked = chart_dict['params']['stacked'],
             use_index = chart_dict['params']['use_index'])   


# In[86]:


#*******************************************************************************************
 #
 #  Function Name:  plot_histogram_chart
 #
 #  Function Description:
 #      The function plots a histogram chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the data array.
 #  array          labels_array     The parameter is the labels array.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_pie_chart \
        (data_array, 
         labels_array, 
         chart_dict):

    plt.pie \
        (data_array,
         labels = labels_array, 
         explode = chart_dict['params']['explode'], 
         colors = chart_dict['params']['colors'],
         hatch = chart_dict['params']['hatch'],
         autopct = chart_dict['params']['autopct'],
         pctdistance = chart_dict['params']['pctdistance'],
         labeldistance = chart_dict['params']['labeldistance'],
         shadow = chart_dict['params']['shadow'],
         startangle = chart_dict['params']['startangle'],
         radius = chart_dict['params']['radius'],
         counterclock = chart_dict['params']['counterclock'],
         wedgeprops = chart_dict['params']['wedgeprops'],
         textprops = chart_dict['params']['textprops'],
         center = chart_dict['params']['center'],
         frame = chart_dict['params']['frame'],
         rotatelabels = chart_dict['params']['rotatelabels'],
         normalize = chart_dict['params']['normalize'])


# In[87]:


#*******************************************************************************************
 #
 #  Function Name:  plot_plot_chart
 #
 #  Function Description:
 #      The function plots a chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         data_series      The parameter is the data series.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_plot_chart \
        (data_series, 
         chart_dict):

    data_series \
        .plot \
            (scalex = chart_dict['params']['scalex'],
             scaley = chart_dict['params']['scaley'],
             color = chart_dict['params']['color'],
             alpha = chart_dict['params']['alpha'])


# In[88]:


#*******************************************************************************************
 #
 #  Function Name:  plot_scatterplot_chart
 #
 #  Function Description:
 #      The function plots a scatterplot chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          x_array          The parameter is the x-axis array.
 #  array          y_array          The parameter is the y-axis array.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_scatterplot_chart \
        (x_array, 
         y_array, 
         chart_dict):

    return \
        plt.scatter \
            (x_array, 
             y_array, 
             marker = chart_dict['marker']['shape'],
             c = chart_dict['marker']['color'],
             s = chart_dict['marker']['size'],
             alpha = chart_dict['marker']['alpha'],
             linewidth = chart_dict['marker']['linewidth'],
             edgecolors = chart_dict['marker']['edgecolors'])


# In[89]:


#*******************************************************************************************
 #
 #  Function Name:  bar_chart
 #
 #  Function Description:
 #      The function plots a bar chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def bar_chart \
        (input_obj,
         title):

    global bar_chart_dict

    bar_chart_dict['title']['text'] = [title]


    plot_figsize(bar_chart_dict)


    temp_obj = proc_chart_input(input_obj, chart_enum.BAR.value)

    plot_bar_chart(temp_obj, bar_chart_dict)


    plot_title_axes(bar_chart_dict)

    plot_limits(bar_chart_dict)

    plot_ticks(bar_chart_dict)

    plot_legend(bar_chart_dict)


    logx.save_plot_image(title)

    plt.show()    


# In[90]:


#*******************************************************************************************
 #
 #  Function Name:  boxplot_chart
 #
 #  Function Description:
 #      The function plots a boxplot chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def boxplot_chart \
        (input_obj,
         title):

    global boxplot_chart_dict

    boxplot_chart_dict['title']['text'] = [title]


    plot_figsize(boxplot_chart_dict)


    data_list, tick_lbls_array \
        = proc_chart_input(input_obj, chart_enum.BOXPLOT.value)

    plot_boxplot_chart(data_list, tick_lbls_array, boxplot_chart_dict)


    plot_title_axes(boxplot_chart_dict)

    plot_limits(boxplot_chart_dict)

    plot_ticks(boxplot_chart_dict, tick_lbls_array, True)


    logx.save_plot_image(title)

    plt.show()


# In[91]:


#*******************************************************************************************
 #
 #  Function Name:  histogram_chart
 #
 #  Function Description:
 #      The function plots a histogram chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def histogram_chart \
        (input_obj,
         title):

    global histogram_chart_dict

    histogram_chart_dict['title']['text'] = [title]


    plot_figsize(histogram_chart_dict)


    data_array = proc_chart_input(input_obj, chart_enum.HISTOGRAM.value)

    plot_histogram_chart(data_array, histogram_chart_dict)


    plot_title_axes(histogram_chart_dict)

    plot_limits(histogram_chart_dict)

    plot_ticks(histogram_chart_dict)

    plot_legend(histogram_chart_dict)


    logx.save_plot_image(title)

    plt.show()


# In[92]:


#*******************************************************************************************
 #
 #  Function Name:  line_chart
 #
 #  Function Description:
 #      The function plots a line chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def line_chart \
        (input_obj,
         title):

    global line_chart_dict

    line_chart_dict['title']['text'] = [title]


    plot_figsize(line_chart_dict)


    temp_obj = proc_chart_input(input_obj, chart_enum.LINE.value)

    plot_line_chart(temp_obj, line_chart_dict)


    plot_title_axes(line_chart_dict)

    plot_limits(line_chart_dict)

    plot_ticks(line_chart_dict)

    plot_legend(line_chart_dict)


    logx.save_plot_image(title)

    plt.show()


# In[93]:


#*******************************************************************************************
 #
 #  Function Name:  pie_chart
 #
 #  Function Description:
 #      The function plots a pie chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def pie_chart \
        (input_obj,
         title):

    global pie_chart_dict

    pie_chart_dict['title']['text'] = [title]


    plot_figsize(scatterplot_chart_dict)


    data_array, labels_array \
        = proc_chart_input(input_obj, chart_enum.PIE.value)

    plot_pie_chart(data_array, labels_array, pie_chart_dict)


    plot_title_axes(pie_chart_dict)

    plot_legend(pie_chart_dict)


    logx.save_plot_image(title)

    plt.show()   


# In[94]:


#*******************************************************************************************
 #
 #  Function Name:  plot_chart
 #
 #  Function Description:
 #      The function plots a plot chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_chart \
        (input_obj,
         title):

    global plot_chart_dict

    plot_chart_dict['title']['text'] = [title]


    plot_figsize(histogram_chart_dict)


    temp_obj = proc_chart_input(input_obj, chart_enum.PLOT.value)

    plot_plot_chart(temp_obj, plot_chart_dict)

    plot_peaks(temp_obj, plot_chart_dict)


    plot_title_axes(plot_chart_dict)

    plot_limits(plot_chart_dict)

    plot_ticks(plot_chart_dict)

    plot_legend(plot_chart_dict)


    logx.save_plot_image(title)

    plt.show()


# In[95]:


#*******************************************************************************************
 #
 #  Function Name:  scatterplot_chart
 #
 #  Function Description:
 #      The function plots a scatterplot chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def scatterplot_chart \
        (input_obj,
         title):

    global scatterplot_chart_dict

    scatterplot_chart_dict['title']['text'] = [title]


    plot_figsize(scatterplot_chart_dict)


    x_array, y_array \
        = proc_chart_input(input_obj, chart_enum.SCATTER.value)

    plot_scatterplot_chart(x_array, y_array, scatterplot_chart_dict)


    plot_title_axes(scatterplot_chart_dict)

    plot_limits(scatterplot_chart_dict)

    plot_ticks(scatterplot_chart_dict)


    plot_regr_line(x_array, y_array, regr_line_dict)


    logx.save_plot_image(title)

    plt.show()


# In[96]:


#*******************************************************************************************
 #
 #  Function Name:  scatterplot_multichart
 #
 #  Function Description:
 #      The function plots a scatterplot multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def scatterplot_multichart \
        (input_obj,
         suptitle):

    global scatterplot_multichart_dict


    scatterplot_multichart_dict['suptitle']['text'] = suptitle

    scatterplot_multichart_dict['figure']['nplots'] \
        = dtypesx.rtn_data_obj_size(input_obj)


    rows, columns \
        = mathx.calc_clst_factors \
            (scatterplot_multichart_dict['figure']['nplots'])

    scatterplot_multichart_dict['figure']['nrows'] = rows

    scatterplot_multichart_dict['figure']['ncols'] = columns


    fig, axs = plot_subplots(scatterplot_multichart_dict)

    plot_suptitle_axes(fig, scatterplot_multichart_dict)


    x_list, y_list \
        = proc_chart_input(input_obj, chart_enum.MULTISCATTER.value) 

    for idx in range(scatterplot_multichart_dict['figure']['nplots']):

        plot_subplot(scatterplot_multichart_dict, idx)


        x_array = dtypesx.cnv_data_to_array(x_list[idx])

        y_array = dtypesx.cnv_data_to_array(y_list[idx])


        plot_scatterplot_chart \
            (x_array, y_array, 
             scatterplot_chart_dict)


        plot_title_axes(scatterplot_chart_dict, idx)

        plot_limits(scatterplot_chart_dict)

        plot_ticks(scatterplot_chart_dict)


        plot_regr_line(x_array, y_array, regr_line_dict, idx)


        plot_tight_layout(scatterplot_multichart_dict)


    logx.save_plot_image(suptitle)

    plt.show()


# In[ ]:




