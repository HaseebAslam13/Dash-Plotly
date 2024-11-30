#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from transformers import pipeline
import math

# Load a pre-trained sentence transformer model
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')


# Sample data


df['predicted_category'] = None
candidate_labels = ['Indian food', 'Chinese food', 'Mediterranean food', 'Mexican food', 'American food', 'Japanese food', 'Italian food', 'Middle Eastern Food', 'Thai food', 'African food']
for index, i in enumerate(df['meal_description']): 
    if i is None or (isinstance(i, float) and math.isnan(i)):
        continue
    result = classifier(i, candidate_labels)
    print(result)
    maximum = 0
    max_score = 0
    max_category = None
    for label, score in zip(result['labels'], result['scores']):
        if score > max_score:
            max_score = score
            max_category = label

    # Save the max_category into the DataFrame
    df.at[index, 'predicted_category'] = max_category

        
        
        
    
    





# In[ ]:


import pandas as pd
from transformers import pipeline
import math

# Load a pre-trained sentence transformer model
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')


# Sample data

df['predicted_category_2'] = None
candidate_labels = ['Unhealthy food', 'Healthy Food']
for index, i in enumerate(df['meal_description']): 
    if i is None or (isinstance(i, float) and math.isnan(i)):
        continue
    result = classifier(i, candidate_labels)
    print(result)
    count = 0
    maximum = 0
    max_score = 0
    max_category = None
    for label, score in zip(result['labels'], result['scores']):
        if score > max_score:
            max_score = score
            max_category = label

    # Save the max_category into the DataFrame
    df.at[index, 'predicted_category_2'] = max_category


# In[ ]:


import pandas as pd
from transformers import pipeline
import math

# Load a pre-trained sentence transformer model


# Sample data

df['predicted_category_3'] = None
candidate_labels = ['Organic food', 'Inorganic food']
for index, i in enumerate(df['meal_description']): 
    if i is None or (isinstance(i, float) and math.isnan(i)):
        continue
    result = classifier(i, candidate_labels)
    print(result)
    count = 0
    maximum = 0
    max_score = 0
    max_category = None
    for label, score in zip(result['labels'], result['scores']):
        if score > max_score:
            max_score = score
            max_category = label

    # Save the max_category into the DataFrame
    df.at[index, 'predicted_category_3'] = max_category


# In[ ]:


import pandas as pd
from transformers import pipeline
import math

# Load a pre-trained sentence transformer model
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')


# Sample data

df['predicted_category_4'] = None
candidate_labels = ['Sweet food', 'Salty food','Sour food', 'Spicy food','Bitter food', 'Umami food']
for index, i in enumerate(df['meal_description']): 
    if i is None or (isinstance(i, float) and math.isnan(i)):
        continue
    result = classifier(i, candidate_labels)
    print(result)
    count = 0
    maximum = 0
    max_score = 0
    max_category = None
    for label, score in zip(result['labels'], result['scores']):
        if score > max_score:
            max_score = score
            max_category = label

    # Save the max_category into the DataFrame
    df.at[index, 'predicted_category_4'] = max_category
    


# In[ ]:


import pandas as pd
from transformers import pipeline
import math

# Load a pre-trained sentence transformer model
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')


# Sample data

df['predicted_category_5'] = None
candidate_labels = ['High Protein', 'High Carbohydrates', 'High Fats', 'High Vitamins', 'High Minerals', 'High Minerals', 'High Water']
for index, i in enumerate(df['meal_description']): 
    if i is None or (isinstance(i, float) and math.isnan(i)):
        continue
    result = classifier(i, candidate_labels)
    print(result)
    count = 0
    maximum = 0
    max_score = 0
    max_category = None
    for label, score in zip(result['labels'], result['scores']):
        if score > max_score:
            max_score = score
            max_category = label

    # Save the max_category into the DataFrame
    df.at[index, 'predicted_category_5'] = max_category
    


# In[ ]:


import pandas as pd
from transformers import pipeline
import math

# Load a pre-trained sentence transformer model
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')


# Sample data

df['predicted_category_6'] = None
candidate_labels = ['Low Protein', 'Low Carbohydrates', 'Low Fats', 'Low Vitamins', 'Low Minerals', 'Low Minerals', 'Low Water']
for index, i in enumerate(df['meal_description']): 
    if i is None or (isinstance(i, float) and math.isnan(i)):
        continue
    result = classifier(i, candidate_labels)
    print(result)
    count = 0
    maximum = 0
    max_score = 0
    max_category = None
    for label, score in zip(result['labels'], result['scores']):
        if score > max_score:
            max_score = score
            max_category = label

    # Save the max_category into the DataFrame
    df.at[index, 'predicted_category_6'] = max_category
    


# In[ ]:


import pandas as pd
from transformers import pipeline
import math

# Load a pre-trained sentence transformer model
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')


# Sample data

df['predicted_category_7'] = None
candidate_labels = ['Meat', 'Salads', 'Fruits', 'Vegetables', 'Rice', 'Bread', 'Processed', 'Beverages', 'Fast Food']
for index, i in enumerate(df['meal_description']): 
    if i is None or (isinstance(i, float) and math.isnan(i)):
        continue
    result = classifier(i, candidate_labels)
    print(result)
    count = 0
    maximum = 0
    max_score = 0
    max_category = None
    for label, score in zip(result['labels'], result['scores']):
        if score > max_score:
            max_score = score
            max_category = label

    # Save the max_category into the DataFrame
    df.at[index, 'predicted_category_7'] = max_category
    


# In[ ]:


import pandas as pd
from transformers import pipeline
import math

# Load a pre-trained sentence transformer model
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')


# Sample data

df['predicted_category_8'] = None
candidate_labels = ['Baked food', 'Fried food', 'Grilled food', 'Raw food']
for index, i in enumerate(df['meal_description']): 
    if i is None or (isinstance(i, float) and math.isnan(i)):
        continue
    result = classifier(i, candidate_labels)
    print(result)
    count = 0
    maximum = 0
    max_score = 0
    max_category = None
    for label, score in zip(result['labels'], result['scores']):
        if score > max_score:
            max_score = score
            max_category = label

    # Save the max_category into the DataFrame
    df.at[index, 'predicted_category_8'] = max_category
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:





# In[1]:





# In[ ]:





# In[ ]:




