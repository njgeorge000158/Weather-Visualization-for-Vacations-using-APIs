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
 #  proc_rvalues
 #  stacked_bar_chart_setup
 #  rtn_fmt_regr_tbl
 #
 #  get_chart_dict
 #  get_chart_def_dict
 #  get_title
 #  get_title_size
 #  get_xylabels
 #  get_xylabels_display
 #  get_chart_colors
 #  get_legend_bbox_to_anchor
 #
 #  get_multichart_fig_dims
 #  get_multichart_stacked
 #  get_multichart_suptitle_xycoords
 #  get_multichart_xysuplabels
 #
 #  set_chart_dict
 #  set_chart_def_dict
 #  set_title
 #  set_title_size
 #  set_xylabels
 #  set_xylabels_display
 #  set_chart_colors
 #  set_legend_bbox_to_anchor
 #
 #  set_multichart_fig_dims
 #  set_multichart_stacked
 #  set_multichart_suptitle_xycoords
 #  set_multichart_xysuplabels
 #
 #  get_regr_line_dict
 #  get_bar_chart_dict
 #  get_boxplot_chart_dict
 #  get_histogram_chart_dict
 #  get_line_chart_dict
 #  get_pie_chart_dict
 #  get_plot_chart_dict
 #  get_scatterplot_chart_dict
 #
 #  get_bar_multichart_dict
 #  get_boxplot_multichart_dict
 #  get_histogram_multichart_dict
 #  get_line_multichart_dict
 #  get_pie_multichart_dict
 #  get_plot_multichart_dict
 #  get_scatterplot_multichart_dict
 #
 #  set_bar_chart_dict
 #  set_boxplot_chart_dict
 #  set_histogram_chart_dict
 #  set_line_chart_dict
 #  set_pie_chart_dict
 #  set_plot_chart_dict
 #  set_scatterplot_chart_dict
 #  set_regr_line_dict
 #
 #  set_bar_multichart_dict
 #  set_boxplot_multichart_dict
 #  set_histogram_multichart_dict
 #  set_line_multichart_dict
 #  set_pie_multichart_dict
 #  set_plot_multichart_dict
 #  set_scatterplot_multichart_dict
 #
 #  get_regr_line_def_dict
 #  get_bar_chart_def_dict
 #  get_boxplot_chart_def_dict
 #  get_histogram_chart_def_dict
 #  get_line_chart_def_dict
 #  get_pie_chart_def_dict
 #  get_plot_chart_def_dict
 #  get_scatterplot_chart_def_dict
 #
 #  get_bar_multichart_def_dict
 #  get_boxplot_multichart_def_dict
 #  get_histogram_multichart_def_dict
 #  get_line_multichart_def_dict
 #  get_pie_multichart_def_dict
 #  get_plot_multichart_def_dict
 #  get_scatterplot_multichart_def_dict
 #
 #  set_bar_chart_def_dict
 #  set_boxplot_chart_def_dict
 #  set_histogram_chart_def_dict
 #  set_line_chart_def_dict
 #  set_pie_chart_def_dict
 #  set_plot_chart_def_dict
 #  set_scatterplot_chart_def_dict
 #  set_regr_line_def_dict
 #
 #  set_bar_multichart_def_dict
 #  set_boxplot_multichart_def_dict
 #  set_histogram_multichart_def_dict
 #  set_line_multichart_def_dict
 #  set_pie_multichart_def_dict
 #  set_plot_multichart_def_dict
 #  set_scatterplot_multichart_def_dict
 #
 #  get_bar_chart_title
 #  get_boxplot_chart_title
 #  get_histogram_chart_title
 #  get_line_chart_title
 #  get_pie_chart_title
 #  get_plot_chart_title
 #  get_scatterplot_chart_title
 #
 #  set_bar_chart_title
 #  set_boxplot_chart_title
 #  set_histogram_chart_title
 #  set_line_chart_title
 #  set_pie_chart_title
 #  set_plot_chart_title
 #  set_scatterplot_chart_title
 #
 #  get_bar_chart_title_size
 #  get_boxplot_chart_title_size
 #  get_histogram_chart_title_size
 #  get_line_chart_title_size
 #  get_pie_chart_title_size
 #  get_plot_chart_title_size
 #  get_scatterplot_chart_title_size
 #
 #  set_bar_chart_title_size
 #  set_boxplot_chart_title_size
 #  set_histogram_chart_title_size
 #  set_line_chart_title_size
 #  set_pie_chart_title_size
 #  set_plot_chart_title_size
 #  set_scatterplot_chart_title_size
 #
 #  get_bar_chart_xylabels
 #  get_boxplot_chart_xylabels
 #  get_histogram_multichart_xylabels
 #  get_line_chart_xylabels
 #  get_pie_chart_xylabels
 #  get_plot_chart_xylabels
 #  get_scatterplot_chart_xylabels
 #
 #  set_bar_chart_xylabels
 #  set_boxplot_chart_xylabels
 #  set_histogram_chart_xylabels
 #  set_line_chart_xylabels
 #  set_pie_chart_xylabels
 #  set_plot_chart_xylabels
 #  set_scatterplot_chart_xylabels
 #
 #  get_bar_chart_xylabels_display
 #  get_boxplot_chart_xylabels_display
 #  get_histogram_multichart_xylabels_display
 #  get_line_chart_xylabels_display
 #  get_pie_chart_xylabels_display
 #  get_plot_chart_xylabels_display
 #  get_scatterplot_chart_xylabels_display
 #
 #  set_bar_chart_xylabels_display
 #  set_boxplot_chart_xylabels_display
 #  set_histogram_chart_xylabels_display
 #  set_line_chart_xylabels_display
 #  set_pie_chart_xylabels_display
 #  set_plot_chart_xylabels_display
 #  set_scatterplot_chart_xylabels_display
 #
 #  get_bar_chart_legend_bbox_to_anchor
 #  get_histogram_chart_legend_bbox_to_anchor
 #  get_line_chart_legend_bbox_to_anchor
 #  get_pie_chart_legend_bbox_to_anchor
 #  get_plot_chart_legend_bbox_to_anchor
 #
 #  set_bar_chart_legend_bbox_to_anchor
 #  set_histogram_chart_legend_bbox_to_anchor
 #  set_line_chart_legend_bbox_to_anchor
 #  set_pie_chart_legend_bbox_to_anchor
 #  set_plot_chart_legend_bbox_to_anchor
 #
 #  get_regr_degree
 #  get_regr_eqn_coords
 #  get_rvalues_display
 #
 #  set_regr_degree
 #  set_regr_eqn_coords
 #  set_rvalues_display
 #
 #  get_bar_chart_colors
 #  get_histogram_chart_colors
 #  get_line_chart_colors
 #  get_pie_chart_colors
 #  get_plot_chart_colors
 #
 #  set_bar_chart_colors
 #  set_histogram_chart_colors
 #  set_line_chart_colors
 #  set_pie_chart_colors
 #  set_plot_chart_colors
 #
 #  get_pie_chart_explode
 #  set_pie_chart_explode
 #
 #  get_bar_multichart_fig_dims
 #  get_boxplot_multichart_fig_dims
 #  get_histogram_multichart_fig_dims
 #  get_line_multichart_fig_dims
 #  get_pie_multichart_fig_dims
 #  get_plot_multichart_fig_dims
 #  get_scatterplot_multichart_fig_dims
 #
 #  set_bar_multichart_fig_dims
 #  set_boxplot_multichart_fig_dims
 #  set_histogram_multichart_fig_dims
 #  set_line_multichart_fig_dims
 #  set_pie_multichart_fig_dims
 #  set_plot_multichart_fig_dims
 #  set_scatterplot_multichart_fig_dims
 #
 #  get_bar_multichart_stacked
 #  get_boxplot_multichart_stacked
 #  get_histogram_multichart_stacked
 #  get_line_multichart_stacked
 #  get_pie_multichart_stacked
 #  get_plot_multichart_stacked
 #  get_scatterplot_multichart_stacked
 #
 #  set_bar_multichart_stacked
 #  set_boxplot_multichart_stacked
 #  set_histogram_multichart_stacked
 #  set_line_multichart_stacked
 #  set_pie_multichart_stacked
 #  set_plot_multichart_stacked
 #  set_scatterplot_multichart_stacked
 #
 #  get_bar_multichart_suptitle_xycoords
 #  get_boxplot_multichart_suptitle_xycoords
 #  get_histogram_multichart_suptitle_xycoords
 #  get_line_multichart_suptitle_xycoords
 #  get_pie_multichart_suptitle_xycoords
 #  get_plot_multichart_suptitle_xycoords
 #  get_scatterplot_multichart_suptitle_xycoords
 #
 #  set_bar_multichart_suptitle_xycoords
 #  set_boxplot_multichart_suptitle_xycoords
 #  set_histogram_multichart_suptitle_xycoords
 #  set_line_multichart_suptitle_xycoords
 #  set_pie_multichart_suptitle_xycoords
 #  set_plot_multichart_suptitle_xycoords
 #  set_scatterplot_multichart_suptitle_xycoords
 #
 #  get_bar_multichart_xysuplabels
 #  get_boxplot_multichart_xysuplabels
 #  get_histogram_multichart_xysuplabels
 #  get_line_multichart_xysuplabels
 #  get_pie_multichart_xysuplabels
 #  get_plot_multichart_xysuplabels
 #  get_scatterplot_multichart_xysuplabels
 #
 #  set_bar_multichart_xysuplabels
 #  set_boxplot_multichart_xysuplabels
 #  set_histogram_multichart_xysuplabels
 #  set_line_multichart_xysuplabels
 #  set_pie_multichart_xysuplabels
 #  set_plot_multichart_xysuplabels
 #  set_scatterplot_multichart_xysuplabels
 #
 #  proc_boxplot_chart_input
 #  proc_bar_chart_input
 #  proc_line_chart_input
 #  proc_pie_chart_input
 #  proc_plot_chart_input
 #  proc_scatterplot_chart_input
 #  proc_pie_multichart_input
 #  proc_scatterplot_multichart_input
 #  proc_multichart_input
 #  proc_chart_input
 #
 #  linear_regr_line
 #  regr_line
 #
 #  plot_subplots
 #  plot_subplot
 #
 #  plot_figsize
 #  plot_title_axes_stacked
 #  plot_title_axes
 #  plot_limits_stacked
 #  plot_limits
 #  plot_ticks_stacked
 #  plot_ticks
 #  plot_legend_stacked
 #  plot_legend
 #  plot_regr_line
 #  plot_peaks
 #  plot_suptitle_axes
 #  plot_tight_layout
 #  plot_subplots_adjust
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
 #  plot_line_multichart_stacked
 #  plot_line_multichart
 #  plot_pie_multichart
 #  plot_scatterplot_multichart
 #
 #  boxplot_chart
 #  bar_chart
 #  histogram_chart
 #  line_chart
 #  pie_chart
 #  plot_chart
 #  scatterplot_chart
 #
 #  line_multichart
 #  pie_multichart
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
import pandasx

import copy
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

    REGR_LINE = auto()

    MULTIBAR = auto()

    MULTIBOXPLOT = auto()

    MULTIHISTOGRAM = auto()

    MULTILINE = auto()

    MULTIPIE = auto()

    MULTIPLOT = auto()

    MULTISCATTER = auto()

stacked_line_chart_colors \
    = ['steelblue', 'tomato', 'mediumseagreen', 'darkorange', 'mediumpurple', 
       'darkturquoise', 'goldenrod', 'crimson', 'slateblue', 'mediumspringgreen'] * 5 

pie_chart_colors \
    = ['steelblue', 'firebrick', 'mediumseagreen', 'goldenrod', 'mediumpurple', 
       'coral', 'cadetblue', 'darkorange', 'mediumvioletred', 'magenta', 'darkkhaki'] * 5


