# SCRAPING-REAL-ESTATE-PROPERTIES-AND-CREATING-VISUALIZATIONS

## Scraping websites using BeautifulSoup.
### Libaries You need to install
1. **BeautifulSoup:** Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
To install Beautiful Soup, Input
> ``` pip install beautifulsoup4 ```

into your command prompt. Click https://pypi.org/project/beautifulsoup4/ To read the documnentaion.

2. **Request:** The requests library is the de facto standard for making HTTP requests in Python. 
>``` pip install requests```

3. **Pandas:** Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
> ```pip install pandas```

4. **Seaborn:** Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
> ```pip install seaborn```

5. **Matplotlib:** Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python
> ```python -m pip install -U matplotlib```


## Data Scraping
The data was scraped from https://privateproperty.com.ng/property-for-rent/ using **_Beautiful Soup_** and **_Requests_**. 
Features scraped from the websites are: 
1. Page number
2. Description of the property
3. Title of the property
4. Number of Bedrooms
5. Number of Bathrooms
6. Location of property
7. City where property is located and
8. Price of the property

## Data Cleaning and Visualization
### Data Cleaning Process
* Performed cleaning on the ***city*** column 
* transformed ***price*** column from ***str*** type to ***int***. 
* Created another feature named *Type* (this describes the kind of property)
* Replaced missing values in bedrooms and bathrooms column with zeros

### Insights from Visualization
* Lagos Island and enivronment(Lekki, Ikoyi and VIctoria Island) has more properties availabe for rent.
* Portharcourt city has the highest avergae rent. This is due to fact that PortHarcout has only one listing and its a hotel. After which Ketu, Ajah and Mushin.
* Hotel is having the highest average price for rent 
* From the **_Price vs Number of bedrooms_** plot, it shows properties that have 7 bedrooms has the highest average price followed by 6,5,1,4,3 and 2 bedrooms.
