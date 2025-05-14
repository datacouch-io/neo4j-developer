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

## Step 1: Clean Up the Database
```
MATCH (n) DETACH DELETE n;
```
To make sure all the old data is deleted, go to Instance and click on the icon.![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeY3OLP2xzb8LoBk2ZmNtuxRzjvyqCBH2TtTEber0B8-tRpYro6cB-8C0fwDl7zdeHow5rPxGnqwItIWdZGSmbqghS14aqWTcdUjQ3kGJNmHQ9mNszAny8jvln7-bk79LwIQilk?key=fSQhMkXZaLSnxkwxr-9KdY8U)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdJCyHDlEdqLSL4P99DKbqINjPFuRxwTymhdpfpkyGEQ3CsbOJpwzJlYnh1ieXHgt74gIIA9tkQHGgzz5ZqJmrLqbraBckaZSNY3blSszXWfPwVv8GzCvsSs5XAjVQ17czc4N8TvQ?key=fSQhMkXZaLSnxkwxr-9KdY8U)

Click on “Reset to blank” and then click on “Reset”.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcYYCUNO_ng-lcS6Owp2CS7YKyty1M2ZUYdwHI_RNEFVNckK8SOD7muXEK3eHFY7SLu_p0f-Mqbh1KmJbqWe9_t-WYHLnbaBszoHgq3Esh9wD5ChZPR3jYMZRn8d2AL-IJPgdhb?key=fSQhMkXZaLSnxkwxr-9KdY8U)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcHJMsIchpvPH1Mo2MxJoYm_Fv5JGRjTJciuTdPcrf7UIAyzc5cRBda-oFSmnC8D8fKYbAnDYVuKVXVH2oeInXtZIOm8nIAJQeG32pdtrLVaE-q7D36LiCW3Rls1HiYjOKO1QSCNA?key=fSQhMkXZaLSnxkwxr-9KdY8U)

Come back to the Query Section, refresh and ensure that the nodes and relationships are not there.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXezxvLD3fXDHxrF-k12v_GOpDMGSbw9UcfkP4-v99UCIVrQhsv4krYfIeHgKhLlAFiJ6kJDpCW6fGgTZ6twyKPUVXFpBDCI_hV_2m53sUoVSfBV1nCKWYBHW3gcP2FFSIXqf-m4?key=fSQhMkXZaLSnxkwxr-9KdY8U)

This will clear any previously created data to ensure a consistent starting point.

## Step 2: Create Sample Data  
Buyers
```
CREATE (:Buyer {id: 1, name: "Alice", email: "alice@example.com"}),  
(:Buyer {id: 2, name: "Bob", email: "bob@example.com"}),  
(:Buyer {id: 3, name: "Charlie", email: "charlie@example.com"});
```
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdN26N7q89HMtpw4kqysle04MSTHgQfSWRlJPw71TPpcmxJVytIjf3s7Xstialv-DNss7GT9-KWuYuv4eh2CvBl3pngwdB59GbNv9_T4k8vj3n4VsF4c3w5frIM_rrAN3NiBoDrmA?key=fSQhMkXZaLSnxkwxr-9KdY8U)

  
Products
```
CREATE (:Product {id: 101, name: "Laptop", price: 1200, category: "Electronics", brand: "TechPro"}),  
(:Product {id: 102, name: "Blender", price: 150, category: "Home Appliances", brand: "HomeMax"}),  
(:Product {id: 103, name: "Smartphone", price: 900, category: "Electronics", brand: "TechPro"}),  
(:Product {id: 104, name: "Toaster", price: 80, category: "Home Appliances", brand: "HomeMax"});
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdS9K6Aln9tsf3h9QDVO0eCux3sfmX2pPh2q54URf4wAYvNr5p6aceg5HUc7Bg_znEbSmogf4LtVeoD4HAxTKo7fBgPyuIFXtyA58UKOxGSzUn0E-hOMnUiQguTep_t-X5vj49E?key=fSQhMkXZaLSnxkwxr-9KdY8U)  
  

Orders and Reviews
```
CREATE (:Order {id: 201, order_date: date("2025-04-01"), amount: 1200}),  
(:Order {id: 202, order_date: date("2025-04-20"), amount: 150}),  
(:Order {id: 203, order_date: date("2025-03-25"), amount: 900}),  
(:Order {id: 204, order_date: date("2025-04-28"), amount: 80});
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcb5eTlcZVfMYq_nPS3gtD1SjnLQuS3yZrnk5aQgWRy4ZuXEMKutc8a4cyyf8jmGT0IgM80aklqgkzvLb3F-bpvXWSVG62lkNFtmfP9zWNs_zHKPjJKQhFgC2EJNGuJGvHKQjsUpg?key=fSQhMkXZaLSnxkwxr-9KdY8U)

  

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
## Step 3: Aggregation Queries

