import matplotlib.font_manager as fm
import urllib.request



# 将字体文件拷贝到字体目录
font_dir = fm.fontManager.ttflist[0].font.dirname
font_path = font_dir + '/' + font_file
import shutil
shutil.copy(font_file, font_path)

# 查看是否安装成功
font_list = fm.findSystemFonts()
for font in font_list:
    if 'MengNaManHuaTi' in font:
        print('字体安装成功！')
        break
else:
    print('字体安装失败，请检查字体目录。')
