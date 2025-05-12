# Lab 5: Advanced Cypher Querying (Aggregation, Lists, Dates)

Estimated Time: 25–30 minutes

## Objective

The objective of this lab is to strengthen your Cypher query skills by introducing advanced concepts in aggregation, list handling, date-based filtering, and multi-step query construction. Participants will use functions like COUNT, SUM, AVG, COLLECT, and WITH to perform insightful analysis on an e-commerce graph. These operations are essential for building analytics pipelines and extracting meaningful patterns from graph data.

## Prerequisites

Before starting this lab, participants should ensure:

-   A Neo4j Aura instance is available and accessible.
    
-   Familiarity with Cypher basics such as MATCH, RETURN, and WHERE (as covered in Lab 4).
    
-   The ability to create and relate nodes like Buyer, Product, and Order.
    
-   Basic understanding of graph structure and data types, including dates and lists.
    

## Lab Overview

This lab focuses on using advanced Cypher queries to extract analytical insights from an e-commerce graph dataset. Participants will first clean up the database to ensure a consistent environment and then insert fresh data covering buyers, products, orders, and their interconnections. Through guided examples and challenges, they will perform aggregations (e.g., total spend, review counts), build lists of related data (e.g., products reviewed by a buyer), apply date filters, and use the WITH clause to chain query logic. The lab concludes with challenge exercises to rank products by popularity and identify heavily reviewed items — preparing participants for real-world graph analytics.

## Scenario

You’re now analyzing the e-commerce platform data for operational and business insights. You will examine how many orders were placed per buyer, calculate the average selling price of products, retrieve lists of products per user, and explore time-based ordering patterns.

From this lab onwards, each lab is fully self-contained. That means:

-   The dataset is created from scratch in each lab  
      
    
-   Cleanup steps are included to avoid residual data issues  
      
    
-   Queries are followed by templates and solutions  
      
    

## Step-by-Step Instructions

### Step 1: Clean Up the Database
```
MATCH (n) DETACH DELETE n;
```
To make sure all the old data is deleted, go to Instance and click on the icon.![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcOntJVoE2SbKbzHDmha9zOkyucF7WqOhWCf9r9SqAtwfhqkS9nH17d3pUcC61-YhVIVLhLWGSBCMd6tvYwbK0-4mlTfYs2dg1P8xsq6GOeLk_lgJ5lWNuy9a2PR8cu_7KKWO_-?key=fSQhMkXZaLSnxkwxr-9KdY8U)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfg3VSqjL6ykmWGi34g82j_hAUrlGzVL7RdBIticD8xPCbJURHAcdkkGu-2OPMpIWKUjpD3xi3fotmHzI-JhYh8Awfq6HP_WSzN7oejqNcMxLtqIzrYDRGS9x5uyvHKt8Aqf2r6fg?key=fSQhMkXZaLSnxkwxr-9KdY8U)

Click on “Reset to blank” and then click on “Reset”.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdx5nqSrOu3ROXcxS6RKqYrdlOdF3WIzIc8m-F8XuWNou-K-aQcbiUv0FBuN3oxWKio-JD5JP9nF9fbm1rgw9XRCZe0Qmgv9emfzJw8JOqJMmx0NmjWKhMJ0edRq8Uue0AB7PCH?key=fSQhMkXZaLSnxkwxr-9KdY8U)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXejbXfZxWzx0on7gEVk0UreNfc4jQ2cgPtC3CQKCCa4jE0nI_4xqSaQglJqHtLojMzMcME34cczUfECnhI-IQ5g4rcynz_Ckn2IQ1ah8NWK7VHYmlJqj4kIlEvNpxk9wRNQ7g3LOA?key=fSQhMkXZaLSnxkwxr-9KdY8U)

Come back to the Query Section, refresh and ensure that the nodes and relationships are not there.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd8r1cnzZav5xTFxtlJcxpFFLBjKzNHI14_BLfXMT3J7PUMfW-xhYA38VK9BUW0WFjmNvwWVbZHVe6fQZQcFTBlnsrTW2CT6tdxcC8Jyv_U38aCV0Te78vLukAb9G0BZz6F1Q24?key=fSQhMkXZaLSnxkwxr-9KdY8U)

This will clear any previously created data to ensure a consistent starting point.

