# Hands-On Lab: Fraud Detection System with FastAPI + Neo4j Aura - Implementation Guide

## Objective

This project will guide you in building a fraud detection system using Neo4j as the graph database and FastAPI as the backend API framework. Your main task is to understand the system design and write the Cypher queries in the provided routes.py file for each route.

### Prerequisites

-   Familiarity with Neo4j Aura and cypher text.
    
-   Completion of previous labs.
    
-   Familiarity with FastAPI routing and Pydantic models.
    

## Tech Stack

-   Neo4j Aura – Cloud-native graph database.  
      
    
-   FastAPI – High-performance Python web framework.  
      
    
-   Python Libraries: neo4j, pandas, python-dotenv, uvicorn, fastapi,requests
    

Project Setup

### Option-1 : Local Setup

### 1.Run load_csv.py

python load_csv.py

### 2. Clone the repository
```
git clone  https://github.com/your-username/fraud-detection.git  
cd fraud-detection
```
### 3. Set up a virtual environment
```
python3 -m venv venv  
source venv/bin/activate # On Windows: venv\Scripts\activate
```
### 4. Install Python dependencies
```
pip install -r requirements.txt
```
### 5. Add Neo4j credentials in .env file
```
NEO4J_URI=bolt+ssc ://<your-neo4j-aura-instance>  
NEO4J_USER=neo4j  
NEO4J_PASSWORD=yourpassword
```
Create a .env file at the project root:You can also add .env to .gitignore to keep credentials safe:
```
echo ".env" >> .gitignore
```
### 6. Run the FastAPI app
```
uvicorn  main:app --host 127.0.0.1  --port 8000 --reload
```
Access the docs:
```
http://127.0.0.1:8000/docs
```
### Option-2: Browser Based Lab

1. Open VS Code  
      
    
2.  Add Neo4j credentials in .env file
    
	```
	NEO4J_URI=bolt+ssc ://<your-neo4j-aura-instance>  
	NEO4J_USER=neo4j  
	NEO4J_PASSWORD=yourpassword
	```
	 
3.  Run load_csv.py
    
	```
	python3 load_csv.py
	```

4.  Run the FastAPI app
    
	```
	uvicorn  main:app --host 127.0.0.1  --port 8000 --reload
	```
Access the docs:
```
http://127.0.0.1:8000/docs
```
###   Project Overview

The application models a simple e-commerce fraud detection graph:

-   Customers initiate Transactions.  
      
    
-   Transactions go to Merchants.  
      
    
-   Each Transaction has metadata: amount, step (time), fraud flag, etc.
    

### Graph Structure:

  
```
(:Customer)-[:INITIATED]->(:Transaction)-[:TO]->(:Merchant)
```
This directional graph helps in identifying high-risk behavior based on relationships between customers, transactions, and merchants.

## Data Model Definitions

Defined in models.py:

1.  Customer
    
```
class Customer(BaseModel):  
customer_id: str  
age: int  
gender: str
```
  

2.  Merchant
    
```
class Merchant(BaseModel):  
merchant_id:  str  
category:  str  
zipMerchant:  str
```
  

3.  Transaction
    
```
class Transaction(BaseModel):  
customer_id: str  
merchant_id: str  
amount: float  
step: int  
category: str  
fraud: int
```
## FastAPI Endpoints to Implement (in routes.py)

1.  Customer Routes
    

	#### POST /customer

	**Create or update a customer node.**

	-   Use MERGE for customer_id and SET age and gender.
    

	#### PATCH /customer/{customer_id}

	Update customer's age or gender.

	-   Use MATCH and conditional SET.
	    

	#### DELETE /customer/{customer_id}

	Delete a customer and all its relationships.

	-   Use DETACH DELETE.  
      
    

2.  Merchant Routes
    
	
	#### POST /merchant

	Create or update a merchant node.

	-   Use MERGE for merchant_id, and SET category and zipMerchant.
	    

	#### PATCH /merchant/{merchant_id}

	Update merchant category.

	-   Use MATCH and SET.
	    

	#### DELETE /merchant/{merchant_id}

	Delete a merchant and its relationships.

	-   Use DETACH DELETE.  
	      
	    

3.  Transaction Routes
    
	
	#### POST /transaction

	Create a transaction node and link to customer and merchant.

	-   Use MATCH for existing Customers and Merchant.
	    
	-   Use CREATE for Transaction nodes.
	    
	-   Use MERGE to connect the relationships.
	    

	#### PATCH /transaction/{customer_id}/{merchant_id}

	Update fields in a transaction (amount, step, fraud).

	-   Traverse via Customer → Transaction → Merchant, then SET fields.
	    

	#### DELETE /transaction/{customer_id}/{merchant_id}

	Delete a specific transaction.

	-   Match the same path and DETACH DELETE the transaction.
    

To verify the successful transaction node and relationship creation run the following query:
```
MATCH (c:Customer {customer_id: "customer-id"})-[:INITIATED]->(t:Transaction)-[:TO]->(m:Merchant {merchant_id: "merchant-id"})  
RETURN  c, t, m
```
## Analytics Routes

Each query will use relationships and properties to answer real-world fraud questions.

### GET /analytics/high-risk-customers

Which customers have committed 3+ frauds?

-   Match fraud transactions.  
      
    
-   Count per customer.  
      
    
-   Filter fraud_count >= 3.  
      
    

### GET /analytics/fraud-merchants

Which merchants have >50% fraudulent transactions?

-   Match all transactions to merchants.  
      
    
-   Count total and fraudulent.  
      
    
-   Filter on fraud ratio.  
      
    

