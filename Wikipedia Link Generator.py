import wikipedia
import nltk
import string
import re
import warnings
from bs4 import BeautifulSoup 
from nltk.corpus import wordnet #  not all are used, but here just in case

def maincode():
    
    question = input("Do you know what article you want to test this with? ")
    if str(question) in ('Y', 'y', 'Yes', 'yes'):
        name = input("Which one is it? ")
        article = wikipedia.page(title=name, auto_suggest=False) #prevent suggesting incorrectly
            # print(article) WORKS
            # an issue arises when the subject matter is too vague
            # perhaps implement warning system
            # requires usage of Beautifulsoup, look into it when time is freed up
    else:
        while True:
            a = (input("Looking for: "))
            x = wikipedia.suggest(a)
            if str(x) == 'None':
                print("ERROR. PLEASE TRY AGAIN.")
                continue
            b = (input("Did you mean " + "'" + str(x) + "'" + " ? " )) 
            if b in ('Y', 'y', 'Yes', 'yes'):
                article = wikipedia.page(title=str(x), auto_suggest=False) #prevent suggesting incorrectly
                #print(article) WORKS
                break
            elif b in ('N', 'n', 'no', 'No'):
                continue
            else:
                break

    content = article.content
    reworked_article = content.translate(str.maketrans('', '', string.punctuation)) #remove punctioatitonoanfgvbhdgxfgn
    sample = reworked_article.lower() # lowercase
    resampled = nltk.word_tokenize(sample)
    tagged = nltk.pos_tag(resampled) # tags them with what kinda words they are, nouns, pronouns, etc.
    # print(text)

    tag_clean = [x for (x,y) in tagged if y in ('NN', 'NNS', 'NNP', 'NNPS', 'JJ')] #removing everything but certain types of words

    d = {} #dictionary generation

    for word in tag_clean:
        d[word] = d.get(word, 0) + 1 #counting

    # print(d)

    word_freq= []
    for key, value in d.items():
        word_freq.append((value, key))
    word_freq.sort(reverse=True) # Highest to lowest

    #print(word_freq)

    names_alone = [y for (x,y) in word_freq if y != int] #removing the weighting numbers to leave just the text
    names_alone = [i for i in names_alone if len(i) > 1]

    top_5 = (names_alone[0:5]) #top 5
    top_10 = (names_alone[0:10]) #top 10

    array_synonyms_5=[] #empty arrays for the two of them
    array_synonyms_10=[]
    
