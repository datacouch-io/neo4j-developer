from fastapi import APIRouter, Depends, HTTPException
from neo4j import Session
from database import get_session
from models import Customer, Merchant, Transaction

router = APIRouter(prefix="/api")

# ---------- Customer Endpoints ----------

@router.post("/customer")
def create_customer(cust: Customer, session: Session = Depends(get_session)):
    session.run(
        """
        MERGE (c:Customer {customer_id: $customer_id})
        SET c.age = $age, c.gender = $gender
        """,
        customer_id=cust.customer_id, age=cust.age, gender=cust.gender
    )
    return {"message": "Customer created or updated"}

@router.patch("/customer/{customer_id}")
def update_customer(customer_id: str, age: int = None, gender: str = None, session: Session = Depends(get_session)):
    sets, params = [], {"customer_id": customer_id}
    if age is not None:
        sets.append("c.age = $age")
        params["age"] = age
    if gender:
        sets.append("c.gender = $gender")
        params["gender"] = gender
    if not sets:
        raise HTTPException(400, "No fields to update")
    session.run(
        f"MATCH (c:Customer {{customer_id: $customer_id}}) SET " + ", ".join(sets),
        **params
    )
    return {"message": "Customer updated"}

@router.delete("/customer/{customer_id}")
def delete_customer(customer_id: str, session: Session = Depends(get_session)):
    session.run(
        "MATCH (c:Customer {customer_id: $customer_id}) DETACH DELETE c",
        customer_id=customer_id
    )
    return {"message": "Customer deleted"}

# ---------- Merchant Endpoints ----------

@router.post("/merchant")
def create_merchant(merchant: Merchant, session: Session = Depends(get_session)):
    session.run(
        """
         ENTER YOUR QUERY HERE
        """,
        merchant_id=merchant.merchant_id, category=merchant.category, zipMerchant=merchant.zipMerchant
    )
    return {"message": "Merchant created or updated"}

@router.patch("/merchant/{merchant_id}")
def update_merchant(merchant_id: str, category: str, session: Session = Depends(get_session)):
    session.run(
        " ENTER YOUR QUERY HERE",
        merchant_id=merchant_id, category=category
    )
    return {"message": "Merchant updated"}

@router.delete("/merchant/{merchant_id}")
def delete_merchant(merchant_id: str, session: Session = Depends(get_session)):
    session.run(
        " ENTER YOUR QUERY HERE",
        merchant_id=merchant_id
    )
    return {"message": "Merchant deleted"}

# ---------- Transaction Endpoints ----------

@router.post("/transaction")
def create_transaction(tx: Transaction, session: Session = Depends(get_session)):
    result = session.run(
        """
        MATCH (c:Customer {customer_id: $customer_id})
        MATCH (m:Merchant {merchant_id: $merchant_id})
        CREATE (t:Transaction {
            amount: $amount,
            step: $step,
            category: $category,
            fraud: $fraud,
            timestamp: timestamp()
        })
        MERGE (c)-[:INITIATED]->(t)
        MERGE (t)-[:TO]->(m)
        RETURN c, m, t
        """,
        customer_id=tx.customer_id,
        merchant_id=tx.merchant_id,
        amount=tx.amount,
        step=tx.step,
        category=tx.category,
        fraud=tx.fraud
    )
    summary = result.consume()
    if summary.counters.nodes_created >= 1:
        return {"message": "Transaction created"}
    else:
        raise HTTPException(400, "Transaction not created")

@router.patch("/transaction/{customer_id}/{merchant_id}")
def update_transaction(customer_id: str, merchant_id: str, amount: float = None, step: int = None, fraud: int = None, session: Session = Depends(get_session)):
    # Check if both customer and merchant exist
    result = session.run(
        """
        OPTIONAL MATCH (c:Customer {customer_id: $customer_id})
        OPTIONAL MATCH (m:Merchant {merchant_id: $merchant_id})
        RETURN c IS NOT NULL AS customer_exists, m IS NOT NULL AS merchant_exists
        """,
        customer_id=customer_id,
        merchant_id=merchant_id
    ).single()

    if not result["customer_exists"]:
        raise HTTPException(status_code=404, detail="Customer does not exist")
    if not result["merchant_exists"]:
        raise HTTPException(status_code=404, detail="Merchant does not exist")

    # Proceed with update if fields are provided
    sets, params = [], {"customer_id": customer_id, "merchant_id": merchant_id}
    if amount is not None:
        sets.append("t.amount = $amount")
        params["amount"] = amount
    if step is not None:
        sets.append("t.step = $step")
        params["step"] = step
    if fraud is not None:
        sets.append("t.fraud = $fraud")
        params["fraud"] = fraud
    if not sets:
        raise HTTPException(400, "No fields to update")

    session.run(
        f"""
         ENTER YOUR QUERY HERE
        """,
        **params
    )
    return {"message": "Transaction updated"}


@router.delete("/transaction/{customer_id}/{merchant_id}")
def delete_transaction(customer_id: str, merchant_id: str, session: Session = Depends(get_session)):
    # Check if both customer and merchant exist
    result = session.run(
        """
        OPTIONAL MATCH (c:Customer {customer_id: $customer_id})
        OPTIONAL MATCH (m:Merchant {merchant_id: $merchant_id})
        RETURN c IS NOT NULL AS customer_exists, m IS NOT NULL AS merchant_exists
        """,
        customer_id=customer_id,
        merchant_id=merchant_id
    ).single()

    if not result["customer_exists"]:
        raise HTTPException(status_code=404, detail="Customer does not exist")
    if not result["merchant_exists"]:
        raise HTTPException(status_code=404, detail="Merchant does not exist")

    # Proceed with deletion
    session.run(
        """
         ENTER YOUR QUERY HERE
        """,
        customer_id=customer_id, merchant_id=merchant_id
    )
    return {"message": "Transaction deleted"}


# ---------- Analytics Endpoints ----------

@router.get("/analytics/high-risk-customers")
def high_risk_customers(session: Session = Depends(get_session)):
    data = session.run("""
         ENTER YOUR QUERY HERE
    """).data()
    return data

@router.get("/analytics/fraud-merchants")
def fraud_merchants(session: Session = Depends(get_session)):
    data = session.run("""
         ENTER YOUR QUERY HERE
    """).data()
    return data

@router.get("/analytics/fraud-trends")
def fraud_trends(session: Session = Depends(get_session)):
    data = session.run("""
         ENTER YOUR QUERY HERE
    """).data()
    return data

@router.get("/analytics/fraud-by-age")
def fraud_by_age(session: Session = Depends(get_session)):
    query = """
     ENTER YOUR QUERY HERE
    """
    data = session.run(query).data()
    return data

@router.get("/analytics/fraud-by-zip")
def fraud_by_zip(session: Session = Depends(get_session)):
    data = session.run("""
        ENTER YOUR QUERY HERE
    """).data()
    return data
