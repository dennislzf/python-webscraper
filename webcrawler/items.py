# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ElectronicsItem(Item):
    name = Field()
    price = Field()
    description = Field()
    rating = Field()
    link = Field()
    shipping= Field()
    savings= Field()
    photourl = Field()
    priceprevious = Field()
    typeitem= Field()

class ClothingItem(Item):
	name = Field()
	price= Field()
	link = Field()
	shipping = Field()
	savings = Field()
	photourl = Field()
	priceprevious = Field()
	typeitem= Field()
	genderitem = Field()

