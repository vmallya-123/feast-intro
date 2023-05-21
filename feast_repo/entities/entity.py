from feast import Entity, ValueType

customer = Entity(
    name="customer_id",
    description="A customer",
    value_type=ValueType.STRING,
)

merchant = Entity(
    name="merchant_id",
    description="A merchant",
    value_type=ValueType.STRING,
)
