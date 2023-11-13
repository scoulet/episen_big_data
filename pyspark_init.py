from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col, when

# Initialiser une session Spark. Cela crée une interface à un cluster Spark.
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("PySpark_Local") \
    .getOrCreate()

# Créer un DataFrame simple
data = [("James", "Smith", "USA", 1), 
        ("Michael", "Rose", "FR", 2), 
        ("Robert", "Williams", "FR", 3), 
        ("Maria", "Jones", "USA", 4)]

columns = ["Prénom", "Nom", "Pays", "ID"]

df = spark.createDataFrame(data).toDF(*columns)

df2 = df.withColumnRenamed("Prénom", "Prenom")
df3 = df2.withColumn("Date", lit("NULL"))
print("df3 :")
df3.show()


df4 = df3.withColumn("Date", when(col("Date")=="NULL", "01-01-1970"))
print("df4 :")
df4.show()

print("exemple of select : ")
df4.where(col("ID")=="4").show()

# saves with partitions :
df4.write.partitionBy("Pays").format("parquet").save("/Users/SIMON/Downloads/episen/data")
print("saved !")

# example of read
#spark.read.parquet("/Users/SIMON/Downloads/episen/data/").show()

# Arrêter la session Spark
spark.stop()