### Step 2: Create Sample Data  
Buyers
```
CREATE (:Buyer {id: 1, name: "Alice", email: "alice@example.com"}),  
(:Buyer {id: 2, name: "Bob", email: "bob@example.com"}),  
(:Buyer {id: 3, name: "Charlie", email: "charlie@example.com"});
```
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPuP2gwttRG7WMtbyCXj_3DfHwU2LTv6sVCuLKHJgkDfiIYpTx9m8G6JBCJptWQDarQaR0nMgmW1MMgtS34Enfm00-FGkePEjjwbTLx_jmIoCOjfw2kjJtZ6zp-yxgNtyAEaFxJw?key=fSQhMkXZaLSnxkwxr-9KdY8U)

  
Products
```
CREATE (:Product {id: 101, name: "Laptop", price: 1200, category: "Electronics", brand: "TechPro"}),  
(:Product {id: 102, name: "Blender", price: 150, category: "Home Appliances", brand: "HomeMax"}),  
(:Product {id: 103, name: "Smartphone", price: 900, category: "Electronics", brand: "TechPro"}),  
(:Product {id: 104, name: "Toaster", price: 80, category: "Home Appliances", brand: "HomeMax"});
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcTAg91TFhgKrxnIRg4slpi-LicMdb3ZYpkLVeRTjZ1MWbimlPseeLT7_FWntR8qBDW5p2UEiIde_rN4RasjB0Cqtp1G7zOkdaVFUYQmGsBUc-aYXyzlxpuv_tAeN1rJfcWjiHI?key=fSQhMkXZaLSnxkwxr-9KdY8U)  
  

Orders and Reviews
```
CREATE (:Order {id: 201, order_date: date("2025-04-01"), amount: 1200}),  
(:Order {id: 202, order_date: date("2025-04-20"), amount: 150}),  
(:Order {id: 203, order_date: date("2025-03-25"), amount: 900}),  
(:Order {id: 204, order_date: date("2025-04-28"), amount: 80});
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd5PtPxa4vECERIZiCCmXBWe59rhrq5rZ1tE4SltFNW14k5XkKIxRxqvInkqDgCLFVl7EHs1p5vAT8gbjKouoyHTch04rPBZC7x2l8n4IXMX_GMT6Fbl1Sd26mrGGE2sO-Tadtvcw?key=fSQhMkXZaLSnxkwxr-9KdY8U)

  

Relationships
```
// Order relationships  
MATCH (b1:Buyer {name: "Alice"}), (b2:Buyer {name: "Bob"}), (b3:Buyer {name: "Charlie"}),  
(p1:Product {name: "Laptop"}), (p2:Product {name: "Blender"}), (p3:Product {name: "Smartphone"}), (p4:Product {name: "Toaster"}),  
(o1:Order {id: 201}), (o2:Order {id: 202}), (o3:Order {id: 203}), (o4:Order {id: 204})  
CREATE (b1)-[:PLACED]->(o1),  
(o1)-[:CONTAINS]->(p1),  
(b2)-[:PLACED]->(o2),  
(o2)-[:CONTAINS]->(p2),  
(b1)-[:PLACED]->(o3),  
(o3)-[:CONTAINS]->(p3),  
(b3)-[:PLACED]->(o4),  
(o4)-[:CONTAINS]->(p4),  
(b1)-[:REVIEWS]->(p1),  
(b1)-[:REVIEWS]->(p3),  
(b2)-[:REVIEWS]->(p1),  
(b2)-[:REVIEWS]->(p2),  
(b3)-[:REVIEWS]->(p1),  
(b3)-[:REVIEWS]->(p3);
```
### Step 3: Aggregation Queries

#### Sample Example – Count total orders per user
```
MATCH (b:Buyer)-[:PLACED]->(o:Order)  
RETURN  b.name  AS  Buyer, COUNT(o) AS  TotalOrders;
```
### Your Turn

Write a query to:

-   Match all orders placed by users
    
-   Sum the amount for each buyer
    
-   Return buyer name and total amount spent
    

### Step 4: Use of COLLECT to Return Lists

#### Sample Example – List all products reviewed by each user
```
MATCH (b:Buyer)-[:REVIEWS]->(p:Product)  
RETURN  b.name  AS  Buyer, COLLECT(p.name) AS  ReviewedProducts;
```
### Your Turn

Write a query to:

-   Match all products bought by Bob
    
-   Return Bob's name and a list of product names he purchased
    

### Step 5: Date Filtering

#### Sample Example – Find all orders placed in the last 15 days
```
MATCH (o:Order)  
WHERE o.order_date >= date() - duration({days: 15})  
RETURN o.id, o.order_date;
```
### Your Turn

Write a query to:

-   Match all orders
    
-   Filter them by order_date between 2025-04-01 and 2025-04-30
    
-   Return order ID and order date
    

### Step 6: Multi-step Queries Using WITH

#### Sample Example – Find average price of TechPro products
```
MATCH (p:Product)  
WHERE p.brand = "TechPro"  
WITH p.category AS category, AVG(p.price) AS avgPrice  
RETURN category, avgPrice;
```
### Your Turn  

**Write a query to:**

-   Match all products reviewed by users  
      
    
-   Group by product  
      
    
-   Return product name and total review count  
    (Use WITH + RETURN)
    

