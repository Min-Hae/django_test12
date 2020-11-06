from django.shortcuts import render, get_object_or_404
from myvote.models import Question, Choice
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def DispFunc(request):
    q_list = Question.objects.all().order_by('pub_date', 'id')
    context = {'q_list':q_list}
    return render(request, 'display.html', context)

def DetailFunc(request, question_id): # /gogo/1  <== question_id
   # return HttpResponse("question_id %s"%question_id) 결과 : question_id 1 또는 2
    '''
    try:
       question = Question.objects.get(pk = question_id)
       
    except Question.DoesNotExist:
       raise Http404("질문이 없어요")    
    '''
    
    question = get_object_or_404(Question, pk = question_id) # 위 주석과 같은 의미
    print(question.question_text)
    print(question.pub_date)
    print(question)
    
    return render(request, 'detail.html', {'question':question})

def VoteFunc(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        sel_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question':question, 'error_msg':'1개의 항목을 반드시 선택하시오'})    
    
    sel_choice.votes += 1 # 선택된 항목에 득표 누적
    sel_choice.save() # Choice 테이블의 votes 항목 수정 
    print(reverse('results', args = (question.id,))) # url 패턴으로부터 url 스트링 얻기
  #  return HttpResponse("voting on question_id %s"%question_id)
  #  return render(request, 'result.html')
    return HttpResponseRedirect(reverse('results', args = (question.id,)))

def ResultsFunc(request, question_id):
    print("result of question_id %s"%question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'result.html', {'question':question})
