
# creating function to extract numerical and categorical features
def get_numerical(dataset):
    numerical_features = dataset.select_dtypes(include=['float64', 'int64']).columns.tolist()
    return numerical_features

def get_categorical(dataset):
    categorical_features = dataset.select_dtypes(include=['object']).columns.tolist()
    return categorical_features