from sklearn.model_selection import train_test_split
from modules import algorithms, fitters, models



bronze_housing_table = 'ml_project_1.default.bronze_housing'

housing_pdf = (
    spark.read.table(bronze_housing_table).toPandas()
    .drop(columns=['longitude', 'latitude', 'ocean_proximity'])
    .dropna()
)

X = housing_pdf.drop(columns=['median_house_value'])
y= housing_pdf.median_house_value
X_train, X_rem, y_train, y_rem = train_test_split(X, y, train_size=0.6, random_state=8)
X_val, X_test, y_val, y_test = train_test_split(X_rem, y_rem, train_size=0.5, random_state=8)

methodGenerator = algorithms.ElasticNetAlgorithmGenerator()

lr = methodGenerator.getAlgorithm()
