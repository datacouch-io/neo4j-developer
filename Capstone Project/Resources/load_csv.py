import os
import pandas as pd
import requests
from neo4j import GraphDatabase, basic_auth
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

# CSV download info
csv_url = "https://drive.google.com/uc?id=17TA40PHgZDm7Qi-xLCgsRlwWoam2YxBE&export=download"
local_csv = "dataset.csv"

# Download CSV if not already present
if not os.path.exists(local_csv):
    response = requests.get(csv_url)
    with open(local_csv, 'wb') as f:
        f.write(response.content)
    print(f"✅ Downloaded CSV to {local_csv}")

# Read and preprocess CSV
df = pd.read_csv(local_csv)

# 🔧 Fix column names in case of quotes or extra spaces
print("📄 Raw columns:", df.columns.tolist())
df.columns = df.columns.str.strip().str.replace("'", "")
print("✅ Cleaned columns:", df.columns.tolist())

# Normalize data
df['customer'] = df['customer'].astype(str).str.strip().str.replace("'", "")
df['merchant'] = df['merchant'].astype(str).str.strip().str.replace("'", "")
df['gender'] = df['gender'].astype(str).str.strip().str.replace("'", "")
df['category'] = df['category'].astype(str).str.strip().str.replace("'", "")
df['zipMerchant'] = df['zipMerchant'].astype(str).str.strip().str.replace("'", "")
df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(-1).astype(int)
df['step'] = df['step'].astype(int)
df['amount'] = df['amount'].astype(float)
df['fraud'] = df['fraud'].astype(int)

# Connect to Neo4j
driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))

# Batch insert transaction
def load_data_batch(tx, batch):
    query = """
    UNWIND $rows AS row
    MERGE (c:Customer {customer_id: row.customer})
      SET c.age = row.age, c.gender = row.gender

    MERGE (m:Merchant {merchant_id: row.merchant})
      SET m.category = row.category, m.zipMerchant = row.zipMerchant

    CREATE (t:Transaction {
        amount: row.amount,
        step: row.step,
        category: row.category,
        fraud: row.fraud,
        timestamp: timestamp()
    })

    MERGE (c)-[:INITIATED]->(t)
    MERGE (t)-[:TO]->(m)
    """
    tx.run(query, rows=batch)

# Write to Neo4j in batches
batch_size = 100
with driver.session() as session:
    batch = []
    for _, row in df.iterrows():
        batch.append({
            'customer': row['customer'],
            'merchant': row['merchant'],
            'gender': row['gender'],
            'category': row['category'],
            'zipMerchant': row['zipMerchant'] if pd.notna(row['zipMerchant']) else '00000',
            'age': int(row['age']),
            'amount': float(row['amount']),
            'step': int(row['step']),
            'fraud': int(row['fraud'])
        })
        if len(batch) >= batch_size:
            session.execute_write(load_data_batch, batch)
            print(f"✅ Inserted batch of {batch_size}")
            batch = []
    if batch:
        session.execute_write(load_data_batch, batch)
        print(f"✅ Inserted final batch of {len(batch)}")

# Validation query to show sample transactions
with driver.session() as session:
    result = session.run("""
        MATCH (c:Customer)-[:INITIATED]->(t:Transaction)-[:TO]->(m:Merchant)
        RETURN c.customer_id AS customer, m.merchant_id AS merchant, t.amount AS amount, t.fraud AS fraud
        LIMIT 5
    """)
    records = result.data()
    if records:
        print("\n Done !")
    else:
        print("\n⚠️ No Transaction nodes found — check the logic!")
