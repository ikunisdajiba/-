import os
from pathlib import Path

# 已经根据你的真实仓库信息自动填好，无需任何修改
BASE_URL = "https://raw.githubusercontent.com/ikunisdajiba/-/master/"
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.svg'}

def generate_raw_links():
    print("🔗 正在扫描并生成 GitHub Raw 链接...\n" + "-" * 50)
    
    current_dir = Path.cwd()
    count = 0
    
    # 递归扫描当前目录及所有子目录下的文件
    for file_path in current_dir.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in IMAGE_EXTENSIONS:
            # 计算相对路径
            rel_path = file_path.relative_to(current_dir)
            # 将路径中的 Windows 反斜杠 "\" 转换为 URL 标准的正斜杠 "/"
            url_path = rel_path.as_posix()
            
            # 拼接最终链接并输出
            print(f"{BASE_URL}{url_path}")
            count += 1
            
    print("-" * 50)
    print(f"✅ 扫描完成！共生成了 {count} 个图片链接，可以直接复制到 story.json 里使用。")

if __name__ == "__main__":
    generate_raw_links()