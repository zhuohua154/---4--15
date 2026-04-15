# test_main.py：单元测试代码
import unittest
from main import add, subtract

# 测试类，继承unittest.TestCase
class TestMathFunctions(unittest.TestCase):
    # 测试add函数
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # 正常加法
        self.assertEqual(add(-1, 1), 0) # 正负相加
        self.assertEqual(add(0, 0), 0)  # 零相加
    
    # 测试subtract函数
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2) # 正常减法
        self.assertEqual(subtract(0, 5), -5) # 减大数
    
if __name__ == '__main__':
    unittest.main()