# In[4]:


regr_line_dict \
    = {'degree': [0],
       'eqn_x_coord': 0.0,
       'eqn_y_coord': 0.0,
       'linecolor': 'red',
       'linewidth': 3.0,
       'alpha': 1.0,
       'coef_prec': 4,
       'fontsize': 16.0,
       'fontweight': 'bold',
       'fontcolor': 'blue',
       'r_disp': True,
       'r_val': np.array([], dtype = float),
       'r_sqr': np.array([], dtype = float)}


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
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
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
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
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
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
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
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
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
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
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
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
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
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
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


bar_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[13]:


boxplot_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.5,
                     'y': 0.01,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[14]:


histogram_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[15]:


line_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[16]:


pie_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[17]:


plot_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[18]:


scatterplot_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[19]:


regr_line_def_dict = copy.deepcopy(regr_line_dict)

bar_chart_def_dict = copy.deepcopy(bar_chart_dict)

boxplot_chart_def_dict = copy.deepcopy(boxplot_chart_dict)

histogram_chart_def_dict = copy.deepcopy(histogram_chart_dict)

line_chart_def_dict = copy.deepcopy(line_chart_dict)

pie_chart_def_dict = copy.deepcopy(pie_chart_dict)

plot_chart_def_dict = copy.deepcopy(plot_chart_dict)

scatterplot_chart_def_dict = copy.deepcopy(scatterplot_chart_dict)


bar_multichart_def_dict = copy.deepcopy(bar_multichart_dict)

boxplot_multichart_def_dict = copy.deepcopy(boxplot_multichart_dict)

histogram_multichart_def_dict = copy.deepcopy(histogram_multichart_dict)

line_multichart_def_dict = copy.deepcopy(line_multichart_dict)

pie_multichart_def_dict = copy.deepcopy(pie_multichart_dict)

plot_multichart_def_dict = copy.deepcopy(plot_multichart_dict)

scatterplot_multichart_def_dict = copy.deepcopy(scatterplot_multichart_dict)


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  proc_rvalues
 #
 #  Function Description:
 #      The function processes the r-value for display or storage.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          rvalue_flt       The parameter is the r-value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def proc_rvalues(rvalue_flt):

    global regr_line_dict


    if regr_line_dict['r_disp']:

        logx.print_and_log_text('r-value:     {:.4f}'.format(rvalue_flt))

        logx.print_and_log_text('r-squared:   {:.4f}\n'.format(rvalue_flt*rvalue_flt))

    else:

        regr_line_dict['r_val'] = np.append(regr_line_dict['r_val'], rvalue_flt)

        regr_line_dict['r_sqr'] = np.append(regr_line_dict['r_sqr'], rvalue_flt*rvalue_flt)


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  stacked_bar_chart_setup
 #
 #  Function Description:
 #      The function sets two parmeters expected for a stacked bar chart.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  bool           stacked_bool     The parameter indicates whether the bar chart is stacked.
 #  bool           lgnd_disp_bool   The parameter indicates whether the bar chart's legend 
 #                                  is visible.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def stacked_bar_chart_setup(stacked_bool = True, lgnd_disp_bool = True):

    global bar_chart_dict

    bar_chart_dict['params']['stacked'] = stacked_bool

    bar_chart_dict['legend']['display'] = lgnd_disp_bool


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_fmt_regr_tbl
 #
 #  Function Description:
 #      The function returns a formatted table of r-values for regressions.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          idx_array        The parameter is the index array.
 #  string         title            The parameter is the table title.
 #  string         first_clr        The parameter is the first highlight color.
 #  string         sec_clr          The parameter is the second highlight color.
 #  boolean        hide_idx_bool    The parameter indicates whether the index is visible.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_fmt_regr_tbl \
        (idx_array, 
         title,
         first_clr = '#50C878', 
         sec_clr = '#C2E5D3', 
         hide_idx_bool = False):

    data_df = pd.DataFrame(zip(regr_line_dict['r_val'], regr_line_dict['r_sqr']))

    data_df.columns = ['r_values', 'r_squared']

    data_df.index = idx_array

    return \
        pandasx.rtn_fmt_tbl \
            (data_df,
             title, 
             hide_idx_bool = hide_idx_bool) \
                .format \
                    ({'r_values': pandasx.fmt_dict['regr_flt'],
                      'r_squared': pandasx.fmt_dict['regr_flt']}) \
                .apply \
                    (pandasx.highlight_top_two,
                     props_max = f'background-color: {first_clr}',
                     props_second = f'background-color: {sec_clr}',
                     subset = data_df.columns)


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  get_chart_dict
 #
 #  Function Description:
 #      The function retrieves the dictionary.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_chart_dict(chart_type):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict

    elif chart_type == chart_enum.BOXPLOT.value: return boxplot_chart_dict

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict

    elif chart_type == chart_enum.LINE.value: return line_chart_dict

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict

    elif chart_type == chart_enum.SCATTER.value: return scatterplot_chart_dict

    elif chart_type == chart_enum.REGR_LINE.value: return regr_line_dict

    elif chart_type == chart_enum.MULTIBAR.value: return bar_multichart_dict

    elif chart_type == chart_enum.MULTIBOXPLOT.value: return boxplot_multichart_dict

    elif chart_type == chart_enum.MULTIHISTOGRAM.value: return histogram_multichart_dict

    elif chart_type == chart_enum.MULTILINE.value: return line_multichart_dict

    elif chart_type == chart_enum.MULTIPIE.value: return pie_multichart_dict

    elif chart_type == chart_enum.MULTIPLOT.value: return plot_multichart_dict

    elif chart_type == chart_enum.MULTISCATTER.value: return scatterplot_multichart_dict

    else: return None


# In[24]:


#*******************************************************************************************
 #
 #  Function Name:  get_chart_def_dict
 #
 #  Function Description:
 #      The function retrieves the default dictionary.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_chart_def_dict(chart_type):

    if chart_type == chart_enum.BAR.value: return copy.deepcopy(bar_chart_def_dict)

    elif chart_type == chart_enum.BOXPLOT.value: return copy.deepcopy(boxplot_chart_def_dict)

    elif chart_type == chart_enum.HISTOGRAM.value: return copy.deepcopy(histogram_chart_def_dict)

    elif chart_type == chart_enum.LINE.value: return copy.deepcopy(line_chart_def_dict)

    elif chart_type == chart_enum.PIE.value: return copy.deepcopy(pie_chart_def_dict)

    elif chart_type == chart_enum.PLOT.value: return copy.deepcopy(plot_chart_def_dict)

    elif chart_type == chart_enum.SCATTER.value: return copy.deepcopy(scatterplot_chart_def_dict)

    elif chart_type == chart_enum.REGR_LINE.value: return copy.deepcopy(regr_line_def_dict)

    elif chart_type == chart_enum.MULTIBAR.value: return copy.deepcopy(bar_multichart_def_dict)

    elif chart_type == chart_enum.MULTIBOXPLOT.value: return copy.deepcopy(boxplot_multichart_def_dict)

    elif chart_type == chart_enum.MULTIHISTOGRAM.value: return copy.deepcopy(histogram_multichart_def_dict)

    elif chart_type == chart_enum.MULTILINE.value: return copy.deepcopy(line_multichart_def_dict)

    elif chart_type == chart_enum.MULTIPIE.value: return copy.deepcopy(pie_multichart_def_dict)

    elif chart_type == chart_enum.MULTIPLOT.value: return copy.deepcopy(plot_multichart_def_dict)

    elif chart_type == chart_enum.MULTISCATTER.value: return copy.deepcopy(scatterplot_multichart_def_dict)

    else: return None


# In[25]:


#*******************************************************************************************
 #
 #  Function Name:  get_title
 #
 #  Function Description:
 #      The function retrieves the chart's titles.
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

def get_title(chart_type):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['title']['text']

    elif chart_type == chart_enum.BOXPLOT.value: return boxplot_chart_dict['title']['text']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['title']['text']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict['title']['text']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['title']['text']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict['title']['text']

    elif chart_type == chart_enum.SCATTER.value: return scatterplot_chart_dict['title']['text']

    else: return None


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  get_title_size
 #
 #  Function Description:
 #      The function retrieves the chart's title font size.
 #
 #
 #  Return Type: float
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

def get_title_size(chart_type):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.BOXPLOT.value: return boxplot_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.SCATTER.value: return scatterplot_chart_dict['title']['fontsize']

    else: return None


# In[27]:


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

    else: return None, None


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  get_xylabels_display
 #
 #  Function Description:
 #      The function retrieves the chart's x-axis label display and y-axis label display.
 #
 #
 #  Return Type: boolean, boolean
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

def get_xylabels_display(chart_type):

    if chart_type == chart_enum.BAR.value:

        return \
            bar_chart_dict['xlabel']['display'], \
            bar_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.BOXPLOT.value:

        return \
            boxplot_chart_dict['xlabel']['display'], \
            boxplot_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.HISTOGRAM.value:

        return \
            histogram_chart_dict['xlabel']['display'], \
            histogram_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.LINE.value:

        return \
            line_chart_dict['xlabel']['display'], \
            line_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.PIE.value:

        return \
            pie_chart_dict['xlabel']['display'], \
            pie_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.PLOT.value:

        return \
            plot_chart_dict['xlabel']['display'], \
            plot_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.SCATTER.value:

        return \
            scatterplot_chart_dict['xlabel']['display'], \
            scatterplot_chart_dict['ylabel']['display']

    else: return None, None


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  get_chart_colors
 #
 #  Function Description:
 #      The function retrieves the chart colors.
 #
 #
 #  Return Type: string or list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #  string         cat              The parameter is the color category.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_chart_colors(chart_type, cat = ''):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['params']['color']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['params']['color']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict[cat]['color']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['params']['colors']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict[cat]['color']

    elif chart_type == chart_enum.SCATTER.value: return scatterplot_chart_dict['marker']['color']

    else: return None


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  get_legend_bbox_to_anchor
 #
 #  Function Description:
 #      The function retrieves the chart legend bbox to anchor.
 #
 #
 #  Return Type: string or list
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

def get_legend_bbox_to_anchor(chart_type):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict['legend']['bbox_to_anchor']

    else: return None


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_fig_dims
 #
 #  Function Description:
 #      The function retrieves the multichart's figure dimensions (width, length).
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_fig_dims(chart_type):

    if chart_type == chart_enum.MULTIBAR.value: 

        return bar_multichart_dict['figure']['width'], \
               bar_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTIBOXPLOT.value: 

        return boxplot_multichart_dict['figure']['width'], \
               boxplot_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value: 

        return histogram_multichart_dict['figure']['width'], \
               histogram_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTILINE.value: 

        return line_multichart_dict['figure']['width'], \
               line_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTIPIE.value: 

        return pie_multichart_dict['figure']['width'], \
               pie_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTIPLOT.value: 

        return plot_multichart_dict['figure']['width'], \
               plot_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTISCATTER.value: 

        return scatterplot_multichart_dict['figure']['width'], \
               scatterplot_multichart_dict['figure']['length']

    else: return None


# In[32]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_stacked
 #
 #  Function Description:
 #      The function retrieves the multichart's stacked boolean value.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_stacked(chart_type):

    if chart_type == chart_enum.MULTIBAR.value: return bar_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTIBOXPLOT.value: return boxplot_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value: return histogram_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTILINE.value: return line_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTIPIE.value: return pie_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTIPLOT.value: return plot_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTISCATTER.value: return scatterplot_multichart_dict['figure']['stacked']

    else: return None


