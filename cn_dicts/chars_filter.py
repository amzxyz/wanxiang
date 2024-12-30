from pathlib import Path

def filter_chars():
    # 使用相对路径
    base_dir = Path(__file__).parent
    origin_file = base_dir / "chars.dict.yaml"
    dest_file = base_dir / "chars.simple.dict.yaml"
    simple_file = base_dir / "8105.dict.yaml"

    try:
        # 读取 simpleFile 并提取符合条件的字符
        with simple_file.open(encoding="utf-8") as sf:
            simple_chars = [line.split("\t")[0] for line in sf if "\t" in line]
        
        # 读取 originFile 中的所有行
        with origin_file.open(encoding="utf-8") as of:
            lines = of.readlines()
        
        # 筛选出符合条件的行
        filtered_lines = [
            line for line in lines 
            if "\t" not in line or line.split("\t")[0] in simple_chars
        ]
        
        # 将筛选后的结果写入 destFile
        with dest_file.open("w", encoding="utf-8") as df:
            df.writelines(filtered_lines)
    except Exception as e:
        print(f"An error occurred: {e}")

# 调用方法
if __name__ == "__main__":
    filter_chars()