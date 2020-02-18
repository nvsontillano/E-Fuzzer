import requests

class HTTP_HEADER(object):
    ACCEPT = "Accept"
    ACCEPT_CHARSET = "Accept-Charset"
    ACCEPT_ENCODING = "Accept-Encoding"
    ACCEPT_LANGUAGE = "Accept-Language"
    AUTHORIZATION = "Authorization"
    CACHE_CONTROL = "Cache-Control"
    CONNECTION = "Connection"
    CONTENT_ENCODING = "Content-Encoding"
    CONTENT_LENGTH = "Content-Length"
    CONTENT_RANGE = "Content-Range"
    CONTENT_TYPE = "Content-Type"
    COOKIE = "Cookie"
    HOST = "Host"
    PROXY_AUTHORIZATION = "Proxy-Authorization"
    PROXY_CONNECTION = "Proxy-Connection"
    TRANSFER_ENCODING = "Transfer-Encoding"
    URI = "URI"
    USER_AGENT = "User-Agent"

"""
This file contains the formulation and sending of 
the HTTP request.
"""
class Request():
    data = {}
    wildcardData = {}
    params = {}
    url = ""
    method = ""
    headers = {}

    """
    Prepare HTTP Cookie, HTTP User-Agent and HTTP Referer headers to use when performing
    the HTTP requests
    """
    def forgeHeaders(self, cookie, authCred):
        if cookie:
            self.headers[HTTP_HEADER.COOKIE] = cookie
        if authCred:
            self.headers[HTTP_HEADER.AUTHORIZATION] = 'Basic %s' % authCred 

    """
    Separate the static data from wildcard data. 
    Format the static data for request. 
    """
    def setData(self, data, static):
        staticIndex = []
        if static:
            for _ in static.split(','):
                staticIndex.append(int(_.strip())-1)

        for index, value in enumerate(data.split(';')):
            print('value: ', value)
            _ = value.split('=')
            if index in staticIndex:
                self.data[_[0].strip()] = _[1].strip()
            else:
                self.wildcardData[_[0].strip()] = _[1].strip()
    
    """
    Set the method of the request
    """
    def setMethod(self, method):
        if not method: 
            self.method = 'get'
        else:
            self.method = method.lower()
    
    """
    Set the target url
    """
    def setUrl(self, url, value=None):
        if value:
            self.url = url.replace('<>', value)
        else:
            self.url = url

    """
    Set the value of the wildcard data.
    Add the wildcard data to the request.
    """
    def setWildcardData(self, value):
        for key in self.wildcardData.keys():
            self.wildcardData[key] = value
        
        self.data.update(self.wildcardData)

    """
    Send the request and return the response
    """
    def sendRequest(self):
        if self.method=='post':
            response = requests.post(self.url, params=self.params, headers=self.headers)
        else:
            response = requests.get(self.url, params=self.params, headers=self.headers)

        return response
