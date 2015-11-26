from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q
from monitors.models import Monitor
from hyips_info.models import Hyips_info
from hyips.models import Hyip
def home(request):
	context = {}
	template = 'home.html'
	# if request.method == 'POST':
	# 	req = request.POST
	# 	program_url = req.get('program_url', False)
	# 	hyip = Hyip.objects.filter(url__icontains='%s' %program_url)
	# 	context = {'hyip': hyip}
	return render(request, template, context)

def show_hyip(request, hyip_id):
	hyip = Hyip.objects.get(id=hyip_id)
	monitors = Monitor.objects.all()
	monitors_for_hyip = Hyips_info.objects.filter(hyip_id=hyip_id) #liczba stron monitorujacych konkretnego hyipa
	if monitors_for_hyip.count() > 0:
		for monitor in monitors:
			lid = Hyips_info.objects.get(hyip_id=hyip_id, monitor_id=monitor.id)
			monitor.url_hyip_details = monitor.url_hyip_details.replace('{{listing_id}}', '%s' %lid.listing_id)
			monitor.url_card = monitor.url_card.replace('{{listing_id}}', '%s' %lid.listing_id)
	context = {'monitors':monitors, 'hyip':hyip, 'monitors_for_hyip':monitors_for_hyip.count()}
	template = 'hyip_page.html'
	return render(request, template, context)

def search(request):
	if request.method == 'POST':
		keyword = request.POST.get('program_url', False).split()
		if len(keyword) != 0:
			hyip = Hyip.objects.filter(reduce(lambda x, y: x | y, [Q(url__contains=word) for word in keyword]))
			if hyip.count() == 1:
				return HttpResponseRedirect('/details/%s/' %hyip[0].id)
			else:
				return HttpResponseRedirect('/search_results/?q=%s' %'+'.join(keyword))
		else:
			return HttpResponseRedirect('/search_results/?q=')
	else:
		return HttpResponseRedirect('/')

def search_results(request):
	context = {}
	template = 'search_results.html'
	if request.method == 'GET':
		keyword = request.GET.get('q').split()
		if len(keyword) != 0:
			hyips = Hyip.objects.filter(reduce(lambda x, y: x | y, [Q(url__contains=word) for word in keyword]))
		else:
			hyips = None
		context = {'hyips':hyips}
	return render(request, template, context)
