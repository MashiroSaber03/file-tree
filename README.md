## 简介

该程序是一个 Python 脚本，用于以树状结构显示指定目录下的所有文件和子目录。它提供了一种简单而直观的方式来查看文件系统的层级结构。

## 功能

*   **树状结构显示:** 以美观的树状结构展示目录内容，清晰展示文件和文件夹的层级关系。
*   **用户交互:** 提示用户输入要扫描的目录路径。
*   **路径验证:** 检查用户输入的路径是否存在，如果不存在则提示用户重新输入。
*   **权限检查:** 尝试访问用户指定的路径，如果权限不足则提示用户重新输入。
*   **异常处理:**  处理无法访问的目录，避免程序崩溃。
*   **可退出:**  用户可以输入 'q' 退出程序。

## 示例

假设你的目录结构如下：

my_project/
├── README.md
├── src/
│ ├── main.py
│ ├── utils.py
│ └── data/
│ └── input.txt
└── docs/
└── user_manual.pdf

TEXT

运行程序并输入 `my_project` 后，输出如下所示：

my_project
├── README.md
├── src
│ ├── main.py
│ ├── utils.py
│ └── data
│ └── input.txt
└── docs
└── user_manual.pdf

TEXT

## 依赖

*   Python 3.x
*   标准库 `os` (无需额外安装)

## 注意事项

*   程序只能显示你拥有访问权限的目录和文件。
*   对于非常大的目录，生成树状结构可能需要一些时间。



*   添加选项以显示文件大小、修改日期等信息。
*   添加选项以过滤特定类型的文件。
*   添加选项将输出保存到文件。
*   添加颜色以使输出更美观。
