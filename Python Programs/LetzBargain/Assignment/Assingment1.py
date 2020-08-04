'''
Problem:
What I want you to do is this:
Given a website link, remove all
the stop words and have a basic HTML created, which shows the tag cloud


'''
from bs4 import BeautifulSoup
import requests

from nltk import download
from nltk.tokenize import word_tokenize
# download('punkt')
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

url = input('Enter the link : ')

# Request To the url
res = requests.get(url)

# Converting the Response object to Beautifulsoup object
soup = BeautifulSoup(res.text, 'lxml')

# To split the words in the string
try:
    tokenised = word_tokenize(soup.get_text().replace('\n\n\n', '').lower())
except:
    from nltk import download

    download('punkt')
    tokenised = word_tokenize(soup.get_text().replace('\n\n\n', '').lower())

# adding custom stop charecters to existing stop words
extend = ['.', ',', '–', '*', '#', '%', '!', ':', "''", '""', '(', ')', '[', ']', '{', '}', "'s"]
sw = list(STOPWORDS) + extend

# Removing the stop words from the list of words
sw_removed = [word for word in tokenised if word.lower() not in sw]

# Join the list of words without the stop words
generate = ''
generate += ' '.join(tokenised) + ' '

# Create a wordcloud
cloud = WordCloud(width=600, height=600,
                  background_color='white',
                  stopwords=sw,
                  min_font_size=10, max_font_size=200).generate(generate)

# To view the word cloud

# Resizing the plot
plt.figure(figsize=(6, 6), facecolor=None)

# Adding the cloud to the plot
plt.imshow(cloud)

# To not to display the axis for the image
plt.axis("off")

# Remove the padding
plt.tight_layout(pad=0)

# Save the image
plt.savefig('cloud.png')

# Display the image
plt.show()

'''
good afternoon 
im bharathn
pursuiung my eng in electronics and comm eng from nmit

ive been trying  to improve my skill set in this peroid of lockdown

ive been working with python and built pretty basic projects in it

im passionate about learn new tech which leads me to take iot course my college

as i learnt that he company is deaeling with ai
 
i hope i would learn new things and add more value to the company

i always wanted to work for ai

Thank you for providing the oppurtunity to learn and work for the company
I hope i would ennce my problem solving skills here



any questions
yes what is my opuurtuntity to grow in this field
'''