### Step 7: Challenge Queries

#### Exercise 1: List products reviewed by more than 2 users

**Write a query to:**

- Match all products reviewed by users
- Group by product
- Filter products reviewed by more than 2 users
- Return product name and review count
    

#### Exercise 2: Find top 3 most purchased products

**Write a query to:**

-  Match all orders and the products they contain
- Count how many times each product appears
- Return top 3 products by purchase frequency
    

## Solutions

### Step 3

Aggregation – Total amount spent by each buyer  
  
```
MATCH (b:Buyer)-[:PLACED]->(o:Order)  
RETURN  b.name  AS  Buyer, SUM(o.amount) AS  TotalSpent;
```
  
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXco-AS-7O5EM5TSfA61wbP-pQ0NuYO42md2uYNOdNTtXTyBPMW3EOUNXu-jgIyprbpdBd2PXmr6KI8IuPOQ_AGpHx9AhHfQoLPl4nEINmxwpfzYsBUO_iLJ6orMGO0R84FPNc1d?key=fSQhMkXZaLSnxkwxr-9KdY8U)

### Step 4
COLLECT – Products purchased by Bob

```
MATCH (b:Buyer {name: "Bob"})-[:PLACED]->(:Order)-[:CONTAINS]->(p:Product)  
RETURN  b.name  AS  Buyer, COLLECT(p.name) AS  ProductsBought;
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcZlQ1nQu9oRLZ8onRfz4pUODEszA3QYfEn72hAMQIk14cebsm_ETvgdpZA6b1oY3h8zypbu8HgCmwc3XYD9uFPwmGOaUrVDNs5K0zXux4WUR7sBRt0jHLl6nFqy08BYMhL6HdW?key=fSQhMkXZaLSnxkwxr-9KdY8U)

### Step 5  
Date Range – Orders placed in April 2025  
```
MATCH (o:Order)  
WHERE o.order_date >= date("2025-04-01") AND o.order_date <= date("2025-04-30")  
RETURN o.id, o.order_date;
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiozDYNcj0jXO7bdFqdNx-xIZaaGp18fCvRERIggCLlBCC4dlKKef1fOhBuzRTSwI8S5GH7JGi-wNNAZiatk8f5ttUBvVNulBAWFwSPTn8W0PC0XFtL__hJApNXLGUbzRtl66grA?key=fSQhMkXZaLSnxkwxr-9KdY8U)

### Step 6  
WITH – Product review count  
```
MATCH (b:Buyer)-[:REVIEWS]->(p:Product)  
WITH p.name AS Product, COUNT(b) AS ReviewCount  
RETURN  Product, ReviewCount;
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiZMOxuy4TZYEapTmKpNXGfYBkAmmwVEoThKjXYHip8tMsdXvCG4pYW1CMmnbbVDOHLo2_DUg-ksmAI41wBmaFb3IIqCmYXTgXU1td1OOjANhs-3bVD6kT2a-4okGXiEBgQGUSGg?key=fSQhMkXZaLSnxkwxr-9KdY8U)

### Step 7
**Challenge 1 – Products reviewed by more than 2 users**  
  
```
MATCH (b:Buyer)-[:REVIEWS]->(p:Product)  
WITH p.name AS Product, COUNT(b) AS ReviewCount  
WHERE ReviewCount > 2  
RETURN  Product, ReviewCount;
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcdOG16A-1HvEduWeURX1Rg2HGriGtOdUun7DPMM9WXqIh_qH-VeADLKAo_cSq23ZR8vyxt3_VXDeZvB5X9DTUfluRqO8HOKLEEUzEqJP8Nf58SStriu_rtDz31lBqjwH4KExhB9g?key=fSQhMkXZaLSnxkwxr-9KdY8U)

### Step 7.1

**Challenge 2 – Top 3 most purchased products**  
  
```
MATCH (:Order)-[:CONTAINS]->(p:Product)  
WITH p.name AS Product, COUNT(*) AS PurchaseCount  
RETURN Product, PurchaseCount  
ORDER  BY PurchaseCount DESC  
LIMIT 3;
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcOgrgASCpV5CxYtlgmYf0kymduIYGNpt2_4_WaNWwx_5HHGDSjA4SpEk4tq1oYuBXA7vw6GkKQDp-9UYzNA_MVFg24W1TJb27k3V23bwJHhcLvHax6_Gw_SpW185ujFXDBJSZV?key=fSQhMkXZaLSnxkwxr-9KdY8U)

## Expected Outcome

By completing this lab, you will:

-   Use aggregations to analyze buyer and product data  
      
    
-   Query and structure list-based results  
      
    
-   Analyze orders by date using date() and filtering logic  
      
    
-   Apply WITH for intermediate computations  
      
    
-   Begin building analysis pipelines using Cypher patterns