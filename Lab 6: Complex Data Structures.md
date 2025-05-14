# Lab 6: Complex Data Structures

Estimated Time: 45 minutes

## Objective

Model three advanced patterns in Neo4j for an e-commerce system:

1.  Intermediate Nodes: Add semantic richness (e.g., :Review)  
      
    
2.  Linked List: Model a stepwise sequence of events (e.g., order lifecycle)  
      
    
3.  Timeline Tree: Model events grouped by time (e.g., orders by year/month/day)
    

These patterns are foundational for temporal queries, analytics, and recommendation systems.

## Step 1: Prepare Your Instance

### Start a new Neo4j instance

1.  Visit: [https://console.neo4j.io/](https://console.neo4j.io/)
    
2.  Create or open an existing Aura DB instance
    

## Step 2: Cleanup Any Existing Data
```
MATCH (n) DETACH DELETE n;
```
To make sure all the old data is deleted, go to Instance and click on the icon.![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe0Op4qS2lcpGQUzRSkRuYzm3cjokZ3dm4oZE_xZdaWoHuYlJ_fzuFdDIKtEpB1TCeeRMDwCD-8cBcDPD5S1agw3TNAJYm9Un4tC0mQmjOJhOEr6h6O-RiqsItMoByeROUXFGqEMQ?key=_dlBYpGBFQn1IO1OQj6eVw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeTgxO_BR1EaqbW4NKJ7o775UpbDvmRAIvuHpRPfl8gjhJEwS27ZS47PLkIX2e4vV0OMCXiEATbMRGUvy1qfCApJugKv-xWVYJel6vDayBK_9RfgtF1YJxr01wBgZ6nBw6HM_adNg?key=_dlBYpGBFQn1IO1OQj6eVw)

Click on “Reset to blank” and then click on “Reset”.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeTwwMuDUHA649NbJWyLngAq6Ny10o43LV5PV9nTcntsaUqJfJJoPixFph8F1yyr3LkH219veyPLnUgfdYP2dcHPxHB4sRfBpkywL8pCRPJODpk6zNBxxCo91SUypeYwUSBEG-QqQ?key=_dlBYpGBFQn1IO1OQj6eVw)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcy6Xpg2LuUwPPMQOUH1_p68aRwuUUct3FRxQ7Qw_fG_NWVctJNimA7Gmne6z9uh_SGNOELnqbfA6gsSdHopLW5CBHEIfN7YQhLAde9c7PmqRR4XsEfcDfMGup2tEiMe0oIzZrm?key=_dlBYpGBFQn1IO1OQj6eVw)

Come back to the Query Section, refresh and ensure that the nodes and relationships are not there.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfFuIJ7JeEYVbX9CU6SMuZJ2GvkMqOM709ajDnDZr-8wmaxQDGpQNnGIOdNFLc686LvPx5bEEw_wCGcww87URYkluYmI_FtRBCIVjktIvKqjw402uSonPUFmZ8A-v-5uR2oH_7adQ?key=_dlBYpGBFQn1IO1OQj6eVw)

This will clear any previously created data to ensure a consistent starting point.

## Step 3: Create Core Data

You’ll create a simplified dataset involving buyers, products, and orders.

### Buyers
```
CREATE (:Buyer {id: 1, name: "Alice"}),  
(:Buyer {id: 2, name: "Bob"});
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd_tVNgtxPJwpmV-I1w0vCbqTfLs9pLHNeMM18EKf0NY0UF_pikB7163_JQLgnvMnvo0Ta7TbaCVXC7wm1pGBRC99naCr1ggN3-J7qkVXKWa4PGDDCN6DJksBETvOP7_MuTShD-yw?key=_dlBYpGBFQn1IO1OQj6eVw)

  

Products
```
CREATE (:Product {id: 101, name: "Laptop", category: "Electronics"}),  
(:Product {id: 102, name: "Blender", category: "Home Appliances"});
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfuAiigwWCV_fSqryzBRY5PJYPgzzC9vE2wzLKYkorpcpgOBBdjvA90kZQJhkyYLcbV3afz8axkhJJ-freR6bDVYT2LLnlrjKIR94aw0ArZvXdIORxBKBNKgeYc-7M6E2p-zU5Iyg?key=_dlBYpGBFQn1IO1OQj6eVw)

  

