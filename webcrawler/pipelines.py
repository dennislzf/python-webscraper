# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


import datetime
import MySQLdb.cursors
import MySQLdb
class ElectronicsSQLPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'scrapydata', charset="utf8",
                           use_unicode=True)
        self.cursor = self.conn.cursor()
  		
        


    def process_item(self, items, spider):
		if 'multipleelectronics' in getattr(spider, 'pipelines', [])[0]:
			for item in items:
				try:
					#if item is already in db, do not add it. 
					self.cursor.execute("""SELECT * FROM electronicstable WHERE name = %s AND price = %s""",(items['name'], items['price']))
					data = self.cursor.fetchall()
					print data
					#if item is not in database, then add it. 
					if data is ():
						self.cursor.execute("""INSERT INTO electronicstable ( name, price, description,link, shipping, savings, photourl,priceprevious,typeitem  )
						VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)""",
						(items['name'],
						items['price'],
						items['description'],
						items['link'],
						items['shipping'],
						items['savings'],
						items['photourl'],
						items['priceprevious'],
						items['typeitem']
						))
						self.conn.commit()
					else: return items
				except MySQLdb.Error,e:
					print ("MySQL Error -------------------------------------------------------")
        			print (e)	
        		
		
		# else:
		# 		try:
		# 			self.cursor.execute("""SELECT * FROM electronicstable WHERE name = %s AND pricedollars = %s""",(items['name'], items['pricedollars']))
		# 			data = self.cursor.fetchall()
		# 			print data
		# 			if data is ():
		# 				self.cursor.execute("""INSERT INTO electronicstable ( name, pricedollars, pricecents, description, rating,link, shipping, savings, photourl,priceprevious,typeitem  )
		# 	                        VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
		# 	                        (items['name'],
		# 			                items['pricedollars'],
		# 			                items['pricecents'],
		# 			                items['description'],
		# 			                items['rating'],
		# 			                items['link'],
		# 			                items['shipping'],
		# 			                items['savings'],
		# 			                items['photourl'],
		# 			                items['priceprevious'],
		# 			                items['typeitem']
		# 			                ))
		# 				self.conn.commit()
		# 			else: return items



		# 		except MySQLdb.Error, e:
		# 			print ("MySQL Error -------------------------------------------------------")
		#         	#print (e)
        	
			
	
		return items

class ClothingPipeline(object):
	def __init__(self):
	    self.conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'scrapydata', charset="utf8",
	                       use_unicode=True)
	    self.cursor = self.conn.cursor()
			
	    


	def process_item(self, items, spider):
		if 'clothing' in getattr(spider, 'pipelines', [])[0]:
			for item in items:
				try:
					#if item is already in db, do not add it. 
					self.cursor.execute("""SELECT * FROM clothingtable WHERE name = %s""",(items['name']))
					data = self.cursor.fetchall()
					print data
					#if item is not in database, then add it. 
					if data is ():
						self.cursor.execute("""INSERT INTO clothingtable ( name, price, link, shipping, savings, photourl,priceprevious,typeitem,genderitem  )
						VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)""",
						(items['name'],
						items['price'],
						items['link'],
						items['shipping'],
						items['savings'],
						items['photourl'],
						items['priceprevious'],
						items['typeitem'],
						items['genderitem']
						))
						self.conn.commit()
					else: return items
				except MySQLdb.Error,e:
					print ("MySQL Error -------------------------------------------------------")
	    				