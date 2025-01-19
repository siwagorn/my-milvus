from pymilvus import connections, Collection, CollectionSchema, FieldSchema, DataType
import config  # Import config.py

# เชื่อมต่อกับ Milvus
connections.connect(alias="default", host=config.MILVUS_HOST, port=config.MILVUS_PORT)

# กำหนด Schema สำหรับ Collection
id_field = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True)
embedding_field = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=config.EMBEDDING_DIM)
meta_field = FieldSchema(name="metadata", dtype=DataType.VARCHAR, max_length=500)
schema = CollectionSchema(fields=[id_field, embedding_field, meta_field], description="Example collection")

# สร้าง Collection
collection = Collection(name="example_collection", schema=schema)

# สร้าง Index
index_params = {
    "index_type": config.INDEX_TYPE,
    "metric_type": config.METRIC_TYPE,
    "params": {"nlist": config.NLIST}
}
collection.create_index(field_name="embedding", index_params=index_params)

print("Collection created:", collection.name)