Orders
```
CREATE (:Order {id: 201, order_date: date("2025-04-01")}),  
(:Order {id: 202, order_date: date("2025-04-10")}),  
(:Order {id: 203, order_date: date("2025-04-15")});
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd69G69F1YGPBGfIIykZJ1hrRCgKx9PW67dQlzmYm2xMrb49Hm4KBVyg4xIu1bdeNDHkXj8Xo2vu_y3FwgGg7OqKjCxUqUjwkZNPaEwW3MvEQOE2F5Nc8CSto3XGsgQBCLx47o3iA?key=_dlBYpGBFQn1IO1OQj6eVw)

  
  
  
  

## Step 4: Model 1 — Intermediate Node: Review

We’ll use a Review node between a Buyer and a Product, allowing richer metadata like rating, comment, and review_date.

### Sample: Create a Review node between Alice and Laptop
```
MATCH (b:Buyer {name: "Alice"}), (p:Product {name: "Laptop"})  
CREATE (b)-[:WROTE]->(r:Review {  
rating: 5,  
comment: "Excellent!",  
review_date: date("2025-04-05")  
})-[:REVIEWS]->(p);
```
  

### Using above model, these business queries can be answered

  

### 🔎 1. What products did Alice review, and what did she say?
```
MATCH (b:Buyer {name: "Alice"})-[:WROTE]->(r:Review)-[:REVIEWS]->(p:Product)  
RETURN  p.name  AS  Product, r.rating  AS  Rating, r.comment  AS  Comment, r.review_date  AS  Date  
ORDER  BY  r.review_date;
```
  
  

⭐ 2. What are the top-rated products with average ratings above 4.5?

  
```
MATCH (p:Product)<-[:REVIEWS]-(r:Review)  
WITH p, avg(r.rating) AS avgRating  
WHERE avgRating > 4.5  
RETURN p.name AS Product, round(avgRating, 2) AS AverageRating  
ORDER  BY avgRating DESC;
```
  
  
  
  
  

🧍 3. Which buyers gave the lowest rating (1 or 2) to any product?

  
```
MATCH (b:Buyer)-[:WROTE]->(r:Review)  
WHERE r.rating <= 2  
RETURN b.name AS Buyer, r.comment AS Comment, r.rating AS Rating;
```

### 📊 4. Which product has received the most reviews?
```
MATCH (r:Review)-[:REVIEWS]->(p:Product)  
RETURN p.name AS Product, count(r) AS ReviewCount  
ORDER  BY ReviewCount DESC  
LIMIT 1;  
  ```

  

📝 5. Show all reviews for the “Laptop” product with buyer names
```
MATCH (b:Buyer)-[:WROTE]->(r:Review)-[:REVIEWS]->(p:Product {name: "Laptop"})  
RETURN  b.name  AS  Buyer, r.rating  AS  Rating, r.comment  AS  Comment, r.review_date  AS  Date  
ORDER  BY  r.review_date;
```
  

### Your Turn

Write a query to:

-   Match Bob and the Blender product  
      
    
-   Create a Review node between them  
      
    
-   Add a comment, rating, and review_date
    

  

💡 Challenge Business Queries Based on This Review

🔹 1. What rating did Bob give to the Blender?

🔹 2. List all products reviewed by Bob

🔹 3. List all buyers who reviewed the Blender

## Step 5: Model 2 — Linked List of Order Events (Order Lifecycle)

Model a single order as a sequence of steps:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeVwA_SaNvpAx9vDc3AyYTw4Lkg0Ly5b7ArnDm8hLqWfYVEylJvGiIm605sVdMK7OoOz_Wtwv30cHKSb_ffVEPhdLqeF4_LyBjPAHyEps1M-VL6CgIYtHx4TYwFAZPLD3594rGPBQ?key=_dlBYpGBFQn1IO1OQj6eVw)

Each step is an :OrderEvent, linked via :NEXT.
```
CREATE (o:Order {id: 301, buyer: "Alice"});

  

