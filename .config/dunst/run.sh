#!/bin/sh

killall dunst
dunst &
notify-send "Lorem" "Ipsum dolor sit amet." -u $1