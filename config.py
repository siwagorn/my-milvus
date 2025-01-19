# Embedding Model Configuration
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # ชื่อโมเดลสำหรับ embedding
EMBEDDING_DIM = 128             # ขนาดของ embedding vector

# Index Configuration
INDEX_TYPE = "IVF_FLAT"         # ประเภทของ Index
METRIC_TYPE = "L2"              # Metric ที่ใช้ (L2 = Euclidean Distance)
NLIST = 128                     # จำนวน cluster สำหรับ IVF Index