### GET /analytics/fraud-trends

How does fraud vary over time (by step)?

-   Group fraud transactions by step.  
      
    
-   Count and order by time.  
      
    

### GET /analytics/fraud-by-age

Which age ranges are most associated with fraud?

-   Match fraud transactions.  
      
    
-   Bucket ages using CASE.  
      
    
-   Group by range and count.  
      
    

### GET /analytics/fraud-by-zip

Which zip codes have the most fraud?

-   Match transactions with fraud.  
      
    
-   Group by merchant’s zip.  
      
    

## Your Task

Go through the routes.py file and implement all the missing Cypher queries where it says:
```
"""  
ENTER YOUR QUERY HERE  
"""
```
  

Use the logic provided in this guide to derive the appropriate query.

## Queries’ Logic

### 1. Create Merchant

**Goal:** Add or update a merchant with category and zip code.

**Logic:**

-   Each merchant has a unique merchant_id. So, use MERGE to avoid duplicates.  
      
    
-   Use SET to update or assign category and zipMerchant even if the node already exists.  
      
    

Think: “If a merchant exists, update it. If not, create it with full details.”

### 2. Update Merchant

**Goal:** Update the category field of an existing merchant.

**Logic:**

-   Find the merchant by merchant_id (use MATCH).  
      
    
-   Use SET to assign the new category.  
      
    

Think: “I’m changing a property on an existing node. Find it by ID and assign new data.”

### 3. Delete Merchant

**Goal:** Remove a merchant and all its connections.

**Logic:**

-   Use MATCH to find by merchant_id.  
      
    
-   Use DETACH DELETE to remove the node and any connected relationships.  
      
    

Think: “I want to completely remove this node and clean up its edges too.”

### 4. Update Transaction

**Goal:** Modify properties (amount, step, fraud) of a transaction between a customer and a merchant.

**Logic:**

-   First, traverse the graph: Customer → Transaction → Merchant.  
      
    
-   Use MATCH to find the path based on customer_id and merchant_id.  
      
    
-   Use SET to update the required fields.  
      
    

Think: “To update the transaction, I need to find it using the customer and merchant it connects.”

### 5. Delete Transaction

**Goal:** Remove a transaction and its relationships between a specific customer and merchant.

**Logic:**

-   Traverse Customer → Transaction → Merchant using MATCH.  
      
    
-   Use DETACH DELETE on the Transaction node.  
      
    

Think: “I need to remove this one transaction and its edges, not the customer or merchant.”

### 6. Get High-Risk Customers

**Goal:** Find customers who have committed fraud multiple times (e.g., 3+).

**Logic:**

-   Traverse from Customer to Transaction with [:INITIATED].  
      
    
-   Filter only fraudulent transactions (fraud = 1).  
      
    
-   Count frauds per customer.  
      
    
-   Return only those with a count ≥ 3.
    

Think: “I want to find repeat fraudsters — people with a pattern of bad behavior.”

### 7. Get Fraud Merchants

**Goal:** Find merchants whose transactions are mostly fraudulent (e.g., > 50%).

**Logic:**

-   Traverse from any customer to Transaction, then to Merchant.  
      
    
-   Count how many total transactions each merchant has.  
      
    
-   Also sum the number of those that are fraudulent.  
      
    
-   Calculate fraud rate and filter if > 0.5.  
      
    

Think: “I want merchants where fraud dominates their activity — possibly compromised or bad actors.”

### 8. Fraud Trends Over Time

**Goal:** Track how fraud incidents evolve with time.

**Logic:**

-   step represents a time unit like hours.  
      
    
-   Match transactions where fraud = 1.  
      
    
-   Group them by step value.  
      
    
-   Count how many happened in each step.  
      
    

Think: “I want to build a fraud timeline — how it increases or decreases across hours/days.”

### 9. Fraud by Age Range

**Goal:** See which age ranges show higher fraud behavior.

**Logic:**

-   Fraud is tied to the Transaction node.  
      
    
-   Age is a property of the Customer.  
      
    
-   Traverse to match fraudulent transactions.  
      
    
-   Use CASE logic to bucket ages (e.g., 20–29, 30–39).  
      
    
-   Count frauds per age range.  
      
    

Think: “Rather than individual ages, group people into age bands to spot vulnerable age groups.”

### 10. Fraud by Zip Code

**Goal:** Spot which zip codes (based on merchants) are hotspots for fraud.

**Logic:**

-   Start with Transaction → Merchant.  
      
    
-   Filter to include only fraudulent transactions.  
      
    
-   Use the zipMerchant property.  
      
    
-   Count how many frauds happen in each zip code.
    

Think: “I want a geographic heatmap of fraud — which merchant zip codes are risky.”

## Conclusion

This project is designed to bridge the gap between theory and real-world graph-based application development. By combining the power of Neo4j with FastAPI, you’ve explored how to build a dynamic backend capable of not only storing data, but also uncovering patterns — in this case, fraudulent behavior.

You’ve:

-   Modeled real-life entities like customers, merchants, and transactions as graph nodes.  
      
    
-   Connected them meaningfully through relationships.  
      
    
-   Designed routes that reflect critical business insights.  
      
    
-   Learned how to translate analytical questions into Cypher queries.  
      
    

Through this process, you've deepened your understanding of:

-   Graph schema design  
      
    
-   Query logic construction  
      
    
-   Practical backend API development
    

This hands-on exercise doesn’t just teach you how to use tools — it teaches you how to think like a graph developer, where relationships are as important as data itself.