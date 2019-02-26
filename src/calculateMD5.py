from lib.md5 import CalculateMD5
from conf.config import SVN_PATH, CODOWN_PATH


def calculate(path_1, path_2):
    m1 = CalculateMD5(path_1)
    m1.calculate()
    m2 = CalculateMD5(path_2)
    m2.calculate()

    # print(m1.nums, m1.file_dict)
    # print(m2.nums, m2.file_dict)

    m1_diff_m2 = set([key for key in m1.file_dict.keys()]) - set([key for key in m2.file_dict.keys()])
    m2_diff_m1 = set([key for key in m2.file_dict.keys()]) - set([key for key in m1.file_dict.keys()])

    if not (m1_diff_m2 or m2_diff_m1):
        print('Success!')
    else:
        print('Faild')
        tmp1 = [(m1.file_dict[md5], md5) for md5 in m1_diff_m2]
        tmp2 = [(m2.file_dict[md5], md5) for md5 in m2_diff_m1]
        if len(tmp1) == len(tmp2):
            pass
        elif len(tmp1) > len(tmp2):
            print("[{}] files num more than [{}] files num.".format(m1.path, m2.path))
        else:
            print('[{}] files num more than [{}] files num.'.format(m2.path, m1.path))
        print(tmp1)
        print(tmp2)




if __name__ == '__main__':
    calculate(SVN_PATH, CODOWN_PATH)