### Sample Example – Count total orders per user
```
MATCH (b:Buyer)-[:PLACED]->(o:Order)  
RETURN  b.name  AS  Buyer, COUNT(o) AS  TotalOrders;
```
### Your Turn

Write a query to:

-   Match all orders placed by users
    
-   Sum the amount for each buyer
    
-   Return buyer name and total amount spent
    

## Step 4: Use of COLLECT to Return Lists

### Sample Example – List all products reviewed by each user
```
MATCH (b:Buyer)-[:REVIEWS]->(p:Product)  
RETURN  b.name  AS  Buyer, COLLECT(p.name) AS  ReviewedProducts;
```
### Your Turn

Write a query to:

-   Match all products bought by Bob
    
-   Return Bob's name and a list of product names he purchased
    

## Step 5: Date Filtering

### Sample Example – Find all orders placed in the last 15 days
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
    

## Step 6: Multi-step Queries Using WITH

### Sample Example – Find average price of TechPro products
```
MATCH (p:Product)  
WHERE p.brand = "TechPro"  
WITH p.category AS category, AVG(p.price) AS avgPrice  
RETURN category, avgPrice;
```
### Your Turn  
  

Write a query to:

-   Match all products reviewed by users  
      
    
-   Group by product  
      
    
-   Return product name and total review count  
    (Use WITH + RETURN)
    

Step 7: Challenge Queries

### Exercise 1: Top Reviewed Products: Which products have the most reviews?

### Exercise 2: List products reviewed by more than 2 users

### Write a query to:

-   Match all products reviewed by users
    
-  Group by product
    
-   Filter products reviewed by more than 2 users
    
-  Return product name and review count
    

### Exercise 3: Find top 3 most purchased products

### Write a query to:

-   Match all orders and the products they contain
    
-   Count how many times each product appears
    
-   Return top 3 products by purchase frequency
    

  
  
  
  
  
  
  
  
  
  

Some more Advanced Queries for you to check

  

### 🔹Products Reviewed But Not Ordered by Buyer

Business Requirement: Who is reviewing products they didn’t buy?

  
```
MATCH (b:Buyer)-[:REVIEWS]->(p:Product)

WHERE NOT EXISTS {

MATCH (b)-[:PLACED]->(:Order)-[:CONTAINS]->(p)

}

RETURN b.name AS Buyer, p.name AS ReviewedProduct;
```
  
  
  
  
  
  

## Solutions

**Step 3** : Aggregation – Total amount spent by each buyer  
  
```
MATCH (b:Buyer)-[:PLACED]->(o:Order)  
RETURN  b.name  AS  Buyer, SUM(o.amount) AS  TotalSpent;
  ```
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcUay14haWVvCCt5M4nSsQdDkvqVxZdI5tD9jUb8x-rceh1c_5in5LSislrP1l4u1bbq8UBARQDjEe5qherhDeecHw6FjhU9eIax07gg73G4BiGoHwyABCF4s5GOqukboZJZbLb?key=fSQhMkXZaLSnxkwxr-9KdY8U)

  

