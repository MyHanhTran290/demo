import scrapy


class DalieucoursecrawlerSpider(scrapy.Spider):
    name = "DaLieuCourseCrawler"
    allowed_domains = ["vnexpress.net"]
    start_urls = ["https://vnexpress.net/luu-y-truoc-khi-triet-long-vinh-vien-4787438.html"]

    def parse(self, response):
        title = response.css('h1.title-detail::text').get()
        description = response.css('p.description::text').get()
        content = response.css('article.fck_detail p::text').getall()
        # author = response.css('span.author-name::text').get()

        yield {
            'title': title,
            'desciption': description,
            'content':'\n\n'.join(content),
        }
        
        
