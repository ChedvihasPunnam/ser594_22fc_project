#### SER594: Project Proposal
#### Title: Keywords Generation
#### Author: Chedvihas Punnam
#### Date: 09/25/2022

Keywords: Natural Language Processing, Keywords, Technology Blogs.

Description: Project idea is to generate keywords from the blog content of technology related blogs written by varoius top tech companies. This can be done by first scraping blogs of vvarious categories from top tech companies. Later using Natural Language processing, keywords should be genrated from the content of the blogs. So for a blog given as input, a list of keywords which are very relevant to the blog content should be given as output.

Intellectual Merit:  Let us say a person is looking for blogs related to Machine Learning, for this he/she need to go to each website and check those blogs related to machine learning. With the help of keywords we generate from the content of the blog, a website can be created where the all the blogs can be filtered based on the keyword the person is looking for, which makes it easily accessible. This can look like leetcode, where we can choose a topic and get all the problems related to that. 

Data Sourcing: For almost every website there is a sitemap where the data is stored in the xml format, from which the blog data can be scraped. The sitemap link for most of the websites are found in the "robots.txt" files of the website. Using requests and beautifusoup modules in python the data can be retrieved from the blogs and can be stored in a csv format to perform futher operations on the data.
               Example: https://engineering.fb.com/sitemap-1.xml
Related Work: DOI - https://doi.org/10.1109/ICTER.2016.7829895