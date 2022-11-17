import scrapy

lists = []
produ = []
been_to = []

with open('results.txt', 'w') as j:
    j.writelines("")

j.close()
class LinktreespiderSpider(scrapy.Spider):
    name = 'linktreespider'
    # allowed_domains = ['pt.youtube.com']

    # Websites to start in
    start_urls = ['http://quotes.toscrape.com/']


    
    def parse(self, response):
        # Appends the Url list it went to 
        # lists.append(response.url)
        
        print("procesing:"+response.url)
       
        # Gets the href= value for the next page
        further_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
    
        produ.append(further_page_url)

        # Combines the next url with the origanl to getto the next page
        complete_url = response.urljoin(further_page_url)

        lists.append(complete_url)
        been_to.append(complete_url)

        for d in range(0, len(lists)):
            if lists[d] == complete_url:
                been_to.append("Failure")
                yield scrapy.Request(complete_url)

            else:
                yield scrapy.Request(complete_url)

        # Writes everything to a file
        for i in range(len(lists)):
            with open('results.txt', 'a') as f:
                f.writelines(lists[i] + '\n')
                print(lists)
                print(produ)
                