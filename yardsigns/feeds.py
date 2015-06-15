from django.contrib.syndication.feeds import Feed
from models import Sign


class LatestEntries(Feed):	
	title = "My Yard Our Message latest signs"
	link = "/signs/"
	description = "The latest signs submitted to the My Yard Our Message project."


	def items(self):
		return Sign.objects.order_by('-time_added')[:10]