##    array_antonyms_5=[] #most likely wont use it
##    array_antonyms_10=[]

    for i in range(len(top_5)):
        for vsyn in wordnet.synsets(top_5[i]):
        #print(vsyn) 
            for l in vsyn.lemmas():
            #print(l.name())
                array_synonyms_5.append(l.name())
            #if l.antonyms():
                #array_antonyms.append(l.antonyms()[0].name())
        
    #print(set(array_synonyms_5))
        #print(set(array_antonyms))                    

    for i in range(len(top_10)): 
        for vsyn in wordnet.synsets(top_10[i]):
        #print(vsyn) 
            for l in vsyn.lemmas():
            #print(l.name())
                array_synonyms_10.append(l.name())
            #if l.antonyms():
                #array_antonyms.append(l.antonyms()[0].name())

    # print(set(array_synonyms_10))

    d5 = {} #for the shortened list of 5

    for word in array_synonyms_5:
        d5[word] = d5.get(word, 0) + 1 #counting

    # print(d)

    word_freq_5= []
    for key, value in d5.items():
        word_freq_5.append((value, key))
    word_freq_5.sort(reverse=True) # Highest to lowest

    # print(word_freq_5)

    names_alone_5 = [y for (x,y) in word_freq_5 if y != int]
    cleaned_5 = names_alone_5[0:5] #after the synonyms

    d10 = {} #for the shortened list of 10

    for word in array_synonyms_10:
        d10[word] = d10.get(word, 0) + 1 #counting

    # print(d)

    word_freq_10= []
    for key, value in d10.items():
        word_freq_10.append((value, key))
    word_freq_10.sort(reverse=True) # Highest to lowest

    # print(word_freq_10)

    names_alone_10 = [y for (x,y) in word_freq_10 if y != int]
    cleaned_10 = names_alone_10[0:10] #after the synonyms

    searching_5 = []

    for i in range(len(cleaned_5)):
        searched_5 = (wikipedia.search(cleaned_5[i])) #using wikipedia to sort through other possible correlations
        for l in searched_5:
            searching_5.append(searched_5)
                
    ds5 = {}

    for word in searched_5:
        ds5[word] = ds5.get(word, 0) + 1
        
    word_freq_s5= []
    for key, value in ds5.items():
        word_freq_s5.append((value, key))
    word_freq_s5.sort(reverse=True) # Highest to lowest

    # print(word_freq_5)

    names_alone_s5 = [y for (x,y) in word_freq_s5 if y != int]
    top_s5 = names_alone_s5[0:5] #after the synonyms

    #print(cleaned_s5)

    searching_10 = []

    for i in range(len(cleaned_10)):
        searched_10 = (wikipedia.search(cleaned_10[i])) #using wikipedia to sort through other possible correlations
        for l in searched_10:
            searching_10.append(searched_10)
                
    ds10 = {}

    for word in searched_5:
        ds10[word] = ds10.get(word, 0) + 1
        
    word_freq_s10= []
    for key, value in ds10.items():
        word_freq_s10.append((value, key))
    word_freq_s10.sort(reverse=True) # Highest to lowest

    # print(word_freq_10)

    names_alone_s10 = [y for (x,y) in word_freq_s10 if y != int]
    top_s10 = names_alone_s10[0:10] #after the synonyms

    # print(cleaned_s10)
    # all the s functions using the wikipedia page come up with either very accurate or very inaccurate articles to also look at
    # better off using the synonym method.
    # could make better use of it if more information was funneled in

    wikilink = 'https://en.wikipedia.org/wiki/' #the string to produce wiki links
    
    while True:
        select=input("Would you like to generate wikipedia URLs from the top 5 or the top 10 results? ")
        if select in ('5', 'top 5', 'Top 5', 'five', 'top five'):
            ask=input("Would you like to generate them from synonyms or using Wikipedia itself? [HIGHLY EXPERIMENTAL]: ")
            if ask in ("wiki", "wikipedia"):
                alsosee = [wikilink + x for x in top_s5]
                alsosee = [x.replace(" ", "_") for x in alsosee]
                print('See Also:', *alsosee, sep='\n- ')
                break
            elif ask in ("syno", "syn", "synonyms"):
                alsosee = [wikilink + x for x in top_5]
                alsosee = [x.replace(" ", "_") for x in alsosee]
                print('See Also:', *alsosee, sep='\n- ')
                break
            else:
                continue

        elif select in ('10', 'top 10', 'Top 10', 'ten', 'top 10'):
            ask=input("Would you like to generate them from synonyms or using Wikipedia itself? [HIGHLY EXPERIMENTAL]: ")
            if ask in ("wiki", "wikipedia"):
                alsosee = [wikilink + x for x in top_s10]
                alsosee = [x.replace(" ", "_") for x in alsosee]
                print('See Also:', *alsosee, sep='\n- ')
                break
            elif ask in ("syno", "syn", "synonyms"):
                alsosee = [wikilink + x for x in top_10]
                alsosee = [x.replace(" ", "_") for x in alsosee]
                print('See Also:', *alsosee, sep='\n- ')
                break
            else:
                continue

    restart=(input("Do you want to generate another list of possible 'see mores'? ").lower()) #answer will always be lower case.
    if restart in ('yes', 'y'):
        maincode()
             
    else:
        exit()

maincode() #loops until restarts arent wanted
# locks the functions to the maincode though so
# attempts to run single variables out of the loop return an error
# downside to looping


            

