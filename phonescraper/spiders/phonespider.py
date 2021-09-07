import scrapy


class PhoneSpider(scrapy.Spider):
    name = "phone"
    start_urls = ["https://www.trendyol.com/cep-telefonu-x-c103498?pi=6"]

    #in built funcitons, response contains the response of the site.
    def parse(self, response):
        for product_descriptions in response.css("div.p-card-chldrn-cntnr"):
            # you can do try except here if necessary.
            yield {
                "product":product_descriptions.css("div.prdct-desc-cntnr-name.hasRatings::text").get(),
                "price":product_descriptions.css("div.prc-box-sllng.prc-box-sllng-w-dscntd::text").get(),
                "image":product_descriptions.css("img.p-card-img").attrib["src"]
            }

        # Hyptotethical function: If the next page exists, go to it.
        next_page = response.css("a.action.next").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse) # Calls the function back.