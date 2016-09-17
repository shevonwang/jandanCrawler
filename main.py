# -*- coding: UTF-8 -*-
import re
import urllib2
import time


def get_page(url):
    html = req_url(url)
    current_page = re.findall(r'.*"current-comment-page">\[(.*?)\]</span>', html)[0]
    print current_page
    return current_page


def req_url(url):
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    head['Connection'] = 'keep-alive'
    head['Upgrade-Insecure-Requests'] = '1'
    head['DNT'] = '1'
    head['Accept-Encoding'] = 'deflate, sdch'
    head['Accept-Language'] = 'zh-CN,zh;q=0.8'
    head['Referer'] = 'http://jandan.net/'
    head['Cookie'] = '2827710474=7690Ak9FjTv1keA3jdHGpKNkknck3u0NLChWTVd%2F8A; 895878518=2fe9toc6iM2l%2F5iQ4WMRitKuQj4UPZf7d1ArCJG20Q; 2827710474=0e6eKvs5LnI5i1zkP1fwPBBr7gbF%2F6vuW%2BGD778e8Q; _gat=1; 895878518=24f9Tt3Nd6o3PaeYWy3meSymtdBbQdDQYEM0b%2FNFMQ; jdna=596e6fb28c1bb47f949e65e1ae03f7f5#1474089065692; _ga=GA1.2.919627943.1474028111'

    req = urllib2.Request(url, headers=head)
    response = urllib2.urlopen(req)
    html = response.read()
    return html


def find_imgs(url):
    html = req_url(url)
    imgs_url = re.findall(r'.*<a href="(.*?)" target=".*[查看原图].*<img.*src=".*" />', html)
    return imgs_url


def save_imgs(img_addrs):
    for path in img_addrs:
        name = path.split('/')
        content = req_url(path)
        with open('E:/Data-mining/python/mm_jpg/' + name[-1], 'wb') as f:
            f.write(content)


def get_img(pages):
    url = 'http://jandan.net/ooxx/'

    page_num = int(get_page(url))
    for i in range(pages):
        page_k = page_num
        page_k -= i
        page_url = url + 'page-' + str(page_k) + '#comments'
        print page_url
        img_addrs = find_imgs(page_url)
        save_imgs(img_addrs)

if __name__ == '__main__':
    print
    get_img(10)