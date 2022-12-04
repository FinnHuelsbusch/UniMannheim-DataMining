from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, KBinsDiscretizer
from imblearn.pipeline import Pipeline

one_hot_encoded_features = ['cp', 'restecg', 'slope', 'ca', 'restwm']
discretizeParameters = {
    'columnTransformer__discretize': [
        'passthrough',
        KBinsDiscretizer(2, encode='ordinal', strategy='uniform'),
        KBinsDiscretizer(5, encode='ordinal', strategy='uniform')]
}
columnTransformer = ColumnTransformer(
    transformers=[
        ('discretize', KBinsDiscretizer(), ['age']),
        ('oneHotEncoder', OneHotEncoder(handle_unknown='ignore'), lambda X: [value for value in one_hot_encoded_features if value in X.columns]),
    ], remainder='passthrough')



