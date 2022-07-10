
import main as n
import logging as log
import sys
import os
import shutil

test_data = ''


def main():
    log.warning(2222)
    n.directory_path = test_data
    n.main()



if __name__ == '__main__':
    # unittest.TestCase.assertPrints(sys.argv)
    w_dir = os.path.dirname(sys.argv[0])
    b_path = os.path.join(w_dir, 'test_data')
    w_dir_orig = os.path.join(b_path, 'origs')
    w_dir_dst = os.path.join(b_path, 'tests')
    shutil.copytree(w_dir_orig, w_dir_dst)
    test_data = w_dir_dst
    log.warning(1111)
    log.error("Some error message.")
    main()
