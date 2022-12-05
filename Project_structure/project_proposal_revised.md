#### SER594: Project Proposal
#### Title: Generating keywords from blog content.
#### Author: Chedvihas Punnam
#### Date: 10/29/2022

Keywords: Natural Language Processing, Keywords, Technology Blogs.

Description: Project idea is to generate keywords from the blog content of technology related blogs written by some top tech companies. This can be done by first scraping blogs of various categories from top tech companies. Later using Natural Language processing, keywords should be genrated from the content of the blogs. So for a blog given as input, a list of keywords which are very relevant to the blog content should be given as output.


Research Questions: 

RO1: To describe the trends within the number of blogs, number of words, number of stopwords from the blogs collected from the websites.

RO2: To predict the labels for each blog. Labels are Keywords in case of this project. So, for each blog the objective is to predictive 3 most relevant keywords.

RO3: To defend the model for performing keywords generation, in RO2.

RO4: To defend the the model for performing keywords generation for each blog in RO2, to find the relationship between frequency of all words in each blog.

Intellectual Merit:  Let us say a person is looking for blogs related to Machine Learning, for this he/she need to go to each website and check those blogs related to machine learning. With the help of keywords we generate from the content of the blog, a website can be created where the all the blogs can be filtered based on the keyword the person is looking for, which makes it easily accessible. This can look like leetcode, where we can choose a topic and get all the problems related to that. 

Data Sourcing: For almost every website there is a sitemap where the data is stored in the xml format, from which the blog data can be scraped. The sitemap link for most of the websites are found in the "robots.txt" files of the website. Using requests and beautifusoup modules in python the data can be retrieved from the blogs and can be stored in a csv format to perform futher operations on the data.

Data Sources: https://aws.amazon.com/sitemaps/sitemap_blogs/
              https://engineering.fb.com/sitemap-1.xml

Related Work: https://dl.acm.org/doi/pdf/10.3115/1119355.1119383
              https://doi.org/10.1109/ICTER.2016.7829895
              https://doi.org/10.1002/9780470689646.ch1
              https://doi.org/10.1109/ICTER.2016.7829895
              https://www.seoptimer.com/keyword-generator