import requests as req
import json

"""
需求：爬取一页京东上销量最高的口红评论区数据
——出于简单先不做分页

1. 在浏览器中打开京东页面，然后搜索口红，再按照销量排序，拿到对应的URL
    https://search.jd.com/Search?keyword=%E5%8F%A3%E7%BA%A2&qrst=1&wq=%E5%8F%A3%E7%BA%A2&stock=1&pvid=07951bb3c9ae43488ca90cb83b8e3004&psort=3&click=0
2. 点击进入到销量最高的口红的URL，再点击商品评价
    https://item.jd.com/100011323932.html
3. 打开F12，然后点击network，点击评论，查看发送的请求。
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
    # print(f'python响应内容为：{all_html}')

    # 解析JSON
    dict = json.loads(all_html)
    print(dict["comments"])