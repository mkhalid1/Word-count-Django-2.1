from django.http import HttpResponse
from django.shortcuts import render
import operator

def HomePage(Request):

	return render(Request, 'home.html')

def about(Request):

	return render(Request, 'about.html')

def count(Request):

	text = Request.GET['text']
	word_list = text.split()
	wordsdict = {}

	for word in word_list:

		if word in wordsdict:

			wordsdict[word] +=1

		else:

			wordsdict[word] = 1
	sorted_dict = sorted(wordsdict.items(), key = operator.itemgetter(1), reverse= True)

	words = len(word_list)
	return render(Request, 'count.html', {'text': text, 'words': words, 
										'word_dict': sorted_dict})

