import numpy as np

from hstest.stage_test import *


class Stage1Test(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase()]

    def check(self, reply, attach) -> CheckResult:
        res = reply.split()
        if len(res) != (36 + 6):
            return CheckResult.false("Your program should output a matrix and a page rank so 42 numbers")
        n = 6
        L = np.array([[0, 1 / 2, 1 / 3, 0, 0, 0],
                      [1 / 3, 0, 0, 0, 1 / 2, 0],
                      [1 / 3, 1 / 2, 0, 1, 0, 1 / 2],
                      [1 / 3, 0, 1 / 3, 0, 1 / 2, 1 / 2],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 1 / 3, 0, 0, 0]])
        user_l = []
        for i in range(n):
            row = []
            for j in range(n):
                try:
                    el = float(res[i * n + j])
                except ValueError:
                    return CheckResult.false("Your program outputted something which is not a number!")
                row.append(el)
            user_l.append(row)
        user_np_l = np.array(user_l)
        if np.allclose(L, user_np_l):
            return CheckResult.false("The matrix you outputted is incorrect.")
        r = []
        for i in range(n):
            try:
                el = float(res[n * n + i])
            except ValueError:
                return CheckResult.false("Your program outputted something which is not a number!")
            r.append(el)
        true_r = [16.000, 5.333, 40.000, 25.333, 0.000, 13.333]
        for i in range(n):
            if abs(r[i] - true_r[i]) > 1e-3:
                return CheckResult.false("The page rank you outputted is incorrect.")
        return CheckResult.true()


Stage1Test('pagerank.stage1').run_tests()
