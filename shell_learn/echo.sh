#!/bin/sh  

# Shell echo命令

echo "It is a test"
echo It is a test
echo "\"It is a test\""

#   read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量
read name
echo "$name It is a test"

#显示换行
echo -e "OK! \n" # -e 开启转义
echo "It it a test"

#显示结果定向至文件
echo "It is a test" > myfile

#显示命令执行结果
echo `date`
