FILE_NAME = "data.xls"
TARGET_FILENAME = "db.xls"

# 开始爬虫的行数
START_INDEX = 8100
SUBMIT_INDEX = 3

# excel带写入信息
TYPE2INDEX = {'编号': 0,
         '公开（公告）号': 1,
         '公开（公告）日': 2,
         '申请号': 3,
         '申请日': 4,
         '申请年': 5,
         '授权与否': 6,
         '名称': 7,
         '主分类号': 8,
         '分类号': 9,
         '申请（专利权）人': 10,
         '发明（设计）人': 11,
         '地址': 12,
         '国省代码': 14,
         'IPC': 15,
         'co-app': 16,
         'co-inv': 17,
         '同族': 18,
         '引证': 19,
         '被引': 20,
         '实质审查的生效': 21,
         '专利权的终止': 22,
         '权利要求数': 23,
         '专利申请或者专利权的恢复': 24,
         '专利实施许可合同备案的生效、变更及注销': 25,
         '专利权人的姓名或者名称、地址的变更': 26,
         '专利申请权、专利权的转移': 27,
         '著录事项变更': 28,
         '发明专利申请更正': 29,
         '发明专利公报更正': 30,
         '地址不明的通知': 31,
         '专利权的质押、保全及解除': 32,
         '实施许可合同的备案': 33,
         '专利权的保全及其解除': 34
}