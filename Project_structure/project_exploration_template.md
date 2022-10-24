#### SER594: Exploratory Data Munging and Visualization
#### Title: Keywords Generation from blog content.
#### Author: Chedvihas Punnam
#### Date: 10/22/2022

## Basic Questions
**Dataset Author(s):** Chedvihas Punnam

**Dataset Construction Date:** 10/23/2022

**Dataset Record Count:** 4717

**Dataset Field Meanings:** The dataset I scraped contains the blog content, url, title of the articles along with the name of the website from which the blog is scraped.

There are 4 columns in the dataset. The columns are:
Website --> This is the name of the website from which the article present in this row is taken from, 
            here I have scraped data from 2 websites: AWS, Facebook. So, either of these 2 values will be present under this column.
Title --> This is the title of the blog that is present in this cell.
Link --> This is the url of the current blog that we have in this cell.
content --> The text present in this blog is the blog content present in the above url.



**Dataset File Hash(es):** I have scraped the datset, so I did not generate the hash.

## Interpretable Records
**Note:**  For the content of the below records, I am only placing first few lines of it, as there are many lines present in the content.
### Record 1
**Raw Data:** AWS(Website), Introducing the AWS SDK for Ruby(Title), https://aws.amazon.com/blogs/aws/introducing-the-aws-sdk-for-ruby/(Link),
                (content) - Ruby is a wonderful programming language.Â Optimized for â€˜developer joyâ€™, it is an object oriented playground for building simple domain specific languages, orchestration tools, and most famously, web applications. In many ways, the Ruby language and Amazon cloud services such as EC2 and S3 have similar goals: to help developers and businesses build innovative products without worrying about the â€˜muckâ€™ that can slow development down.Today weâ€™re bringing Ruby and AWS even closer together, with the AWS SDK for Ruby.The AWS SDK for Ruby gemThe SDK features a new Ruby gem for accessing a wealth of AWS compute, storage and middleware services whilst handling common tasks such as authentication, request retries, XML processing, error handling and more. With this release of the SDK you can access Amazon EC2,Â S3, SQS, SNS andÂ the Simple Email................

**Note:**  For
Interpretation:** In the above raw data, we can see that name of the website is AWS, link has "aws.amazon.com". Along with this title has something related to AWS, SDK, Ruby, the content of the blog also discusses regarding these words.

### Record 2
**Raw Data:** Facebook(website), Android native library merging(Title), https://engineering.fb.com/2018/01/23/android/android-native-library-merging/(link), 
                content - Android developers who use lots of C++ code might be familiar with the native library limit that exists in Android versions prior to 4.3. When targeting older Android versions, one must carefully manage the number of libraries in their app to avoid hitting this....

**Interpretation:** In the above data, we can see that name of the website is Facebook and link also contains "engineering.fb.com". The title of the blog says about Android native library merging, as we can see in the blog content it is saying something relevant to android developers, versions, libraries.

## Data Sources
    I have scraped dataset from sitemap urls of facebook, aws tech blogs websites where the links of all the respective articles are present. 
    Following are the sitemap urls:
    AWS - https://aws.amazon.com/sitemaps/sitemap_blogs/
    Facebook - https://engineering.fb.com/sitemap-1.xml

### Transformation 1
**Description:** - Null values removal. I have got only 2 null values in the 'content' in the dataset scraped. So, I have dropped these 2 rows from the datset.


**Soundness Justification:** - The operation doesn't affect datset in a bad way because there are only 2 rows containing null values among 4717 rows. So dropping those won't be an issue. And these null values are present in the content. The content of the blog is very important and can't be empty as we generate keywords from the content, so I felt that dropping won't affect the dataset.


### Transformation 2
**Description:** - Adding title to the blog content. A sour usecase is generating keywrods, I felt that there can be some relevant keywords in the title as well, so I have added title to the blog content.


**Soundness Justification:** - The operation doesnot affect the dataset because title defines or summarizes most of the blog content, so adding it to the content helps.

### Transformation 3
**Description:** - Removing punctuation. I have removed punctuation from the content of the blog as they do not help in generating keywords.


**Soundness Justification:** - The operation doesnot affect the dataset because punctuation cannot be a part of keywords.

### Transformation 4
**Description:** - Removing stopwords and lemmatizing. English stopwords are removed and all the text is lemmatized from the content of each blog.


**Soundness Justification:** - The operation doesnot affect the dataset because stopwords cannot be the keywords, because they only help in forming meaningful sentences and they can't define or represent the whole blog content. Lemmatization also won't affect because it removes the plurals and stuff from the words, in the sense of our usecase, to generate keywords, plural of the word doesn't help.



## Visualization
### Visual barplots :

**Analysis:** I have created barplots between the blog count from each of AWS and Facebook. From the graph we can observe that the number of blogs of Facebook are almot 25-30% of the blogs from AWS website. Another barplot which shows count of words in the original datset vs the preprocessed dataset. We can observe that in the preprocessed data there is a significant decrease in number of words, this means that there are significant amount of stopwords present in the whole content.

## Visualization
### Visual ScatterPlots:

**Analysis:** I have created scatterplots between word count of original vs preprocessed data. In this we can observe that the data isn't that scattered. Whereas in the scatterplots which shows word count of original vs stopwords count and word count of preprocessed vs stop words count, we can observe that the data points are a bit scattered.

## Visualization
### Visual PieCharts:

**Analysis:** I have created piecharts showing the blogs percentage from each website. In this we can see that contribution of AWS is more towards the number of blogs. In other chart showing contribution towards number of words we can see that even though facebook only has 18% of the blogs among all blogs, it has about 33% contribution towards word count, the reason for this can be the word count in each blog of facebook might be greater compared to that in AWS blogs. In the other pie chart we can see the contribution of AWS and Facebook towards stopwords.




(duplicate above as many times as needed; remove this line when done)