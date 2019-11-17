import numpy as np

from hstest.stage_test import *


class Stage1Test(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase()]

    def check(self, reply, attach) -> CheckResult:
        res = reply.split()
        if len(res) != (7 * 7 + 7 + 7):
            return CheckResult.false("Your program should contain a matrix and two page rank vectors so 63 numbers (7 * 7 + 7 + 7)")
        n = 7
        L2 = np.array([[0, 1 / 2, 1 / 3, 0, 0, 0, 0],
                       [1 / 3, 0, 0, 0, 1 / 2, 0, 0],
                       [1 / 3, 1 / 2, 0, 1, 0, 1 / 3, 0],
                       [1 / 3, 0, 1 / 3, 0, 1 / 2, 1 / 3, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1 / 3, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1 / 3, 1]])
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
        if np.allclose(L2, user_np_l):
            return CheckResult.false("The matrix you outputted is incorrect.")
        pr_wo_damp = [0.033, 0.012, 0.078, 0.049, 0.000, 0.027, 99.801]
        pr_with_damp = [13.682, 11.209, 22.420, 16.759, 7.143, 10.880, 17.907]
        eps = 1e-2
        # wo damping
        pr = []
        for i in range(n):
            try:
                el = float(res[n * n + i])
            except ValueError:
                return CheckResult.false("Your program outputted something which is not a number!")
            pr.append(el)
        for i in range(n):
            if abs(pr[i] - pr_wo_damp[i]) > eps:
                return CheckResult.false("The first Page Rank you outputted is incorrect.")
        # with damping
        for i in range(n):
            try:
                pr[i] = float(res[n * n + n + i])
            except ValueError:
                return CheckResult.false("Your program outputted something which is not a number!")
        for i in range(n):
            if abs(pr[i] - pr_with_damp[i]) > eps:
                return CheckResult.false("The second Page Rank you outputted is incorrect.")
        return CheckResult.true()


Stage1Test('pagerank.stage3').run_tests()