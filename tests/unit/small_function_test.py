from erictome_cicd_databricks_aws.small_function import square

def test_square():
    assert square(3) == 9