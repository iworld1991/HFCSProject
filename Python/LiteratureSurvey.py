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

# + {"code_folding": []}
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

# #  Presentation title: xxx
#

# ## Section 1. literature survey that is based on the existing data

# ### Section 1.1. Major topics covered by this literature
#
# - Drivers of wealth inequality 
#    - Homeownership 
#      - <cite data-cite="7250895/QK8EPBGS"></cite>: differences in homeownership rates and house price dynamics are important for explaining wealth differences across euro area countries.
#      - <cite data-cite="7250895/DNPW7XVC"></cite>: negative correlation between wealth inequality and home ownership, mostly driven by large between-group inequality across owners and renters.
#      - <cite data-cite="7250895/R8NAIB7B"></cite>: wedges in reantal market are one of the important drivers of differences in wealth inequality across European countries. 
#    - Institutions
#      - public insurance and labor risks. <cite data-cite="7250895/5NVRDSGH"></cite>: wealth inequality across Euro Area countries mostly explained by the differences in welfare policies and less by labor income risks.
#      - household structure. <cite data-cite="7250895/CZ3XDZTX"></cite>: imposing a common household structure has strong effects on both the full unconditional distributions as well as its mappings to different inequality measures.
#      - friction in the debt and equity market.<cite data-cite="7250895/DTHQHGZQ"></cite>: more wealth inequality in countries where there are more private held firms and ownership of publicly traded firms is more concentrated.
#    - Income distribution
#      - <cite data-cite="7250895/R3NVYQYY"></cite>: the location in the income distributions is positively correlated with the location in the wealth distribution. 
#    - Distributional effects of monetary policy
#      - <cite data-cite="7250895/EIPKT7KF"></cite>: monetary policy plays a limited role in driving wealth inequality compared to to income differences. 
#      - <cite data-cite="7250895/7TCJF4DR"></cite>: ECB's non-standard monetary policies produced more benefits to bottom-income group as the general economic and employment benifits overweigh those via financial markets. 
#   
#    - Distributional effects of fiscal policies
#      - <cite data-cite="7250895/X43MNXDK"></cite>: study the income inequality and stronger recessive impacts of fiscal consolidation programs in Euro Area countries in a calibrated life-cycle model.
#    - Distributional effects of asset price increase
#      - <cite data-cite="7250895/U8D8T656"></cite>: different impacts of changes in housing, debt and equity prices on households with different levels of wealth. 
#
#
#  
# - Implications of wealth inequality and market incompleteness
#    - The wealth effect of consumption
#      - <cite data-cite="7250895/ZQKHNQHG"></cite>: a survey paper on wealth effect of consumption.
#    - Heterogeneity in MPCs
#      - <cite data-cite="7250895/LYGFNASY"></cite>: "wealthy hand-to-month".
#      - <cite data-cite="7250895/4BG3W9GZ"></cite>: heterogeneous MPCS across 15 Euro Zone countries.
#      
#    - Monetary policy transmission
#      - <cite data-cite="7250895/X7STV7A6"></cite>:  the indirect income channel dominates other transmission channels of monetary policies, especially for households holding few or no liquid assets.
#      - <cite data-cite="7250895/5AIFVER9"></cite>: monetary policies, operating through its effects on household income and asset market returns, has a differential impact on individuals within and across four Euro area countries. 
#    - Precautionary saving and deflationary spirals: <cite data-cite="7250895/RPWC4MNU"></cite>
#
# - Use of the data on other questions
#
#   - How macro experiences affect saving decisions? 
#      - <cite data-cite="7250895/265UI24R"></cite>: experience of stock market returns affect households's risk-taking and stock market participation across countries in the Euro Area.
#      - <cite data-cite="7250895/8HVWLRJK"></cite>: rent-or-buy decisions shaped by macroeconomic experiences. For instance, higher inflation experiences increases likelihood of home ownership. 
#   - Social interactions and borrowing behaviors.
#      - <cite data-cite="7250895/HL2L3Y36"></cite>: perceived peer income contributes affects debt choice and financial fragility of households.
#   - Financial decisions with bounded rationality 
#      - <cite data-cite="7250895/7TLDTVUQ"></cite>: a lecture on consumer financial regulation in an environment where many households lack the knowledge to manage their financial affairs effectively.
#   - Saving and borrowing behaviors across countries
#      - <cite data-cite="7250895/XE6JTE7U"></cite>: relatively homogeneity in saving preferences but heterogeneity in borrowing constraints across Euro Zone countries.
#      - <cite data-cite="7250895/VT3W29DZ"></cite>: how institutional factors affect the distribution of debt across Euro area countries.
#      - <cite data-cite="7250895/4A5LC8LW"></cite>: the drivers of differences in debt-holding positions between the U.S. and median European countries.
#      - <cite data-cite="7250895/XE6JTE7U"></cite> examines self-assessed saving motives in 15 European countries, the most common one of which is precautionary. 
#   - Diagosis of euro zone debt crisis
#      - <cite data-cite="7250895/K8YWNJB6"></cite>: evaluate impacts of private leverage, fiscal austerity and sudden stop before and after the crisis.
#     
#   - Macroprudential policy and household balance sheet
#      - <cite data-cite="7250895/X7STV7A6"></cite>: stress testing on household balance sheets across Euro Zone countries. 
#   - Top tail of the wealth inequality
#     - <cite data-cite="7250895/LRFKDVCT"></cite>: proposes an approach to address non-response of wealthy group and underreporting of wealth surveys.
#     - <cite data-cite="7250895/F7FEBMJE"></cite>: adding extreme observations help remove downward bias of wealth distribution from survey. 
#     
#   - Mortgage choices
#     - <cite data-cite="7250895/JRXR8Q7W"></cite>: studied the mortgage choice between fixed-interest-rate mortgages (FRMs) and adjustable-interest-rate mortgages (ARMs) across countries.
#   
#   
# ### Section 1.2.  Merits of the HFCS
#
# - Cross-country variation
#   
#   - institutional differences 
#     - labor markets
#     - financial markets
#     - housing market
# - Cross-country variation but with a single currency zone 
#   - particularly useful to study how monetary policy generates distributional consequences depending on the country's specific characteristics.
#   - before the credit boom: the role of household leverage and private borrowing 
#   - after the euro debt crisis, credit supply shock through the bank balance sheet  
#   
# - Cultural differences in affecting household saving borrowing decisions
#     - in particular, the intergenerational concerns
#   
# - Coexistence of wealth/income data
#   
# - The exact form of wealth 
#   - composition of the household assets in terms of liquidity
#   - the particular role of housing wealth

