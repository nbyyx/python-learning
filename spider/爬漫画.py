import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from pathlib import Path

def get_content(url, referer_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': referer_url,
    }
    req = requests.get(url=url, headers=headers, timeout=10)
    return req.content

# 配置
directory_url = 'https://www.dm5.com/m1040375/'  # 漫画章节页面
save_path = Path('/Users/yyx/Documents/github/my-repositroy/python-learning/spider')
save_path.mkdir(parents=True, exist_ok=True)  # 自动创建目录

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

try:
    # 1. 获取章节页面
    response = requests.get(directory_url, headers=headers, timeout=10)
    
    if response.status_code == 200:
        html = response.text
        bs = BeautifulSoup(html, 'lxml')
        
        # 2. 找到所有图片（正确的位置）
        chapter = bs.find('div', id='barChapter')
        if not chapter:
            print("未找到 id='barChapter' 的元素，页面结构可能已变化")
            exit()
            
        imgs = chapter.find_all('img', class_='load-src')
        print(f"找到 {len(imgs)} 张图片，开始下载...")
        
        # 3. 下载图片
        for i, img in enumerate(tqdm(imgs, desc="下载进度")):
            img_url = img.get('data-src')
            if not img_url:
                continue
                
            # 生成文件名（保留原始格式）
            file_name = f'{i+1:03d}.jpg'
            file_path = save_path / file_name
            
            # 下载并保存
            content = get_content(img_url, directory_url)
            with open(file_path, 'wb') as f:
                f.write(content)
        
        print(f"\n✅ 图片下载完成！共 {len(imgs)} 张，保存在：{save_path}")
    else:
        print(f"❌ 请求失败，状态码: {response.status_code}")
        
except Exception as e:
    print(f"❌ 请求异常: {e}")