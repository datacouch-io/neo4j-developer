# Lab 2: Introduction to Neo4j Aura

## Objective

The objective of this lab is to introduce participants to the Neo4j Aura cloud platform and guide them through the process of importing a dataset and exploring graph data visually. By the end of this lab, participants will be able to navigate the Neo4j Aura interface, upload CSV-based data using the built-in import tool, and interpret nodes, relationships, and property keys using both graphical and query-based methods.

## Prerequisites

Before starting this lab, ensure the following requirements are met:

-   A registered [Neo4j Aura](https://neo4j.com/cloud/aura/) account (Free or Paid version).
    
-   Basic understanding of graph database concepts (nodes, relationships, properties).
    
-   Access to the lab’s dataset (CSV files), downloadable from:  
    [Lab Dataset Folder](https://drive.google.com/drive/folders/1C1nykfGwm4OaQZnrE82qIQY2G3fFRIxu?usp=drive_link)
    
-   A modern web browser (Google Chrome, Firefox, or Microsoft Edge).
    

## Lab Overview

In this lab, participants will work directly in the Neo4j Aura cloud environment to gain practical experience with graph databases. The lab begins by logging into the Neo4j console and connecting to an instance. Participants will then upload CSV files using the integrated Data Importer, automatically creating graph nodes and relationships. The lab concludes with an exploration of the data through the visual “Explore” interface and basic querying using the Cypher Query Editor. This hands-on experience will reinforce understanding of graph structures, data models, and the Neo4j Aura UI.

# Step-by-Step Instructions

## Step 1: Log in to Neo4j Browser

1.  Open your browser and go to:
    

https://console.neo4j.io/

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfgLnnccSE9sLoW57_w18eg63jBJehNrptZrNT3QQY8z_h2_I5rD2R2CtNoQqM_a_aEUTQ_2K3IuSYOjC4eCWheHIXE9MaC4phk3v1MtkDHkJ4A0C2pkF5suynSLSUBGgZjuqDo?key=MVUMBubVWObqGhv-nBk1M66o)

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfD05rw9mei7VdnR0llzN07178Y3qDGQyPhQAzoCM_3Gk_R79yxDNSzhTqmi44-AQWvXbWTpLnkq0c4dxrDzgwADjNy3b7eNh6vukfCAvhkTyeeeLAy-2KqluTsRblHwRsE7TfT?key=MVUMBubVWObqGhv-nBk1M66o)

2.  Select the version (paid or free)
    

Copy the key and click on download and continue

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeAZoNy52OSZzAWiOOUEAfv1qr9ryWGEe9mhs-5Kq0hJN1tm3EjWX-MLIa-amVnxsAWeahxD3RwavB4GyvNVjylXjv7UMVrbOeXQXR1Dkmk79RZoDuxxWzjNUvrLa6IwLyx1n0V?key=MVUMBubVWObqGhv-nBk1M66o)

3.  Instances are created, now select Query and connect to an instance. You will be forwarded to the query page.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeuBcM2i_VgdQ4iifha6vV1iwqlhQISSL9xDL5x--NiyLfyvShpc6lDGZH-jZWvLlEUcrlvXRYSQVaJ_6EcqPYmpKLgKD_1KMAZC5hn8ZUWNh6SEA5iC8ZQnGMnU6SedLhfEv05?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeNvIP9m7Ad6r0k8Z-iWkglalYq6cqvaxzGVS3RlvXu62GQUWe6NGQXYyU1hKBzVgTXrQ9qv2NAa4XZfHfvqqrGmJx5Dxvl-zDAnANJJISJLeYJhZf4pg5BouiVvgiSLBj70Jdd5Q?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdfn6uXP0KJt6-x6Zb-Hw7iL9fehwm76yB30rG6jdzjTnHX1EKS_BwSMF1sgYTFrIPARQCTKRnS5ZhJvD71iuHvgC4YVoFO5YPaa9McKVz9z3elq--MJ6Cz-M7ojp8wGOzI1r-Y2w?key=MVUMBubVWObqGhv-nBk1M66o)

  

## Step 2: Upload the CSV Dataset

We’ll use the “Import” option for this task.

1.  In the Neo4j Browser, click on the "Import" option
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe-QPRcTe2zXzSpb84iU25_qikC-bDcICklvaDG3Yeg6G40VSa87n0OXB4ILS-6MoM4PpfVYUYJkyu12dt_0pyA93kINa-EfAU5D-UuM96we-wkDxIzzIhBibo0i7mxwaonKBv3Lw?key=MVUMBubVWObqGhv-nBk1M66o)  
  

  
  

2.  Click on "New data source".
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcG1TkxE3ayGAh7pNms8zf7CDYlh4wX1Lrs8XwIbuN1Smt7DptgCYM6MCcJhtNK8KCdw5mx7D_1DEd8ogBzQ90-IMME0M1XsjB8oSzRc2UDRN1Q1IkfjY0y_FZxV_ccqSHxd_Vllw?key=MVUMBubVWObqGhv-nBk1M66o)  
  

