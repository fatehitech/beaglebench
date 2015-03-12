cat <<EOF > /etc/default/capemgr
#Docs: http://elinux.org/Beagleboard:U-boot_partitioning_layout_2.0

uname_r=3.8.13-bone70
#dtb=
cmdline=quiet init=/lib/systemd/systemd

##Example
#cape_disable=capemgr.disable_partno=
#cape_enable=capemgr.enable_partno=

##Enable UART1 and UART2
cape_enable=capemgr.enable_partno=BB-UART1,BB-UART2

##Disable HDMI/eMMC
#cape_disable=capemgr.disable_partno=BB-BONELT-HDMI,BB-BONELT-HDMIN,BB-BONE-EMMC-2G

##Disable HDMI
#cape_disable=capemgr.disable_partno=BB-BONELT-HDMI,BB-BONELT-HDMIN

##Disable eMMC
#cape_disable=capemgr.disable_partno=BB-BONE-EMMC-2G

##Audio Cape (needs HDMI Audio disabled)
#cape_disable=capemgr.disable_partno=BB-BONELT-HDMI
#cape_enable=capemgr.enable_partno=BB-BONE-AUDI-02


##enable BBB: eMMC Flasher:
##make sure, these tools are installed: dosfstools rsync
#cmdline=init=/opt/scripts/tools/eMMC/init-eMMC-flasher-v3.sh
EOF
