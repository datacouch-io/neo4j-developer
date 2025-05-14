# Lab 1: Graph Data Modeling - "Simple E-Commerce System"

## Objective

Design a graph data model for a simple e-commerce platform. The goal is to identify nodes, relationships, and properties, and to draw an ERD (Entity-Relationship Diagram) using a whiteboard or paper.

## Scenario

The system requirements are as follows:

-   Customers can place orders.  
      
    
-   Each order can contain multiple products.  
      
    
-   Each product belongs to a specific category.  
      
    
-   Products are sold by different sellers.  
      
    
-   Customers can write reviews for products, including a rating and a comment.  
      
    
-   Each customer has a profile containing name, email, and address.  
      
    

## Step-by-Step Instructions

### Step 1: Identify Nodes

List all the distinct entities that should exist as nodes in the graph.

Questions to consider:

-   Who are the people or things involved?  
      
    
-   What objects need to be stored separately?
    

  

### Step 2: Identify Relationships

Define how nodes are connected by relationships.

Questions to consider:

-   What actions or links exist between different entities?  
      
    
-   Which node is the starting point, and which is the endpoint of each relationship?
    

  

### Step 3: Identify Properties

For each node and each relationship, identify key properties (attributes) that should be stored.

Questions to consider:

-   What information do we need to know about this node or relationship?
    

  

### Step 4: Draw the ERD (Graph Model)

On a whiteboard or plain paper:

-   Represent nodes as circles.  
      
    
-   Represent relationships as arrows connecting nodes.  
      
    
-   Write properties inside the node or alongside the relationship.  
      
    
-   Clearly label each relationship with a verb or action word (e.g., "PLACED", "CONTAINS").
    

  
  
  

## Submission Requirements

Submit a clear photo or scanned copy of your ERD diagram.

Ensure:

-   All nodes and relationships are properly labeled.  
      
    
-   All properties are clearly indicated.  
      
    
-   The diagram is easy to read.
    

## Important Notes

-   Focus on conceptual design rather than implementation.  
      
    
-   Ensure all critical entities and interactions from the scenario are included.
    

  

*Please check the solution below only once you are done and submit your answer.*

  

**Solution PDF download link:** [Lab2_Ecommerce_Solution](https://drive.google.com/file/d/1YSnL3d-V7oYRHh6854BTHUb_4Zouu1F7/view?usp=drive_link)

  

### 💡 Business Questions for Model Evolution

Now that you’ve built your initial model, your

business stakeholders have raised additional analytical needs.

Based on the following questions, evolve your model by introducing new properties, relationships, or labels/sub-labels (hierarchies):

  

**Requirement 1: Customer Reviews Sentiment:**

"Can we analyze the sentiment of customer reviews?"

  

**Requirement 2 Customer Segmentation:**

"Can we analyze customers by their behavior – such as frequency of purchases, average order value?"

  

**Requirement 3: Location-Based Recommendations:**

"Can we recommend local sellers or show delivery time estimates?"