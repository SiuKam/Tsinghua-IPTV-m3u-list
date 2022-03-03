# -*- coding: utf-8 -*-

import json
from urllib import request

channels_url = 'https://iptv.tsinghua.edu.cn/channels.json'
channels_json = request.urlopen(channels_url).read().decode('utf8')
channels = json.loads(channels_json)

f = open('channels.m3u', 'w+', encoding='utf-8')
f.write('#EXTM3U\n')
for i in range(len(channels['Categories'])):
    for j in range(len(channels['Categories'][i]['Channels'])):
        line_1 = '#EXTINF:-1 group-title="' + channels['Categories'][i]['Name'] + '",' + channels['Categories'][i]['Channels'][j]['Name'] + '\n'
        m3u8_url = 'https://iptv.tsinghua.edu.cn/hls/' + channels['Categories'][i]['Channels'][j]['Vid'] + '.m3u8'
        f.write(line_1)
        f.write(m3u8_url + '\n')
f.close()

f = open('channels.txt', 'w+', encoding='utf-8')
for i in range(len(channels['Categories'])):
    f.write(channels['Categories'][i]['Name'] + '\n')
    for j in range(len(channels['Categories'][i]['Channels'])):
        m3u8_url = channels['Categories'][i]['Channels'][j]['Name'] + ',https://iptv.tsinghua.edu.cn/hls/' + channels['Categories'][i]['Channels'][j]['Vid'] + '.m3u8'
        f.write(m3u8_url + '\n')
f.close()
