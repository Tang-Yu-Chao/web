# web


build.py

位于仓库根目录，把path目录下的所有 .md 变成网页能读的列表存到data.json。
这里可以改为：1个.md一个句子列表，或识别一个.md中的一个句子(二级标题)作为一个句子列表，填到 data.json 








index.html

抓取 (Fetch) 文件 data.json，将 JSON 字符串还原成一个数组，点击“刷一个”时程序运行 Math.random()随机产生一个索引数字X，
最后通过 document.getElementById('box').innerText = data[X] 把文字塞进网页那个白色的方块里。
