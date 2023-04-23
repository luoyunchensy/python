import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 指定字体路径
font_path = '/Library/Fonts/YouSheShaYuFeiTeJianKangTi-2.ttf'

# 从字体文件中读取字体信息，并设置为默认字体
plt.rcParams['font.family'] = FontProperties(fname=font_path).get_name()

# 测试中文显示
plt.title('你好，世界')
plt.show()
