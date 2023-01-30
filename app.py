import streamlit
import numpy as np
import matplotlib.pyplot as plt
from micrograd.engine import Value
import long_texts, table_of_contents, introduction

streamlit.set_page_config(layout="wide")

sidebar = streamlit.sidebar
sidebar.markdown('<h1>Select the page you want to see:</h1>', unsafe_allow_html=True)
page_name = sidebar.radio(
    'In this article:', 
    ['Introduction', 'Derivatives', 'The Chain Rule', 'Maximizing/Minimizing a function', 'Building micrograd', 'Backpropagation']
)

if page_name.lower() == 'introduction':
    introduction.create_intro_page(sidebar=sidebar)

elif page_name.lower() == 'derivatives':
    introduction.create_derivatives_page(sidebar=sidebar)

elif page_name.lower() == 'the chain rule':
    introduction.create_chain_rule_page(sidebar=sidebar)

elif page_name.lower() == 'maximizing/minimizing a function':
    introduction.create_max_min_concept_derivatives(sidebar=sidebar)