# this file will be responsible for grabbing stream information from the stream link provided
from m3u_parser import M3uParser

Playlist = open("Input Your Link Here.txt")
M3U = Playlist.readlines()[1]
Playlist.close()

useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
parser = M3uParser(timeout=5, useragent=useragent)
parser.parse_m3u(M3U)
parser.filter_by('status', 'GOOD')


# parser.retrieve_by_category("religi")

# get all channels list Format
def get_List():

    list = parser.get_list()
    return list


# Get all channels in Json format (for a better view)
def get_Json():
    list = parser.get_json()
    return list


# get all channels in the link return list
def get_AllName(list):
    channel_names = []
    x=0
    while x<len(list):
        channel_names.append(list[int(x)]['name'])
        x+=1
    return channel_names

#get all categories in the link| Return a list

def get_AllCategories():
    channel_category = []
    for channels in get_List():
        if channels["category"] in  channel_category: continue
        channel_category.append(channels["category"])

    return channel_category



#search for channel using a categories

def searchcategory(categ):
    categ = str(categ)
    parser.filter_by("category", categ)
    channels = get_List()
    parser.reset_operations()
    return channels


#search for the channel with the name then return a lsit  with channels
def searchChannel(channelName):
    channelName = str(channelName)
    parser.filter_by('name', channelName)
    channels = get_List()
    parser.reset_operations()
    return channels


#return a string witht the link from a list of channels
def linkFromList(lisT, number):
    link = lisT[int(number)]['url']
    return link





#print channels from  list of channels
def listPrinter(list):

    printer = ""
    q = 0
    for x in list:
        printer += str(q) + " : " + x + "\n"
        q += 1
    return printer



#print(get_AllName(searchChannel(s)))