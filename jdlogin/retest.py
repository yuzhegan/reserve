# encoding='utf-8

# @Time: 2023-10-24
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import re

str1 = 'var _jdtdmap_sessionId = "562847547574216884";'

# str2 = re.findall(r'_jdtdmap_sessionId = \"(.+?)\"', str1)[0]
str2 = re.search(r'_jdtdmap_sessionId = \"(.+?)\"', str1).group(1)
print(str2)
