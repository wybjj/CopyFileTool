#Copyright(C) 2012-2013 Bai Junjie( wybjj@163.com )
#copyfiles.py verision 0.1

Get The latest version from github: https://github.com/wybjj/CopyFileTool

LICENSE:
This program is free software,
you can use this file under the GNU General Public License(GPL) published by the Free Software Foundation, 
version 3 or later of the GPL license is optional.
You can view The full GPL license here: http://www.gnu.org/licenses/gpl.html.

NOTICE:
The files in test directory is not part of the project and may not licensed under GPL, you can use these files for test this tool. but it can't be used in other project, unless you get another license of these files.

CHANGE LOG:
#01/18/2012 create by Bai Junjie( wybjj@163.com )
#06/10/2013 published under GPL license by Bai Junjie( wybjj@163.com )

copyfiles.py USAGE:
    Use this tool to copy files described in copyfiles.ini. The tool allows you to copy one file to multiple targets and also allows you to define you own copy commond. Use configuration file copyfiles.ini to describe which and how files will be copy.

copyfiles.ini file USAGE:
    This File is the configuration file( ini file ) of copyfiles.py. Use this ini file to describe which and how files will be copy. The tool allows you to copy one file to multiple target files. The format of this ini file follows the python ini file formart. Use '#' to comment a line. Section and it's options must have the same indentation, always we begins start of the line.
		
    The section [common] is the default section which defines global variants. These global variants can be used int other section like ¡°%(var)s¡±. 
	
    Every file which will be copy need to define a section mark between '[' and ']'.  These sections must have "src_file" and "des_files" option. "src_file" defines the source file which will be copy. Every section has only one source file. "des_files" optin defines the target files list. More then one target files is allowed, every line one target file. Every target must have indentation with the "des_files" text. "commond" is a optional option which defines the custom commond used to copy file. If no "commond" option, the source file will be copied use default copy commond. When define a custom commond, you can use "{src_file}" to mark the source file and "{des_file}" to mark the tatget file as the parameters of your custom commond. "enable" is another optional option, when true file copies, when false the section does nothing.