from django.shortcuts import render
import operator

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    full_text = request.GET['fulltext']
    textlist = full_text.split('\n')
    textlist2 = full_text.split()
    worddic = {}
    for word in textlist2:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    sorted_word_dictionary = sorted(worddic.items(), key=operator.itemgetter(1,0), reverse=True)
         
    return render(request, 'about.html', {'enterlist':textlist, 'worddic':sorted_word_dictionary})

def intro(request):
    return render(request, 'intro.html')