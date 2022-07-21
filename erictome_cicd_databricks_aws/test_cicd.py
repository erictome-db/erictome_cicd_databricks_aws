# Databricks notebook source
#
# To get all clusters: databricks clusters list --output JSON | jq '[ .clusters[] | { name: .cluster_name, id: .cluster_id } ]' 
#
# USAGE: 
#       
#     dbx execute --job=test_cicd --cluster-name="test1"

from pyspark.sql.types import *
from datetime import date

# COMMAND ----------

#added a cell

# COMMAND ----------

schema = StructType([
   StructField('AirportCode', StringType(), False),
   StructField('Date', DateType(), False),
   StructField('TempHighF', IntegerType(), False),
   StructField('TempLowF', IntegerType(), False)
])

data = [
   [ 'BLI', date(2021, 4, 3), 52, 43],
   [ 'BLI', date(2021, 4, 2), 50, 38],
   [ 'BLI', date(2021, 4, 1), 52, 41],
   [ 'PDX', date(2021, 4, 3), 64, 45],
   [ 'PDX', date(2021, 4, 2), 61, 41],
   [ 'PDX', date(2021, 4, 1), 66, 39],
   [ 'SEA', date(2021, 4, 3), 57, 43],
   [ 'SEA', date(2021, 4, 2), 54, 39],
   [ 'SEA', date(2021, 4, 1), 56, 41]
]

# COMMAND ----------

temps = spark.createDataFrame(data, schema)
spark.sql('USE default')
spark.sql('DROP TABLE IF EXISTS erictome_temp_cicd')
temps.write.saveAsTable('erictome_temp_cicd')


# COMMAND ----------

df_temps = spark.sql("SELECT * FROM erictome_temp_cicd " \
   "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' " \
   "GROUP BY AirportCode, Date, TempHighF, TempLowF " \
   "ORDER BY TempHighF DESC")
display(df_temps)

# COMMAND ----------
