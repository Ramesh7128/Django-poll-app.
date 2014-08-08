# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from polls.models import Poll

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('index.html')
	c = Context({
		'latest_poll_list': latest_poll_list,
	})		
	#output = ','.join([p.questions for p in latest_poll_list])
	return HttpResponse(t.render(c))
	

def detail(request, poll_id):
	return HttpResponse("this is the poll %s" % poll_id)

def results(request, poll_id):
	return HttpResponse("this is the result for the poll %s" % poll_id)


def vote(request, poll_id):
	return HttpResponse("this is the voting on the poll %s" % poll_id)
