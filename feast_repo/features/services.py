from features.views import customer_demo,customer_stats
from feast.feature_service import FeatureService

customer_engagement_feature_svc = FeatureService(
    name="customer_engagement",
    features=[customer_demo]
)