3.  Choose the CSV option:
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXczggWNAsToUM-RkNOp56L_ZrfVC3kG2x0E0DwVMIE55mkvp3F2WQiM7pb4FFIUesoI_hovxWCz8J0nQPgdjOZrndQfu7i6JMqQYDViAU02oAKvconMw0Ry6353kEv10HLDSao2_g?key=MVUMBubVWObqGhv-nBk1M66o)

  
  

4.  Click on browse option from drag and drop option
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcUpn1FPzahPLAdU8hpl2iGfy-EOauDwLgW_Q1H-F5c7BHEyCrc7H4Fy6uclVCha8zYEE_5Z9bar_sq0B0satSDZvvdhScdGZ--r67MdjtyXJrT-y6ax4vX3xO7PQ3P1pa1vSCriw?key=MVUMBubVWObqGhv-nBk1M66o)

5.  Upload the files from the data folder, which is inside the resources/day1 directory.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdqOkYqGrW0Z2mz7Q46NaTN1TqCwKamxufRjddDSM6PtsTUMmB2jl9giVarznM6kKAxx2vs9zzTyOGMd5vMm_Q8QkQ0sdgCaVFL828KiBR5xbKmK0F7z982rA3OdNeEu95tQcxI?key=MVUMBubVWObqGhv-nBk1M66o)

  

## Step 3: View Your Data

After you’ve successfully uploaded your CSV files using Neo4j Aura’s Data Importer, the system processes those files and transforms them into graph components - nodes and relationships - based on the headers and structure of the data.

### What Happens in This Step?

-   Neo4j parses your CSV data.
    
-   It creates nodes (e.g., Person, Movie) and relationships based on how you mapped columns in the import tool.
    
-   These components are stored in the graph and are now ready for exploration and querying.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcOR8BdEUpleDzfNyM-_GSnhoNPVed2_sq9G_wuap21lfv_kqi6bsFV5iZTd-4-bAyJMsk3ltuvPJ5K2qwl1g1yx9RJ682MUcA0xk-ZlyjmjkpCWs6jDpCu1XSDFDs0r0btYRCKVw?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc84n5Fbf6EHo4dBdzMgZeTXjkJhz8u4TfCiZfx0FRcaSkAskV28qDV69TLdUSqY9xk_AZ9AaOJ2Du4ATgVWmEe5CtiLE9HGXsSjM893iPkb8fTm1OGoEadJcngVUfUY2hb5k5vGQ?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfzspeliNO2Mjz0dNa1XNRbkTAPVDVIRMAbBO5p-kVERKCIO15LZNlQO8oJPwc8O0aXL2y0dTbUuPRZX2MsPC6V1qYKHIlQ2rTic_R6GVXWqMWPmrMG1bKftpwmajntdist6YMd?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdd93JPlsb4KEC3VGcdPUy4NtymnUqIeKYGK9PT56Pq1rfhpo0fUgkyV3TCx1gsNTAn-dDzSFbqyg1wS2jammqOmB2JHmYHB3Da5OMUxCZOYg-MI25wIPTolwQgPKgkE7IaaUojpg?key=MVUMBubVWObqGhv-nBk1M66o)

## Step 4: Explore the Data Visually

  

1.  After clicking on "Run Import" you will be directed to the Explore section.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfv3YE4MDT0K4yfvAcHzZvqiwqARAObCKYffYusdOdyYt8831RduvXxzjmBuv9flJcxvIs5NKjSJWMe9VOQFmtvtW6-GKmQ3PuD9NpFHwWQhILEgrdjnTTMXU1G5oN8Vbf2RLRb4g?key=MVUMBubVWObqGhv-nBk1M66o)

The Explore Section is divided into 4 major parts. They are as follows:

1.  Search Bar – This is where you input Cypher queries or use natural language prompts to retrieve data from the graph.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeoKadCYygN-Ksi-DWT-pceeieqTNTijF1HZeow48vY66-QPj6CF9Wf7hvniPx-4dx6xxmiks_EAjYx-nBnD4MNGDa90LjmoG0XXbbn1KfN8RRhuLHrClaq6QWS58vRMyOBLXC5?key=MVUMBubVWObqGhv-nBk1M66o)  
  

2.  Selection Summary – Displays the total number of nodes/relationships shown and how many are currently selected.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd7LBnX200mqtsI2rtPki-Yt2lBkhbAkXjeQtR1IMN_jTkiUsc5qrHjfOsdsHYiL96JrLe4EDGeyMZf-v4N4rqX_b-JF-Vedml0ynMwKRwdUNvRNMODwu85x14vYVCQUInj1x6Axg?key=MVUMBubVWObqGhv-nBk1M66o)

  
  
  
  
  

