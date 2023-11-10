from pyspark.sql import SparkSession

# Initialiser une session Spark. Cela crée une interface à un cluster Spark.
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("PySpark_Local") \
    .getOrCreate()

# Créer un DataFrame simple
data = [("James", "Smith", "USA", 1), 
        ("Michael", "Rose", "USA", 2), 
        ("Robert", "Williams", "USA", 3), 
        ("Maria", "Jones", "USA", 4)]

columns = ["Prénom", "Nom", "Pays", "ID"]

df = spark.createDataFrame(data).toDF(*columns)

# Afficher le DataFrame
df.show()

# Arrêter la session Spark
spark.stop()
