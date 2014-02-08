
PREFIX = "/video/channel9"
NAME = "Channel9"
URL = "http://channel9.msdn.com/" 

ART = 'art-default.jpg'
ICON = 'icon-default.png'

####################################################################################################

def Start():

    ObjectContainer.title1 = NAME
    HTTP.CacheTime = CACHE_1HOUR
    HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20100101 Firefox/23.0'

# Initialize the plugin
@handler(PREFIX, NAME)
def MainMenu():
    oc = ObjectContainer()

    oc.add(DirectoryObject(
        key = Callback(ShowListBrowser, title='Shows', mode=""),
        title = 'Shows'
    ))

    oc.add(DirectoryObject(
        key = Callback(SeriesListBrowser, title='Series', mode=""),
        title = 'Series'
    ))

    return oc

@route(PREFIX + '/showlist')
def ShowListBrowser(title, mode):

    oc = ObjectContainer(title2=title)
    html = HTML.ElementFromURL(URL + "Browse/Shows")

    return oc

@route(PREFIX + '/serieslist')
def SeriesListBrowser(title, mode):

    oc = ObjectContainer(title2=title)
    html = HTML.ElementFromURL(URL + "Browse/Series")
    
    for show in html.xpath(r'//div[@id="gallery_index_display"]'):
        title = ""
        summary = ""
        url = ""

        oc.add(DirectoryObject(
            key = Callback(SeriesBrowser, show_url=url, show_name=title),
            title = title,
            summary = summary
        ))

    return oc

@route(PREFIX + '/serieslist/series')
def SeriesBrowser(series_name, series_url):
    pass
