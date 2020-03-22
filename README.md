# schools data
For those interested in schools data such as ratings, performance or what good schools there are in your area. Currently, the best way is to utilise data provided by ofsted. I used **beautiful soup** to crawl their website and ofsted csv files, putting them through **panda dataframes**.

Source: https://www.compare-school-performance.service.gov.uk/download-data

I used **ETL** to extract the relevent data and stored them into **mysql** - designed so that new datasets can be added with minimal work. **mysql workbench** was very handy for data validation during testing.

So that's the data part. The next phase will be visualisation.

