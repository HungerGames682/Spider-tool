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
        # Appends the Url list it went to 
        lists.append(response.url)
        
        print("procesing:"+response.url)
       
        # Gets the href= value for the next page
        further_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
    
        produ.append(further_page_url)

        # Combines the next url with the origanl to getto the next page
        complete_url = response.urljoin(further_page_url)

        lists.append(complete_url)
        

        # Writes everything to a file
        for i in range(len(lists)):
            with open('results.txt', 'a') as f:
                f.writelines(lists[i] + '\n')
                print(lists)
                print(produ)
                