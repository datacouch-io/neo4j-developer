# Lab 4: Querying the Graph (Basic Cypher Querying)

E-commerce Graph Analytics - Retrieval and Pattern Matching

## Objective

The objective of this lab is to develop core querying skills using Cypher, Neo4j’s query language, in the context of an e-commerce graph database. Participants will learn to retrieve and filter data using MATCH, RETURN, and WHERE, apply pattern matching for real-world scenarios, and construct logical queries to answer business questions such as customer activity, product reviews, and order history.

## Prerequisites

To successfully complete this lab, participants should have:

-   A running Neo4j Aura instance
    
-   Core graph entities (e.g., Buyers, Products, Orders, Reviews, Sellers) already created and linked with relationships.
    
-   Basic familiarity with Cypher syntax and Neo4j Browser interface.
    
-   The provided lab setup script executed to initialize consistent data for querying.
    

## Lab Overview

In this lab, you will transition from graph modeling to graph querying. Using Cypher, you will retrieve information from your e-commerce graph by writing pattern-matching queries. This includes filtering nodes based on property values, finding relationships and interactions (like purchases and reviews), and applying logical conditions to combine criteria. You’ll also answer practical business questions - for example, listing products a user purchased, identifying recent orders, and filtering products by rating or category. This lab solidifies your understanding of how to extract insights from a graph database using Cypher - a critical skill in any data-driven application.

## Real-World Scenario

Now that you have modeled your e-commerce system with products, buyers, orders, and reviews, it’s time to start asking questions like:

-   Which users purchased a given product?  
      
    
-   What are the most reviewed items?  
      
    
-   What orders were placed in the last 30 days?  
      
    
-   Which products cost more than a certain threshold?  
      
    

These are common graph traversal and filtering questions - exactly what Cypher was designed for.

## Lab Initialization: Cleanup
```
MATCH (n) DETACH DELETE(n)
```
  

## Lab Initialization: Setup Sample Data

To ensure that all future queries return valid and relevant results, please execute the following setup script once at the beginning of this lab. It prepares a consistent dataset with buyers, products, orders, and realistic relationships for graph analysis.

  

Now run the following command:

  
```
// === Buyers ===  
MERGE (alice:Buyer {name: "Alice", email: "alice@example.com", location: "New York"})  
MERGE (bob:Buyer {name: "Bob", email: "bob@example.com", location: "California"})  
  
// === Sellers ===  
MERGE (s1:Seller {name: "TechStore", store_name: "TechWorld"})  
MERGE (s2:Seller {name: "HomeEssentials", store_name: "HomeWorld"})  
  
// === Products ===  
MERGE (p1:Product {  
product_id: "P101", name: "Laptop", description: "Gaming Laptop", category: "Electronics",  
price: 1200, currency: "USD", stock_quantity: 25, brand: "Lenovo", rating: 4.7,  
created_at: datetime("2024-12-15")  
})  
MERGE (p2:Product {  
product_id: "P102", name: "Vacuum Cleaner", description: "High suction vacuum", category: "Home Appliances",  
price: 350, currency: "USD", stock_quantity: 40, brand: "Dyson", rating: 4.5,  
created_at: datetime("2025-01-10")  
})  
MERGE (p3:Product {  
product_id: "P103", name: "Wireless Earbuds", description: "Bluetooth earbuds", category: "Electronics",  
price: 80, currency: "USD", stock_quantity: 100, brand: "Sony", rating: 4.2,  
created_at: datetime("2025-02-10")  
})  
MERGE (p4:Product {  
product_id: "P104", name: "Microwave Oven", description: "Compact oven", category: "Home Appliances",  
price: 450, currency: "USD", stock_quantity: 15, brand: "Panasonic", rating: 4.6,  
created_at: datetime("2025-03-10")  
})  
  
// === Orders ===  
MERGE (o1:Order {order_id: "O301", order_date: date() - duration({days: 15}), amount: 1200})  
MERGE (o2:Order {order_id: "O302", order_date: date() - duration({days: 10}), amount: 80})  
MERGE (o3:Order {order_id: "O303", order_date: date() - duration({days: 35}), amount: 450})  
  
// === Relationships ===  
// Buyers placed orders  
MERGE (alice)-[:PLACED]->(o1)  
MERGE (alice)-[:PLACED]->(o2)  
MERGE (bob)-[:PLACED]->(o3)  
  
// Orders contain products  
MERGE (o1)-[:CONTAINS]->(p1)  
MERGE (o2)-[:CONTAINS]->(p3)  
MERGE (o3)-[:CONTAINS]->(p4)  
  
// Buyers reviewed products  
MERGE (alice)-[:REVIEWS {rating: 5, comment: "Amazing product!"}]->(p1)  
MERGE (bob)-[:REVIEWS {rating: 4, comment: "Decent value"}]->(p2)  
  
// Direct BUYS relationships (for advanced querying)  
MERGE (bob)-[:BUYS {purchase_date: "2025-04-15", quantity: 1, payment_method: "Credit Card", rating: 4.5}]->(p2)  
MERGE (alice)-[:BUYS {purchase_date: "2025-04-10", quantity: 1, payment_method: "Credit Card", rating: 5}]->(p1)
```
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcAurLZb92nG9y9ImlR36HxIFbzoB_apUXN0pco-9WqN2d_1v11rPJ-nx_CEZ3k3fRxKk_ILieyYdzcWwd0v3Xcu4PwJVaSPiFXwZYJyM_Kuqp5k8Xbq8y0NB0p087PflFIN97eUg?key=RIKNCgfgalpOddP8aiexC5jX)

