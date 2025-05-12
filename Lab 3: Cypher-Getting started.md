# Lab 3: Getting Started with Cypher

Estimated Time: 20 mins

## Objective

The objective of this lab is to provide hands-on experience with Cypher, Neo4j’s declarative query language, to model and manipulate data in an e-commerce graph. By completing this lab, participants will learn to create nodes and relationships, assign properties, perform batch inserts, prevent duplication using MERGE, and query the graph structure efficiently.

## Prerequisites

Before beginning this lab, ensure the following are in place:

-   A working [Neo4j Aura](https://console.neo4j.io/) account with an active instance.
    
-   Basic knowledge of graph database concepts (nodes, relationships, properties).
    
-   Completion of Lab 2: Introduction to Neo4j Aura or equivalent familiarity with uploading data and navigating the Neo4j interface.
    
-   Familiarity with using a web-based query editor.
    

## Lab Overview

This lab builds on your previous graph modeling work by introducing Cypher — Neo4j’s powerful query language. You will expand an e-commerce graph model by manually creating buyers, sellers, products, and orders using CREATE, and connect them through realistic relationships such as BUYS, SELLS, FOLLOWS, PLACED, and CONTAINS. You’ll use MERGE to prevent duplicate entries and UNWIND to batch insert data. The lab concludes with basic queries to explore and verify your graph structure. This practical exercise solidifies your ability to construct and manage graph data programmatically.

## Scenario

You are continuing development of the e-commerce platform where:

-   Buyers purchase Products sold by Sellers.  
      
    
-   Buyers can follow Sellers, recommend Products to friends, and place Orders.  
      
    
-   New types of interactions like orders are modeled.
    

## Step-by-Step Instructions

### Step 1: Log into Neo4j Aura

-   Visit: [https://console.neo4j.io/](https://console.neo4j.io/)
    
-   Create or select an instance.  
      
    
-   Connect to the Neo4j Browser.
    

### Step 2: Create Nodes

1.  Click on “Query” section.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcP0eDSz8LEJnRE1gNHzhB3NhTKNUMVc9PgkHnoQNdt9P8uektLzEzDAj1hPhtVkZqKWpe3hTjlKHbKEQTIf2D6eEVi7K_MjgQKsmSs_zJiHCy2KOafEWMhtckcnq4TRrmHP1ch?key=8DB8J4SCCoOVJG5UrjanCcyJ)

2.  Use Cypher CREATE to insert sample buyers, sellers, products, and orders.
	```
	// Create Buyer Nodes  
	CREATE (b1:Buyer {id:  1, name:  "Alice", email:  "alice@example.com"}),  
	(b2:Buyer {id:  2, name:  "Bob", email:  "bob@example.com"});  
	 ``` 

**Your Tasks:**

-   Write queries to create:  
      
    

-   Two Seller nodes: TechStore (id=101) and HomeEssentials (id=102)  
      
    
-   Two Product nodes: Laptop (id=201, price=1200) and Vacuum Cleaner (id=202, price=200)  
      
    
-   Two Order nodes: Order 301 and 302 with respective dates and amounts.  
      
  
> Tip: Use the example format to create these nodes.

  
3.  Paste the query and click Enter or click on the icon to process the query.
    
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfivFWem6EcBI6ygDglv-M5G-QoFzsmEjl1h9TKtdjIwDDlz2HuN2JnGI0C7a0dbVMuxnjqxB2KoputkI7al0jY05tKrX-A5BXzS0RWHIW3AoxN1SdZ1wtyGYqRI8L-gMdOWDohhw?key=8DB8J4SCCoOVJG5UrjanCcyJ)

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfKDriwW93gkp177Lad-OM8WUODB1cq6F28qzBQ-f-z27xXV4SWwXAq-2AWObvBI9hx5fG6pMs8fpG8-89lVVn6ARjeACdkzYB9ENabrRozgUPp4tTPOMGKyRJgUAMTWPAqImou?key=8DB8J4SCCoOVJG5UrjanCcyJ)


### Step 3: Create Relationships

Use Cypher MATCH + CREATE to add meaningful relationships.

1.  Enter the query:
    
	```
	// Buyer buys a product  
	MATCH (b:Buyer {name: "Alice"}), (p:Product {name: "Laptop"})  
	CREATE (b)-[:BUYS]->(p);  
	```  
**Your Tasks:**

-   Write queries to create:
    
	**Relationship 2: Seller sells a Product**  

	-   Connect TechStore (Seller) to Laptop (Product) using a SELLS relationship.  

	**Relationship 3: Buyer follows a Seller**

	-   Connect Bob (Buyer) to HomeEssentials (Seller) using a FOLLOWS relationship.
    
	**Relationship 44: Buyer places an Order**

	-   Alice placed an Order with id = 301.
	    
	-   You have to match the Buyer and the Order nodes.
	    
	-   Add PLACED relationship between Buyer and Order
    
	**Relationship 5: Order contains Product**

	-   The Order 301 should contain the Laptop.
	-   Add CONTAINS relationship between Buyer and Order  


![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfXWz82EAZ2UbKL7utintNh-iPIzscS0ddfrylBhMTGKtyTeW2A2EDLcOpS0ycmdxbCTdY4rIx12RMtRHbSzrFoGwfO58tzKl_9SlvrKwH8E-SIlmbFl056ZyWWFJIIWt5b2YpvrQ?key=8DB8J4SCCoOVJG5UrjanCcyJ)

  
  