CREATE (e1:OrderEvent {status: "Placed", timestamp: datetime("2025-04-01T10:00:00")}),

(e2:OrderEvent {status: "Packed", timestamp: datetime("2025-04-01T12:00:00")}),

(e3:OrderEvent {status: "Shipped", timestamp: datetime("2025-04-02T09:00:00")}),

(e4:OrderEvent {status: "Delivered", timestamp: datetime("2025-04-03T17:00:00")});

  

MATCH (o:Order {id: 301})

MATCH (e1:OrderEvent {status: "Placed"})

MATCH (e2:OrderEvent {status: "Packed"})

MATCH (e3:OrderEvent {status: "Shipped"})

MATCH (e4:OrderEvent {status: "Delivered"})

MERGE (o)-[:HAS_EVENT]->(e1)

MERGE (e1)-[:NEXT]->(e2)

MERGE (e2)-[:NEXT]->(e3)

MERGE (e3)-[:NEXT]->(e4);
```
  

  

Check the complete path

  
```
MATCH (o:Order {id:  301})-[:HAS_EVENT]->(e:OrderEvent)  
MATCH path = (e)-[:NEXT*0..]->(next)  
RETURN o, path;
```
  
  

### Business Queries that can be answered by above

### 🔹 1.  What is the current status of Order 301?

(Assumes no future :NEXT event means it's the latest)
```
MATCH (:Order {id: 301})-[:HAS_EVENT]->(:OrderEvent)-[:NEXT*0..]->(e)  
WHERE  NOT (e)-[:NEXT]->()  
RETURN  e.status  AS  CurrentStatus, e.timestamp  AS  LastUpdated;
```
  
  
  

### Your Turn

### 🔄 Use Case: Product Return Workflow

A customer returns a product. The return process goes through multiple stages, such as:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc5x9Vr-ZoM_uLqBgDSSLlKTmFPAjc338B8xPZ3KJUNCeHUeFRBb4dim6w2TL7S61hblh3x22Nu_M-yeboj4FoS4IB0IpY6FO0_3onkGqSZsZqQwvN7vaPYVgIJbIjOJSu2VuU_Vg?key=_dlBYpGBFQn1IO1OQj6eVw)

1.  Create a Return node with:

	-   return_id: 1001
	    
	-   order_id: 301
    

  

2.  Create 5 ReturnEvent nodes with the following status and timestamp:  
      
    

	-   Return Requested: 2025-04-05T10:00:00  
	      
	    
	-   Pickup Scheduled: 2025-04-06T09:00:00  
	      
	    
	-   Item Received: 2025-04-07T11:30:00  
	      
	    
	-   Refund Initiated: 2025-04-08T14:45:00  
	      
	    
	-   Refund Completed: 2025-04-09T17:00:00  
      
    

3.  Connect the Return node to the first ReturnEvent using :HAS_EVENT.  
  

4. Connect the events together in a chain using :NEXT.

5. Visualize it using cypher query

  

✅ Bonus Challenge

Write a query to:

-   Identify the current status of the return process.
    

  

## Step 6: Model 3 — Timeline Tree (Year → Month → Day → Order)

### 🧩 Use Case

We want to store and analyze orders grouped by date so that we can easily:

-   Slice orders by year/month/day  
      
    
-   Run time-based aggregations (e.g., daily/monthly sales)  
      
    
-   Support time-filtered queries
    

👤 Create an Order
```
CREATE (:Order {id: 501, buyer: "Bob", order_date: date("2025-06-10")});
```
  

🌳 Create Timeline Tree & Link the Order
```
MATCH (o:Order {id: 501})  
WITH  o, o.order_date  AS  date  
MERGE (y:Year {value: date.year})  
MERGE (m:Month {value: date.month})  
MERGE (d:Day {value: date.day})  
MERGE (y)-[:HAS_MONTH]->(m)  
MERGE (m)-[:HAS_DAY]->(d)  
MERGE (d)-[:HAS_ORDER]->(o);
```
  

## 👁 Visualize the Tree
```
MATCH (y:Year)-[:HAS_MONTH]->(m:Month)-[:HAS_DAY]->(d:Day)-[:HAS_ORDER]->(o:Order)  
RETURN  y, m, d, o;
```
  

## ✅ Business Questions You Can Answer with This Graph

----------

### 📆 1. How many orders were placed in each year/month/day?

  
```
MATCH (y:Year)-[:HAS_MONTH]->(:Month)-[:HAS_DAY]->(:Day)-[:HAS_ORDER]->(o:Order)  
RETURN  y.value  AS  Year, count(o) AS  Orders;
```
  
  

### 📅 2. How many orders were placed each day in June 2025?

  
```
MATCH (y:Year {value: 2025})-[:HAS_MONTH]->(m:Month {value: 6})-[:HAS_DAY]->(d:Day)-[:HAS_ORDER]->(o:Order)  
RETURN  d.value  AS  Day, count(o) AS  Orders  
ORDER  BY  d.value;
```
  
  
  
  

### 👤 3. List all orders placed by a specific buyer (e.g., Bob) in a given month

  
```
MATCH (y:Year {value:  2025})-[:HAS_MONTH]->(m:Month {value:  6})-[:HAS_DAY]->(d:Day)-[:HAS_ORDER]->(o:Order)  
WHERE o.buyer = "Bob"  
RETURN d.value AS Day, o.id AS OrderID, o.order_date;
```
  

## 🎯 Your Challenge

## Now that you've created the tree for one order, do the same for the following:

-   Order ID: 502  
      
    
-   Buyer: Bob  
      
    
-   Order Date: 2025-06-11  
      
    

## ✏️ Steps:

1.  Create the order node  
      
    
2.  Reuse Year: 2025 and Month: 6 and Day: 11  
      
    
3.  Link them using the same pattern
    

  

After adding your data, run below to check

### ⏳ 5. Show total orders over time — year/month/day trend
```
MATCH (y:Year)-[:HAS_MONTH]->(m:Month)-[:HAS_DAY]->(d:Day)-[:HAS_ORDER]->(o:Order)  
RETURN  y.value  AS  Year, m.value  AS  Month, d.value  AS  Day, count(o) AS  OrderCount  
ORDER  BY  Year, Month, Day;
```
  
  
  
  
  

## Solutions

### **Step 4:**  Bob’s Review on Blender
```
MATCH (b:Buyer {name: "Bob"}), (p:Product {name: "Blender"})  
CREATE (b)-[:WROTE]->(r:Review {  
rating: 4,  
comment: "Works well for smoothies",  
review_date: date("2025-04-08")  
})-[:REVIEWS]->(p);
```

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdWvqi8TthTmmvSWuO4vTLf9vLBktMjeXUyK_SOZ3MRLA86V-ly5RbbsWtiG-jj87G0zuKIm7VIr0bqli29DIawoZMuQ7zZs0HZxxN5n1RxYGsrHN9Ntcnsp4DCeHHOeUNzG8oVqQ?key=_dlBYpGBFQn1IO1OQj6eVw)


💡 Challenge Business Queries Based on This Review

**🔹 1. What rating did Bob give to the Blender?**
```
MATCH (b:Buyer {name: "Bob"})-[:WROTE]->(r:Review)-[:REVIEWS]->(p:Product {name: "Blender"})  
RETURN  r.rating  AS  Rating;
```
  

**🔹 2. List all products reviewed by Bob**
```
MATCH (b:Buyer {name: "Bob"})-[:WROTE]->(:Review)-[:REVIEWS]->(p:Product)  
RETURN  p.name  AS  ProductName;
```
  

**🔹 3. List all buyers who reviewed the Blender**
```
MATCH (b:Buyer)-[:WROTE]->(:Review)-[:REVIEWS]->(p:Product {name: "Blender"})  
RETURN  DISTINCT  b.name  AS  BuyerName;
```
  

### Step 5:
```
CREATE (:Return {return_id: 1001, order_id: 301, customer: "Alice"});  
  
