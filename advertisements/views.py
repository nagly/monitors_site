from django.shortcuts import render
from advertisements.models import Ad
# Create your views here.
def advertise(request):
	left_ads = Ad.objects.filter(place='1')
	slots = [i for i in range(30,40,2)]
	for i in range(len(slots)):
		for j in range(len(left_ads)):
			if left_ads[j].price == slots[i]:
				slots[i] = left_ads[j]
	if isinstance(slots[len(slots)-1], int) == False:
		slots.append(int(slots[len(slots)-1].price + 2))
	slots = slots[::-1]
	context = {'slots':slots}
	template = "advertise.html"
	return render(request, template, context)