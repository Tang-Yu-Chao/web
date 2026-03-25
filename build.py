import os, json
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
    #位于仓库根目录，自动把所有 .md 变成网页能读的列表。
    build()