# In[33]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_xysuplabels
 #
 #  Function Description:
 #      The function retrieves the multichart's x-axis suplabel and y-axis suplabel.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_xysuplabels(chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        return \
            bar_multichart_dict['supxlabel']['text'], \
            bar_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        return \
            boxplot_multichart_dict['supxlabel']['text'], \
            boxplot_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        return \
            histogram_multichart_dict['supxlabel']['text'], \
            histogram_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTILINE.value:

        return \
            line_multichart_dict['supxlabel']['text'], \
            line_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTIPIE.value:

        return \
            pie_multichart_dict['supxlabel']['text'], \
            pie_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTIPLOT.value:

        return \
            plot_multichart_dict['supxlabel']['text'], \
            plot_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTISCATTER.value:

        return \
            scatterplot_multichart_dict['supxlabel']['text'], \
            scatterplot_multichart_dict['supylabel']['text']

    else: return None, None


# In[34]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_suptitle_xycoords
 #
 #  Function Description:
 #      The function retrieves the multichart suptitle x and y coordinates.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_suptitle_xycoords(chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        return \
            bar_multichart_dict['suptitle']['x'], \
            bar_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        return \
            boxplot_multichart_dict['suptitle']['x'], \
            boxplot_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        return \
            histogram_multichart_dict['suptitle']['x'], \
            histogram_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTILINE.value:

        return \
            line_multichart_dict['suptitle']['x'], \
            line_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTIPIE.value:

        return \
            pie_multichart_dict['suptitle']['x'], \
            pie_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTIPLOT.value:

        return \
            plot_multichart_dict['suptitle']['x'], \
            plot_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTISCATTER.value:

        return \
            scatterplot_multichart_dict['suptitle']['x'], \
            scatterplot_multichart_dict['suptitle']['y']

    else: return None, None


# In[35]:


#*******************************************************************************************
 #
 #  Function Name:  set_chart_dict
 #
 #  Function Description:
 #      The function sets the global chart dictionary.
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
 #  int            chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_chart_dict(upd_dict, chart_type):

    if chart_type == chart_enum.BAR.value: 

        global bar_chart_dict

        bar_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.PLOT.value: 

        global plot_chart_dict

        plot_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.REGR_LINE.value:

        global regr_line_dict

        regr_line_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict = copy.deepcopy(upd_dict)


# In[36]:


#*******************************************************************************************
 #
 #  Function Name:  set_chart_def_dict
 #
 #  Function Description:
 #      The function sets the global chart default dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_chart_def_dict(chart_type):

    if chart_type == chart_enum.BAR.value: 

        global bar_chart_dict

        bar_chart_dict = copy.deepcopy(bar_chart_def_dict)

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict = copy.deepcopy(boxplot_chart_def_dict)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict = copy.deepcopy(histogram_chart_def_dict)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict = copy.deepcopy(line_chart_def_dict)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict = copy.deepcopy(pie_chart_def_dict)

    elif chart_type == chart_enum.PLOT.value: 

        global plot_chart_dict

        plot_chart_dict = copy.deepcopy(plot_chart_def_dict)

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict = copy.deepcopy(scatterplot_chart_def_dict)

    elif chart_type == chart_enum.REGR_LINE.value:

        global regr_line_dict

        regr_line_dict = copy.deepcopy(regr_line_def_dict)

    elif chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict = copy.deepcopy(bar_multichart_def_dict)

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict = copy.deepcopy(boxplot_multichart_def_dict)

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict = copy.deepcopy(histogram_multichart_def_dict)

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict = copy.deepcopy(line_multichart_def_dict)

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict = copy.deepcopy(pie_multichart_def_dict)

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict = copy.deepcopy(plot_multichart_def_dict)

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict = copy.deepcopy(scatterplot_multichart_def_dict)


# In[37]:


#*******************************************************************************************
 #
 #  Function Name:  set_title
 #
 #  Function Description:
 #      The function sets the chart's titles.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         titles           The parameter is the chart's titles.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_title(titles, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        if isinstance(titles, str): \

            bar_chart_dict['title']['text'] = np.array([titles], dtype = str)

        else: bar_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        if isinstance(titles, str): \

            boxplot_chart_dict['title']['text'] = np.array([titles], dtype = str)

        else: boxplot_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        if isinstance(titles, str): \

            histogram_chart_dict['title']['text'] = np.array([titles], dtype = str)

        else: histogram_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        if isinstance(titles, str): \

            line_chart_dict['title']['text'] = np.array([titles], dtype = str)

        else: line_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        if isinstance(titles, str): \

            pie_chart_dict['title']['text'] = np.array([titles], dtype = str)

        else: pie_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        if isinstance(titles, str): \

            plot_chart_dict['title']['text'] = np.array([titles], dtype = str)

        else: plot_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        if isinstance(titles, str): \

            scatterplot_chart_dict['title']['text'] = np.array([titles], dtype = str)

        else: scatterplot_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)


# In[38]:


#*******************************************************************************************
 #
 #  Function Name:  set_title_size
 #
 #  Function Description:
 #      The function sets the chart's title sizes.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          size_flt         The parameter is the chart's title font sizes.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_title_size(size_flt, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['title']['fontsize'] = size_flt


# In[39]:


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

def set_xylabels(xlabel, ylabel, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        if isinstance(xlabel, str): \

            bar_chart_dict['xlabel']['text'] = np.array([xlabel], dtype = str)

        else: bar_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        if isinstance(ylabel, str): \

            bar_chart_dict['ylabel']['text'] = np.array([ylabel], dtype = str)

        else: bar_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        if isinstance(xlabel, str): \

            boxplot_chart_dict['xlabel']['text'] = np.array([xlabel], dtype = str)

        else: boxplot_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        if isinstance(ylabel, str): \

            boxplot_chart_dict['ylabel']['text'] = np.array([ylabel], dtype = str)

        else: boxplot_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        if isinstance(xlabel, str): \

            histogram_chart_dict['xlabel']['text'] = np.array([xlabel], dtype = str)

        else: histogram_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        if isinstance(ylabel, str): \

            histogram_chart_dict['ylabel']['text'] = np.array([ylabel], dtype = str)

        else: histogram_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        if isinstance(xlabel, str): \

            line_chart_dict['xlabel']['text'] = np.array([xlabel], dtype = str)

        else: line_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        if isinstance(ylabel, str): \

            line_chart_dict['ylabel']['text'] = np.array([ylabel], dtype = str)

        else: line_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        if isinstance(xlabel, str): \

            pie_chart_dict['xlabel']['text'] = np.array([xlabel], dtype = str)

        else: pie_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        if isinstance(ylabel, str): \

            pie_chart_dict['ylabel']['text'] = np.array([ylabel], dtype = str)

        else: pie_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        if isinstance(xlabel, str): \

            plot_chart_dict['xlabel']['text'] = np.array([xlabel], dtype = str)

        else: plot_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        if isinstance(ylabel, str): \

            plot_chart_dict['ylabel']['text'] = np.array([ylabel], dtype = str)

        else: plot_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        if isinstance(xlabel, str): \

            scatterplot_chart_dict['xlabel']['text'] = np.array([xlabel], dtype = str)

        else: scatterplot_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        if isinstance(ylabel, str): \

            scatterplot_chart_dict['ylabel']['text'] = np.array([ylabel], dtype = str)

        else: scatterplot_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)


# In[40]:


#*******************************************************************************************
 #
 #  Function Name:  set_xylabels_display
 #
 #  Function Description:
 #      The function sets the chart's x-axis label display and y-axis label display.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        xdisp_bool   The parameter is the chart's x-axis label display.
 #  boolean        ydisp_bool   The parameter is the chart's y-axis label display.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_xylabels_display(xdisplay_bool, ydisplay_bool, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['xlabel']['display'] = xdisplay_bool

        bar_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['xlabel']['display'] = xdisplay_bool

        boxplot_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['xlabel']['display'] = xdisplay_bool

        histogram_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['xlabel']['display'] = xdisplay_bool

        line_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['xlabel']['display'] = xdisplay_bool

        pie_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['xlabel']['display'] = xdisplay_bool

        plot_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['xlabel']['display'] = xdisplay_bool

        scatterplot_chart_dict['ylabel']['display'] = ydisplay_bool


# In[41]:


#*******************************************************************************************
 #
 #  Function Name:  set_chart_colors
 #
 #  Function Description:
 #      The function sets the chart colors.
 #
 #
 #  Return Type: string or list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         upd_obj          The parameter is the updated group of chart colors.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #  string         cat              The parameter is the color category.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_chart_colors(upd_obj, chart_type, cat = ''):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        if isinstance(upd_obj, str):

            bar_chart_dict['params']['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            bar_chart_dict['params']['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        if isinstance(upd_obj, str):

            histogram_chart_dict['params']['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            histogram_chart_dict['params']['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        if isinstance(upd_obj, str):

            line_chart_dict[cat]['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            line_chart_dict[cat]['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        if isinstance(upd_obj, str):

            pie_chart_dict['params']['colors'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            pie_chart_dict['params']['colors'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        if isinstance(upd_obj, str):

            plot_chart_dict[cat]['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            plot_chart_dict[cat]['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        if isinstance(upd_obj, str):

            scatterplot_chart_dict['marker']['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            scatterplot_chart_dict['marker']['color'] = dtypesx.cnv_data_to_array(upd_obj)


# In[42]:


#*******************************************************************************************
 #
 #  Function Name:  set_legend_bbox_to_anchor
 #
 #  Function Description:
 #      The function sets a chart's legend bbox to anchor.
 #
 #
 #  Return Type: string or list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the x-coordinate.
 #  float          y_flt            The parameter is the y-coordinate.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_legend_bbox_to_anchor(x_flt, y_flt, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)


# In[43]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_fig_dims
 #
 #  Function Description:
 #      The function sets the multichart's figure dimensions (width, length).
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          width_flt        The parameter is the chart figure's width.
 #  float          length_flt       The parameter is the chart figure's length.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_fig_dims(width_flt, length_flt, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['figure']['width'] = width_flt

        bar_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['figure']['width'] = width_flt

        boxplot_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['figure']['width'] = width_flt

        histogram_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['figure']['width'] = width_flt

        line_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['figure']['width'] = width_flt

        pie_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['figure']['width'] = width_flt

        plot_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['figure']['width'] = width_flt

        scatterplot_multichart_dict['figure']['length'] = length_flt


# In[44]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_stacked
 #
 #  Function Description:
 #      The function sets the multichart's stacked boolean value.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        upd_bool         The parameter is the chart's updated stacked boolean.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_stacked(upd_bool, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['figure']['stacked'] = upd_bool


# In[45]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_suptitle_xycoords
 #
 #  Function Description:
 #      The function sets the multichart suptitle's x and y coordinates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the suptitle's x-coordinate.
 #  float          y_flt            The parameter is the suptitle's y-coordinate.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_suptitle_xycoords(x_flt, y_flt, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['suptitle']['x'] = x_flt
        bar_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['suptitle']['x'] = x_flt
        boxplot_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['suptitle']['x'] = x_flt
        histogram_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['suptitle']['x'] = x_flt
        line_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['suptitle']['x'] = x_flt
        pie_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['suptitle']['x'] = x_flt
        plot_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['suptitle']['x'] = x_flt
        scatterplot_multichart_dict['suptitle']['y'] = y_flt


# In[46]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_xysuplabels
 #
 #  Function Description:
 #      The function sets the multichart's x-axis suplabel and y-axis suplabel.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xsuplabel        The parameter is the chart's x-axis suplabel.
 #  string         ysuplabel        The parameter is the chart's y-axis suplabel.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['supxlabel']['text'] = xsuplabel
        bar_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['supxlabel']['text'] = xsuplabel
        boxplot_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['supxlabel']['text'] = xsuplabel
        histogram_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['supxlabel']['text'] = xsuplabel
        line_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['supxlabel']['text'] = xsuplabel
        pie_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['supxlabel']['text'] = xsuplabel
        plot_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['supxlabel']['text'] = xsuplabel
        scatterplot_multichart_dict['supylabel']['text'] = ysuplabel


# In[47]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_dict
 #                  get_boxplot_chart_dict
 #                  get_histogram_chart_dict
 #                  get_line_chart_dict
 #                  get_pie_chart_dict
 #                  get_plot_chart_dict
 #                  get_scatterplot_chart_dict
 #                  get_regr_line_dict
 #
 #                  get_bar_multichart_dict
 #                  get_boxplot_multichart_dict
 #                  get_histogram_multichart_dict
 #                  get_line_multichart_dict
 #                  get_pie_multichart_dict
 #                  get_plot_multichart_dict
 #                  get_scatterplot_multichart_dict
 #
 #  Function Description:
 #      The function retrieves the global chart dictionary.
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

def get_bar_chart_dict(): return get_chart_dict(chart_enum.BAR.value)
def get_boxplot_chart_dict(): return get_chart_dict(chart_enum.BOXPLOT.value)
def get_histogram_chart_dict(): return get_chart_dict(chart_enum.HISTOGRAM.value)
def get_line_chart_dict(): return get_chart_dict(chart_enum.LINE.value)
def get_pie_chart_dict(): return get_chart_dict(chart_enum.PIE.value)
def get_plot_chart_dict(): return get_chart_dict(chart_enum.PLOT.value)
def get_scatterplot_chart_dict(): return get_chart_dict(chart_enum.SCATTER.value)
def get_regr_line_dict(): return get_chart_dict(chart_enum.REGR_LINE.value)

def get_bar_multichart_dict(): return get_chart_dict(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_dict(): return get_chart_dict(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_dict(): return get_chart_dict(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_dict(): return get_chart_dict(chart_enum.MULTILINE.value)
def get_pie_multichart_dict(): return get_chart_dict(chart_enum.MULTIPIE.value)
def get_plot_multichart_dict(): return get_chart_dict(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_dict(): return get_chart_dict(chart_enum.MULTISCATTER.value)


# In[48]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_dict
 #                  set_boxplot_chart_dict
 #                  set_histogram_chart_dict
 #                  set_line_chart_dict
 #                  set_pie_chart_dict
 #                  set_plot_chart_dict
 #                  set_scatterplot_chart_dict
 #                  set_regr_line_dict
 #
 #                  set_bar_multichart_dict
 #                  set_boxplot_multichart_dict
 #                  set_histogram_multichart_dict
 #                  set_line_multichart_dict
 #                  set_pie_multichart_dict
 #                  set_plot_multichart_dict
 #                  set_scatterplot_multichart_dict
 #
 #  Function Description:
 #      The function sets the global chart dictionary.
 #
 #
 #  Return Type: dictionary
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

def set_bar_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.BAR.value)
def set_boxplot_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.BOXPLOT.value)
def set_histogram_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.HISTOGRAM.value)
def set_line_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.LINE.value)
def set_pie_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.PIE.value)
def set_plot_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.PLOT.value)
def set_scatterplot_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.SCATTER.value)
def set_regr_line_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.REGR_LINE.value)

def set_bar_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTILINE.value)
def set_pie_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTIPIE.value)
def set_plot_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTISCATTER.value)


