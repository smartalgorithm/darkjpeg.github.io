import webapp2
import urllib2
import base64

cors = '*'
hugs = '<p style="font: 120px Verdana;">\(^_^)/</p>'
size = 64 * 1024

class RootHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(hugs)

class ProxyHandler(webapp2.RequestHandler):
    def get(self, url):
        try:
            url = base64.standard_b64decode(url)
            req = urllib2.urlopen(url)

            chunk = req.read(10)
            if not chunk or chunk[6:10] != 'JFIF':
                self.response.status = '405 Method Not Allowed'
                self.response.headers.add('Access-Control-Allow-Origin', cors)
                self.response.write(hugs)
                return

            clen = [y for (x, y)
                      in req.headers.items()
                      if x == 'content-length'] or [0]

            self.response.headers.add('Content-Length', clen[0])
            self.response.headers.add('Content-Type', 'image/jpeg')
            self.response.headers.add('Access-Control-Allow-Origin', cors)

            while True:
                self.response.write(chunk)
                chunk = req.read(size)
                if not chunk: break
        except:
            self.response.status = '406 Not Acceptable'
            self.response.headers.add('Access-Control-Allow-Origin', cors)
            self.response.write(hugs)


application = webapp2.WSGIApplication([
    ('/',     RootHandler),
    ('/(.+)', ProxyHandler),
])
