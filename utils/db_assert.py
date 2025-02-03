import sqlite3
from contextlib import contextmanager
from typing import List, Tuple, Any


class DBAssert:
    """
    数据库断言工具

    功能：
    1. 执行SQL查询并返回结果
    2. 断言查询结果是否符合预期

    示例：
    >>> db = DBAssert('test.db')
    >>> expected = [('IT', 'Alice', 90000)]
    >>> db.assert_query(
    ...     "SELECT d.name, e.name, e.salary FROM Employee e JOIN Department d ON e.departmentId = d.id",
    ...     expected
    ... )
    """

    def __init__(self, db_path: str):
        self.db_path = db_path

    @contextmanager
    def _get_connection(self):
        """上下文管理器，自动处理数据库连接"""
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def execute_query(self, query: str) -> List[Tuple[Any]]:
        """执行SQL查询并返回结果"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    def assert_query(self, query: str, expected: List[Tuple], order_matters: bool = False):
        """
        断言查询结果是否匹配预期
        :param order_matters: 是否检查结果顺序（默认不检查）
        """
        actual = self.execute_query(query)
        actual_sorted = sorted(actual) if not order_matters else actual
        expected_sorted = sorted(expected) if not order_matters else expected

        assert actual_sorted == expected_sorted, \
            f"断言失败！\n实际结果: {actual}\n预期结果: {expected}"


# 示例用法
if __name__ == "__main__":
    # 初始化测试数据
    with sqlite3.connect('test.db') as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Department(id INT, name TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS Employee(id INT, name TEXT, salary INT, departmentId INT)")
        cursor.execute("INSERT INTO Department VALUES (1, 'IT'), (2, 'HR')")
        cursor.execute(
            "INSERT INTO Employee VALUES (1, 'Alice', 90000, 1), (2, 'Bob', 80000, 1), (3, 'Charlie', 80000, 2)")
        conn.commit()

    # 验证部门最高工资
    db = DBAssert('test.db')
    expected_result = [('IT', 'Alice', 90000), ('HR', 'Charlie', 80000)]
    db.assert_query("""
        SELECT d.name, e.name, e.salary 
        FROM Employee e 
        JOIN Department d ON e.departmentId = d.id
        WHERE (e.departmentId, e.salary) IN (
            SELECT departmentId, MAX(salary) 
            FROM Employee 
            GROUP BY departmentId
        )
    """, expected_result)
    print("数据库断言测试通过！")