## Practice Insert (For Testing)

You can insert your own test products using this structured template:
```
CREATE (p:Product {  
product_id: '________',  
name: '________',  
description: '________',  
category: '________',  
price: ________,  
currency: '________',  
stock_quantity: ________,  
brand: '________',  
rating: ________,  
created_at: datetime('________')  
});
```
Try creating a few diverse entries with varying prices, brands, and ratings. This will help you practice all the queries above.

## Step 1: Basic Retrieval with MATCH + RETURN

### Sample Example
```
// Retrieve all products  
MATCH (p:Product)  
RETURN p.name, p.price, p.category;
```
  

### Your Task

Retrieve all buyers with their names and email addresses.
```
// Template  
MATCH (________:Buyer)  
RETURN ________, ________;
```
## Step 2: Filtering with WHERE Conditions

### Sample Example
```
// Find products priced above $100  
MATCH (p:Product)  
WHERE p.price > 100  
RETURN p.name, p.price;
```
### Your Task

Find all products in the "Electronics" category that are priced under $500.
```
// Template  
MATCH (p:Product)  
WHERE ________ AND ________  
RETURN p.name, p.price, p.category;
```
  

## Step 3: Pattern Matching – Real Interactions

### Sample Example
```
// Find all products that have reviews  
MATCH (p:Product)<-[:REVIEWS]-(:Buyer)  
RETURN p.name, count(*) AS review_count;
```

### Your Task

Write a query to find all users who purchased a product named “Laptop”.
```
// Template  
MATCH (________:Buyer)-[:PLACED]->(:Order)-[:CONTAINS]->(________:Product {name: "Laptop"})  
RETURN  ________;
```
## Step 4: Logical Combination Queries

### Sample Example
```
// Find buyers from New York or California  
MATCH (b:Buyer)  
WHERE  b.location = "New York" OR b.location = "California"  
RETURN  b.name, b.location;
```
### Your Task

Find products in the “Home Appliances” category with price greater than 300 and rating above 4.
```
// Template  
MATCH (p:Product)  
WHERE ________  AND  ________  AND  ________  
RETURN p.name, p.price, p.rating;
```
  
  
  
  

## Step 5: Sample Business Queries

Query 1: Find all orders placed in the last 30 days  
  
```
// Template  
MATCH (o:Order)  
WHERE o.order_date >= date() - duration({days: ________})  
RETURN o.order_id, o.order_date;
```
  

Query 2: List all products purchased by a particular user (e.g., “Alice”)
```
// Template  
MATCH (b:Buyer {name: "________"})-[:PLACED]->(:Order)-[:CONTAINS]->(p:Product)  
RETURN  DISTINCT  p.name, p.price;
```
  

## END OF LAB

  
  
  
  
  
  
  
  
  
  
  
  
  

## Solution Key