# ### Section 2. A proposal to including a module on expectations
#
# - What is included in the HFCS 
#   - Only realized variables, no question on expectations
#   - But the survey may benefit from including at least some expectation questions
#
#
# - Why include expectations in the existing survey? 
#
#  - General rationale:
#    - Economists like the approach revealed preference, but strong assumption on expectation is needed when both preference and beliefs are not observable. (Manski's idea)
#  
#    - Better identifiction in empirical macro research relies on turely _unanticipated_ shocks by the agents? The best way to control for the antipated change is to directly available in the surveys.
#    
#    
#  - Better answer many questions that puzzle macro/finance literature 
#      - Housing bubble driven by change in credit conditions, or beliefs?
#      - Equity premium puzzle: the current framework requires an unrealistically large degree of risk-aversion to be compatible with the observed stock market participation and risk premium. But this may be because the agents' perception of the risk profile facing their decisions are different. 
#      
#      - The literature on macroeconomic experiences and household investment decisions approximate experience by the year of birth of individuals, but we can do better by asking people why?
#      
#
# - What should be included in future (ranked by decreasing priority) 
#
#   - Micro variables 
#      - from macro to micro 
#      - more individual variables are more relevant to household decisions, i.e. labor income, asset market returns, housing prices, expectations help address participation/asset pricing puzzle
#
#   - Higher Moments
#      - from average forecast to density forecast
#      - probability type of questions in general, not a continuous variable, at least 
#      - higher-order uncertainty, i.e. model uncertainty. 
#
#   - Structure of the survey 
#      - the panel, i.e. individuals need to be asked for repeated times 
#      - inclusion of both realization and expectation 
#         - then better identification of unexpected shocks
#         - allowing to characterize deviations of expectation from the ``truth''
#  
#   - Other Questions
#      - Not just what but also why. 
#          - subjective beliefs 
#          - information sources
#          - experience 
#         
#      - Importance of having expectations as well as behavioral intentions and decisions, 
#        - at least questions that express the inclination of actions 

# ## Reference 
#
# 1. [HFCS Core Questionaire](https://www.ecb.europa.eu/home/pdf/research/hfcn/HFCS_Core_and_derived_variables_Wave2.pdf?8d19475a7edb8ff7de6d99a885e527ec)
