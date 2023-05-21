import os

import pandas as pd
from feast import FeatureStore

feature_store = FeatureStore('.')

entity_df = pd.read_csv("data/entity_df.csv")
entity_df["event_timestamp"] = pd.to_datetime(entity_df.event_timestamp)
#retrieve feature from offline store
customer_demo_features = feature_store.get_historical_features(features=['customer_demo:age','customer_demo:gender'],
                                                    entity_df=entity_df)
# print(customer_demo_features.to_df())
entity_dict = {'customer_id': '123456'}
online_customer_demo_features = feature_store.get_online_features(
    features=[
        'customer_demo:age',
        'customer_demo:gender',
    ],
    entity_rows=[
        entity_dict
        
    ]
)
# print(online_customer_demo_features.to_df())
feature_service = feature_store.get_feature_service("customer_engagement")
online_features_from_service = feature_store.get_online_features(
    features=feature_service, entity_rows=[entity_dict]
)
# print(online_features_from_service.to_df())

offline_features_from_service = feature_store.get_historical_features(features=feature_service, entity_df=entity_df)
#print(offline_features_from_service.to_df())
