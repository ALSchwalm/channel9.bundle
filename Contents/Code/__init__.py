
PREFIX = "/video/channel9"

NAME = "Channel9"

ART      = 'art-default.jpg'
ICON     = 'icon-default.png'

####################################################################################################

# This function is initially called by the PMS framework to initialize the plugin. This includes
# setting up the Plugin static instance along with the displayed artwork.
def Start():

    # Setup the default breadcrumb title for the plugin
    ObjectContainer.title1 = NAME

# This main function will setup the displayed items.
# Initialize the plugin
@handler(PREFIX, NAME)
def MainMenu():
    oc = ObjectContainer()

    return oc