The options are clickable and can be expanded to get more information.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd-9LW12KvfOtCj9QO38Pvx-Rg3niujFE3qQB0P_YjIbO9YNnizOwip-sYLamWcuS990uEj7bBq7IsDgXVaCYZVXAoiFFTvIagA-zWOPn7VjnlFfyx_0X0ghHSe3IgjtyDQ0Fts7Q?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXflS9giUGaGHm1zHQP0ixNYrPwrxM7fgcJbL7PHRRCVLrFW8awfH-duMqC4uIPj6-jd6_23zTTbtzjWOMJ8thIWb5IeUj-nwW9DiFj9e9YCmgrrs9SP8cSJSA_ZLJHzqXdD57Ol?key=MVUMBubVWObqGhv-nBk1M66o)  
  

3.  Layout Selector – Allows you to choose different graph layout styles, such as force-based layout, hierarchical, etc. By default it is Forced-based layout.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcJTNbvHH4Bhc2RnWkMMg8emHSoOmq2ttni0kuK5AdIGBM9iW-yJCrBpIHL73wYLudUn2JWyBXeL87D-8U-usET4d8KXyyzpYh3yeebJTBEUbNlVGdZSTvaVWB6IKpNqW6BScRQPQ?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe4oBZO-KsRgvaLNXG__ZQs6-mESMdmzsrex1MsAJ42RS2os17xMZ568tfVZ72F69tS59yFuSN6XLxyQwflhRzfMt4skPdPwKyrXnbeirDZDOmO9XdsmVSqIZ60iB-kDHaI0Ni8PQ?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXftUVYYvbgpfW-tq9wuIHUFKi3vvTC_bucJk2I_sQvdDks1jDF9Pt3ZU4cOHUzJ1Lff5PKj1hGGKFKA-tnmEYaiqJa0P3ui0V641qngOIRjFYeaR0W1NIiZcf-66sDopiS7hpP0_A?key=MVUMBubVWObqGhv-nBk1M66o)

  
  

4.  Node/Relationship Categories Panel – Provides filtering options by category (like "ActedIn", "Movie", etc.), allowing you to control what’s visible in the graph.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfise7XhA7MwVAiNwHeSBO8NnxiZLYkD4TUw_G3lj9N7j-e9UxnC16xi3GyahH-M-h-3N_t54QOUESw-oLgg6lWTnPuDPRxM73FkskSIbE-Qj4G-kmpV-zCEfyBGbOmXCoLEjIArg?key=MVUMBubVWObqGhv-nBk1M66o)

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeO9fJc9o4TMJRFkdN2dhFVQG2oWgVe0LBbWC2ezp0bUH8p8qZ5C1ototutsqmtohdwYqbgSjPX4CMtlvtrl0-3ZCKkK2AktlgEr2XBn7bLnb-rM7Zokg8Ls4yEkLjsE5mz9-Am?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcFCToB54GiLwUu3lMJoZvyZL2wEzvMbNtvWvbdFcqW9TnzJyTT0-icoLTJZDC9YGABIR8vQuvMaLHEaB2OcnpAxhHMr7F5NJCnGI0rGb-cgXtn0ltWIQe-4kp4JQvzyuiff-5Lfw?key=MVUMBubVWObqGhv-nBk1M66o)

  
  
  

## Step 5: Exploring Neo4j Aura

1.  The query section contains the section for running queries on the graph. You can check the nodes , relationships and property keys’ values.
    

  

2.  Database Information Panel (Left Sidebar)  
      
    

1.  Nodes (725): Displays total node count and their labels like ActedIn, Directed, Movie, Person, Rating.  
      
    
2.  Relationships (750): Shows the relationship types like IS_IN_MOVIE, IS_PERSON.  
      
    
3.  Property Keys: Lists the properties (fields) used in the nodes and relationships (e.g., name, genre, imdbRating, etc.).  
      
    

4.  Cypher Query Editor (Top Center)  
      
    

1.  This is where you write and run Cypher queries to interact with the graph database. The prompt (neo4j$) indicates the Cypher shell.
    

These areas help you explore the schema and query structure of your Neo4j database visually and programmatically.

  
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcLkJ0EX8YbCVQgsegN7mATV0vlLwABbvDzkqrZDIorlVnC4SXnQ62YzvIiTIcwYVMibt4IyHdWJJdUiOq3w6wI7PsVC4lgn3TA5RIoLBC1HGNOc5_hxxenetFJH2GSzHMLv5GU?key=MVUMBubVWObqGhv-nBk1M66o)

  

## Conclusion

In this lab, you learned:

-   How to access and set up Neo4j Aura  
      
    
-   How to upload data using Data Importer  
      
    
-   How to visually explore a graph without writing Cypher