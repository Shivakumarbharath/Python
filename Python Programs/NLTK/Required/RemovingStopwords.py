from nltk.corpus import stopwords
from nltk import download
#download once
#download('stopwords')
from nltk.tokenize import word_tokenize
download('punkt')

print(stopwords.words('english'))

text='Hi I an bharath from India to the why what . , ;;'
token=word_tokenize(text)
print(token)

removed=[word for word in token if word.lower() not in stopwords.words()]
print(removed)