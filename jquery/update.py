import urllib2
import os

jquery_url = "http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"

jquery_ui_url = "http://ajax.googleapis.com/ajax/libs/jqueryui/1/jquery-ui.min.js"



def download(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    dir_name = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static")
    f = open(os.path.join(dir_name, file_name), 'w')
    meta = u.info()
    #file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s " % file_name
    
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
    
        file_size_dl += block_sz
        f.write(buffer)
        #status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        #status = status + chr(8)*(len(status)+1)
        #print status,
    
    f.close()
    
def update():
    download(jquery_url)
    download(jquery_ui_url)
    
if __name__ == '__main__':
    update()
