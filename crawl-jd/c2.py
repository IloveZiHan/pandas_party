import requests as req
import json

"""
需求：利用for循环写一段代码，爬取评论中口红的色号数据
"""

if __name__ == '__main__':
    goods_url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100011323932&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    # 发送请求
    rep = req.get(goods_url, headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    })
    # HTML内容
    all_html = rep.text

    # 替换出来json串
    all_html = all_html.replace('fetchJSON_comment98(', '')
    # 替换最后的');'
    all_html = all_html[:len(all_html) - 2]

    # 解析JSON
    dict = json.loads(all_html)
    comments = dict["comments"]

    colors = []
    for comment in comments:
        reference_name = comment["referenceName"]
        colors.append(str(reference_name).split(" ")[1])

    print(colors)