# In[49]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_def_dict
 #                  get_boxplot_chart_def_dict
 #                  get_histogram_chart_def_dict
 #                  get_line_chart_def_dict
 #                  get_pie_chart_def_dict
 #                  get_plot_chart_def_dict
 #                  get_scatterplot_chart_def_dict
 #                  get_regr_line_def_dict
 #
 #                  get_bar_multichart_def_dict
 #                  get_boxplot_multichart_def_dict
 #                  get_histogram_multichart_def_dict
 #                  get_line_multichart_def_dict
 #                  get_pie_multichart_def_dict
 #                  get_plot_multichart_def_dict
 #                  get_scatterplot_multichart_def_dict
 #
 #  Function Description:
 #      The function retrieves the global chart default dictionary.
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

def get_bar_chart_def_dict(): return get_chart_def_dict(chart_enum.BAR.value)
def get_boxplot_chart_def_dict(): return get_chart_def_dict(chart_enum.BOXPLOT.value)
def get_histogram_chart_def_dict(): return get_chart_def_dict(chart_enum.HISTOGRAM.value)
def get_line_chart_def_dict(): return get_chart_def_dict(chart_enum.LINE.value)
def get_pie_chart_def_dict(): return get_chart_def_dict(chart_enum.PIE.value)
def get_plot_chart_def_dict(): return get_chart_def_dict(chart_enum.PLOT.value)
def get_scatterplot_chart_def_dict(): return get_chart_def_dict(chart_enum.SCATTER.value)
def get_regr_line_def_dict(): return get_chart_def_dict(chart_enum.REGR_LINE.value)

def get_bar_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTILINE.value)
def get_pie_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTIPIE.value)
def get_plot_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTISCATTER.value)


# In[50]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_def_dict
 #                  set_boxplot_chart_def_dict
 #                  set_histogram_chart_def_dict
 #                  set_line_chart_def_dict
 #                  set_pie_chart_def_dict
 #                  set_plot_chart_def_dict
 #                  set_scatterplot_chart_def_dict
 #                  set_regr_line_def_dict
 #
 #                  set_bar_multichart_def_dict
 #                  set_boxplot_multichart_def_dict
 #                  set_histogram_multichart_def_dict
 #                  set_line_multichart_def_dict
 #                  set_pie_multichart_def_dict
 #                  set_plot_multichart_def_dict
 #                  set_scatterplot_multichart_def_dict
 #
 #  Function Description:
 #      The function sets the global chart dictionary with default values.
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

def set_bar_chart_def_dict(): set_chart_def_dict(chart_enum.BAR.value)
def set_boxplot_chart_def_dict(): set_chart_def_dict(chart_enum.BOXPLOT.value)
def set_histogram_chart_def_dict(): set_chart_def_dict(chart_enum.HISTOGRAM.value)
def set_line_chart_def_dict(): set_chart_def_dict(chart_enum.LINE.value)
def set_pie_chart_def_dict(): set_chart_def_dict(chart_enum.PIE.value)
def set_plot_chart_def_dict(): set_chart_def_dict(chart_enum.PLOT.value)
def set_scatterplot_chart_def_dict(): set_chart_def_dict(chart_enum.SCATTER.value)
def set_regr_line_def_dict(): set_chart_def_dict(chart_enum.REGR_LINE.value)

def set_bar_multichart_def_dict(): set_chart_def_dict(chart_enum.MULTIBAR.value)
def set_boxplot_multichart_def_dict(): set_chart_def_dict(chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_def_dict(): set_chart_def_dict(chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_def_dict(): set_chart_def_dict(chart_enum.MULTILINE.value)
def set_pie_multichart_def_dict(): set_chart_def_dict(chart_enum.MULTIPIE.value)
def set_plot_multichart_def_dict(): set_chart_def_dict(chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_def_dict(): set_chart_def_dict(chart_enum.MULTISCATTER.value)


# In[51]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_title
 #                  get_boxplot_chart_title
 #                  get_histogram_chart_title
 #                  get_line_chart_title
 #                  get_pie_chart_title
 #                  get_plot_chart_title
 #                  get_scatterplot_chart_title
 #
 #  Function Description:
 #      The function retrieves the chart's titles.
 #
 #
 #  Return Type: string, string
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

def get_bar_chart_title(): return get_title(chart_enum.BAR.value)
def get_boxplot_chart_title(): return get_title(chart_enum.BOXPLOT.value)
def get_histogram_chart_title(): return get_title(chart_enum.HISTOGRAM.value)
def get_line_chart_title(): return get_title(chart_enum.LINE.value)
def get_pie_chart_title(): return get_title(chart_enum.PIE.value)
def get_plot_chart_title(): return get_title(chart_enum.PLOT.value)
def get_scatterplot_chart_title(): return get_title(chart_enum.SCATTER.value)


# In[52]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_title
 #                  set_boxplot_chart_title
 #                  set_histogram_chart_title
 #                  set_line_chart_title
 #                  set_pie_chart_title
 #                  set_plot_chart_title
 #                  set_scatterplot_chart_title
 #
 #  Function Description:
 #      The function sets the chart's titles.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         titles           The parameter is the chart's titles.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_title(titles): set_title(titles, chart_enum.BAR.value)
def set_boxplot_chart_title(titles): set_title(titles, chart_enum.BOXPLOT.value)
def set_histogram_chart_title(titles): set_title(titles, chart_enum.HISTOGRAM.value)
def set_line_chart_title(titles): set_title(titles, chart_enum.LINE.value)
def set_pie_chart_title(titles): set_title(titles, chart_enum.PIE.value)
def set_plot_chart_title(titles): set_title(titles, chart_enum.PLOT.value)
def set_scatterplot_chart_title(titles): set_title(titles, chart_enum.SCATTER.value)


# In[53]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_title_size
 #                  get_boxplot_chart_title_size
 #                  get_histogram_chart_title_size
 #                  get_line_chart_title_size
 #                  get_pie_chart_title_size
 #                  get_plot_chart_title_size
 #                  get_scatterplot_chart_title_size
 #
 #  Function Description:
 #      The function retrieves the chart's title size.
 #
 #
 #  Return Type: string, string
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

def get_bar_chart_title_size(): return get_title_size(chart_enum.BAR.value)
def get_boxplot_chart_title_size(): return get_title_size(chart_enum.BOXPLOT.value)
def get_histogram_chart_title_size(): return get_title_size(chart_enum.HISTOGRAM.value)
def get_line_chart_title_size(): return get_title_size(chart_enum.LINE.value)
def get_pie_chart_title_size(): return get_title_size(chart_enum.PIE.value)
def get_plot_chart_title_size(): return get_title_size(chart_enum.PLOT.value)
def get_scatterplot_chart_title_size(): return get_title_size(chart_enum.SCATTER.value)


# In[54]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_title_size
 #                  set_boxplot_chart_title_size
 #                  set_histogram_chart_title_size
 #                  set_line_chart_title_size
 #                  set_pie_chart_title_size
 #                  set_plot_chart_title_size
 #                  set_scatterplot_chart_title_size
 #
 #  Function Description:
 #      The function sets the chart's title size.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          size_flt         The parameter is the chart title's font size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_title_size(size_flt): set_title_size(size_flt, chart_enum.BAR.value)
def set_boxplot_chart_title_size(size_flt): set_title_size(size_flt, chart_enum.BOXPLOT.value)
def set_histogram_chart_title_size(size_flt): set_title_size(size_flt, chart_enum.HISTOGRAM.value)
def set_line_chart_title_size(size_flt): set_title_size(size_flt, chart_enum.LINE.value)
def set_pie_chart_title_size(size_flt): set_title_size(size_flt, chart_enum.PIE.value)
def set_plot_chart_title_size(size_flt): set_title_size(size_flt, chart_enum.PLOT.value)
def set_scatterplot_chart_title_size(size_flt): set_title_size(size_flt, chart_enum.SCATTER.value)


# In[55]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_xylabels
 #                  get_boxplot_chart_xylabels
 #                  get_histogram_multichart_xylabels
 #                  get_line_chart_xylabels
 #                  get_pie_chart_xylabels
 #                  get_plot_chart_xylabels
 #                  get_scatterplot_chart_xylabels
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
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_xylabels(): return get_xylabels(chart_enum.BAR.value)
def get_boxplot_chart_xylabels(): return get_xylabels(chart_enum.BOXPLOT.value)
def get_histogram_multichart_xylabels(): return get_xylabels(chart_enum.HISTOGRAM.value)
def get_line_chart_xylabels(): return get_xylabels(chart_enum.LINE.value)
def get_pie_chart_xylabels(): return get_xylabels(chart_enum.PIE.value)
def get_plot_chart_xylabels(): return get_xylabels(chart_enum.PLOT.value)
def get_scatterplot_chart_xylabels(): return get_xylabels(chart_enum.SCATTER.value)


# In[56]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_xylabels
 #                  set_boxplot_chart_xylabels
 #                  set_histogram_chart_xylabels
 #                  set_line_chart_xylabels
 #                  set_pie_chart_xylabels
 #                  set_plot_chart_xylabels
 #                  set_scatterplot_chart_xylabels
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
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_xylabels(xlabel, ylabel): 

    set_xylabels(xlabel, ylabel, chart_enum.BAR.value)

def set_boxplot_chart_xylabels(xlabel, ylabel): 

    set_xylabels(xlabel, ylabel, chart_enum.BOXPLOT.value)

def set_histogram_chart_xylabels(xlabel, ylabel): 

    set_xylabels(xlabel, ylabel, chart_enum.HISTOGRAM.value)

def set_line_chart_xylabels(xlabel, ylabel): 

    set_xylabels(xlabel, ylabel, chart_enum.LINE.value)

def set_pie_chart_xylabels(xlabel, ylabel): 

    set_xylabels(xlabel, ylabel, chart_enum.PIE.value)

def set_plot_chart_xylabels(xlabel, ylabel): 

    set_xylabels(xlabel, ylabel, chart_enum.PLOT.value)

def set_scatterplot_chart_xylabels(xlabel, ylabel): 

    set_xylabels(xlabel, ylabel, chart_enum.SCATTER.value)


# In[57]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_xylabels_display
 #                  get_boxplot_chart_xylabels_display
 #                  get_histogram_multichart_xylabels_display
 #                  get_line_chart_xylabels_display
 #                  get_pie_chart_xylabels_display
 #                  get_plot_chart_xylabels_display
 #                  get_scatterplot_chart_xylabels_display
 #
 #  Function Description:
 #      The function retrieves the chart's x-axis label display and y-axis label display.
 #
 #
 #  Return Type: boolean, boolean
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

def get_bar_chart_xylabels_display(): return get_xylabels_display(chart_enum.BAR.value)
def get_boxplot_chart_xylabels_display(): return get_xylabels_display(chart_enum.BOXPLOT.value)
def get_histogram_multichart_xylabels_display(): return get_xylabels_display(chart_enum.HISTOGRAM.value)
def get_line_chart_xylabels_display(): return get_xylabels_display(chart_enum.LINE.value)
def get_pie_chart_xylabels_display(): return get_xylabels_display(chart_enum.PIE.value)
def get_plot_chart_xylabels_display(): return get_xylabels_display(chart_enum.PLOT.value)
def get_scatterplot_chart_xylabels_display(): return get_xylabels_display(chart_enum.SCATTER.value)


# In[58]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_xylabels_display
 #                  set_boxplot_chart_xylabels_display
 #                  set_histogram_chart_xylabels_display
 #                  set_line_chart_xylabels_display
 #                  set_pie_chart_xylabels_display
 #                  set_plot_chart_xylabels_display
 #                  set_scatterplot_chart_xylabels_display
 #
 #  Function Description:
 #      The function sets the chart's x-axis label display and y-axis label display.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        xdisp_bool       The parameter is the chart's x-axis label display.
 #  boolean        ydisp_bool       The parameter is the chart's y-axis label display.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_xylabels_display(xdisp_bool, ydisp_bool): 

    set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.BAR.value)

def set_boxplot_chart_xylabels_display(xdisp_bool, ydisp_bool): 

    set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.BOXPLOT.value)

def set_histogram_chart_xylabels_display(xdisp_bool, ydisp_bool): 

    set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.HISTOGRAM.value)

