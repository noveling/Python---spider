import os
from urllib import request
import sys
'http://video.pearvideo.com/mp4/adshort/20180714/cont-1388592-12455023_adpkg-ad_hd.mp4'
def Schedule(a,b,c):
    per = 100.0*a*b/c
    if per >100:
        per=100
    sys.stdout.write("  " + "%.2f%% 已经下载的大小:%ldB 文件大小:%ldB" % (per,a*b,c) + '\r')
    sys.stdout.flush()

def video_download(url,filename):
    request.urlretrieve(url=url, filename=filename, reporthook=Schedule)


if __name__ == '__main__':
    exp = 'http://video.pearvideo.com/mp4/adshort/20180715/cont-1389084-12460008_adpkg-ad_hd.mp4'
    url = input("输入url:")
    filename = '.'+url.split('/')[-1]
    video_download(url,filename)