**Step 1**: Retrieve all Buyers

  
```
MATCH (b:Buyer)  
RETURN  b.name, b.email;
```
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXftyX5UIuR5Gh5PGLtmKLVQudxIu-ZNb22O5670mKvQuD0Lb_hh58LOP7yn-VOnz4-bFtzaQwYukj1mIP8YkajSqtMXOOBJwP6AIiuIAZwMl9yEI2rpGpxJMJ-w20UqKqOeMscU7A?key=RIKNCgfgalpOddP8aiexC5jX)

**Step 2**: Products in Electronics under $500
```
MATCH (p:Product)  
WHERE p.category = "Electronics"  AND p.price < 500  
RETURN p.name, p.price, p.category;
```
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcpH1Efa52IzSevl63FO2zWgLCF0KplvVQn1f28cFOVObFmErbK-vrEF6NVfWyGoO1LEsASg2wrHuf5jBHcOjZHVqXV_Sd8lEk-Vodi7zrPaNfqKLvOUxGX5eD-Gkrdo9-tv8Wyzg?key=RIKNCgfgalpOddP8aiexC5jX)

**Step 3**: Users who bought “Laptop”
```
MATCH (b:Buyer)-[:PLACED]->(:Order)-[:CONTAINS]->(p:Product {name: "Laptop"})  
RETURN  DISTINCT  b.name;
```
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcV4vQlkv1pM9wEaImzxFLrZL76ANaN92fi5qtblZL2lTomygB48vvUcwKlMdEh64dVovLywF4qV9JlVUCwnRXbUrJv1_6WVfa4CDDumizkXtIAmGj0eBMM4ovWibPmoGy2iiItaA?key=RIKNCgfgalpOddP8aiexC5jX)

**Step 4**: Home Appliances with high price and rating
```
MATCH (p:Product)  
WHERE p.category = "Home Appliances"  AND p.price > 300  AND p.rating > 4  
RETURN p.name, p.price, p.rating;
```
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdjLEp1mgMkkk-PyKdhiajl9UwSGNiUvguIfaZ1eqn7tmW9ruTTf3w2w7QCuDXD9qYVs2E0Vn6hillMCHSRk89tTF9CMhiahCIv8WAKF7ip0QvZXMwmopjXd6snsyxukqtb2IFh?key=RIKNCgfgalpOddP8aiexC5jX)

**Step 5.1**: Orders in last 30 days
```
MATCH (o:Order)  
WHERE o.order_date >= date() - duration({days: 30})  
RETURN o.order_id, o.order_date;
```
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeSIkAgae3RpgqYHK3Re4JncpL8C6ViWhcvrdeP3Vt1rMvACevSqDmBEjJlRPaaN7zMitXYf7sY3-2874PnHhIeXdfHjO70kQnjOPP5enKa4r4a5vvDhXOFNuvpaAILx_UXapZE_g?key=RIKNCgfgalpOddP8aiexC5jX)

**Step 5.2**: Products purchased by "Alice"
```
MATCH (b:Buyer {name: "Alice"})-[:PLACED]->(:Order)-[:CONTAINS]->(p:Product)  
RETURN  DISTINCT  p.name, p.price;
```
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXesflGDdK9tq_ju5LrL6FWyo5iRIfjQQdWLL3y8ggkbvybHMoLb7ZxWK-QLFYFLv0XX6yMaXFUpiyJrJ92O2PqKeAILCBQ2lt_KCBe4NuFCcUI8a3-lOcBq6gFguN8Sdlr9OA3W9A?key=RIKNCgfgalpOddP8aiexC5jX)

**Expected Outcome**

  

By the end of this lab, you will be able to:

-   Use MATCH and RETURN to retrieve nodes and relationships from a Neo4j graph  
      
    
-   Apply WHERE filters to narrow down query results based on property values  
      
    
-   Perform pattern matching to identify interactions such as purchases and reviews  
      
    
-   Combine multiple conditions using logical operators (AND, OR)  
      
    
-   Query the graph to answer realistic business questions - such as identifying recent orders, filtering by price and rating, or tracing customer purchase history  
      
    

You will also have built confidence working with the Cypher query language to analyze an e-commerce graph and extract actionable insights. These are critical foundational skills for any graph-driven application.