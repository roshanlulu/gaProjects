![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)
## PROJECT 4 Web Scraping Job Postings

### Description of the folders/files/data-dictionaries used in this project

#### 0. database[folder]
    - The dataset(csv format) and the database(SQL db) created as a result of scrapping have been consolidated in this folder.
    Result of Scraping
        - Search_Results_Final.csv - CSV file with the search results(i.e. links to job posts) from seek.
        - Job_Posts_Final.csv - CSV file with the job features extracted from job posts obtained from Search results.
        - job_seek_final.sqlite - SQL database of Job_Posts_Final.csv
    Result of Cleaning
        - all_jobpost_cleaned_data.csv - CSV file with the cleaned data for all the job posts available after scraping. This will be the master dataset for cases where salary is not the target.
        
        - valid_jobpost_cleaned_data.csv - CSV file with the cleaned data. It contains the job posts with a valid salary amount. This will be used for cases were the salary needs ot be predicted.
        
        - valid_jobpost_text_cleaned_data.csv - CSV file is exactly same as valid_jobpost_cleaned_data.csv with additional features obtained after vectorizing the Job description for valid salaries.
        
#### 1. project4-roshan-01-scraping [ Python NB ]
    - The Job postings i.e. the database/dataset required to answer the questions for this project is obtained in this notebook.
    In short, the web scraping is implemented in this notebook.
##### DATA DICTIONARY - Search_Results_Final.csv
    Job_Desc - Search String given in seek
    Job_Loc - Job Location searched
    Page_Num - Page num of the search results
    url_link - url link of the search result page
    Job_Posts - Job posts links obtained from each url_linl
    
##### DATA DICTIONARY - Job_Posts_Final.csv
    keyword - Search key
    pagenum - Page num of the job post in the search result page
    title - Job Description title
    region - Job posting region in the city(CBD/ Inner West etc)
    location - Job posting location(Sydney/Melbourne)
    salary - Stated salary
    worktype - Stated work type(full time/part time/contract)
    adv - Job Advertiser details
    classif - Job Industry classification
    jd1 - Job description
    jd2 - Job description
    jd3 - Job description
    url - Job posting url

#### 2. project-4-roshan-02-clean-eda [ Python NB ]
    - The Data cleaning and EDA of the scraped data is done in this notebook
    

##### DATA DICTIONARY - all_jobpost_cleaned_data.csv,  valid_jobpost_cleaned_data.csv, valid_jobpost_text_cleaned_data.csv

    Title_Code
        0 - Junior/Associate 
        1 - No Tag/ Mide-level
        2 - Senior/ Officer, 
        3 - Principal/Consultant/Architect/Designer, 
        4 - Lead/Expert/Group, 
        5 - Manager, 
        6 - Post-Doctoral, 
        7 - Head/Director/

    Location_Code
        0 - Sydney
        1 - Melbourne
        2 - Brisbane

    Region_Code
        Sydney
        0 - CBD, Inner West & Eastern Suburbs
        1 - Parramatta & Western Suburbs
        2 - North Shore & Northern Beaches 
        3 - Ryde & Macquarie Park 
        4 - North West & Hills District 
        5 - Southern Suburbs & Sutherland Shire , South West & M5 Corridor 
        6 - Unknown
        Melbourne
        7 - CBD & Inner Suburbs                
        8 - Bayside & South Eastern Suburbs
        9 - Eastern Suburbs
        10 - Northern Suburbs
        11 - Western Suburbs
        12 - Unknown
        Brisbane
        13 - CBD & Inner Suburbs
        14 - Southern Suburbs & Logan
        15 - Bayside & Eastern Suburbs
        16 - Northern Suburbs
        17 - Western Suburbs & Ipswich
        18 - Unknown

    WorkType_Code
        0 - Full Time
        1 - Contract/Temp
        2 - Others - Casual/Vacation/PartTime

    Classif_Code
        0 - Information & Communication Technology
        1 - Science & Technology
        2 - Banking & Financial Services 
          - Accounting
        3 - Consulting & Strategy
          - Marketing & Communications 
        4 - Government & Defence
        5 - Education & Training
        6 - Healthcare & Medical
        7 - Others

    Adv_Code
        0 - Recruiters/Consultants
        1 - Universities
        2 - Companies

    KeyJob_Code
        0 - Data-Analyst
        1 - Data-Science
        2 - Research-Scientist
        3 - Business-Analyst
        4 - Business-Intelligence

    Salary
        Salary per annum with

    Job Description
        Full Job description text
        
#### 3. project-4-roshan-03-qn1-qn2 [ Python NB ]
    - Answers to the Problem statement have been provided in this notebook 
    - Machine learning Regression/Classification Modelling and Validation techniques have been used.

#### 4. Summary_Report.md
    - Report to the Principal detailing the project analysis and findings.