CREATE  
(:ReturnEvent {status: "Return Requested", timestamp: datetime("2025-04-05T10:00:00")}),  
(:ReturnEvent {status: "Pickup Scheduled", timestamp: datetime("2025-04-06T09:00:00")}),  
(:ReturnEvent {status: "Item Received", timestamp: datetime("2025-04-07T11:30:00")}),  
(:ReturnEvent {status: "Refund Initiated", timestamp: datetime("2025-04-08T14:45:00")}),  
(:ReturnEvent {status: "Refund Completed", timestamp: datetime("2025-04-09T17:00:00")});  
 
  
MATCH (r:Return {return_id: 1001}),  
(e:ReturnEvent {status: "Return Requested"})  
MERGE (r)-[:HAS_EVENT]->(e);

  
  

MATCH (a:ReturnEvent {status: "Return Requested"}),  
(b:ReturnEvent {status: "Pickup Scheduled"}),  
(c:ReturnEvent {status: "Item Received"}),  
(d:ReturnEvent {status: "Refund Initiated"}),  
(e:ReturnEvent {status: "Refund Completed"})  
MERGE (a)-[:NEXT]->(b)  
MERGE (b)-[:NEXT]->(c)  
MERGE (c)-[:NEXT]->(d)  
MERGE (d)-[:NEXT]->(e);
```
  
  

Visualize the event flow

  
```
MATCH (r:Return {return_id:  1001})-[:HAS_EVENT]->(first:ReturnEvent)  
MATCH path = (first)-[:NEXT*0..]->(last)  
RETURN r, path;  
```
  

## ✅ 🎯 Bonus Challenge: Get Current Return Status
```
MATCH (:Return {return_id:  1001})-[:HAS_EVENT]->(first:ReturnEvent)  
MATCH path = (first)-[:NEXT*0..]->(e)  
WHERE NOT (e)-[:NEXT]->()  
RETURN e.status AS CurrentStatus, e.timestamp AS LastUpdated;
```
  
  

### Step 6: Timeline Tree Solution

### 🧱 1. Create the Order node
```
CREATE (:Order {id: 502, buyer: "Bob", order_date: date("2025-06-11")});
```
  

----------

### 🔗 2. Reuse Year and Month, Create Day, and Link Order

  
```
MATCH (o:Order {id: 502})  
WITH  o, o.order_date  AS  date  
MERGE (y:Year {value: date.year}) // Year: 2025 (reuse)  
MERGE (m:Month {value: date.month}) // Month: 6 (reuse)  
MERGE (d:Day {value: date.day}) // Day: 11 (create new)  
MERGE (y)-[:HAS_MONTH]->(m)  
MERGE (m)-[:HAS_DAY]->(d)  
MERGE (d)-[:HAS_ORDER]->(o);  
```

----------

### 👁️ 3. Visualize the Timeline Tree for Bob’s Orders
```
MATCH (y:Year)-[:HAS_MONTH]->(m:Month)-[:HAS_DAY]->(d:Day)-[:HAS_ORDER]->(o:Order)  
WHERE o.buyer = "Bob"  
RETURN y, m, d, o;
```