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

# +
## Literature survey on HFCS
# -

import pandas as pd
import os
path = os.path.dirname(os.getcwd())

db = pd.read_excel(path+"/201707_HFCS_citations_selected.xlsx")

db.head()

pub_list = set(db["Publisher"])
print(pub_list)

source_list = set(db["Source"])
print(source_list)

for i in range(len(db)):
    gs_link = db['ArticleURL'][i]
    print(gs_link)

for i in range(len(db)):
    gs_link = db['CitesURL'][i]
    print(gs_link)

# ##  Literature Survey 

# ### Section 1.
#
# <cite data-cite="kaplan_wealthy_2014"></cite> studies the wealthy hands-to-month.


