#!/bin/sh
image_sign=`cat /etc/config/image_sign`
TELNETD=`rgdb -g /sys/telnetd`
if [ "$TELNETD" = "true" ]; then
	echo "Start telnetd ..." > /dev/console
	if [ -f "/usr/sbin/login" ]; then
		lf=`rgdb -i -g /runtime/layout/lanif`
		telnetd -l "/usr/sbin/login" -u Alphanetworks:$image_sign -i $lf &
	else
		telnetd &
	fi
fi
