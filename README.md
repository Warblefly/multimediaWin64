multimediaWin64
===============

Scripts for building open-source multimedia utilities for Win64 from Cygwin. Includes FFmpeg, sox, MP4Box, raw2bmx, opusenc, lame and many others and their associated libraries.


BACKGROUND
==========

Supporting the cross-compilation of the very versatile FFmpeg utilities under mingw64, Zeranoe and others publish a set of patches and a build script to, first, compile a working mingw64 environment on a POSIX system, then compile a very full FFmpeg and associated libraries and utilities within mingw64 ready for installation on a Windows 64-bit system.

With grateful thanks to Zeranoe and other developers, I have extended this build system for my own purposes. A more comprehensive set of command-line utilities for multimedia work is build on Cygwin64 using my script.

Because this is my own personal build system, I have probably severely compromised compatibility with other POSIX-compatible systems e.g. Linux.


HOW TO
======

1.  Install Cygwin64. Make sure you have the facility to build programs using a very recent version of the Gnu Compiler Collection. I will add specifics later.
2.  Checkout the script cross_compile_ffmpeg_cygwin.sh
3.  Make sure it is executable.
4.  Run it with this command line:
    ./cross_compile_ffmpeg_cygwin64.sh --build-ffmpeg-shared=n --build-ffmpeg-static=y --disable-nonfree=n --sandbox-ok=y --build-libmxf=y --build-mp4box=y --build-choice=win64 --cflags=-march=core2 --git-get-latest=y --prefer-stable=n
5.  Copy binaries from ./sandbox/mingw-w64-x86_64/x86_64-w64-mingw32/bin
6.  Enjoy and share.
7.  Run the command again to incorporate updates. Only the parts that need rebuilding will be built.

I have tested neither other command lines nor other builds.


TO DO
=====

I should hard-encode that command line.


THANKS
======

Zeranoe and associated developers. http://zeranoe.com/
The FFmpeg developers. http://ffmpeg.org
The BBC developers behind Ingest and libMXF
Videolan, programmers of x264
The programmers of x265
Creator of SoX. http://sox.sourceforge.net/
Many others.


LICENCE
=======

My script is released under the GNU Affero GPL Version 3 licence. You will find it at the top of this repository. Please adhere to it.