def set_line_chart_xylabels_display(xdisp_bool, ydisp_bool): 

    set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.LINE.value)

def set_pie_chart_xylabels_display(xdisp_bool, ydisp_bool): 

    set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.PIE.value)

def set_plot_chart_xylabels_display(xdisp_bool, ydisp_bool): 

    set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.PLOT.value)

def set_scatterplot_chart_xylabels_display(xdisp_bool, ydisp_bool): 

    set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.SCATTER.value)


# In[59]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_legend_bbox_to_anchor
 #                  get_histogram_chart_legend_bbox_to_anchor
 #                  get_line_chart_legend_bbox_to_anchor
 #                  get_pie_chart_legend_bbox_to_anchor
 #                  get_plot_chart_legend_bbox_to_anchor
 #
 #  Function Description:
 #      The function retrieves the chart's legend bbox to anchor.
 #
 #
 #  Return Type: (float, float)
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

def get_bar_chart_legend_bbox_to_anchor(): 

    return get_legend_bbox_to_anchor(chart_enum.BAR.value)

def get_histogram_chart_legend_bbox_to_anchor(): 

    return get_legend_bbox_to_anchor(chart_enum.HISTOGRAM.value)

def get_line_chart_legend_bbox_to_anchor(): 

    return get_legend_bbox_to_anchor(chart_enum.LINE.value)

def get_pie_chart_legend_bbox_to_anchor(): 

    return get_legend_bbox_to_anchor(chart_enum.PIE.value)

def get_plot_chart_legend_bbox_to_anchor(): 

    return get_legend_bbox_to_anchor(chart_enum.PLOT.value)


# In[60]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_legend_bbox_to_anchor
 #                  set_histogram_chart_legend_bbox_to_anchor
 #                  set_line_chart_legend_bbox_to_anchor
 #                  set_pie_chart_legend_bbox_to_anchor
 #                  set_plot_chart_legend_bbox_to_anchor
 #
 #  Function Description:
 #      The function sets the chart's legend bbox to anchor.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the x-coordinate.
 #  float          y_flt            The parameter is the y-coordinate.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_legend_bbox_to_anchor(x_flt, y_flt): 

    set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.BAR.value)

def set_histogram_chart_legend_bbox_to_anchor(x_flt, y_flt): 

    set_legend_bbox_to_anchor(x_flt, ylabel, chart_enum.HISTOGRAM.value)

def set_line_chart_legend_bbox_to_anchor(x_flt, y_flt): 

    set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.LINE.value)

def set_pie_chart_legend_bbox_to_anchor(x_flt, y_flt): 

    set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.PIE.value)

def set_plot_chart_legend_bbox_to_anchor(x_flt, y_flt): 

    set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.PLOT.value)


# In[61]:


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


# In[62]:


#*******************************************************************************************
 #
 #  Function Name:  get_regr_eqn_coords
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


# In[63]:


#*******************************************************************************************
 #
 #  Function Name:  get_rvalues_display
 #
 #  Function Description:
 #      The function retrieves the r-value display indicator.
 #
 #
 #  Return Type: boolean
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

def get_rvalues_display():

    return regr_line_dict['r_disp']


# In[64]:


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


    if isinstance(input_obj, int): regr_line_dict['degree'] = [abs(input_obj)]

    elif isinstance(input_obj, float): regr_line_dict['degree'] = [int(abs(input_obj))]

    elif isinstance(input_obj, list): regr_line_dict['degree'] = np.array(input_obj)

    elif isinstance(input_obj, np.ndarray): regr_line_dict['degree'] = input_obj

    elif isinstance(input_obj, pd.Series): regr_line_dict['degree'] = input_obj.to_numpy()


# In[65]:


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


    if isinstance(x_crd_obj, int) \
        or isinstance(x_crd_obj, float): regr_line_dict['eqn_x_coord'] = [x_crd_obj]

    elif isinstance(x_crd_obj, list): regr_line_dict['eqn_x_coord'] = x_crd_obj


    if isinstance(y_crd_obj, int) \
        or isinstance(y_crd_obj, float): regr_line_dict['eqn_y_coord'] = [y_crd_obj]

    elif isinstance(y_crd_obj, list): regr_line_dict['eqn_y_coord'] = y_crd_obj  


# In[66]:


#*******************************************************************************************
 #
 #  Function Name:  set_rvalues_display
 #
 #  Function Description:
 #      The function sets the r-value display indicator.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        upd_bool         The parameter is the updated regression value display 
 #                                  indicator.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_rvalues_display(upd_bool):

    global regr_line_dict

    regr_line_dict['r_disp'] = upd_bool


# In[67]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_colors
 #                  get_histogram_chart_colors
 #                  get_line_chart_colors
 #                  get_pie_chart_colors
 #                  get_plot_chart_colors
 #                  get_scatterplot_chart_colors
 #
 #  Function Description:
 #      The function retrieves the chart colors.
 #
 #
 #  Return Type: string or list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         cat              The parameter is the color category.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_colors(cat = ''): return get_chart_colors(chart_enum.BAR.value, cat)
def get_histogram_chart_colors(cat = ''): return get_chart_colors(chart_enum.HISTOGRAM.value, cat)
def get_line_chart_colors(cat = 'line'): return get_chart_colors(chart_enum.LINE.value, cat)
def get_pie_chart_colors(cat = ''): return get_chart_colors(chart_enum.PIE.value, cat)
def get_plot_chart_colors(cat = 'params'): return get_chart_colors(chart_enum.PLOT.value, cat)
def get_scatterplot_chart_colors(cat = 'marker'): return get_chart_colors(chart_enum.PLOT.value, cat)


# In[68]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_colors
 #                  set_histogram_chart_colors
 #                  set_line_chart_colors
 #                  set_pie_chart_colors
 #                  set_plot_chart_colors
 #                  set_scatterplot_chart_colors
 #
 #  Function Description:
 #      The function sets the chart face colors.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         upd_obj          The parameter is the updated group of chart colors.
 #  string         cat              The parameter is the color category.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_colors(upd_obj, cat = ''): set_chart_colors(upd_obj, chart_enum.BAR.value, cat)
def set_histogram_chart_colors(upd_obj, cat = ''): set_chart_colors(upd_obj, chart_enum.HISTOGRAM.value, cat)
def set_line_chart_colors(upd_obj, cat = 'line'): set_chart_colors(upd_obj, chart_enum.LINE.value, cat)
def set_pie_chart_colors(upd_obj, cat = ''): set_chart_colors(upd_obj, chart_enum.PIE.value, cat)
def set_plot_chart_colors(upd_obj, cat = 'params'): set_chart_colors(upd_obj, chart_enum.PLOT.value, cat)     
def set_scatterplot_chart_colors(upd_obj, cat = 'marker'): set_chart_colors(upd_obj, chart_enum.SCATTER.value, cat) 


# In[69]:


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


# In[70]:


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

    pie_chart_dict['params']['explode'] = dtypesx.cnv_data_to_array(upd_obj)


# In[71]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_fig_dims
 #                  get_boxplot_multichart_fig_dims
 #                  get_histogram_multichart_fig_dims
 #                  get_line_multichart_fig_dims
 #                  get_pie_multichart_fig_dims
 #                  get_plot_multichart_fig_dims
 #                  get_scatterplot_multichart_fig_dims
 #
 #  Function Description:
 #      The function retrieves the multichart figure dimensions (width, length).
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

def get_bar_multichart_fig_dims():

    return get_multichart_fig_dims(chart_enum.MULTIBAR.value)

def get_boxplot_multichart_fig_dims(): 

    return get_multichart_fig_dims(chart_enum.MULTIBOXPLOT.value)

def get_histogram_multichart_fig_dims(): 

    return get_multichart_fig_dims(chart_enum.MULTIHISTOGRAM.value)

