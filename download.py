import xmlrpc.client

#s = xmlrpc.client.ServerProxy('http://localhost:6800/rpc') 
#filename = 'qq.exe'
#path = './'
#s.aria2.addUri("token:dht",['http://dl_dir.qq.com/qqfile/qq/QQ2011/QQ2011.exe'], {"out": filename, "dir": path}) #添加下载链接
#print(dir(s))

#from pyaria2 import Aria2RPC
#jsonrpc = Aria2RPC(url='http://localhost:6800/rpc', token='dht')
#resp = jsonrpc.addUris('https://music.snowmusic.cc/radio/13714_1507261169_4.mp3', options={"out": "aa.mp3"})
#print(resp)

import requests, json
from pprint import pprint
import sys

if len(sys.argv) >0:
    uri = sys.argv[1]
download_req = {
    "jsonrpc": "2.0",
    "id": "magnet",
    "method": "aria2.addUri",
    "params": [
        "token:dht",
        ['magnet:?xt=urn:btih:'+uri],
    ],
}

status_req = {
    "jsonrpc": "2.0",
    "id": "magnet",
    #"method":"aria2.getOption",
    "method":"aria2.tellStatus",
    "params": [
        "token:dht", 
    ],
}

url = 'http://localhost:6800/jsonrpc'
#r = requests.post(url, data= json.dumps(download_req),headers={"Content-Type": "application/json"})
#r = json.loads(r.text)
#pprint(r)
#if "result" in r:
if True:
#gid = r['result']
    gid = 'a6b94f9e672e7443'
    status_req['params'].append(gid)
    r = requests.post(url, data= json.dumps(status_req),headers={"Content-Type": "application/json"})
    pprint(json.loads(r.text))
else:
    print("NONE")
