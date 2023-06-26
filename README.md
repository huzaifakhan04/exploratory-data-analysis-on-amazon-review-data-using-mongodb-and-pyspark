# Exploratory Data Analysis (EDA) on Amazon Review Data (2018) Using MongoDB & PySpark:

This repository showcases the outcomes of an Exploratory Data Analysis (EDA), including visualisation, conducted on the comprehensive Amazon Review Data (2018) dataset, consisting of nearly 233.1 million records and occupying approximately 128 gigabytes (GB) of data storage, using MongoDB and PySpark, as part of the final project for the Fundamental of Big Data Analytics (DS2004) course.

In the context of product reviews, Exploratory Data Analysis (EDA) can be used to examine various aspects of the reviews, such as the number of reviews per product, the distribution of ratings, the frequency of certain keywords or phrases in the reviews, and the relationship between the length of the review and the rating. It can also be used to inform further analysis and modelling of the data, as well as to identify potential data quality issues that may need to be addressed.

### Dependencies:

* Jupyter Notebook ([install](https://docs.jupyter.org/en/latest/install.html))
* PySpark ([install](https://spark.apache.org/docs/latest/api/python/getting_started/install.html))
* MongoDB Community Edition ([install](https://www.mongodb.com/docs/manual/administration/install-community/))
* pandas ([install](https://pandas.pydata.org/docs/getting_started/install.html))
* NumPy ([install](https://numpy.org/install/))
* SciPy ([install](https://scipy.org/install/))
* Matplotlib ([install](https://matplotlib.org/stable/users/installing/index.html))
* seaborn ([install](https://seaborn.pydata.org/installing.html))
* Plotly ([install](https://plotly.com/python/getting-started/))
* wordcloud (install - [Anaconda](https://anaconda.org/conda-forge/wordcloud) | install - [PyPI](https://pypi.org/project/wordcloud/))
* NLTK ([install](https://www.nltk.org/install.html))

### What is the Amazon Review Data (2018)?

The Amazon Review Data (2018) dataset is an open-source [collection](https://nijianmo.github.io/amazon/index.html) of nearly 233.1 million product reviews from the Amazon.com marketplace in a JavaScript Object Notation (JSON) format. It contains text reviews and ratings for various products, including books, electronics, movies, and more. The dataset is often used in natural language processing (NLP) and sentiment analysis research. It provides a valuable resource for training machine learning models to understand and analyse customer reviews.

## What Is Our Approach?

For our analysis of the Amazon Review Data (2018) dataset, we utilise inferential statistical analysis as a key component of our approach to Exploratory Data Analysis (EDA). Inferential statistical analysis involves analysing a sample of data to make predictions or draw conclusions about a larger population from which the sample was drawn. Given the large size of the dataset, our goal is to use a sample of the data to make predictions or draw inferences about the larger population with a certain degree of confidence or probability.

### What Problem Does Our Approach Aim to Alleviate?

Amazon Review Data (2018) is an extensive dataset, comprising almost 233.1 million records, and requiring around 60 gigabytes (GB) of data storage. Due to its size, the dataset demands a considerable amount of computation that ordinary computers cannot handle easily. To overcome this challenge, we adopt an inferential statistical analysis approach, which enables us to draw accurate conclusions about the entire population using only a sample of the data. By estimating the parameters of the population with a certain degree of confidence or probability, we can reduce the computational overhead significantly. However, it is crucial to carefully consider the assumptions and limitations of the statistical models and methods employed to ensure reliable and precise results.

### What Sampling Technique Did We Use?

Given the wide range of products and reviews covered in the dataset, there is an inherent imbalance between attributes. To address this issue, we utilised stratified random sampling to extract a sample of 100,000 records from the population while ensuring that the ratio of products in the dataset is maintained. **(sample.py, 1-52)** Stratified random sampling involves dividing the population into subgroups or strata based on specific characteristics and then selecting a random sample from each stratum in proportion to its size or importance within the population. The resulting samples from each stratum are then combined to form the overall sample, resulting in a more representative and accurate sample for analysis.

The advantage of stratified random sampling over random sampling is that it ensures that each stratum is well-represented in the sample, which can improve the accuracy and precision of the estimates. This is particularly important when there are significant differences or variations within the population, as it allows for more accurate estimates of the characteristics of each subgroup.

## Questions Explored:

* Is there evidence to suggest that the product reviews rated as 5.0 are genuine customer feedback or are they possibly fake reviews generated by automated bots?
* Is there a correlation between the length of reviews and the ratings they receive?
* Is there a significant difference in the mean rating received between verified and non-verified reviewers?
* Can we observe any correlation between the number of reviews a reviewer has submitted and the ratings they receive?
* Which topics are most commonly referenced in the customer reviews?

## Usage:

* ``Amazon Review Data (2018) Analysis.ipynb`` — Contains the complete Exploratory Data Analysis (EDA) conducted on the Amazon Review Data (2018) dataset.
* ``src\data.py`` — Source code for storing the dataset from the JavaScript Object Notation (JSON) file into a MongoDB database as a collection.
* ``src\sample.py`` — Source code for extracting a stratified random sample of a specified sample size from the dataset stored in the MongoDB database as a collection and storing it as a comma-separated values (CSV) file.

## Contributors:

This project exists thanks to the extraordinary people who contributed to it.
* **[Wajeeh Ul Hassan](https://github.com/wajeehulhassanr) (i212684@nu.edu.pk)**
* **[Mohammad Abubakar Siddiq](https://github.com/bakar0208) (i212742@nu.edu.pk)**

---

### References:

Ni, J., Li, J. and McAuley, J. (2019) ‘Justifying Recommendations using Distantly-Labeled Reviews and Fine-Grained Aspects’, *Empirical Methods in Natural Language Processing (EMNLP)* [Preprint]. Available at: https://cseweb.ucsd.edu//~jmcauley/pdfs/emnlp19a.pdf (Accessed: 25 June 2023).