def get_line_multichart_fig_dims(): 

    return get_multichart_fig_dims(chart_enum.MULTILINE.value)

def get_pie_multichart_fig_dims(): 

    return get_multichart_fig_dims(chart_enum.MULTIPIE.value)

def get_plot_multichart_fig_dims(): 

    return get_multichart_fig_dims(chart_enum.MULTIPLOT.value)

def get_scatterplot_multichart_fig_dims(): 

    return get_multichart_fig_dims(chart_enum.MULTISCATTER.value)


# In[72]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_fig_dims
 #
 #  Function Description:
 #      The function sets the multichartfigure dimesions (width, length)
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          width_flt        The parameter is the chart figure's width.
 #  float          length_flt       The parameter is the chart figure's length.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_fig_dims(width_flt, length_flt): 

    set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTIBAR.value)

def set_boxplot_multichart_fig_dims(width_flt, length_flt): 

    set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTIBOXPLOT.value)

def set_histogram_multichart_fig_dims(width_flt, length_flt): 

    set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTIHISTOGRAM.value)

def set_line_multichart_fig_dims(width_flt, length_flt): 

    set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTILINE.value)

def set_pie_multichart_fig_dims(width_flt, length_flt): 

    set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTIPIE.value)

def set_plot_multichart_fig_dims(width_flt, length_flt): 

    set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTIPLOT.value)

def set_scatterplot_multichart_fig_dims(width_flt, length_flt): 

    set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTISCATTER.value)


# In[73]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_stacked
 #                  get_boxplot_multichart_stacked
 #                  get_histogram_multichart_stacked
 #                  get_line_multichart_stacked
 #                  get_pie_multichart_stacked
 #                  get_plot_multichart_stacked
 #                  get_scatterplot_multichart_stacked
 #
 #  Function Description:
 #      The function retrieves the multichart's stacked boolean value.
 #
 #
 #  Return Type: boolean
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

def get_bar_multichart_stacked(): 

    return get_multichart_stacked(chart_enum.MULTIBAR.value)

def get_boxplot_multichart_stacked(): 

    return get_multichart_stacked(chart_enum.MULTIBOXPLOT.value)

def get_histogram_multichart_stacked(): 

    return get_multichart_stacked(chart_enum.MULTIHISTOGRAM.value)

def get_line_multichart_stacked(): 

    return get_multichart_stacked(chart_enum.MULTILINE.value)

def get_pie_multichart_stacked(): 

    return get_multichart_stacked(chart_enum.MULTIPIE.value)

def get_plot_multichart_stacked(): 

    return get_multichart_stacked(chart_enum.MULTIPLOT.value)

def get_scatterplot_multichart_stacked(): 

    return get_multichart_stacked(chart_enum.MULTISCATTER.value)


# In[74]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_stacked
 #
 #  Function Description:
 #      The function sets the multichart's stacked boolean value.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        upd_bool         The parameter is the chart's updated stacked boolean.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_stacked(input_bool): 

    set_multichart_stacked(input_bool, chart_enum.MULTIBAR.value)

def set_boxplot_multichart_stacked(input_bool): 

    set_multichart_stacked(input_bool, chart_enum.MULTIBOXPLOT.value)

def set_histogram_multichart_stacked(input_bool): 

    set_multichart_stacked(input_bool, chart_enum.MULTIHISTOGRAM.value)

def set_line_multichart_stacked(input_bool): 

    set_multichart_stacked(input_bool, chart_enum.MULTILINE.value)

def set_pie_multichart_stacked(input_bool): 

    set_multichart_stacked(input_bool, chart_enum.MULTIPIE.value)

def set_plot_multichart_stacked(input_bool): 

    set_multichart_stacked(input_bool, chart_enum.MULTIPLOT.value)

def set_scatterplot_multichart_stacked(input_bool): 

    set_multichart_stacked(input_bool, chart_enum.MULTISCATTER.value)


# In[75]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_suptitle_xycoords
 #                  get_boxplot_multichart_suptitle_xycoords
 #                  get_histogram_multichart_suptitle_xycoords
 #                  get_line_multichart_suptitle_xycoords
 #                  get_pie_multichart_suptitle_xycoords
 #                  get_plot_multichart_suptitle_xycoords
 #                  get_scatterplot_multichart_suptitle_xycoords
 #
 #  Function Description:
 #      The function retrieves the multichart suptitle x and y coordinates.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_suptitle_xycoords(): 

    return get_multichart_suptitle_xycoords(chart_enum.MULTIBAR.value)

def get_boxplot_multichart_suptitle_xycoords(): 

    return get_multichart_suptitle_xycoords(chart_enum.MULTIBOXPLOT.value)

def get_histogram_multichart_suptitle_xycoords(): 

    return get_multichart_suptitle_xycoords(chart_enum.MULTIHISTOGRAM.value)

def get_line_multichart_suptitle_xycoords(): 

    return get_multichart_suptitle_xycoords(chart_enum.MULTILINE.value)

def get_pie_multichart_suptitle_xycoords(): 

    return get_multichart_suptitle_xycoords(chart_enum.MULTIPIE.value)

def get_plot_multichart_suptitle_xycoords(): 

    return get_multichart_suptitle_xycoords(chart_enum.MULTIPLOT.value)

def get_scatterplot_multichart_suptitle_xycoords(): 

    return get_multichart_suptitle_xycoords(chart_enum.MULTISCATTER.value)


# In[76]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_suptitle_xycoords
 #                  set_boxplot_multichart_suptitle_xycoords
 #                  set_histogram_chart_suptitle_xycoords
 #                  set_line_multichart_suptitle_xycoords
 #                  set_pie_multichart_suptitle_xycoords
 #                  set_plot_multichart_suptitle_xycoords
 #                  set_scatterplot_multichart_suptitle_xycoords
 #
 #  Function Description:
 #      The function sets the multichart suptitle's x and y coordinates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the multichart suptitle's x-coordinate.
 #  float          y_flt            The parameter is the multichart suptitle's y-coordinate.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_suptitle_xycoords(x_flt, y_flt):

    set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTIBAR.value)

def set_boxplot_multichart_suptitle_xycoords(x_flt, y_flt):

    set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTIBOXPLOT.value)

def set_histogram_multichart_suptitle_xycoords(x_flt, y_flt):

    set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTIHISTOGRAM.value)

def set_line_multichart_suptitle_xycoords(x_flt, y_flt):

    set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTILINE.value)

def set_pie_multichart_suptitle_xycoords(x_flt, y_flt):

    set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTIPIE.value)

def set_plot_multichart_suptitle_xycoords(x_flt, y_flt):

    set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTIPLOT.value)

def set_scatterplot_multichart_suptitle_xycoords(x_flt, y_flt):

    set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTISCATTER.value)


# In[77]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_xysuplabels
 #                  get_boxplot_multichart_xysuplabels
 #                  get_histogram_multichart_xylabels
 #                  get_line_multichart_xysuplabels
 #                  get_pie_multichart_xysuplabels
 #                  get_plot_multichart_xysuplabels
 #                  get_scatterplot_multichart_xysuplabels
 #
 #  Function Description:
 #      The function retrieves the multichart's x-axis suplabel and y-axis suplabel.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_xysuplabels(): 

    return get_multichart_xysuplabels(chart_enum.MULTIBAR.value)

def get_boxplot_multichart_xysuplabels(): 

    return get_multichart_xysuplabels(chart_enum.MULTIBOXPLOT.value)

def get_histogram_multichart_xylabels(): 

    return get_multichart_xysuplabels(chart_enum.MULTIHISTOGRAM.value)

def get_line_multichart_xysuplabels(): 

    return get_multichart_xysuplabels(chart_enum.MULTILINE.value)

def get_pie_multichart_xysuplabels(): 

    return get_multichart_xysuplabels(chart_enum.MULTIPIE.value)

def get_plot_multichart_xysuplabels(): 

    return get_multichart_xysuplabels(chart_enum.MULTIPLOT.value)

def get_scatterplot_multichart_xysuplabels(): 

    return get_multichart_xysuplabels(chart_enum.MULTISCATTER.value)


# In[78]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_xysuplabels
 #                  set_boxplot_multichart_xysuplabels
 #                  set_histogram_chart_xylabels
 #                  set_line_multichart_xysuplabels
 #                  set_pie_multichart_xysuplabels
 #                  set_plot_multichart_xysuplabels
 #                  set_scatterplot_multichart_xysuplabels
 #
 #  Function Description:
 #      The function sets the multichart's x-axis suplabel and y-axis suplabel.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xsuplabel        The parameter is the multichart's x-axis suplabel.
 #  string         ysuplabel        The parameter is the multichart's y-axis suplabel.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_xysuplabels(xsuplabel, ysuplabel):

    set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTIBAR.value)

def set_boxplot_multichart_xysuplabels(xsuplabel, ysuplabel):

    set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTIBOXPLOT.value)

def set_histogram_multichart_xysuplabels(xsuplabel, ysuplabel):

    set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTIHISTOGRAM.value)

def set_line_multichart_xysuplabels(xsuplabel, ysuplabel):

    set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTILINE.value)

def set_pie_multichart_xysuplabels(xsuplabel, ysuplabel):

    set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTIPIE.value)

def set_plot_multichart_xysuplabels(xsuplabel, ysuplabel):

    set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTIPLOT.value)

def set_scatterplot_multichart_xysuplabels(xsuplabel, ysuplabel):

    set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTISCATTER.value)


# In[79]:


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
 #  Return Type: series or dataframe or none
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
        or isinstance(input_obj, pd.DataFrame): return input_obj

    elif isinstance(input_obj, dict) \
        or isinstance(input_obj, list) \
        or isinstance(input_obj, np.ndarray): return pd.DataFrame(input_obj)

    else: return None


# In[80]:


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
 #  Return Type: series, array, or none
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

    if isinstance(input_obj, list) and len(input_obj) >= 2:

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


# In[81]:


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
 #  Return Type: series or dataframe or none
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

    elif isinstance(input_obj, list \
          or isinstance(input_obj, np.ndarray)) \
            and len(input_obj) >= 2:

        index = dtypesx.cnv_data_to_array(input_obj[0])

        data = dtypesx.cnv_data_to_array(input_obj[1])

        input_series = pd.Series(data, index = index)

        return input_series

    else: return None


# In[82]:


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
 #  Return Type: array, array or none, none
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


# In[83]:


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
 #  Return Type: series or none
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


# In[84]:


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
 #  Return Type: array, array or none, none
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


# In[85]:


#*******************************************************************************************
 #
 #  Function Name:  proc_pie_multichart_input
 #
 #  Function Description:
 #      The function takes a dataframe, dictionary, or list as input for a pie multichart 
 #      and returns a dataframe.
 #
 #
 #  Return Type: dataframe
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

def proc_pie_multichart_input(input_obj):

    if isinstance(input_obj, pd.DataFrame): return input_obj

    elif isinstance(input_obj, dict): return pd.DataFrame(input_obj)

    elif isinstance(input_obj, list): return pd.DataFrame(input_obj)

    else: None


# In[86]:


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
 #  Return Type: list, list or none, none
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


# In[87]:


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

def proc_chart_input(input_obj, chart_enum_value):

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

    elif chart_enum_value == chart_enum.MULTILINE.value:

        return None

    elif chart_enum_value == chart_enum.MULTIPIE.value:

        return proc_pie_multichart_input(input_obj)

    elif chart_enum_value == chart_enum.MULTISCATTER.value:

        return proc_scatterplot_multichart_input(input_obj)


# In[88]:


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


    proc_rvalues(rvalue)


# In[89]:


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


    proc_rvalues(math.sqrt(r_sqr_flt))


