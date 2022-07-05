# Databricks notebook source
from pyspark.sql.types import *
from datetime import date

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
spark.sql('DROP TABLE IF EXISTS demo_temps_table')
temps.write.saveAsTable('demo_temps_table')


# COMMAND ----------

df_temps = spark.sql("SELECT * FROM demo_temps_table " \
   "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' " \
   "GROUP BY AirportCode, Date, TempHighF, TempLowF " \
   "ORDER BY TempHighF DESC")
display(df_temps)

# COMMAND ----------


