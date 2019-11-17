import numpy as np

from hstest.stage_test import *


class Stage4Test(StageTest):
    def generate(self) -> List[TestCase]:
        return [
            TestCase(
                stdin="3 0.15\n0.333 0.000 0.500\n0.333 1.000 0.000\n0.333 0.000 0.500",
                attach=("Doesn't return correct result on a network of 3 nodes.", "32.375 35.231 32.375")
            ),
            TestCase(
                stdin="10 0.5\n0.100 0.100 0.000 0.100 0.500 0.000 0.500 0.000 0.100 0.000\n0.100 0.100 0.000 0.100 0.000 0.000 0.000 0.000 0.100 0.000\n0.100 0.100 1.000 0.100 0.000 0.000 0.500 0.500 0.100 0.000\n0.100 0.100 0.000 0.100 0.000 0.000 0.000 0.000 0.100 0.000\n0.100 0.100 0.000 0.100 0.500 0.000 0.000 0.000 0.100 0.000\n0.100 0.100 0.000 0.100 0.000 0.500 0.000 0.000 0.100 0.000\n0.100 0.100 0.000 0.100 0.000 0.500 0.000 0.000 0.100 0.000\n0.100 0.100 0.000 0.100 0.000 0.000 0.000 0.500 0.100 1.000\n0.100 0.100 0.000 0.100 0.000 0.000 0.000 0.000 0.100 0.000\n0.100 0.100 0.000 0.100 0.000 0.000 0.000 0.000 0.100 0.000\n",
                attach=("Doesn't return correct result on a network of 10 nodes.", "10.870 6.522 23.910 6.522 8.696 8.696 8.696 13.044 6.522 6.522")
            ),
            TestCase(
                stdin="20 0.6\n0.050 0.000 0.000 0.000 0.250 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 1.000 1.000 0.000 0.000 0.000 0.000 0.250 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 1.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 1.000 0.250 0.000 0.500 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.500 0.000 0.500 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.250 0.000 0.000 0.250 0.000 0.000 0.333 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.250 0.000 0.500 0.000 0.500 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.500 0.333 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.250 0.500 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.250 0.000 0.000 0.000 0.000 0.000 0.333 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.500 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 1.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 1.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 1.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000\n0.050 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.050 0.050 0.000 0.050 0.000 0.050 0.050 0.000",
                attach=("Doesn't return correct result on a network which has more than 10 nodes.", "3.798 12.954 2.725 2.725 7.148 7.369 6.454 5.509 5.973 2.725 4.428 5.344 4.682 4.329 5.342 5.931 4.360 2.725 2.725 2.725")
            )
        ]

    def check(self, reply, attach) -> CheckResult:
        feedback, ans = attach
        true_res = ans.split()
        n = len(true_res)
        res = reply.split()
        if len(res) != n:
            return CheckResult.false("Your program should contain a page rank vector of size " + str(n) + ".")
        pr = []
        for i in range(n):
            try:
                el = float(res[i])
            except ValueError:
                return CheckResult.false("Your program outputted something which is not a number!")
            pr.append(el)
        pr_true = []
        for i in range(n):
            el = float(true_res[i])
            pr_true.append(el)
        eps = 1e-1
        for i in range(n):
            if abs(pr[i] - pr_true[i]) > eps:
                return CheckResult.false(feedback)
        return CheckResult.true()


Stage4Test('pagerank.stage4').run_tests()