from django.shortcuts import render
from monitors.models import Monitor
from hyips_info.models import Hyips_info
from hyips.models import Hyip
def home(request):
	context = {}
	template = 'home.html'
	return render(request, template, context)

def show_hyip(request, hyip_id):
	hyip = Hyip.objects.get(id=hyip_id)
	monitors = Monitor.objects.all()
	for monitor in monitors:
		lid = Hyips_info.objects.get(hyip_id=hyip_id, monitor_id=monitor.id)
		monitor.url_hyip_details = monitor.url_hyip_details.replace('{{listing_id}}', '%s' %lid.listing_id)
		monitor.url_card = monitor.url_card.replace('{{listing_id}}', '%s' %lid.listing_id)
	context = {'monitors':monitors, 'hyip':hyip}
	template = 'hyip_page.html'
	return render(request, template, context)