from erictome_cicd_databricks_aws.jobs.julia_file import julia_function


def test_julia_function():
    assert julia_function(2, 4) == 6
    