### Step 4: Using MERGE to Avoid Duplicates

If you want to ensure you don't create duplicate buyers, sellers, or products, use MERGE:

1.  Enter the query:
	```    
	// Merge ensures no  duplicate Alice  
	MERGE (b:Buyer {email: "alice@example.com"})  
	ON  CREATE  SET b.name = "Alice", b.id = 1  
	ON  MATCH  SET b.last_login = timestamp();
	```
  
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfBvo5HPibWGWzUHNrnd-cNgdXgfWzDQLCGPxf1nqs63JNd0HsuyEAxUBLRhcaZsl4w2f6JXvnsnv5y2VlXS4ZUSAdXEzcY9bTLzLUZ7u3Anc8hGIpf1zAjf_RJ0vetyhSJuUsPjg?key=8DB8J4SCCoOVJG5UrjanCcyJ)

**Notes:**

-   ON CREATE block runs if node didn’t exist.  
      
-   ON MATCH block runs if node already exists.
    
### Step 5: Batch Insert New Data

Batch inserting helps when inserting large sets.
```
UNWIND [  
{id:  3, name:  "Charlie", email:  "charlie@example.com"},  
{id:  4, name:  "Diana", email:  "diana@example.com"}  
] AS buyer  
CREATE (:Buyer {id: buyer.id, name: buyer.name, email: buyer.email});
```

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdAWS6pzPzEJJvRfQ_hLtIr7AMJhEo24_Oc2_K7xqHk-pgyMVgIrPAfe7gAexTamkzSHT4HG_q6Qc9S6RlAaOtjoqKa_kmzXNeGbKIAaZaXSEj20P6XF095hF3uufrmRj7rrnoy?key=8DB8J4SCCoOVJG5UrjanCcyJ)

### Step 6: Query Your Graph

1.  #### View all nodes
 
	```   
	MATCH (n) RETURN n;
	```

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf34q4p8fsYMIlql5pDM5YirNEmcYrEkCb-h91MNbD5s4tjNG4qK5IvjrojikyXqmU01r7-3O56sgD1UKtvd48_xJg2NLF9VCLpluz3vmVMsitZ4QVE3_VwIOJ6wdc0iK9oW58nsA?key=8DB8J4SCCoOVJG5UrjanCcyJ)

2.  View all relationships

	```    
	MATCH (a)-[r]->(b) RETURN  a, r, b;
	```

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdCehmCX_QRyqtBVJGuVOrB3JTTCz0kz2w5QEjCqSDuHg6DKsdMrVJpthQrjD13WxXsGY_isNZFWoaIb13pBMaHLXpGE0bbDbfUOeWv5DIuhybPy7Wyen4oStoVwl5ITM8-L-Xh3A?key=8DB8J4SCCoOVJG5UrjanCcyJ)

## Expected Outcome

By the end of this lab, you will have:

-   Created buyers, sellers, products, and orders.  
      
    
-   Connected them meaningfully.  
      
    
-   Used MERGE to prevent duplication.  
      
    
-   Practiced batch insertion.
    
## Solutions

### Step 2: Create Nodes

Use Cypher CREATE to insert sample buyers, sellers, products, and orders.

```
// Create Seller Nodes  
CREATE (s1:Seller {id:  101, name:  "TechStore", store_name:  "TechWorld"}),  
(s2:Seller {id:  102, name:  "HomeEssentials", store_name:  "HomeWorld"});  
  
// Create Product Nodes  
CREATE (p1:Product {id:  201, name:  "Laptop", price:  1200, category:  "Electronics"}),  
(p2:Product {id:  202, name:  "Vacuum Cleaner", price:  200, category:  "Home Appliances"});  
  
// Create Order Nodes  
CREATE (o1:Order {id:  301, order_date:  "2024-04-01", amount:  1200}),  
(o2:Order {id:  302, order_date:  "2024-04-02", amount:  200});
```
  
### Step 3: Create Relationships

Use Cypher MATCH + CREATE to add meaningful relationships.

Enter the query:
    
```
// Buyer buys a product  
MATCH (b:Buyer {name: "Alice"}), (p:Product {name: "Laptop"})  
CREATE (b)-[:BUYS]->(p);  
  
// Seller sells a product  
MATCH (s:Seller {name: "TechStore"}), (p:Product {name: "Laptop"})  
CREATE (s)-[:SELLS]->(p);  
  
// Buyer follows Seller  
MATCH (b:Buyer {name: "Bob"}), (s:Seller {name: "HomeEssentials"})  
CREATE (b)-[:FOLLOWS]->(s);  
  
// Buyer recommends product  
MATCH (b1:Buyer {name: "Alice"}), (b2:Buyer {name: "Bob"}), (p:Product {name: "Laptop"})  
CREATE (b1)-[:RECOMMENDS {comment: "Great for gaming!"}]->(p),  
(b1)-[:FRIENDS_WITH]->(b2);  
  
// Buyer places an order  
MATCH (b:Buyer {name: "Alice"}), (o:Order {id: 301})  
CREATE (b)-[:PLACED]->(o);  
  
// Order contains product  
MATCH (o:Order {id: 301}), (p:Product {name: "Laptop"})  
CREATE (o)-[:CONTAINS]->(p);
```