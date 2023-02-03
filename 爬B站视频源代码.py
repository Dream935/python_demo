
import json
import re
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import requests
from tqdm import tqdm


def get_response(html_url, stream=False):
    headers = {
        "referer": "https://www.bilibili.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    response = requests.get(html_url, headers=headers, stream=stream)
    return response


def get_url(html_url):
    r = requests.get(html_url)
    a = re.search(r"window\.__INITIAL_STATE__=(.*?)};", r.text).group(1)
    json_data = json.loads(a + "}")
    video_data = json_data['videoData']
    avid = str(video_data['aid'])
    qn = '112'
    urls = []

    for p in video_data['pages']:
        cid = str(p['cid'])
        title = p['part']
        if len(video_data['pages']) == 1:
            title = video_data['title']
        urls.append({
            'title': title,
            "url": "https://api.bilibili.com/x/player/playurl?cid=" + cid + "&avid=" + avid + "&an=" + qn + "&otype=json&fourk=1"
        })
    return urls


def save(video_url, video_size, title):
    video_res = get_response(video_url, True)
    with open(r'C:\Users\70503\Desktop\哔哩哔哩\\'+title + '.mp4', 'wb') as fd:
        print('开始下载文件：{}, 当前文件大小：{}KB'.format(title, video_size / 1024))
        for c in tqdm(iterable=video_res.iter_content(), total=video_size, unit='b', desc=None):
            fd.write(c)
        print('{},文件下载成功'.format(title))


def a_single_download(info):
    response = get_response(info['url'])
    json_data = json.loads(response.text)
    video_url = json_data['data']['durl'][0]['url']
    video_size = json_data['data']['durl'][0]['size']
    save(video_url, video_size, info['title'])


def concurrent_download(base_infos):
    executor = ThreadPoolExecutor(max_workers=10)
    futur_tasks = [executor.submit(a_single_download, info)
                   for info in base_infos]
    wait(futur_tasks, return_when=ALL_COMPLETED)


if __name__ == '__main__':
    base_infos = get_url(
        'https://www.bilibili.com/video/BV1Tg411m7Zm/?spm_id_from=333.1073.high_energy.content.click&vd_source=6960fbd74a4815904b180eb6ec96849d')
    print(base_infos)
    concurrent_download(base_infos)
