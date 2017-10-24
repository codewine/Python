#!/bin/sh  

# 1 Shell 变量

#
your_name="runoob.com"

#for in 格式
for file in `ls ./`;do
    echo ${file}
done

#使用变量
echo ${your_name}

#拼接字符串
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting $greeting_1

#提取子字符串
string="runoob is a great site"
echo ${string:1:4}

#查找子字符串
string="runoob is a great company"
echo `expr index "$string" is`  # 输出 8

#双引号
your_name='qinjx'
str="Hello, I know your are \"$your_name\"! \n"
str2='Hello, I know your are \"$your_name\"! \n'
echo $str
echo $str2

#   Shell 数组
array_name=('value0' 'value1' 'value2' 'value3')
echo ${array_name[3]}
#获取数组的长度
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[2]}
echo ${lengthn}

