import datetime, os
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from advertisements.models import Ad, Buffer
from advertisements.forms import AdForm

# Create your views here.


def advertise(request):
	now = timezone.now()
	minimum = 20
	maximum = 40
	interval = 4
	maximum_left = maximum
	maximum_right = maximum

	price_list_left = list(Ad.objects.filter(place='1').order_by('price').values_list('price', flat=True))
	price_list_right = list(Ad.objects.filter(place='2').order_by('price').values_list('price', flat=True))

	try:
		if maximum_left < max(price_list_left):
			maximum_left = max(price_list_left)
	except ValueError: #if price_list_left is an empty list
		pass
	try:
		if maximum_right < max(price_list_right):
			maximum_right = max(price_list_right)
	except ValueError:
		pass

	slots_left = [i for i in range(minimum,int(maximum_left)+1,interval)]
	slots_right = [i for i in range(minimum,int(maximum_right)+1,interval)]
	# prepare all left slots
	all_slots = slots_left + price_list_left
	all_slots = set(all_slots)
	all_slots = list(all_slots)
	all_slots.sort()
	for index, item in enumerate(all_slots):
		try:
			obj = Ad.objects.get(price=item)
		except:
			obj = item
		all_slots[index] = obj
	slots_left = all_slots
	if isinstance(slots_left[len(slots_left)-1], int) == False:
		slots_left.append(int(slots_left[len(slots_left)-1].price + interval))
	slots_left = slots_left[::-1]
	# prepare all right slots
	all_slots = slots_right + price_list_right
	all_slots = set(all_slots)
	all_slots = list(all_slots)
	all_slots.sort()
	for index, item in enumerate(all_slots):
		try:
			obj = Ad.objects.get(price=item)
		except:
			obj = item
		all_slots[index] = obj
	slots_right = all_slots
	if isinstance(slots_right[len(slots_right)-1], int) == False:
		slots_right.append(int(slots_right[len(slots_right)-1].price + interval))
	slots_right = slots_right[::-1]

	top_small_banners = len(list(Ad.objects.filter(place='3')))
	try:
		top_small_fastest_av = Ad.objects.filter(place='3').order_by('expiration')[0]
	except:
		top_small_fastest_av = None
	bottom_big_banners = len(list(Ad.objects.filter(place='4')))
	try:
		bottom_big_fastest_av = Ad.objects.filter(place='4').order_by('expiration')[0]
	except:
		bottom_big_fastest_av = None
	bottom_small_banners = len(list(Ad.objects.filter(place='5')))
	try:
		bottom_small_fastest_av = Ad.objects.filter(place='3').order_by('expiration')[0]
	except:
		bottom_small_fastest_av = None
	max_rotation = 2
	top_s_price = 25
	bottom_s_price = 20
	bottom_b_price = 30

	context = {'slots_left':slots_left,'slots_right':slots_right,
				'top_small_banners_av':max_rotation-top_small_banners,
				'bottom_small_banners_av':max_rotation-bottom_small_banners,
				'bottom_big_banners_av':max_rotation-bottom_big_banners,
				'max_rotation':max_rotation,
				'top_s_price':top_s_price,
				'bottom_b_price':bottom_b_price,
				'bottom_s_price':bottom_s_price,
				'top_small_fastest_av':top_small_fastest_av,
				'bottom_big_fastest_av':bottom_big_fastest_av,
				'bottom_small_fastest_av':bottom_small_fastest_av}

	template = "advertise.html"
	return render(request, template, context)

def buy_ad(request):
	place = request.POST.get('place', False)
	price = float(request.POST.get('price', False))
	if request.method == "POST":
		form = AdForm(request.POST, request.FILES)
		if form.is_valid():
			new_ad = form.save(commit=False)
			new_ad.place = request.POST.get('place', False)
			new_ad.price = float(request.POST.get('price', False))
			new_ad.expiration = timezone.now() + datetime.timedelta(days=new_ad.weeks*7)
			new_ad.save()
			return HttpResponseRedirect('/advertise/%s/' %new_ad.unique_id)
	else:
		form = AdForm()
	context={'place':place, 'price':price, 'form':form}
	template = "buy_ad.html"
	return render(request, template, context)

def preview(request, id):
	ad = Buffer.objects.get(unique_id=id)
	context = {'ad': ad}
	template = 'ad_preview.html'
	return render(request, template, context)

def delete_ad(request, ad_id):
	to_delete = Buffer.objects.get(id = ad_id)
	try:
		os.remove('static/media/' + '%s' %to_delete.image)
	except:
		pass
	to_delete.delete()
	return HttpResponseRedirect('/')