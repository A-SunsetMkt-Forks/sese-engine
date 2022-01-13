# 注释的内容都是加大这些参数的情况下的变化

单键最多url = 10000  # 增加多关键词查找能力，增加硬盘消耗，略微降低爬取效率
单键内存最多url = 400  # 增加爬取效率，增大峰值内存消耗
单键最多相同域名url = 20  # 增加有效结果的相关性，减少有效结果数量
大清洗间隔 = 130000  # 稍微增加爬取效率，增大峰值内存消耗

爬虫的名字 = 'loli_tentacle'
爬取线程数 = 22 # 增加爬取效率，增加网络和CPU消耗
单网页最多关键词 = 200

使用在线摘要 = True  # 增加搜索结果信息的可读性，增加搜索时间
在线摘要限时 = 3  # 减少信息不完整的搜索结果数量，增加搜索时间

存储位置 = './savedata'  # 代码里还没加上，等等再改……
