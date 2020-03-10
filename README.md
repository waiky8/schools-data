# schools data
If you have kids then at some point you will be interested in finding out the good schools in your area, or for some you may even look to move to a desirable catchment area. At the moment, the best way (and it's not perfect) is to look into data provided by ofsted. There are plenty of ways to view the data on the web but I wanted more. So I started to build my own database using the data provided by ofsted. I started off using "beautiful soup" (bs) to crawl the data from their websites but discovered it was more efficient to make use of the plethora of csv files that they have available. Though I did leave some bs code in there. Fortunately, they also provided decent explanations to the data columns so I was able to navigate easy enough.

Source: https://www.compare-school-performance.service.gov.uk/download-data

I applied ETL technique to extract the relevent data from the csv files and stored them into mysql for later consumption (next phase is visualisation).

Let's begin...
