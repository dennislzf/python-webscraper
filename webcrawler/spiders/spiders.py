from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector	
from webcrawler.items import ElectronicsItem,ClothingItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class NeweggWeeklySpider(BaseSpider):
    pipelines= ['multipleelectronics']
    name = "neweggweekly"
    allowed_domains = ["newegg.ca"]
    start_urls = [
       "http://www.newegg.ca/DailyDeal.aspx?Page=1",
       "http://www.newegg.ca/DailyDeal.aspx?Page=2",
       "http://www.newegg.ca/DailyDeal.aspx?Page=3",
       "http://www.newegg.ca/DailyDeal.aspx?Page=4",  
    ]

    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select("//div[@class='itemCell']")
       items = []
       for site in sites:
           item = ElectronicsItem()
           item['name'] =  site.select("div[@class='itemText']/div[@class='wrapper']//span[contains(@id,'title')]/text()").extract()[0].strip()
           pricedollars = site.select("div[@class='itemAction']/ul//li/strong/text()").extract()[0].strip()
           pricecents= site.select("div[@class='itemAction']/ul//li/sup/text()").extract()[0].strip()
           pricedollars = pricedollars.replace(',','')
           pricecents = pricecents.replace('.','')
           price = pricedollars + '.' + pricecents
           item['price'] = price
           item['shipping']= site.select("div[@class='itemAction']/ul/li[@class='price-ship']/text()").extract()[0].strip()
           item['link'] = site.select("div[@class='itemText']/div[@class='wrapper']/a/@href").extract()[0].strip()
           item['description'] = site.select("div[@class='itemText']/ul[@class='itemFeatures']/li/text()").extract()[0].strip()
           item['savings']= ''.join(site.select("div[@class='itemAction']/ul/li[@class='price-save ']/span[@class='price-save-percent']/text()").extract()).strip()
           item['photourl'] = ''.join(site.select("div[@class = 'itemGraphics']/a[@class = 'itemImage']/img/@src").extract()).strip()
           item['priceprevious']= site.select("div[@class='itemAction']/ul/li[@class= 'price-was ']/text()").extract()[0].strip()
           item['typeitem'] = "Neweggweekly"
           item['rating'] = None
           items.append(item)
       return items

class NeweggDailySpider(BaseSpider):
    pipelines= ['multipleelectronics']
    name = "neweggdaily"
    allowed_domains = ["newegg.ca"]
    start_urls = [
       "http://www.newegg.ca"
    ]

    def parse(self, response):
       items = []
       hxs = HtmlXPathSelector(response)
       site = hxs.select("//div[@id='shellShocker2011']")
       item = ElectronicsItem()
       mainwrapper = site.select("//div[@class='wrapper']")[0]
       item = ElectronicsItem()
       item['name']= site.select("//a[@class='prodTitle']//span/text()").extract()[0].strip()
       pricedollars = mainwrapper.select("span[@class='prodPrice']/ul/li[@class='price-current ']/strong/text()").extract()[0].strip()
       pricecents= mainwrapper.select("span[@class='prodPrice']/ul/li[@class='price-current ']/sup/text()").extract()[0].strip()
       price = pricedollars + '.' + pricecents
       item['price']= price 
       item['description'] = None
       item['rating']= None
       item['link'] = mainwrapper.select("a/@href").extract()[0].strip()
       item['shipping'] = "Free Shipping"
       item['savings']= mainwrapper.select("span[@class='prodPrice']/ul/li[@class='price-save ']/span[@class = 'price-save-percent']/text()").extract()[0].strip()
       item['photourl'] = mainwrapper.select("a/img/@src").extract()[0].strip()
       item['priceprevious']= mainwrapper.select("span[@class='prodPrice']/ul/li[@class='price-was ']/text()").extract()[0].strip()
       item['typeitem'] = "Neweggdaily"
       items.append(item)
       print items   
       return items

       
