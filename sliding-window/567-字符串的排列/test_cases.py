import pytest
from solution import check_inclusion

def test_error_log_monitoring():
    # 场景：检测日志中连续3次"ERROR 404"
    logs = ["INFO 200", "ERROR 404", "ERROR 404", "ERROR 404", "INFO 200"]
    s1 = "ERROR 404" * 3  # 目标模式
    s2 = "".join(logs)     # 模拟日志流
    assert check_inclusion(s1, s2) == True  # 应触发告警

def test_api_health_check():
    # 场景：接口健康检测（连续5次心跳正常）
    s1 = "OK" * 5
    s2 = "OKOKOKOKOK"
    assert check_inclusion(s1, s2) == True