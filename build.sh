#|/bin/bash

# This does nothing but call the script with the paramenters I use on a daily basis.
# No other parameters have been tested.
# My aim is to make the cross compilation script defualt to these values, then
# this command line can be discarded.

./cross_compile_ffmpeg_cygwin64.sh --build-ffmpeg-shared=n --build-ffmpeg-static=y --disable-nonfree=n --sandbox-ok=y --build-libmxf=y --build-mp4box=y --build-choice=win64 --cflags=-march=core2 --git-get-latest=y --prefer-stable=n

