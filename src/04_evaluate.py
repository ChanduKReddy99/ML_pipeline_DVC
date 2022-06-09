import pandas as pd
import argparse
from src.utils.common_utils import read_params, save_reports
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib



def eval_metrics(actual, pred):
    rmse = mean_squared_error(actual, pred)
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2 

def evaluate(config_path):
    config = read_params(config_path)

    artifacts = config['artifacts']
    test_data_path = artifacts['split_data']['test_data']
    model_path = artifacts['model_path']
    target = config['base']['target']
    scores_file = artifacts['reports']['scores']

    test = pd.read_csv(test_data_path, sep=",")

    y_test = test[target]
    x_test = test.drop(target, axis=1)

    lr = joblib.load(model_path)
    

    predicted_values = lr.predict(x_test)

    rmse, mae, r2 = eval_metrics(y_test ,predicted_values)

    scores = {
    "rmse": rmse,
    "mae": mae,
    "r2": r2
    }

    save_reports(scores_file, scores)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='test model')
    parser.add_argument('--config', type=str, default='params.yaml')
    parsed_args = parser.parse_args()
    
    try:
        data = evaluate(config_path= parsed_args.config)

    except Exception as e:
        raise e