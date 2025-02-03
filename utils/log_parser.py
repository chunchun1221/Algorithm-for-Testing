import re
from datetime import datetime, timedelta
from collections import deque


class LogParser:
    """
    日志分析工具 - 基于滑动窗口检测异常模式

    功能：
    1. 检测固定时间窗口内的错误码频率
    2. 识别连续出现的异常事件

    示例：
    >>> parser = LogParser(time_window=300, error_code='500', threshold=3)
    >>> parser.add_log('[2024-02-01 12:00:00] GET /api 500')
    >>> parser.add_log('[2024-02-01 12:01:00] GET /api 500')
    >>> parser.add_log('[2024-02-01 12:02:00] GET /api 500')
    >>> parser.check_alert()
    True  # 触发告警
    """

    def __init__(self, time_window: int, error_code: str, threshold: int):
        """
        :param time_window: 时间窗口长度（秒）
        :param error_code: 监控的错误码
        :param threshold: 触发告警的阈值（窗口内允许的最大次数）
        """
        self.time_window = time_window
        self.error_code = error_code
        self.threshold = threshold
        self.window = deque()  # 窗口队列，保存(时间戳, 错误码)

    def _parse_log(self, log: str) -> tuple:
        """解析单条日志，提取时间和错误码"""
        # 示例日志格式: [2024-02-01 12:00:00] GET /api 500
        time_part, _, _, code = re.split(r'\s+', log.strip(), maxsplit=3)
        time_str = time_part[1:-1]  # 去除方括号
        timestamp = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").timestamp()
        return timestamp, code

    def add_log(self, log: str):
        """添加日志到分析窗口"""
        timestamp, code = self._parse_log(log)
        if code == self.error_code:
            self.window.append((timestamp, code))
            self._slide_window(timestamp)

    def _slide_window(self, current_time: float):
        """滑动窗口，移除超出时间范围的日志"""
        while self.window and current_time - self.window[0][0] > self.time_window:
            self.window.popleft()

    def check_alert(self) -> bool:
        """检查当前窗口是否触发告警"""
        return len(self.window) >= self.threshold

    @classmethod
    def from_file(cls, file_path: str, **kwargs):
        """从文件加载日志并初始化分析器"""
        parser = cls(**kwargs)
        with open(file_path, 'r') as f:
            for line in f:
                parser.add_log(line)
        return parser


# 示例用法
if __name__ == "__main__":
    # 场景：监控5分钟内出现3次500错误
    parser = LogParser(time_window=300, error_code='500', threshold=3)
    logs = [
        '[2024-02-01 12:00:00] GET /api 500',
        '[2024-02-01 12:01:00] GET /api 500',
        '[2024-02-01 12:02:00] GET /api 500'
    ]
    for log in logs:
        parser.add_log(log)
    print("是否触发告警:", parser.check_alert())  # 输出: True