# 简介


## 构建


### 中文文档

```shell
# 安装依赖, 建议在虚拟环境中
pip install requirements.doc.txt

# 调试
sphinx-autobuild -W cn_docs _build/html

# 输出html
sphinx-build cn_docs _build/html
```

### 英文文档

```shell
# 安装runestone , 建议在虚拟环境中
pip install runestone

# 到 en_docs目录下
cd en_docs

# 构建
runestone build

# 预览
runestone preview
# or
runestone serve
```