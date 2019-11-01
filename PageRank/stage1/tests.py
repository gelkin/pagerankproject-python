from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class Stage1Test(StageTest):
    def generate(self):
        return [TestCase()]

    def check(self, reply, attach):
        return CheckResult.true()


Stage1Test('pagerank.stage1').run_tests()