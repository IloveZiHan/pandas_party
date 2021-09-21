import json
import re

import requests as req

if __name__ == '__main__':
    goods_url = 'https://item.jd.com/100021670148.html'
    # 发送请求
    rep = req.get(goods_url, headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    })
    # HTML内容
    all_html = rep.text
    # 遍历文档
    color_selection_index = all_html.find('<div class="dt ">选择颜色')
    color_selection_end_index = all_html.find('<div class="dt ">选择尺码')
    size_selection_index = color_selection_end_index
    size_selection_end_index = \
        all_html.find('<div id="choose-results" class="li" style="display:none"><div class="dt">已选择</div><div class="dd"></div></div>')

    print(f'颜色选择索引范围：{color_selection_index}, {color_selection_end_index}')
    print(f'尺码选择索引范围：{size_selection_index}, {size_selection_end_index}')

    color_selection = all_html[color_selection_index: color_selection_end_index].replace("\n", '')
    size_selection = all_html[size_selection_index: size_selection_end_index].replace("\n", '')
    print(color_selection)
    print(size_selection)
    print("-" * 100)

    start_color_index = -1
    end_color_index = -1
    start_size_index = -1
    end_size_index = -1

    i_color_index = 0
    i_size_index = 0
    colors = []
    sizes = []

    while True:
        start_color_index = color_selection.find("<i>", i_color_index)
        end_color_index = color_selection.find("</i>", start_color_index)

        if start_color_index < end_color_index:
            # print(start_i_index, end_i_index)
            colors.append(color_selection[start_color_index + 3: end_color_index])
            i_color_index = end_color_index
        else:
            break

    START_TAG = ' <a href="#none" clstag="shangpin|keycount|product|yanse-'
    while True:
        start_size_index = size_selection.find(START_TAG, i_size_index)
        end_size_index = size_selection.find("</a>", start_size_index)

        if start_size_index < end_size_index:
            # print(start_size_index, end_size_index)
            sizes.append(size_selection[start_size_index + len(START_TAG) + 4: end_size_index].strip())
            i_size_index = end_size_index
        else:
            break

    print(colors)
    print(sizes)