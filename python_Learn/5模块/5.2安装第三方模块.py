from PIL import Image

im = Image.open('../sources/img.jpg')

print(im.format, im.size, im.mode)

print('生成缩略图')
im.thumbnail((200, 100))
im.save('../sources/thumb.jpg', 'JPEG')


print('其他常用的第三方库还有MySQL的驱动：mysql-connector-python，'
      '用于科学计算的NumPy库：numpy，'
      '用于生成文本的模板工具Jinja2，'
      '等等')



print('默认情况下，Python解释器会搜索当前目录、'
      '所有已安装的内置模块和第三方模块，'
      '搜索路径存放在sys模块的path变量中')


import sys
print(sys.path)


print('方法一')

# 如果我们要添加自己的搜索目录，有两种方法：
#
# 一是直接修改sys.path，添加要搜索的目录：
#
# import sys
# sys.path.append('/Users/michael/my_py_scripts')

print('方法二')

# 第二种方法是设置环境变量PYTHONPATH，
# 该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似。
# 注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。