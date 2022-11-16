import scrapy

lists = []
produ = []

with open('results.txt', 'w') as j:
    j.writelines("")

j.close()
class AliexpressTabletsSpider(scrapy.Spider):
    name = 'aliexpress_tablets'
    # allowed_domains = ['pt.youtube.com']
    start_urls = ['http://quotes.toscrape.com/']


    
    def parse(self, response):
        lists.append(response.url)
        
        print("procesing:"+response.url)
        #Extract data using css selectors
        product_name=response.css('href::text').extract()
    
        
        produ.append(product_name)


        for i in range(len(lists)):
            with open('results.txt', 'a') as f:
                f.writelines(lists[i] + '\n')
                print(lists)
                print(produ)
                