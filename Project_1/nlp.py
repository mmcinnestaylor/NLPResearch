"""Currently working on Task 1 for the NLP project."""
import sys
import nltk
#need to make sure we install nltk and nltk data to use these functions:
from nltk.corpus import stopwords               #remove_stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize         #remove_stopwords
from nltk.stem import PorterStemmer, SnowballStemmer    #stem
from nltk.tokenize import sent_tokenize         #stem
from nltk.tokenize import RegexpTokenizer       #remove_punctuation
nltk.download('punkt')

def populateData():
    dataset= []
    with open(sys.argv[1], 'r') as file:
            for line in file:
                if len(line) == 1:      #checks if the line is blank/empty
                    continue            #does not store it if it is empty
                else:
                    dataset.append(line)
    return dataset

def remove_stopwords(tokens):
    return [word for word in tokens if not word in stopwords.words()]

def remove_punctuation(tokens_wo_sw):
    return [word for word in tokens_wo_sw if word.isalnum()]

def stem(user_input):
    output = []
    if user_input == "porter":          #porter stemming
        ps = PorterStemmer()
        for sentence in new_input:
            output.append(" ".join([ps.stem(i) for i in sentence.split()]))
        for item in output:
            print(item, end="\n\n")
    elif user_input == "snowball":      #snowball stemming
        ss = SnowballStemmer("english")
        for sentence in new_input:
            output.append(" ".join([ss.stem(i) for i in sentence.split()]))
        for item in output:
            print(item, end="\n\n")  
    return output


if __name__ == "__main__":
    data = populateData() #list of lists to store data from dataset file
    new_input = []  #list to contain updated parsed sentences
    output = []     #list to contain updated data after stemming

    #removing stopwords and punctuation:
    for _ in range(len(data)):
        tokens = word_tokenize(data[_])    #tokenize the sentence
        """
            tokens without stopwords:
            in the following line I iterate through all the words in the sentence tokens
            list and check if the word exists in the stop words collection or not.
            If it doesnt exist, meaning it is not a stopword, then it is appended to tokens_wo_sw.
            tokens_wo_sw contains a list of the sentence tokenized without stopwords.

            Nic--modified Haley's code to be placed into separate function calls
            ->tokens_wo_punkt = [word for word in tokens_wo_sw if word.isalnum()]
            ->tokens_wo_sw = [word for word in tokens if not word in stopwords.words()]
        """
        tokens_wo_sw = remove_stopwords(tokens)
        #removing puctuation similarly:
        tokens_wo_punkt = remove_punctuation(tokens_wo_sw)
        #Joining the list of tokens without stopwords to create a sentence:
        new_sentence = (" ").join(tokens_wo_punkt)
        #new_input will gain modified dataset with removal of stopwords and punctuation
        new_input.append(new_sentence)
        
        user_input = input("Please choose how you would like to stem the data: Porter or Snowball Stemming\n")
        user_input = user_input.lower()

        #stemming
        output = stem(user_input) 
