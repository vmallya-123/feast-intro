import os
from datetime import timedelta

from feast import FeatureView, Feature, ValueType, FileSource, PushSource
from feast.data_format import ParquetFormat

PROJECT = os.getenv('PROJECT', 'specify_a_project')

customer_demo_parquet_file_source = FileSource(
    file_format=ParquetFormat(),
    path="data/customer_demo.parquet",
)

customer_stats_parquet_file_source = FileSource(
    file_format=ParquetFormat(),
    path="data/customer_stats.parquet",
)

merchant_stats_parquet_file_source = FileSource(
    file_format=ParquetFormat(),
    path="data/merchant_stats.parquet",
)

customer_demo = FeatureView(
    name="customer_demo",
    entities=["customer_id"],
    features=[
        Feature(name="age", dtype=ValueType.INT64),Feature(name="gender", dtype=ValueType.STRING)],
    ttl=timedelta(days=7),
    batch_source=customer_demo_parquet_file_source,
    tags={
        'authors': "Benjamin Tan <benjamin.tan@tech.jago.com, Varun Mallya <varun.mallya@tech.jago.com",
        'description': 'Customer Demographics',
        'used_by': 'Customer_Retention_Team',
    },
)
customer_stats = FeatureView(
    name="customer_stats",
    entities=["customer_id"],
    features=[
        Feature(name="number_of_logins", dtype=ValueType.INT64),
        Feature(name="number_of_purchases", dtype=ValueType.INT64)],
    ttl=timedelta(days=7),
    batch_source=customer_stats_parquet_file_source,
    tags={
        'authors': "Benjamin Tan <benjamin.tan@tech.jago.com, Varun Mallya <varun.mallya@tech.jago.com",
        'description': 'Insight types',
        'used_by': 'Customer_Retention_Team',
    },
)

# merchant_stats = FeatureView(
#     name="merchant_stats",
#     entities=["merchant_id"],
#     features=[
#         Feature(name="vertical", dtype=ValueType.STRING),
#         Feature(name="rank", dtype=ValueType.INT64)],
#     ttl=timedelta(days=7),
#     batch_source=merchant_stats_parquet_file_source,
#     tags={
#         'authors': "Benjamin Tan <benjamin.tan@tech.jago.com, Varun Mallya <varun.mallya@tech.jago.com",
#         'description': 'Insight types, but using the copied table',
#         'used_by': 'Customer_Retention_Team,Merchant_Aquisition_Team',
#     },
# )