class TigerdirectDailySpider(BaseSpider):
    pipelines= ['multipleelectronics']
    name = "tigerdirectdaily"
    allowed_domains = ["tigerdirect.ca"]
    start_urls = [
       "http://www.tigerdirect.ca/sectors/category/deal-of-the-dayca.asp?cm_sp=Masthead-_-DailyDeal-_-NA"
    ]

    def parse(self, response):
       items =[]
       hxs = HtmlXPathSelector(response)
       site = hxs.select("//div[@class='dod-box clearfix']")
       item = ElectronicsItem()
       item['name']= site.select("div[@class='col2']/h1[@class='dod-title']/a/text()").extract()[0].strip()
       pricedollars=site.select("div[@class='col2']/dl[@class='priceBox']/dd[@class='priceFinal']/div[@class='fPrice']/span[@class='salePrice']/text()").extract()[1].strip()
       pricecents= site.select("div[@class='col2']/dl[@class='priceBox']/dd[@class='priceFinal']/div[@class='fPrice']/span[@class='salePrice']/sup/text()").extract()[1].strip()
       price = pricedollars + "." + pricecents
       item['price'] = price
       item['link'] = site.select("div[@class='col2']/h1[@class='dod-title']/a/@href").extract()[0].strip()
       item['savings']= ''.join(site.select("div[@class='col2']/dl[@class='priceBox']/dd[@class='priceSave']/text()").extract()).strip()
       item['photourl'] = site.select("div[@class='col1 clearfix']/div[@class='dod-prodImg']/table/tr/td/a/img/@src").extract()[0].strip()
       item['priceprevious']= site.select("div[@class='col2']/dl[@class='priceBox']/dd[@class='priceSale']/text()").extract()[0].strip()
       item['shipping'] = None
       item['rating'] = None
       item['description'] = None 
       item['typeitem'] = "Tigerdirectdaily"
       items.append(item)
       return items

class MemoryExpressSpider(BaseSpider):
  pipelines= ['multipleelectronics']
  name = "memoryexpressfeatured"
  allowed_domains = ["http://www.memoryexpress.com"]
  start_urls = [
     "http://www.memoryexpress.com/"
  ]

  def parse(self, response):
    items =[]
    hxs = HtmlXPathSelector(response)
    sites = hxs.select("//div[@class='auto-load Product-IconView PIV_Regular']")
    items =[]
    for site in sites:
      item = ElectronicsItem()
      #get the price of the sale item we must split the string as the value isnt formatted correctly
      priceitem = ''.join(site.select("div[@class='PIV_BotCap']/div[@class='PIV_BotPrices']/div[@class='PIV_PriceSale']/text()").extract()).strip()
      #if item is not on sale, price is in a different div
      priceitem = priceitem.replace('$','')
      priceseperate = []
      priceseperate = priceitem.split('.')
      #if it's a sale item, this will work
      try :
        pricedollars = priceseperate.pop(0)
        pricedollars = pricedollars.replace(',','')
        pricecents= priceseperate.pop()
        price = pricedollars + '.' + pricecents
        item['price'] = price
        #if not sale item, will fail and change value of price item
      except:
        priceitem = ''.join(site.select("div[@class='PIV_BotCap']/div[@class='PIV_BotPrices']/div[@class='PIV_Price']/span/text()").extract()).strip()
        print priceitem
        priceitem = priceitem.replace('$','')
        priceseperate = []
        priceseperate = priceitem.split('.')
        #if end is reached, then print cant find price
        try:
          pricedollars = priceseperate.pop(0)
          pricecents= priceseperate.pop()
          price = pricedollars + "." + pricecents
          item['price'] = price
        except:
          print "Cant find price"

      item['name']= site.select("div[@class='PIV_Body']/div[@class='ProductTitle']/a/text()").extract()[0].strip()
      item['link'] = ''.join(site.select("div[@class='PIV_Body']/div[@class='ProductTitle']/a/@href").extract()).strip()
      item['link'] = 'http://memoryexpress.com' + item['link']
      item['savings']= None
      item['photourl'] = site.select("div[@class='PIV_Body']/div[@class='PIV_ProductImage']/a/img/@src").extract()[0].strip()
      item['priceprevious']= ''.join(site.select("div[@class='PIV_BotCap']/div[@class='PIV_BotPrices']/div[@class='PIV_PriceRegular']/span/text()").extract()).strip()
      item['shipping'] = None
      item['rating'] = None
      item['description'] = None 
      item['typeitem'] = "MemoryExpressFeatured"
      items.append(item)
    return items


