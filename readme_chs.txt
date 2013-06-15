#版权所有(C) 2012-2013 白俊杰( wybjj@163.com )
#copyfiles.py verision 0.1

从github获取最新版本: https://github.com/wybjj/CopyFileTool

许可协议:
本工具是自由软件，可以在GNU General Public License(GPL)第三版的许可下使用。许可协议原文请参考：http://www.gnu.org/licenses/gpl.html.

特别注意：
test目录下的文件，不属于本项目，也可能不在GPL协议许可下。您可以使用那些文档来测试本工具，但若没有特别许可请不要用作其他用途。

修改记录:
	#01/18/2012 白俊杰（wybjj@163.com）  创建本工具
	#06/10/2013 白俊杰（wybjj@163.com ） 在GPL许可协议下发布本工具

用法:
	本工具用于拷贝文件，通过配置copyfiles.ini，可以拷贝一个文件到多个路径，也允许使用自定义拷贝命令。配置文件copyfiles.ini描述了拷贝哪些文件，及文件如何拷贝。

copyfiles.ini 配置文件说明：
	配置文件中的注释以“#”号开头。段和段内的选项要有相同的缩进，一般都顶格开始。
	[common]段为默认段，[common]段内定义全局通用的变量。其他段可以用%(var)s的形式引用[common]段内定义的变量var。
	每一个需要拷贝的文件占用一个段，段用[]号标记单独一行。需要拷贝的段内必须具备src_file和des_files选项。src_file的值为源文件的路径。每个段只能有一个源文件。des_files选项的值为目标文件列表，可以有多个目标文件，每行只能列出一个，各行必须较des_files有缩进。commond是普通段内的一个可选选项，没有指定commond选项时，直接拷贝源文件，指定了commond选项后，执行commond命令完成自定义拷贝。commond命令参数中需要用到用来拷贝的源文件时以{src_file}标记，用到被拷贝的目标文件时以{des_file}标记。enable是另一个可选选项，bool型，默认为true执行拷贝，false时跳过所在段的拷贝