**Step 4:** COLLECT – Products purchased by Bob

 ``` 
MATCH (b:Buyer {name: "Bob"})-[:PLACED]->(:Order)-[:CONTAINS]->(p:Product)  
RETURN  b.name  AS  Buyer, COLLECT(p.name) AS  ProductsBought;
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdlWsbQ5OPL-rv2nKV_KXLsEX2IBXGRt1CJhjd_srDc1sSzwdVW5lzvuW02My5aB3bHd7mYyxK5oE4gOeMPldPqylffh8WLfP_E3s6MAxrxATfOdPi6JciEddOborzxXOlIjYAd?key=fSQhMkXZaLSnxkwxr-9KdY8U)

  
  
  

**Step 5:** Date Range – Orders placed in April 2025  
  
```
MATCH (o:Order)  
WHERE o.order_date >= date("2025-04-01") AND o.order_date <= date("2025-04-30")  
RETURN o.id, o.order_date;
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcFL-Yob-UnsqJBkac_1aHqWnRhoE2PKSQhbf0A8hH7M7JnFcJJW047Yz0LPV9AX1qHF69BFIx2YBEK5_dpvmE5XPCsnammLij5mgGHVtlzPTul2ClGkbyuPGMCn4Yem_NhlXV-qg?key=fSQhMkXZaLSnxkwxr-9KdY8U)

  

**Step 6** : WITH – Product review count  
  
```
MATCH (b:Buyer)-[:REVIEWS]->(p:Product)  
WITH p.name AS Product, COUNT(b) AS ReviewCount  
RETURN  Product, ReviewCount;
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdqMY-n-xcWuCQYNIsLu9RYQnurdj86huv7x3KmzPYxZnbJ6M-zygHYpldtoDcWZFFMXukjS0wpKvLPELiRrnIAOes3MhJeGGYdsIaZ7Tpplpex5ksb9TQjT1fdbj-P-5fiTzswmg?key=fSQhMkXZaLSnxkwxr-9KdY8U)

  
**Step 7.1**

Challenge 1 - Top Products with maximum reviews

```  
MATCH (b:Buyer)-[:REVIEWS]->(p:Product)

RETURN p.name AS Product, COUNT(b) AS ReviewCount

ORDER BY ReviewCount DESC

LIMIT 5;
```
  
  
  

**Step 7.2**

  

Challenge 2 – Products reviewed by more than 2 users  
  
```
MATCH (b:Buyer)-[:REVIEWS]->(p:Product)  
WITH p.name AS Product, COUNT(b) AS ReviewCount  
WHERE ReviewCount > 2  
RETURN  Product, ReviewCount;
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc185B2ODFHshlnbpNXyWg_pOlGOMvPVGvLE-RIe4sHEDrP8RsU_-MpKddRid66VWKvI2aK-jirOV9-5gQTloRIOm8lEpt7hkjDzObIZHSNmG7ZaEKB5R_4LjizaXbQ7Kzj9gUIow?key=fSQhMkXZaLSnxkwxr-9KdY8U)

  
  

**Step 7.3**

  

Challenge 3 – Top 3 most purchased products  
  
```
MATCH (:Order)-[:CONTAINS]->(p:Product)  
WITH p.name AS Product, COUNT(*) AS PurchaseCount  
RETURN Product, PurchaseCount  
ORDER  BY PurchaseCount DESC  
LIMIT 3;
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf7hNkUz7dLqxWKmKwcys0-TqDzVBi3iUQIyAqNG9Bv0jfyPXnHx6dkIKphF4_JzukaRtKrkKDH2eQdjPgR-dAXNFAKXjoML9jTBMEqUGopdddcWX-a8HZvSHLPtZgkLmAjS8Zv?key=fSQhMkXZaLSnxkwxr-9KdY8U)

  

## Expected Outcome

By completing this lab, you will:

-   Use aggregations to analyze buyer and product data  
      
    
-   Query and structure list-based results  
      
    
-   Analyze orders by date using date() and filtering logic  
      
    
-   Apply WITH for intermediate computations  
      
    
-   Begin building analysis pipelines using Cypher patterns