# In[90]:


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

    if chart_dict['figure']['stacked']:

        return \
            plt.subplots \
                (chart_dict['figure']['nplots'], 
                 figsize 
                     = (chart_dict['figure']['width'], 
                        chart_dict['figure']['length']),
                 sharex = chart_dict['figure']['sharex'],
                 sharey = chart_dict['figure']['sharey'])

    else:

        return \
            plt.subplots \
                (figsize 
                     = (chart_dict['figure']['width'], 
                        chart_dict['figure']['length']),
                 nrows = chart_dict['figure']['nrows'], 
                 ncols = chart_dict['figure']['ncols'],
                 sharex = chart_dict['figure']['sharex'],
                 sharey = chart_dict['figure']['sharey'])


# In[91]:


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


# In[92]:


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


# In[93]:


#*******************************************************************************************
 #
 #  Function Name:  plot_title_axes_stacked
 #
 #  Function Description:
 #      The function plots the stacked multichart's title, x-axis label, and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         subplot          The parameter is the subplot object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  integer        idx              The parameter is the plot index.
 #  integer        last_idx         The parameter is the last plot index.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_title_axes_stacked \
        (subplot,
         chart_dict,
         idx,
         last_idx):

    if chart_dict['title']['display'] \
        and chart_dict['title']['text'][idx] is not None:

        subplot.set_title \
            (chart_dict['title']['text'][idx],
             fontdict = {'fontsize': chart_dict['title']['fontsize'], 
                         'fontstyle': chart_dict['title']['fontstyle'],
                         'fontweight': chart_dict['title']['fontweight']},
             loc = chart_dict['title']['loc'], 
             pad = chart_dict['title']['pad'])        

    if chart_dict['xlabel']['display'] \
        and chart_dict['xlabel']['text'][idx] is not None \
        and idx == last_idx:

        subplot.set_xlabel \
            (chart_dict['xlabel']['text'][idx],  
             fontsize = chart_dict['xlabel']['fontsize'], 
             fontstyle = chart_dict['xlabel']['fontstyle'], 
             fontweight = chart_dict['xlabel']['fontweight'],
             labelpad = chart_dict['xlabel']['labelpad'],
             loc = chart_dict['xlabel']['loc'])

    if chart_dict['ylabel']['display'] \
        and chart_dict['ylabel']['text'][idx] is not None:

        subplot.set_ylabel \
            (chart_dict['ylabel']['text'][idx],  
             fontsize = chart_dict['ylabel']['fontsize'], 
             fontstyle = chart_dict['ylabel']['fontstyle'], 
             fontweight = chart_dict['ylabel']['fontweight'],
             labelpad = chart_dict['ylabel']['labelpad'],
             loc = chart_dict['ylabel']['loc'])


# In[94]:


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

def plot_title_axes(chart_dict, idx = 0):

    if chart_dict['title']['display'] and chart_dict['title']['text'][idx] is not None:

        plt.title \
            (chart_dict['title']['text'][idx],
             fontdict = {'fontsize': chart_dict['title']['fontsize'], 
                         'fontstyle': chart_dict['title']['fontstyle'],
                         'fontweight': chart_dict['title']['fontweight']},
             loc = chart_dict['title']['loc'],
             pad = chart_dict['title']['pad'])

    if chart_dict['xlabel']['display'] and chart_dict['xlabel']['text'][idx] is not None:

        plt.xlabel \
            (chart_dict['xlabel']['text'][idx],
             fontdict = {'fontsize': chart_dict['xlabel']['fontsize'],
                         'fontstyle': chart_dict['xlabel']['fontstyle'],
                         'fontweight': chart_dict['title']['fontweight']},
             loc = chart_dict['xlabel']['loc'],
             labelpad = chart_dict['xlabel']['pad'])

    if chart_dict['ylabel']['display'] and chart_dict['ylabel']['text'][idx] is not None:

        plt.ylabel \
            (chart_dict['ylabel']['text'][idx],
             fontdict = {'fontsize': chart_dict['ylabel']['fontsize'],
                         'fontstyle': chart_dict['ylabel']['fontstyle'],
                         'fontweight': chart_dict['title']['fontweight']},
             loc = chart_dict['ylabel']['loc'],
             labelpad = chart_dict['ylabel']['pad'])   


# In[95]:


#*******************************************************************************************
 #
 #  Function Name:  plot_limits_stacked
 #
 #  Function Description:
 #      The function sets the x-axis and y-axis limits for a stacked multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         subplot          The parameter is the subplot object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_limits_stacked(subplot, chart_dict):

    if chart_dict['xlim']['display']:

        if chart_dict['xlim']['mode'] == 'set':

            subplot.set_xlim \
                (bottom = chart_dict['xlim']['set']['min'], 
                 top = chart_dict['xlim']['set']['max'],
                 emit = chart_dict['xlim']['emit'],
                 auto = chart_dict['xlim']['auto'])


    if chart_dict['ylim']['display']:

        if chart_dict['ylim']['mode'] == 'set':

            subplot.set_ylim \
                (bottom = chart_dict['ylim']['set']['min'], 
                 top = chart_dict['ylim']['set']['max'],
                 emit = chart_dict['ylim']['emit'],
                 auto = chart_dict['ylim']['auto'])


# In[96]:


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

    if chart_dict['xlim']['display']:

        if chart_dict['xlim']['mode'] == 'set':

            plt.xlim \
                (chart_dict['xlim']['set']['min'], 
                 chart_dict['xlim']['set']['max'])
        else:

            plt.xlim(left = chart_dict['xlim']['adjust']['left'])

            plt.xlim(right = chart_dict['xlim']['adjust']['right'])


    if chart_dict['ylim']['display']:

        if chart_dict['ylim']['mode'] == 'set':

            plt.ylim \
                (chart_dict['ylim']['set']['min'], 
                 chart_dict['ylim']['set']['max'])
        else:

            plt.ylim(left = chart_dict['ylim']['adjust']['left'])

            plt.ylim(right = chart_dict['ylim']['adjust']['right']) 


# In[97]:


#*******************************************************************************************
 #
 #  Function Name:  plot_ticks_stacked
 #
 #  Function Description:
 #      The function plots the x-axis and y-axis ticks and chart grid 
 #      for a stacked multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         subplot          The parameter is the subplot object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  integer        idx              The parameter is the plot index.
 #  integer        last_idx         The parameter is the last plot index.
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

def plot_ticks_stacked \
        (subplot,
         chart_dict,
         idx,
         last_idx,
         tick_lbls_array = np.array([], dtype = str),
         boxplot_bool = False):

    if not boxplot_bool:

        if chart_dict['xticks']['display']:

            if idx != last_idx:

                subplot.set_xticklabels(labels = [])

            subplot.tick_params \
                (axis = 'x', 
                 labelrotation = chart_dict['xticks']['rotation'], 
                 labelsize = chart_dict['xticks']['fontsize'])

    else:

        if chart_dict['xticks']['display']:

            ticks_idx_array = np.array([], dtype = int)

            for idx, lbl in enumerate(tick_lbls_array):

                ticks_idx_array = np.append(ticks_idx_array, idx + 1)


            subplot.set_xticks(ticks_idx_array, tick_lbls_array)

            subplot.tick_params \
                (axis = 'x', 
                 labelrotation = chart_dict['xticks']['rotation'], 
                 labelsize = chart_dict['xticks']['fontsize'])


    if chart_dict['yticks']['display']:

        subplot.tick_params \
            (axis = 'y', 
             labelrotation = chart_dict['yticks']['rotation'], 
             labelsize = chart_dict['yticks']['fontsize'])


    if chart_dict['grid']['display']:

        subplot.grid \
            (visible = chart_dict['grid']['visible'],
             which = chart_dict['grid']['which'],
             axis =  chart_dict['grid']['axis'])   


# In[98]:


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

    if not boxplot_bool:

        if chart_dict['xticks']['display']:

            plt.xticks \
                (fontsize = chart_dict['xticks']['fontsize'], 
                 rotation = chart_dict['xticks']['rotation'])

    else:

        if chart_dict['xticks']['display']:

            ticks_idx_array = np.array([], dtype = int)

            for idx, lbl in enumerate(tick_lbls_array):

                ticks_idx_array = np.append(ticks_idx_array, idx + 1)


            plt.xticks \
                (ticks_idx_array, 
                 tick_lbls_array,
                 fontsize = chart_dict['xticks']['fontsize'], 
                 rotation = chart_dict['xticks']['rotation'])


    if chart_dict['yticks']['display']:

        plt.yticks \
            (fontsize = chart_dict['yticks']['fontsize'], 
             rotation = chart_dict['yticks']['rotation'])


    if chart_dict['grid']['display']:

        plt.grid \
            (visible = chart_dict['grid']['visible'],
             which = chart_dict['grid']['which'],
             axis =  chart_dict['grid']['axis'])   


# In[99]:


#*******************************************************************************************
 #
 #  Function Name:  plot_legend_stacked
 #
 #  Function Description:
 #      The function plots the chart's legend for a stacked multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          plot_array       The parameter is the plot array.   
 #  array          names_array      The parameter is the names array.   
 #  object         axs              The parameter is the axes object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_legend_stacked \
        (plot_array, 
         names_array, 
         axs, 
         chart_dict):

    if chart_dict['legend']['display']:

        plt.legend \
            (plot_array, 
             names_array, 
             loc = chart_dict['legend']['loc'],
             fontsize = chart_dict['legend']['fontsize'],
             bbox_to_anchor = chart_dict['legend']['bbox_to_anchor'])


# In[100]:


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

    if chart_dict['legend']['display']:

        plt.legend \
            (loc = chart_dict['legend']['loc'],
             fontsize = chart_dict['legend']['fontsize'],
             bbox_to_anchor = chart_dict['legend']['bbox_to_anchor'])


# In[101]:


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


# In[102]:


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

def plot_peaks(input_series, chart_dict):

    if chart_dict['peaks']['display']:

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


# In[103]:


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

def plot_suptitle_axes(figure, chart_dict):

    if chart_dict['suptitle']['text'] is not None:

        figure.suptitle \
            (t = chart_dict['suptitle']['text'], 
             x = chart_dict['suptitle']['x'],
             y = chart_dict['suptitle']['y'],
             horizontalalignment = chart_dict['suptitle']['horizontalalignment'],
             verticalalignment = chart_dict['suptitle']['verticalalignment'],
             fontproperties = chart_dict['suptitle']['fontproperties'])

    if chart_dict['supxlabel']['text'] is not None:

        figure.supxlabel \
            (t = chart_dict['supxlabel']['text'], 
             x = chart_dict['supxlabel']['x'],
             y = chart_dict['supxlabel']['y'],
             horizontalalignment = chart_dict['supxlabel']['horizontalalignment'],
             verticalalignment = chart_dict['supxlabel']['verticalalignment'],
             fontproperties = chart_dict['supxlabel']['fontproperties'])

    if chart_dict['supylabel']['text'] is not None:

        figure.supylabel \
            (t = chart_dict['supylabel']['text'], 
             x = chart_dict['supylabel']['x'],
             y = chart_dict['supylabel']['y'],
             horizontalalignment = chart_dict['supylabel']['horizontalalignment'],
             verticalalignment = chart_dict['supylabel']['verticalalignment'],
             fontproperties = chart_dict['supylabel']['fontproperties'])


# In[104]:


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

    if chart_dict['tight_layout']['display']:

        plt.tight_layout \
            (pad = chart_dict['tight_layout']['pad'],
             h_pad = chart_dict['tight_layout']['h_pad'],
             w_pad = chart_dict['tight_layout']['w_pad'],
             rect = chart_dict['tight_layout']['rect'])


# In[105]:


#*******************************************************************************************
 #
 #  Function Name:  plot_subplots_adjust
 #
 #  Function Description:
 #      The function plots width and height spaces for subplots.
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

