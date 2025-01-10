import sys
import unittest
import importlib.util
import os
import time
from zipfile import ZipFile
from pyzipper import AESZipFile

import zz

# 构建文件路径
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
file_path = os.path.join(parent_dir, "zz.py")

# 加载模块
spec = importlib.util.spec_from_file_location(".", file_path)
file_in_parent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(file_in_parent)

zzCrack = zz.zzCrack()


# 10kb_1.zip - pwd
# 10kb_2.zip - pass
# 10kb_3.zip - pwd  - AES encrypted
# 10kb_4.zip - pass - AES encrypted

class TestZzCrack(unittest.TestCase):
    def test_bruteforce_1(self):
        start_time = time.time()
        zip_file = ZipFile("10kb_1.zip", "r")
        ret = zzCrack.bruteforce_crack(0, zip_file, False, "0", 3)
        elapsed_time = time.time() - start_time
        self.assertEqual(ret, 'pwd')
        print(f"Cost time: {elapsed_time:.3f} seconds")

    def test_bruteforce_1_mp(self):
        start_time = time.time()
        ret = zzCrack.bruteforce_crack_mp(0, "10kb_1.zip", ZipFile, False, "0", 3)
        elapsed_time = time.time() - start_time
        self.assertEqual(ret, 'pwd')
        print(f"Cost time: {elapsed_time:.3f} seconds")

    def test_bruteforce_2(self):
        start_time = time.time()
        zip_file = ZipFile("10kb_2.zip", "r")
        ret = zzCrack.bruteforce_crack(0, zip_file, False, "0", 4)
        elapsed_time = time.time() - start_time
        self.assertEqual(ret, 'pass')
        print(f"Cost time: {elapsed_time:.3f} seconds")

    def test_bruteforce_2_mp(self):
        start_time = time.time()
        ret = zzCrack.bruteforce_crack_mp(0, "10kb_2.zip", False, "0", 4)
        elapsed_time = time.time() - start_time
        self.assertEqual(ret, 'pass')
        print(f"Cost time: {elapsed_time:.3f} seconds")

    def test_bruteforce_3(self):
        start_time = time.time()
        zip_file = AESZipFile("10kb_3.zip", "r")
        ret = zzCrack.bruteforce_crack(0, zip_file, False, "0", 4)
        elapsed_time = time.time() - start_time
        self.assertEqual(ret, 'pwd')
        print(f"Cost time: {elapsed_time:.3f} seconds")