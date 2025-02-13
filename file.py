import os

def build_tree(path, indent=''):
    """
    递归地构建文件和文件夹的树状结构。

    Args:
        path: 要扫描的根目录的路径。
        indent: 用于表示层级关系的缩进字符串。
    """
    try:
        items = os.listdir(path)  # 获取目录下所有文件和文件夹
    except OSError as e:
        print(f"无法访问 {path}: {e}")  # 处理无法访问目录的情况
        return

    items.sort()  # 可选：对文件和文件夹排序，使输出更易读

    for i, item in enumerate(items):
        item_path = os.path.join(path, item)  # 构建完整路径

        # 根据是否是最后一个元素，选择不同的前缀，使树状结构更美观
        if i == len(items) - 1:
            prefix = "└── "
            new_indent = indent + "    "  # 增加下一级的缩进
        else:
            prefix = "├── "
            new_indent = indent + "│   "  # 增加下一级的缩进

        print(indent + prefix + item)  # 打印当前项

        if os.path.isdir(item_path):  # 如果是文件夹，则递归调用 build_tree
            build_tree(item_path, new_indent)


# 获取用户输入的路径，并进行验证
while True:
    path = input("请输入要生成树状结构的文件夹路径（输入 'q' 退出）：")

    if path.lower() == 'q':
        print("程序已退出。")
        break  # 用户输入 'q'，退出程序

    # 移除路径两侧的引号 (如果存在)
    path = path.strip('"').strip("'")

    if not os.path.exists(path):
        print("路径不存在！请重新输入。")
    else:
        try:
            os.listdir(path)  # 尝试访问路径，检查权限

            # 获取路径的最后一个组成部分（主文件夹名）
            folder_name = os.path.basename(path)
            print(folder_name)  # 打印主文件夹名

            build_tree(path)  # 开始构建树状结构

        except OSError as e:
            print(f"无法访问 {path}: {e} 请重新输入。")
