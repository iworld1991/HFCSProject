# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Literature survey on HFCS
#
# - This notebook has an automized reader that goes over a list of papers regarding HFCS whose citation information is stored in the excel sheet.
# - It prints out all the title and abstracts in the notebook, so that I can draft the literature review here within the same notebook.
# - It also cites the literature from bib file. 

import pandas as pd
import os
import scholarly as sc
path = os.path.dirname(os.getcwd())

db = pd.read_excel(path+"/201707_HFCS_citations_selected.xlsx")

db.head()

# + {"code_folding": []}
#list(db['Abstract'])
# -

pub_list = set(db["Publisher"])
print(pub_list)

source_list = set(db["Source"])
print(source_list)

## links
for i in range(len(db)):
    gs_link = db['ArticleURL'][i]
    #print(gs_link)

# + {"code_folding": [0]}
## google links
for i in range(len(db)):
    gs_link = db['CitesURL'][i]
    #print(gs_link)

# + {"code_folding": []}
## try to search google again

#for i in range(len(db)):
    #search_query = sc.search_pubs_query(db['Title'][i])
    #citedby  = next(search_query)
    #print(db['Title'][i])
    #print(citedby.bib['abstract'])

# + {"code_folding": [0]}
for i in range(len(db)):
    title = db['Title'][i]
    author = db['Authors'][i]
    abstract = db['Abstract'][i]
    print(title)
    print(author)
    print("\n")
    print(abstract)
    print("\n")
# -

# ##  Literature Survey 

# ### Section 1.
#
# <cite data-cite="kaplan_wealthy_2014"></cite> studies the wealthy hands-to-month.

# the paper [cite](#cite-PER-GRA:2007)

# <!--bibtex
#
# @Article{PER-GRA:2007,
#   Author    = {P\'erez, Fernando and Granger, Brian E.},
#   Title     = {{IP}ython: a System for Interactive Scientific Computing},
#   Journal   = {Computing in Science and Engineering},
#   Volume    = {9},
#   Number    = {3},
#   Pages     = {21--29},
#   month     = may,
#   year      = 2007,
#   url       = "http://ipython.org",
#   ISSN      = "1521-9615",
#   doi       = {10.1109/MCSE.2007.53},
#   publisher = {IEEE Computer Society},
# }
#
# ... Other Bibtex entries go here.
#
# -->

# __Major topics covered by this literature__
#
#
# - Drivers of wealth inequality 
#    - Home ownership
#    - Institutions
#    - Distributional effects of monetary policy 
#    - Distributional effects of fiscal policies
#  
# - Implications of wealth inequality
#    - Wealth effect of consumption
#    - Heterogeneity in MPCs
#    - Monetary policy transimission
#
# - Use of the data on other questions
#   - How macro experiences affect saving decision? 
#   - Social interactions and borrowing behaviors.
#   
# __Merits of the HFCS__
#
# - Cross-country variation 
# - Cross-country variation but with a single currency zone
# - Coexistence of wealth/income data
# - Exact form of wealth 


