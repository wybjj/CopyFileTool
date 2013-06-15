#Copyright(C) 2012-2013 Bai Junjie( wybjj@163.com )
#copyfiles.py verision 0.1
#Get The latest version: https://github.com/wybjj/CopyFileTool

'''
USAGE:
Use this tool to copy files described in copyfiles.ini. 
The tool allows you to copy one file to multiple targets and also allows you to define you own copy commond.
Use configuration file copyfiles.ini to describe which and how files will be copy.

LICENSE:
This program is free software,
you can use this file under the GNU General Public License(GPL) published by the Free Software Foundation, 
version 3 or later of the GPL license is optional.
You can view The full GPL license here: http://www.gnu.org/licenses/gpl.html.

CHANGE LOG:
#01/18/2012 create by Bai Junjie( wybjj@163.com )
#06/10/2013 published under GPL license by Bai Junjie( wybjj@163.com )
'''
import configparser
import os, configparser, shutil
conf = configparser.ConfigParser()
conf.default_section = 'common'
conf.read( 'copyfiles.ini' )
for sec in conf.sections() :
    copySec = conf.has_option( sec, 'src_file' ) and conf.has_option( sec, 'des_files' )
    if conf.has_option( sec, 'enable' ) and not conf.getboolean( sec , 'enable') :
        copySec = False
    src_file = None
    #check src_file
    if copySec :
        print( 'now process section ' + sec )
        src_file = conf[sec]['src_file']
        if copySec and not os.path.exists( src_file ) :
            print( 'source file ' + src_file + ' not exists.' )
            copySec = False
        if copySec and not os.path.isfile( src_file ) :
            print( 'source file ' + src_file + ' is not a file.' )
            copySec = False
    copyCount = 0
    if copySec :
        print( 'now replace files with ' + src_file )
        des_fiels = conf[sec]['des_files']
        for file in des_fiels.rsplit( '\n' ) :
            if len(file) > 0 :
                #copy file or use custom commond
                if not conf.has_option( sec, 'commond' ) :
                    shutil.copy2( src_file, file )
                    print( "copy file to " + file )
                    copyCount = copyCount + 1
                else :
                    cmdf = conf[sec]['commond']
                    cmd = cmdf.format( src_file = src_file, des_file = file )
                    print( cmd )
                    if len( cmdf ) > 0 :
                        os.system( cmd )
input("press return to exit..." )

    

