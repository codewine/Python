#!/bin/sh  

# 1 输出重定向

who > users

#不希望文件内容被覆盖，可以使用 >> 追加到文件末尾
echo "菜鸟教程：www.runoob.com" >> users


# 2 输入重定向
wc -l users
cat users
wc -l < users
cat users


#一般情况下，每个 Unix/Linux 命令运行时都会打开三个文件：
#标准输入文件(stdin)：stdin的文件描述符为0，Unix程序默认从stdin读取数据。
#标准输出文件(stdout)：stdout 的文件描述符为1，Unix程序默认向stdout输出数据。
#标准错误文件(stderr)：stderr的文件描述符为2，Unix程序会向stderr流中写入错误信息。
#默认情况下，command > file 将 stdout 重定向到 file，command < file 将stdin 重定向到 file。


cat users >> file 2>&1&0


#command1 < infile > outfile
#同时替换输入和输出，执行command1，从文件infile读取内容，然后将输出写入到outfile中。


echo < file > output

#/dev/null 文件
#如果希望执行某个命令，但又不希望在屏幕上显示输出结果，
#那么可以将输出重定向到 /dev/nul

#Here Document
#Here Document 是 Shell 中的一种特殊的重定向方式，用来将输入重定向到一个交互式 Shell 脚本或程序。

#它的基本的形式如下：
#command << delimiter
#document
#delimiter

# 例子

#cat << EOF
#欢迎来到
#菜鸟教程
#www.runoob.com
#EOF

