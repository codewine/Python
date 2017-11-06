#!/bin/sh  

# Shell 流程控制 命令

echo '流程控制 命令'

#
#if condition
#then
#command1
#command2
#...
#commandN
#fi



#if condition
#then
#command1
#command2
#...
#commandN
#else
#command
#fi

#
#if condition1
#then
#command1
#elif condition2
#then
#command2
#else
#commandN
#fi

a='_101'
b=20
if [ $a == $b ]
then
echo "a 等于 b"
elif [ $a -gt $b ]
then
echo "a 大于 b"
elif [ $a -lt $b ]
then
echo "a 小于 b"
else
echo "没有符合的条件"
fi


#

num1=$[2*3]
num2=$[1+5]
if test $[num1] -eq $[num2]
then
echo '两个数字相等!'
else
echo '两个数字不相等!'
fi

#for 循环
for loop in 1 2 3 4 5
do
echo "The value is: $loop"
done
#
for str in 'This is a string'
do
echo $str
done

#while 语句
#
int=1
while(( $int<=5 ))
do
echo $int
let "int++"
#let 命令，它用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量
done

#while循环可用于读取键盘信息
echo '按下 <CTRL-D> 退出'
echo -n '输入你最喜欢的网站名: '
while read FILM
do
echo "是的！$FILM 是一个好网站"
done

#无限循环
echo '无限循环'

#while :
#do
#command
#done
#
#
#while true
#do
#command
#done

#或者
#for (( ; ; ))


#until 循环
echo 'until 循环'

#until condition
#do
#command
#done


#case

echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
1)  echo '你选择了 1'
;;
2)  echo '你选择了 2'
;;
3)  echo '你选择了 3'
;;
4)  echo '你选择了 4'
;;
*)  echo '你没有输入 1 到 4 之间的数字'
;;
esac


#   跳出循环

echo '跳出循环 break 和 continue'
while :
do
    echo -n "输入 1 到 5 之间的数字:"
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的! 游戏结束"
        break
        ;;
    esac
done


while :
do
    echo -n "输入 3 到 6 之间的数字: "
    read aNum
    case $aNum in
        3|4|5|6) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 3 到 6 之间的!"
            continue
            echo "游戏结束"
        ;;
    esac
done

#
#esac
#case的语法和C family语言差别很大，
#它需要一个esac（就是case反过来）作为结束标记，
#每个case分支用右圆括号，
#用两个分号表示break。






