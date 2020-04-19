from django.http import HttpResponse
from django.shortcuts import render #this defines the render function
import operator

def home(request):
    return render(request, 'home.html', {'dictionary':'a dictionary call example'})
def count(request):
    fulltext = request.GET['fulltext']
    #split the data into a list
    wordlist = fulltext.split()
    worddictionary = {}
    #for loop to count words typed
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to worddictionary
            worddictionary[word] = 1
#sort items listed
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    #to check the parameter full text but also show the fulltext data on the html. count:len (length). Passing data to count.html
    return render(request, "count.html", {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})
