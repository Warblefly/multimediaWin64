multimediaWin64
===============

Scripts for building open-source multimedia utilities for Win64 from Cygwin. Includes FFmpeg, sox, MP4Box, raw2bmx, opusenc, lame, cdrtools, exiv2 and many others and their associated libraries. The compiled programs are native Windows 64-bit binaries, and do not require Cygwin libraries.


BACKGROUND
==========

Supporting the cross-compilation of the very versatile FFmpeg utilities under mingw64, Zeranoe and others publish a set of patches and a build script to, first, compile a working mingw64 environment on a POSIX system, then compile a very full FFmpeg and associated libraries and utilities within mingw64 ready for installation on a Windows 64-bit system.

With grateful thanks to Zeranoe and other developers, I have extended this build system for my own purposes. A more comprehensive set of command-line utilities for multimedia work is build on Cygwin64 using my script.

Because this is my own personal build system (Windows 8.1 64-bit with Cygwin64), I have probably severely compromised compatibility with other POSIX-compatible systems e.g. Linux.


HOW TO
======

1.  Install Cygwin64. Make sure you have the facility to build programs using a very recent version of the Gnu Compiler Collection. Currently, I use gcc-4.9.0
2.  Checkout the scripts cross_compile_ffmpeg_cygwin64.sh and build.sh
3.  Make sure they are both executable.
4.  Run ./build.sh
5.  Wait quite a long time.
6.  Copy binaries from ./sandbox/mingw-w64-x86_64/x86_64-w64-mingw32/bin and other files (e.g. ../doc/) as needed
7.  Enjoy and share.
8.  Run the command again to incorporate updates. Only the parts that need rebuilding will be built.

I have tested neither other command lines nor other builds.


THANKS
======

Zeranoe and associated developers. http://zeranoe.com/
The FFmpeg developers. http://ffmpeg.org
The BBC developers behind Ingest and libMXF
Videolan, programmers of x264
The programmers of x265
Creator of SoX. http://sox.sourceforge.net/
Jörg Schilling, writer of cdrtools, smake and other programs
All whose work is incorporated, and I hope I have preserved their licences.


LICENCE
=======

My script, very much derived from others' work, is released under the GNU Affero GPL Version 3 licence. You will find it at the top of this repository. Please adhere to it.

The version of FFmpeg built here is non-redistributable.
