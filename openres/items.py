from scrapy.item import Item, Field


class Website(Item):
    total = Field()   
    hindex= Field()
    title = Field()
    authors = Field()
    source = Field()
    year =Field()
    citation = Field()
