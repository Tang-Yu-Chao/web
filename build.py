import os, json

#位于仓库根目录，把path目录下的所有 .md 变成网页能读的列表存到data.json。
#这里可以改为：1个.md一个句子列表，或识别一个.md中的一个句子(二级标题)作为一个句子列表，填到 data.json 


def build():
    qs = []
    path = "quotes"
    if os.path.exists(path):
        for f in os.listdir(path):
            if f.endswith(".md"):
                with open(os.path.join(path, f), 'r', encoding='utf-8') as file:
                    qs.append(file.read().strip())
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(qs, f, ensure_ascii=False)
if __name__ == "__main__":
    
    build()