class AsosMenSpider(BaseSpider):
    pipelines= ['clothing']
    rules = (
        Rule(SgmlLinkExtractor(allow=('\?pgesize=\d+'),)))
    

    name = "AsosMen"
    allowed_domains = ["asos.com"]
    start_urls = [
       "http://www.asos.com/Men/Sale/New-In/Cat/pgecategory.aspx?cid=8410&pge=0&pgesize=-1&sort=-1",
       
    ]

    def parse(self, response):
      items =[]
      hxs = HtmlXPathSelector(response)
      mainsite = hxs.select("//div[@class='category-items']")
      sites = mainsite.select("div[@class = 'items']/ul//li")
      print sites.extract()
      for site in sites:
        print site
        item = ClothingItem()
        item['name'] = ''.join(site.select("div[@class ='categoryImageDiv']/a/@title").extract()).strip()
        #change price to type string
        pricestr = ''.join(site.select("div[@class= 'productprice']/span[@class = 'price outlet-current-price']/text()").extract()).strip()
        print pricestr
        #get rid of both the C and the $ sign from price as Asos returns that infomation
        pricestr = pricestr.replace('C','')
        pricestr = pricestr.replace('$','')
        item['price'] = pricestr
        templink = ''.join(site.select("div[@class ='categoryImageDiv']/a/@href").extract()).strip()
        item['link'] = "http://www.asos.com" + templink
        item['shipping'] = "free"
        item['savings'] = None
        item['photourl'] = ''.join(site.select("div[@class ='categoryImageDiv']/a/img/@src").extract())
        #change previous price to string and get rid of unwanted chars
        pricepreviousstr = ''.join(site.select("div[@class= 'productprice']/span[@class = 'recRP rrp']/text()").extract()).strip()
        pricepreviousstr = pricepreviousstr.replace('C','')
        pricepreviousstr = pricepreviousstr.replace('$','')
        pricepreviousstr = pricepreviousstr.replace('R','')
        pricepreviousstr = pricepreviousstr.replace('P','')
        pricepreviousstr = pricepreviousstr.replace(' ','')
        item['priceprevious'] = pricepreviousstr
        item['typeitem']= "AsosMen"
        item['genderitem'] = "Men"
        items.append(item)
      print len(items)
      return items

class AsosWomenSpider(BaseSpider):
    pipelines= ['clothing']
    name = "AsosWomen"
    allowed_domains = ["asos.com"]
    start_urls = [
       "http://www.asos.com/Women/Sale/New-In-Clothing/Cat/pgecategory.aspx?cid=5524&&pge=0&pgesize=-1&sort=-1",
       "http://www.asos.com/Women/Sale/New-In-Shoes-Accs/Cat/pgecategory.aspx?cid=8956?cid=8956&pge=0&pgesize=-1&sort=-1",
       "http://www.asos.com/Women/Sale/New-In-Designer/Cat/pgecategory.aspx?cid=14985&pge=0&pgesize=-1&sort=-1"
       
    ]

    def parse(self, response):
      items =[]
      hxs = HtmlXPathSelector(response)
      mainsite = hxs.select("//div[@class='category-items']")
      sites = mainsite.select("div[@class = 'items']/ul//li")
      print sites.extract()
      for site in sites:
        print site
        item = ClothingItem()
        item['name'] = ''.join(site.select("div[@class ='categoryImageDiv']/a/@title").extract()).strip()
        #change price to type string
        pricestr = ''.join(site.select("div[@class= 'productprice']/span[@class = 'price outlet-current-price']/text()").extract()).strip()
        print pricestr
        #get rid of both the C and the $ sign from price as Asos returns that infomation
        pricestr = pricestr.replace('C','')
        pricestr = pricestr.replace('$','')
        item['price'] = pricestr
        templink = ''.join(site.select("div[@class ='categoryImageDiv']/a/@href").extract()).strip()
        item['link'] = "http://www.asos.com" + templink
        item['shipping'] = "free"
        item['savings'] = None
        item['photourl'] = ''.join(site.select("div[@class ='categoryImageDiv']/a/img/@src").extract())
        #change previous price to string and get rid of unwanted chars
        pricepreviousstr = ''.join(site.select("div[@class= 'productprice']/span[@class = 'recRP rrp']/text()").extract()).strip()
        pricepreviousstr = pricepreviousstr.replace('C','')
        pricepreviousstr = pricepreviousstr.replace('$','')
        pricepreviousstr = pricepreviousstr.replace('R','')
        pricepreviousstr = pricepreviousstr.replace('P','')
        pricepreviousstr = pricepreviousstr.replace(' ','')
        item['priceprevious'] = pricepreviousstr
        item['typeitem']= "AsosWomen"
        item['genderitem'] = "Women"
        items.append(item)
      print len(items)
      return items
