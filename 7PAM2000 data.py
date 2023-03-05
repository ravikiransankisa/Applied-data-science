#!/usr/bin/env python
# coding: utf-8

# In[25]:


# import pandas as name of pd
import pandas as pd
# read data from CSV file
data = pd.read_csv("API_19_DS2_en_csv_v2_4773766.csv",skiprows=3)
data


# In[26]:


# Drop the unused columns from the data set
data = data.drop(columns = ["1960","1961","1962","1963","1964","1966","1967","1968",'1969','1971',"1972","1973","1974",
                            "1976","1977","1978","1979","1981","1982","1983","1984","1986","1987","1988","1989","1991",
                            "1992","1993",'1994',"1996","1997","1998","1999","2001","2002","2003","2004","2007","2008",
                            "2009","2011","2012","2013","2014","2016","2017","2018","2019","2021",'Unnamed: 66'])


# In[27]:


data.info() # Grtting the information of the dataset


# In[28]:


data.isnull().sum() #finding the null values in the dataset


# In[29]:


# Replace tyhe null value with the Zero and print the data set
data = data.fillna(0)
data


# In[30]:


# calling the metplotlib for the ploting the data
import matplotlib.pyplot as plt


# In[31]:


# creating the funtion lineplot() to ploting
def lineplot(N):
    '''
    CO2 emissions from gaseous fuel consumption contribute to climate change by increasing the concentration of greenhouse
    gases in the atmosphere. When fossil fuels such as natural gas are burned for energy, they release carbon dioxide into
    the atmosphere. This CO2 traps heat from the sun and causes the Earth's temperature to rise, leading to global warming.
    :return: Line plot - to visualization the efferent country use in different year
    '''
    N = N.drop(["Country Code","Indicator Code"],axis =1) #drop the un-used column form the dataset
    N.set_index("Indicator Name",inplace = True) # set-up the index for the "Indicator Name"
    N = N.loc["CO2 emissions from gaseous fuel consumption (% of total)"] # Lock the column of "CO2 emissions from gaseous
#     fuel consumption (% of total)"
    N = N.reset_index(level = "Indicator Name")
    N.groupby(["Country Name"]).sum() #group the data on the base of country Name
    # taking the head 10 simple data
    N = N.head(10)
    # ploting the data in the line plot
    N.plot(x= "Country Name",y = ['1965', '1970', '1975', '1980', '1985', '1990','1995','2000','2005',],figsize = (15,5))
    plt.title("CO2 emissions from gaseous fuel consumption (% of total)")
    plt.show()


# In[32]:


# defind the data in new variable and calling the function
data1= data
lineplot(data1)


# In[33]:


# creating the funtion kdeplot() to ploting
def kdeplot(k):
    '''
    On the positive side, agricultural lands can act as carbon sinks, which means they can absorb and store carbon from 
    the atmosphere through plant growth and soil organic matter. This can help to mitigate climate change by removing
    carbon dioxide from the atmosphere and reducing its concentration
    :return: Kernel Distribution Estimation Plot-  to visualization the density of the Agriculture land in different year
    '''
    k = k.drop(["Country Code","Indicator Code"],axis =1) #drop the un-used column form the dataset
    k.set_index("Indicator Name",inplace = True) # set-up the index for the "Indicator Name"
    k = k.loc["Agricultural land (% of land area)"] # Lock the column of "Agricultural land (% of land area)"
    k = k.reset_index(level = "Indicator Name")
    k.groupby(["Country Name"]).sum() #group the data on the base of country Name
    # taking the head 10 simple data
    k = k.head(15)
    print(k)
    # ploting the data in the kde plot of different year
    k.plot.kde(y = ['1965', '1970', '1975', '1980', '1985', '1990','1995','2000','2005'],figsize = (15,5))
    plt.title("Agricultural land (% of land area)")
    plt.show()


# In[34]:


# defind the data in new variable and calling the function
data2=data
kdeplot(data2)


# In[35]:


# creating the funtion boxplot() to ploting
def boxpot(S):
    '''
    As the population grows, so does the demand for food, energy, and resources such as water and land. This can lead to
    increased greenhouse gas emissions, as more fossil fuels are burned to meet the energy demands of the growing 
    population. Additionally, deforestation and land-use changes to accommodate the growing population can also result 
    in increased greenhouse gas emissions.
    :return: Box plot - to visualization the efferent year population that effect the green house effect
    '''
    S = S.drop(["Country Code","Indicator Code"],axis =1) #drop the un-used column form the dataset
    S.set_index("Indicator Name",inplace = True) # set-up the index for the "Indicator Name"
    S = S.loc["Population growth (annual %)"] # Lock the column of "Population growth (annual %)"
    S = S.reset_index(level = "Indicator Name")
    S.groupby(["Country Name"]).sum() #group the data on the base of country Name
    # taking the head 15 simple data
    S = S.head(15)
    print(S)
    # ploting the data in the Box plot
    S.plot.box(y = ['1965', '1970', '1975', '1980', '1985', '1990','1995','2000','2005'],figsize = (15,5))
    plt.title("Population growth (annual %)")
    plt.xlabel("Year")
    plt.ylabel("growth index")
    plt.show()


# In[36]:


# defind the data in new variable and calling the function
data3= data
boxpot(data3)


# In[36]:





# In[36]:




