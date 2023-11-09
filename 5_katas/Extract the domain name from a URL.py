# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"



from urllib.parse import urlparse


def domain_name(url):
    if "://" not in url:
        url = "http://" + url
    domain = urlparse(url).netloc
    if domain.startswith("www."):
        domain = domain.split('www.')[1]
    return domain.split('.')[0]


print(domain_name("www.xakep.ru"))



#way shorter 
def domain_name_2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]