def plot_subplots_adjust(chart_dict):

    if chart_dict['figure']['wspace'] is not None \
        and chart_dict['figure']['hspace'] is not None:

        plt.plot_subplots_adjust \
            (wspace = chart_dict['figure']['wspace'], 
             hspace = chart_dict['figure']['hspace'])


# In[106]:


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

def plot_bar_chart_series(input_series, chart_dict):

    if chart_dict['params']['horizontal']:

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

    else: 

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


# In[107]:


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

def plot_bar_chart_df(input_df, chart_dict):

    if chart_dict['params']['horizontal']:

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



# In[108]:


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

def plot_bar_chart(input_obj, chart_dict):

    if isinstance(input_obj, pd.Series): plot_bar_chart_series(input_obj, chart_dict)

    elif isinstance(input_obj, pd.DataFrame): plot_bar_chart_df(input_obj, chart_dict)


# In[109]:


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

def plot_boxplot_chart(data_list, tick_lbls_array, chart_dict):

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


# In[110]:


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

def plot_histogram_chart(data_array, chart_dict):

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


# In[111]:


#*******************************************************************************************
 #
 #  Function Name:  plot_line_chart
 #
 #  Function Description:
 #      The function plots a line chart only from a series or dataframe.
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

def plot_line_chart(input_obj, chart_dict):

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


# In[112]:


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

def plot_pie_chart(data_array, labels_array, chart_dict):

    plt.pie \
        (data_array,
         labels = labels_array, 
         explode = chart_dict['params']['explode'] * len(data_array), 
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


# In[113]:


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

def plot_plot_chart(data_series, chart_dict):

    data_series \
        .plot \
            (scalex = chart_dict['params']['scalex'],
             scaley = chart_dict['params']['scaley'],
             color = chart_dict['params']['color'],
             alpha = chart_dict['params']['alpha'])


# In[114]:


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

def plot_scatterplot_chart(x_array, y_array, chart_dict):

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


# In[115]:


#*******************************************************************************************
 #
 #  Function Name:  plot_line_multichart_stacked
 #
 #  Function Description:
 #      The function plots a stacked line multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_line_multichart_stacked(input_df, suptitle):

    global line_multichart_dict


    line_multichart_dict['suptitle']['text'] \
        = suptitle

    line_multichart_dict['figure']['nplots'] \
        = dtypesx.rtn_data_obj_size(input_df)

    last_idx \
        = line_multichart_dict['figure']['nplots'] - 1


    fig, axs = plot_subplots(line_multichart_dict)

    plot_suptitle_axes(fig, line_multichart_dict)


    legend_plot_array = np.array([], dtype = object)

    legend_names_array = np.array([], dtype = str)


    if line_chart_dict['ylabel']['text'][0] is None: ylabel_bool = True

    else: ylabel_bool = False


    for idx, subplot in enumerate(axs):

        curr_series = input_df.iloc[:, idx]

        line_subplot, \
            = subplot.plot \
                (curr_series.dropna(), 
                 color = line_chart_dict['line']['color'][idx])


        legend_plot_array = np.append(legend_plot_array, line_subplot)

        legend_names_array = np.append(legend_names_array, curr_series.name)


        if ylabel_bool:

            line_chart_dict['ylabel']['text'] = legend_names_array


        plot_title_axes_stacked(subplot, line_chart_dict, idx, last_idx)

        plot_limits_stacked(subplot, line_chart_dict)

        plot_ticks_stacked(subplot, line_chart_dict, idx, last_idx)


    plot_legend_stacked \
        (legend_plot_array, 
         legend_names_array, 
         axs, 
         line_chart_dict)


    plot_subplots_adjust(line_multichart_dict)


    line_chart_dict['ylabel']['text'] = [None]

    logx.save_matplotlib_image(line_multichart_dict['suptitle']['text'])


    plt.show()


# In[116]:


#*******************************************************************************************
 #
 #  Function Name:  plot_line_multichart
 #
 #  Function Description:
 #      The function plots a line multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_line_multichart(input_df, suptitle):

    global line_multichart_dict


    line_multichart_dict['suptitle']['text'] \
        = suptitle

    line_multichart_dict['figure']['nplots'] \
        = dtypesx.rtn_data_obj_size(input_df)


    nrows, ncols = mathx.calc_rows_and_cols(line_multichart_dict)


    line_multichart_dict['figure']['nrows'] = nrows

    line_multichart_dict['figure']['ncols'] = ncols


    fig, axs = plot_subplots(line_multichart_dict)

    plot_suptitle_axes(fig, line_multichart_dict)


    for idx in range(line_multichart_dict['figure']['nplots']):

        plot_subplot(line_multichart_dict, idx)


        series = input_df.iloc[: ,idx]

        plot_line_chart(series.dropna(), line_chart_dict)


        plot_title_axes(line_chart_dict, idx)

        plot_limits(line_chart_dict)

        plot_ticks(line_chart_dict)


        plot_tight_layout(line_multichart_dict)


    plot_subplots_adjust(line_multichart_dict)


    logx.save_matplotlib_image(suptitle)

    plt.show()


# In[117]:


#*******************************************************************************************
 #
 #  Function Name:  plot_pie_multichart
 #
 #  Function Description:
 #      The function plots a pie multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj         The parameter is the input object.
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_pie_multichart(input_obj, suptitle):

    global pie_multichart_dict

    global pie_chart_dict


    data_df = proc_chart_input(input_obj, chart_enum.MULTIPIE.value) 


    pie_multichart_dict['suptitle']['text'] = suptitle

    pie_multichart_dict['figure']['nplots'] = dtypesx.rtn_data_obj_size(data_df)


    nrows, ncols = mathx.calc_rows_and_cols(pie_multichart_dict)


    pie_multichart_dict['figure']['nrows'] = nrows

    pie_multichart_dict['figure']['ncols'] = ncols


    fig, axs = plot_subplots(pie_multichart_dict)

    plot_suptitle_axes(fig, pie_multichart_dict)


    for idx in range(pie_multichart_dict['figure']['nplots']):

        plot_subplot(pie_multichart_dict, idx)


        series = data_df.iloc[:, idx]

        data_array = series.to_numpy()


        pie_chart_dict['title']['text'] = series.name.title(),

        labels_array = series.index.to_numpy()


        plot_pie_chart(data_array, labels_array, pie_chart_dict)


        plot_title_axes(pie_chart_dict)

        plot_legend(pie_chart_dict)


        plot_tight_layout(pie_multichart_dict)


    plot_subplots_adjust(line_multichart_dict)


    logx.save_matplotlib_image(suptitle)

    plt.show()


# In[118]:


#*******************************************************************************************
 #
 #  Function Name:  plot_scatterplot_multichart
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

def plot_scatterplot_multichart(input_obj, suptitle):

    global scatterplot_multichart_dict


    scatterplot_multichart_dict['suptitle']['text'] \
        = suptitle

    scatterplot_multichart_dict['figure']['nplots'] \
        = dtypesx.rtn_data_obj_size(input_obj)


    nrows, ncols = mathx.calc_rows_and_cols(scatterplot_multichart_dict)


    scatterplot_multichart_dict['figure']['nrows'] = nrows

    scatterplot_multichart_dict['figure']['ncols'] = ncols


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


    logx.save_matplotlib_image(suptitle)

    plt.show()


# In[119]:


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

def bar_chart(input_obj, title):

    global bar_chart_dict


    bar_chart_dict['title']['text'] = [title]

    plot_figsize(bar_chart_dict)


    temp_obj = proc_chart_input(input_obj, chart_enum.BAR.value)

    plot_bar_chart(temp_obj, bar_chart_dict)


    plot_title_axes(bar_chart_dict)

    plot_limits(bar_chart_dict)

    plot_ticks(bar_chart_dict)

    plot_legend(bar_chart_dict)


    logx.save_matplotlib_image(title)

    plt.show()    


# In[120]:


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

def boxplot_chart(input_obj, title):

    global boxplot_chart_dict


    boxplot_chart_dict['title']['text'] = [title]

    plot_figsize(boxplot_chart_dict)


    data_list, tick_lbls_array = proc_chart_input(input_obj, chart_enum.BOXPLOT.value)

    plot_boxplot_chart(data_list, tick_lbls_array, boxplot_chart_dict)


    plot_title_axes(boxplot_chart_dict)

    plot_limits(boxplot_chart_dict)

    plot_ticks(boxplot_chart_dict, tick_lbls_array, True)


    logx.save_matplotlib_image(title)

    plt.show()


# In[121]:


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

def histogram_chart(input_obj, title):

    global histogram_chart_dict


    histogram_chart_dict['title']['text'] = [title]        

    plot_figsize(histogram_chart_dict)


    data_array = proc_chart_input(input_obj, chart_enum.HISTOGRAM.value)

    plot_histogram_chart(data_array, histogram_chart_dict)


    plot_title_axes(histogram_chart_dict)

    plot_limits(histogram_chart_dict)

    plot_ticks(histogram_chart_dict)

    plot_legend(histogram_chart_dict)


    logx.save_matplotlib_image(title)

    plt.show()


# In[122]:


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

def line_chart(input_obj, title):

    global line_chart_dict


    line_chart_dict['title']['text'] = [title]        

    plot_figsize(line_chart_dict)


    temp_obj = proc_chart_input(input_obj, chart_enum.LINE.value)

    plot_line_chart(temp_obj, line_chart_dict)


    plot_title_axes(line_chart_dict)

    plot_limits(line_chart_dict)

    plot_ticks(line_chart_dict)

    plot_legend(line_chart_dict)


    logx.save_matplotlib_image(title)

    plt.show()


# In[123]:


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

def pie_chart(input_obj, title):

    global pie_chart_dict


    pie_chart_dict['title']['text'] = [title]        

    plot_figsize(scatterplot_chart_dict)


    data_array, labels_array = proc_chart_input(input_obj, chart_enum.PIE.value)

    plot_pie_chart(data_array, labels_array, pie_chart_dict)


    plot_title_axes(pie_chart_dict)

    plot_legend(pie_chart_dict)


    logx.save_matplotlib_image(title)

    plt.show()   


# In[124]:


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

def plot_chart(input_obj, title):

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


    logx.save_matplotlib_image(title)

    plt.show()


# In[125]:


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

def scatterplot_chart(input_obj, title):

    global scatterplot_chart_dict


    scatterplot_chart_dict['title']['text'] = [title]

    plot_figsize(scatterplot_chart_dict)


    x_array, y_array = proc_chart_input(input_obj, chart_enum.SCATTER.value)

    plot_scatterplot_chart(x_array, y_array, scatterplot_chart_dict)


    plot_title_axes(scatterplot_chart_dict)

    plot_limits(scatterplot_chart_dict)

    plot_ticks(scatterplot_chart_dict)


    plot_regr_line(x_array, y_array, regr_line_dict)


    logx.save_matplotlib_image(title)

    plt.show()


# In[126]:


#*******************************************************************************************
 #
 #  Function Name:  line_multichart
 #
 #  Function Description:
 #      The function plots a line multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def line_multichart(input_df, suptitle):

    if line_multichart_dict['figure']['stacked']: 

        plot_line_multichart_stacked(input_df, suptitle)

    else: plot_line_multichart(input_df, suptitle)


# In[127]:


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

def pie_multichart(input_obj, suptitle):

    if pie_multichart_dict['figure']['stacked']: pass

    else: plot_pie_multichart(input_obj, suptitle)


# In[128]:


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

def scatterplot_multichart(input_obj, suptitle):

    if scatterplot_multichart_dict['figure']['stacked']: pass

    else: plot_scatterplot_multichart(input_obj, suptitle)


# In[ ]:




