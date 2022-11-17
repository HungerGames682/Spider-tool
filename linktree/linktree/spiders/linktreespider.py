import scrapy
import turtle
m = turtle.Turtle()
lists = []
produ = []
been_to = []
# Wipes the prevoise data
with open('results.txt', 'w') as j:
    j.writelines("")

with open('been_to.txt', 'w') as g:
    g.writelines("")

with open('full_results.txt', 'w') as ki:
    ki.writelines("")

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
        

       
                
                
        yield scrapy.Request(complete_url)
                
                


        # Writes everything to a file
        for i in range(len(lists)):
            with open('results.txt', 'a') as f:
                f.writelines(lists[i] + '\n')
                print(lists)
                print(produ)

        for f in range(len(been_to)):
            with open('been_to.txt', 'a') as dk:
                dk.writelines(been_to[f] + '\n')

        for k in range(len(produ)):
            with open('uncut.txt','a') as jj:
                jj.writelines(produ[k] + '\n')


       

       
        


        # Sorts the data out or something
        # with open('results.txt', 'r') as ff:
        #     bob = ff.readlines()

        #     for a in range(len(bob)):
        #         b = a + 1
        #         if bob[a] == bob[b]:
        #             with open('full_results.txt','a') as dd:
        #                dd.writelines(bob[a] + '\n')

        #         elif bob[a] != bob[b]:
        #          print("AHGHHHFHJDSAKL;FHADJSKL")

        



                