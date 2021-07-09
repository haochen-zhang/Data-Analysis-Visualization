# -*- coding: utf-8 -*-
"""
Created on Tue May 18 09:28:39 2021

@author: Haochen Zhang
"""

import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Revies")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    return wp

jp.justpy(app)