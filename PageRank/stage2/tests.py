import numpy as np

from hstest.stage_test import *


class Stage1Test(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase()]

    def check(self, reply, attach) -> CheckResult:
        res = reply.split()
        if len(res) != (6 + 6 + 6):
            return CheckResult.false("Your program should output three page rank vectors so 18 numbers")
        n = 6
        L = np.array([[0, 1 / 2, 1 / 3, 0, 0, 0],
                      [1 / 3, 0, 0, 0, 1 / 2, 0],
                      [1 / 3, 1 / 2, 0, 1, 0, 1 / 2],
                      [1 / 3, 0, 1 / 3, 0, 1 / 2, 1 / 2],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 1 / 3, 0, 0, 0]])
        pr_iter1 = [13.889, 13.889, 38.889, 27.778, 0.000, 5.556]
        pr_iter100 = [16.000, 5.333, 40.000, 25.333, 0.000, 13.333]
        pr_precision = [15.998, 5.334, 40.003, 25.334, 0.000, 13.331]
        eps = 1e-2
        # 1
        pr = []
        for i in range(n):
            try:
                el = float(res[i])
            except ValueError:
                return CheckResult.false("Your program outputted something which is not a number!")
            pr.append(el)
        for i in range(n):
            if abs(pr[i] - pr_iter1[i]) > eps:
                return CheckResult.false("The first Page Rank you outputted is incorrect.")
        # 2
        for i in range(n):
            try:
                pr[i] = float(res[n + i])
            except ValueError:
                return CheckResult.false("Your program outputted something which is not a number!")
        for i in range(n):
            if abs(pr[i] - pr_iter100[i]) > eps:
                return CheckResult.false("The second Page Rank you outputted is incorrect.")
        # 3
        for i in range(n):
            try:
                pr[i] = float(res[2 * n + i])
            except ValueError:
                return CheckResult.false("Your program outputted something which is not a number!")
        for i in range(n):
            if abs(pr[i] - pr_precision[i]) > eps:
                return CheckResult.false("The third Page Rank you outputted is incorrect.")
        return CheckResult.true()


Stage1Test('pagerank.stage2').run_tests()
