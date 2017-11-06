#!/bin/bash

# Shell 基本运算符

#bash不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr，expr 最常用。
#expr 是一款表达式计算工具，使用它能完成表达式的求值操作。

val=`expr 2 + 2`
echo "两数之和为 : $val"

a=10
b=20

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

if [ $a == $b ]
then
echo "a 等于 b"
fi
if [ $a != $b ]
then
echo "a 不等于 b"
fi


#2 关系运算符
#运算符    说明    举例
#-eq    检测两个数是否相等，相等返回 true。    [ $a -eq $b ] 返回 false。
#-ne    检测两个数是否相等，不相等返回 true。    [ $a -ne $b ] 返回 true。
#-gt    检测左边的数是否大于右边的，如果是，则返回 true。    [ $a -gt $b ] 返回 false。
#-lt    检测左边的数是否小于右边的，如果是，则返回 true。    [ $a -lt $b ] 返回 true。
#-ge    检测左边的数是否大于等于右边的，如果是，则返回 true。    [ $a -ge $b ] 返回 false。
#-le    检测左边的数是否小于等于右边的，如果是，则返回 true。    [ $a -le $b ] 返回 true。



#3 布尔运算符
#运算符    说明    举例
#!    非运算，表达式为 true 则返回 false，否则返回 true。    [ ! false ] 返回 true。
#-o    或运算，有一个表达式为 true 则返回 true。    [ $a -lt 20 -o $b -gt 100 ] 返回 true。
#-a    与运算，两个表达式都为 true 才返回 true。    [ $a -lt 20 -a $b -gt 100 ] 返回 false。

#4 逻辑运算符
#&&    逻辑的 AND    [[ $a -lt 100 && $b -gt 100 ]] 返回 false
#||    逻辑的 OR    [[ $a -lt 100 || $b -gt 100 ]] 返回 true

#5 字符串运算符
#=    检测两个字符串是否相等，相等返回 true。    [ $a = $b ] 返回 false。
#!=    检测两个字符串是否相等，不相等返回 true。    [ $a != $b ] 返回 true。
#-z    检测字符串长度是否为0，为0返回 true。    [ -z $a ] 返回 false。
#-n    检测字符串长度是否为0，不为0返回 true。    [ -n $a ] 返回 true。
#str    检测字符串是否为空，不为空返回 true。    [ $a ] 返回 true。


#6 文件测试运算符
#操作符    说明    举例
#-b file    检测文件是否是块设备文件，如果是，则返回 true。    [ -b $file ] 返回 false。
#-c file    检测文件是否是字符设备文件，如果是，则返回 true。    [ -c $file ] 返回 false。
#-d file    检测文件是否是目录，如果是，则返回 true。    [ -d $file ] 返回 false。
#-f file    检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。    [ -f $file ] 返回 true。
#-g file    检测文件是否设置了 SGID 位，如果是，则返回 true。    [ -g $file ] 返回 false。
#-k file    检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。    [ -k $file ] 返回 false。
#-p file    检测文件是否是有名管道，如果是，则返回 true。    [ -p $file ] 返回 false。
#-u file    检测文件是否设置了 SUID 位，如果是，则返回 true。    [ -u $file ] 返回 false。
#-r file    检测文件是否可读，如果是，则返回 true。    [ -r $file ] 返回 true。
#-w file    检测文件是否可写，如果是，则返回 true。    [ -w $file ] 返回 true。
#-x file    检测文件是否可执行，如果是，则返回 true。    [ -x $file ] 返回 true。
#-s file    检测文件是否为空（文件大小是否大于0），不为空返回 true。    [ -s $file ] 返回 true。
#-e file    检测文件（包括目录）是否存在，如果是，则返回 true。    [ -e $file ] 返回 true。











