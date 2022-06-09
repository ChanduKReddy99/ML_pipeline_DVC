import pandas as pd
import argparse
from src.utils.common_utils import read_params,create_dir, save_reports
from sklearn.linear_model import ElasticNet
import joblib



def train(config_path):
    config = read_params(config_path)
    
    artifacts = config['artifacts']

    split_data = artifacts['split_data']
    processed_data_dir = split_data['processed_data_dir']
    train_data_path = split_data['train_data']
    test_data_path = split_data['test_data']
    

    base = config['base']
    random_state = base['random_state']
    target = base['target']

    reports = artifacts['reports']
    reports_dir = reports['reports_dir']
    params_file = reports['params']

    ElasticNet_params = config['estimators']['ElasticNet']['params']
    alpha = ElasticNet_params['alpha']
    l1_ratio = ElasticNet_params['l1_ratio']

    train = pd.read_csv(train_data_path,  sep=',')

    y_train = train[target]
    x_train = train.drop(target, axis=1)

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    lr.fit(x_train, y_train)

    model_dir = artifacts['model_dir']
    model_path = artifacts['model_path']

    create_dir([model_dir, reports_dir])

    params = {
        "alpha": alpha,
        "l1_ratio": l1_ratio,
    }

    save_reports(params_file, params)

    joblib.dump(lr, model_path)

    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='train model')
    parser.add_argument('--config', type=str, default='params.yaml')
    parsed_args = parser.parse_args()
    
    try:
        data = train(config_path= parsed_args.config)

    except Exception as e:
        raise e