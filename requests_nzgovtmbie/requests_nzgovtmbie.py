from requests.auth import AuthBase
import hmac
import hashlib
import base64
from datetime import datetime

class HttpNzgovtmbieAuth(AuthBase):
    """Authentication Handler for Requests to connect to NZ Government MBIE data services
    
    NB: URLencoding must have been applied to the get string otherwise you will get a 
    401 "Invalid message Signature error"""

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def hmac(self, message):
        signature = hmac.new( key=self.secret, msg=message, digestmod=hashlib.sha256)
        sig_text = base64.b64encode(signature.digest())
        return sig_text

    def cleanhost(self, fullpath, uripath):
        #NB fullpath & uripath both contain fullpath when a proxy is used
        #if this becomes an issue - might need to rewrite this func
        hostarr = fullpath.split(uripath)
        if hostarr and len(hostarr) == 2:
            host = hostarr[0]
            cleanhostarr = host.split('//')
            if cleanhostarr and len(hostarr) == 2:
                cleanhost = cleanhostarr[1]
                return cleanhost
            else:
                raise Exception("Issue with Host - not in standard format, odd url scheme?")
        else:
            raise Exception("Issue with Host - not in standard format?")

    def httpdate(self, ):
        """Return a string representation of the current date/time, according to RFC 1123
        (HTTP/1.1).
        """
        dt = datetime.now()
        weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][dt.weekday()]
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                 "Oct", "Nov", "Dec"][dt.month - 1]
        return "%s, %02d %s %04d %02d:%02d:%02d GMT" % (weekday, dt.day, month,
            dt.year, dt.hour, dt.minute, dt.second)

    def format_accept(self, format):
        if format == "json":
            accept = "application/json"
        else: # output xml
            accept = "application/xml"
        return accept

    def accept_header(self, format):
        ah = {}
        if format == "json":
            accept = "application/json"
        else: # output xml
            accept = "application/xml"
        ah['Accept']=accept
        return ah

    def date_header(self, datestr):
        dh = {}
        dh['Date'] = datestr
        return dh

    def host_header(self, host):
        hh = {}
        hh['Host'] = host
        return hh

    def __call__(self,r, format="json"):
        authheader = {}
        method = 'GET'
        host = self.cleanhost(r.full_url, r.path_url)
        url = r.path_url
        timestamp=  self.httpdate()
        accept = self.format_accept(format)
        #also need to set http accept accordingly
        accept_header = self.accept_header(format)
        r.headers.update(accept_header) 
        # and add the host header
        host_header = self.host_header(host)
        r.headers.update(host_header) 
        # and the date header
        date_header =self.date_header(timestamp)
        r.headers.update(date_header) 
        paramarr = [method, host, uri, timestamp, self.key, accept,''] #last string just to get trailing \n
        message = '\n'.join(paramarr)
        hashedmessage = self.hmac(message)
        auth_header_value = ':'.join([self.key, hashedmessage])
        authheader['Authorization'] = auth_header_value
        r.headers.update(authheader) 
        return r
