from erictome_cicd_databricks_aws.jobs.sample.small_function import square
import unittest

def test_square():
    assert square(3)==9


    