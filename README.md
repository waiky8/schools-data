# schools data
If you have kids then at some point you will be interested in finding out the good schools in your area, or for some you may even consider moving to a desirable catchment area. At the moment, the best way is to look at the data provided by ofsted. There are plenty of ways to view the data on the web but I wanted more flexibility in my queries. So I started to build my own database using data provided by ofsted. I began by using **beautiful soup** (bs) to crawl the data from their websites but discovered it was more efficient just to make use of the suite of csv files available for download. Though I did leave some bs code in there for specific tasks. Fortunately, they also provided decent explanations to the data so I was able to navigate easy enough.

Source: https://www.compare-school-performance.service.gov.uk/download-data

I applied ETL technique to extract the relevent data from the csv files and stored them into **mysql** for later consumption - **mysql workbench** was useful in verifying the data during testing. The next phase is visualisation.

Let's begin...
