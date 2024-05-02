
# i have used views
from django.shortcuts import render
from django.http import HttpResponse

def index( request):
    return render(request,'index_update.html')



def  analyze(request):
    djtext = request.POST.get('text', 'default') # instead of GET use POST
    removepunctuation = request.POST.get('removepunctuation', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    charcount = request.POST.get('charcount' , 'off')
    removenewline = request.POST.get('removenewline' ,'off')

    orginal = djtext
    set_ = {}
    if( len(orginal) == 0 or orginal == '  ' or  orginal == ""):
        return render(request, "wordnotenter.html")


    if( removepunctuation == 'on'):
       punctuators = [
              '(', ')', '[', ']', '{', '}', ',', ':', '.', ';', '@', '=', '->', '+=', '-=',
              '*=', '/=', '//=', '%=', '**=', '&=', '|=', '^=', '>>=', '<<=', '==', '!=', '<', '>',
              '<=', '>=', '+', '-', '*', '/', '//', '%', '**', '&', '|', '^', '~', '<<', '>>' ,'#' , '"'  , "'"
       ]

       analyzedtext = ''
       for i in djtext:
              if(i in punctuators):
                pass
              else:
                analyzedtext= analyzedtext+i
       djtext = analyzedtext
       set_ = {'purpose': 'remove punctuations', 'Analyzed_text': analyzedtext}





    if( fullcaps =='on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        set_ = {'purpose': 'full caps', 'Analyzed_text': analyzed}
        djtext = analyzed


    if(charcount == 'on'):
        i = 0
        for char in djtext:
            i = i + 1
        set_ = {'purpose': 'Char Count', 'Analyzed_text': i}

    if( removenewline  == 'on'):
        analyzed = ''
        for i in djtext:
            if( i != '\n' and i != '\r'):
               analyzed = analyzed + i
            else:
                analyzed = analyzed + " "
        djtext = analyzed
        set_ = {'purpose': 'Remove NewLine', 'Analyzed_text': djtext}

    if( (charcount == 'off') and  (removepunctuation == 'off') and (fullcaps == 'off') and removenewline == 'off'):
        # return HttpResponse("<h1> please click on checkbutton before going onwards  <a href = '/'> back</a></h1>")
        return render(request , "uncertain.html")
    else:
        return render(request  , "analyzed_update.html" ,set_)

