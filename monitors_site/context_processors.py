def current_url(request):
	return {'current_url': request.get_full_path()}

def random_ad(request):
	from advertisements.models import Ad
	from django.utils import timezone
	now = timezone.now()
	try:
		random_ad_3 = Ad.objects.filter(place='3', expiration__gt=now).order_by('?')[0]
	except:
		random_ad_3 = None
	try:
		random_ad_4 = Ad.objects.filter(place='4', expiration__gt=now).order_by('?')[0]
	except:
		random_ad_4 = None
	try:
		random_ad_5 = Ad.objects.filter(place='5', expiration__gt=now).order_by('?')[0]
	except:
		random_ad_5 = None
	
	return {'random_ad_3': random_ad_3, 'random_ad_4': random_ad_4, 'random_ad_5': random_ad_5}

def side_ads(request):
	from advertisements.models import Ad
	from django.utils import timezone
	now = timezone.now()
	try:
		left_ads = Ad.objects.filter(place='1', expiration__gt=now).order_by('-price')
	except:
		left_ads = None
	try:
		right_ads = Ad.objects.filter(place='2', expiration__gt=now).order_by('-price')
	except:
		right_ads = None

	return {'right_ads' : right_ads, 'left_ads' : left_ads}