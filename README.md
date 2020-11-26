# UK Schools Data
For those interested in schools data such as ratings, performance or what good schools there are in your area. Currently, the best way is to utilise data provided by ofsted. **beautiful soup** was used to traverse their website as well as levereaging some of the ofsted csv files available. Data processed through **panda dataframes** - significant time expended on research , data cleansing and formatting.

Source: https://www.compare-school-performance.service.gov.uk/download-data

**ETL** to extract the relevent data and stored them into **mysql** - designed so that new datasets can be added with minimal work. **mysql workbench** came in handy for data validation during testing.

Note, below flowcharts depicting data flow from source to database were created using **y_ed Graph Editor**.

GENERAL
![alt text](https://github.com/waiky8/uk-schools-data/blob/master/school_general.png)

PERFORMANCE
![alt text](https://github.com/waiky8/uk-schools-data/blob/master/school_performance.png)

FINANCIALS
![alt text](https://github.com/waiky8/uk-schools-data/blob/master/school_financials.png)

So that's the data part. Next is the fun bit - visualisation.

COVID-19 Update:

"The Government has announced that it will not publish any school or college level educational performance data based on tests, assessments or exams for 2020."

