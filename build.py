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
    build()
