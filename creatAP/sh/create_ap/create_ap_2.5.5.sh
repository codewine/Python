#!/bin/bash
dirname=`dirname $0`
tmp="${dirname#?}"

if [ "${dirname%$tmp}" != "/" ]; then
dirname=$PWD/$dirname
fi
cd $dirname

wan=`sudo ifconfig|grep "^wl"|cut -d':' -f1`
lan=`sudo ifconfig|grep "^en"|cut -d':' -f1`
ppp=`sudo ifconfig|grep "^ppp"|cut -d':' -f1`
#======================================

#======================================
sudo apt-get install ethtool
clear
echo 1.网卡及驱动信息
echo 网卡信息：
sudo lspci -vvnn | grep Network
echo 
echo 驱动信息：
sudo ethtool -i $wan|grep "^driver"
sudo ethtool -i $wan|grep "^version"
echo 
echo 下一行有“* AP”字样说明支持AP，如果没有，考虑是不是网卡驱动不对。
sudo iw list|grep -E "^* AP$"
echo 
echo 
echo ======================================
echo 打开下面的网址，查看AP模式支持的驱动列表里的查找网卡芯片以及驱动，查看AP项为yes的，证明支持AP。
echo http://wireless.kernel.org/en/users/Drivers
echo 
echo 同一网卡芯片可能会有几个驱动可用，但某些版本的驱动可能不支持AP，如果当前驱动不支持，可以试试网卡芯片可用的其它驱动。
echo 
echo 如果确认支持AP，请按任意键继续安装hostapd和create_ap。
read -n 1
#======================================
clear
echo 安装hostapd……
sudo apt-get install hostapd dnsmasq haveged iptables


sudo create_ap --stop $wan
  if (( $? )); then

    clear
    echo 安装git……
    sudo apt-get install git

    clear
    echo 安装create_ap……
    git clone https://github.com/oblique/create_ap
    cd create_ap
    sudo make install

    cd $dirname
    sudo rm -r create_ap
fi


clear
echo 2.网络接口查询
echo 无线网卡接口\：$wan
echo 有线网卡接口\：$lan
echo 宽带接口\：$ppp
echo 
echo 3.不可用信道查询
echo 建AP时不能用以下信道！若是共享连接的WiFi，WiFi也不能是以下信道，否则开启会失败：
sudo iw list|grep "(no IR)"|cut -d' ' -f4
sudo iw list|grep "(disabled)"|cut -d' ' -f4
echo 
echo 4.创建快捷方式
#-------------------------------
cd $dirname
sudo cp ./ico/ap_start.png /usr/share/icons/hicolor/scalable/apps/ap_start.png
sudo cp ./ico/ap_stop.png /usr/share/icons/hicolor/scalable/apps/ap_stop.png

#-------------------------------
cat <<  EOF > ./ap-wlan.desktop
[Desktop Entry]
Categories=System;
Type=Application
Icon=ap_start

Name=ap-wlan.desktop
Comment=creat ap-wlan
Name[zh_CN]=热点-无线.desktop
Comment[zh_CN]=创建热点-无线
EOF
echo Exec=gksudo \"create_ap $wan $wan Deepin_AP 123456789\" >>./ap-wlan.desktop

#-------------------------------
cat <<  EOF > ./ap-lan.desktop
[Desktop Entry]
Categories=System;
Type=Application
Icon=ap_start

Name=ap-lan.desktop
Comment=creat ap-lan
Name[zh_CN]=热点-有线.desktop
Comment[zh_CN]=创建热点-有线
EOF
echo Exec=gksudo \"create_ap $wan $lan Deepin_AP 123456789\" >>./ap-lan.desktop

#-------------------------------
cat <<  EOF > ./ap-ppp.desktop
[Desktop Entry]
Categories=System;
Type=Application
Icon=ap_start

Name=ap-ppp.desktop
Comment=creat ap-ppp
Name[zh_CN]=热点-宽带.desktop
Comment[zh_CN]=创建热点-宽带
EOF
echo Exec=gksudo \”create_ap $wan $ppp Deepin_AP 123456789\“ >>./ap-ppp.desktop

#-------------------------------
cat <<  EOF > ./ap-wlan-stop.desktop
[Desktop Entry]
Categories=System;
Type=Application
Icon=ap_stop

Name=ap-stop.desktop
Comment=stop ap
Name[zh_CN]=关闭热点.desktop
Comment[zh_CN]=关闭热点
EOF
echo Exec=gksudo \"create_ap --stop $wan\" >>./ap-wlan-stop.desktop

echo 
echo 完成！
read -n 1
#-------------------------------
create_ap
echo 
echo 任意键退出
read -n 1

exit
#======================================
echo 5.输出示例
clear
cat <<  EOF > ./ap_create_示例.txt
## 示例
### 无密码 (开放网络):
create_ap wlan0 eth0 MyAccessPoint

### WPA + WPA2 密码:
create_ap wlan0 eth0 MyAccessPoint MyPassPhrase

### AP 无Internet访问:
create_ap -n wlan0 MyAccessPoint MyPassPhrase

### 桥接共享 Internet:
create_ap -m bridge wlan0 eth0 MyAccessPoint MyPassPhrase

### 桥接共享 Internet (预配置桥接接口):
create_ap -m bridge wlan0 br0 MyAccessPoint MyPassPhrase

### 同一WiFi接口共享 Internet:
create_ap wlan0 wlan0 MyAccessPoint MyPassPhrase

### 选择不同的 WiFi 适配器驱动
create_ap --driver rtl871xdrv wlan0 eth0 MyAccessPoint MyPassPhrase

### 无密码 (开放网络) 使用 pipe:
echo -e "MyAccessPoint" | create_ap wlan0 eth0

### WPA + WPA2 密码 使用 pipe:
echo -e "MyAccessPoint MyPassPhrase" | create_ap wlan0 eth0

### 启用 IEEE 802.11n
create_ap --ieee80211n --ht_capab '[HT40+]' wlan0 eth0 MyAccessPoint MyPassPhrase

### Client Isolation:
create_ap --isolate-clients wlan0 eth0 MyAccessPoint MyPassPhrase

## 系统服务
Using the persistent [systemd](https://wiki.archlinux.org/index.php/systemd#Basic_systemctl_usage) service

### 启动系统服务:
systemctl start create_ap

### 开机自启:
systemctl enable create_ap

## License
FreeBSD
EOF
