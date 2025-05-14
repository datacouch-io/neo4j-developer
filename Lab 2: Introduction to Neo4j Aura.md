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

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfYmlT5i2EL25aTeNHJu5xAXZIP7egz-oIYwhkh2lRleE57JzC28ZCMNI4RhQ-r_qZNEPFgCKjOlBc9hjQjFfb1ok_HUKKuZaa-lCjJTTffljE2Oil5f1lT5RG08fXkFc4B-sLo?key=MVUMBubVWObqGhv-nBk1M66o)

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfKLn0hFMKxMZgLRu-4rdE-bwUo8uETvi65Al2W8W5KGq2bwUpDUVeMgqkPRgytA2o4VuqQp099iAYB1yB_BAS8EAqEvIXGP5_gZwn2TmMITdPzyH2SMYUl_1cd_acHwHjEZkTi?key=MVUMBubVWObqGhv-nBk1M66o)

  
  
  
  
  
  
  
  
  
  

2.  Select the version (paid or free)
    

Copy the key and click on download and continue

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfd48xPNsqe6MsNM9yHo-THOaJJgoq8BDtd5WQsIBovrwAJDTmf9kMhA5k6EhgcydfVRsECt_koRP-zgR_rRom5lQLYTUpaVYLbN_lH4ypJz2zlHjeqqke1QHwFqtEHMSrFq6Rr?key=MVUMBubVWObqGhv-nBk1M66o)

  
  
  
  
  
  
  
  
  
  

3.  Instances are created, now select Query and connect to an instance. You will be forwarded to the query page.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdRUB1YZgeJ6ni8_Pq-6B8VSqWnYgxriGXyigdGgbgv9E20WgG7pYomSeNW-RriBHW9_UbDLJcz1eq2pP4v8dZj5M1cWmJfVSG0vRs2nyQNCPJ6dVxLtnq7ePGGjNzSMuh_rmah?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXePhoYp5WUoOe-fd0PCjXrmG8r4vUUCXROTyOd_rBif7_2Me-wRx7PnQ2r7lRSvP8KTjUv3JOxyngxdplT35i0TcdDMQP801vTt94Ic_T2ivm0a0GyKJRCzYE078Xd_aycXijYJgg?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeUMyu6e0Lrrf4oFGnWVLoZv6HplLhj6xhGVp4v2QfTrnbvHa219BpxMGEIqb8s9AiHM9VOm0F8RRdHYQ-DNCk7Yx-NTlHqZerG-J5jVYGdLRPxvTvOn0XzboUhfisdT_d6NDMXag?key=MVUMBubVWObqGhv-nBk1M66o)

  

## Step 2: Upload the CSV Dataset

We’ll use the “Import” option for this task.

1.  In the Neo4j Browser, click on the "Import" option
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc63QVXOs2rSzDLAbfzyjpGeD-s-pp-wU7a05uorGIdQWTHeb8eog51HeedqICgC2Cs9gDHVOkN1sywUE4UvtCMNaFaa-q_kwLiyTZI8e9jTA4tAKobjNIXJelhaNq7_jkiwJDPsQ?key=MVUMBubVWObqGhv-nBk1M66o)  
  

  
  

2.  Click on "New data source".
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdoD0nMwfWMvMP4OS4plQP9ycv22rf6Icpl8Pl7JPCMGrliF4NbYjSA8uGTgplWBduSnIJFrgycbIMJJWU1jYvk5nGx6Vy9DUVNURgP1NxrXaYBq2w8MKi30CmuGQgfBChU8rZJeg?key=MVUMBubVWObqGhv-nBk1M66o)  
  

3.  Choose the CSV option:
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXda0TR4csysdNFu6ArPFptkkelFtoVOzrcHaoLj5F7ufMaO8wOwhBrN54MHtM2I_hM3FuddNsiIip0yRch8v_Fb27vlMw6IuyT1tCiv7zvFBhod5gzmdga0QoyuecIZqB4p9RTKaw?key=MVUMBubVWObqGhv-nBk1M66o)

  
  

4.  Click on browse option from drag and drop option
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfwIeNmbDuEQOhL9JsAZ3JfaI5uY7oxksmU975mgmjuqof8HGCrmyE__kNmY8KALocDOd9DH_VkLxfKfeNpPNE1c9MEHgMnew01B-ltb756HdZ4bcVct3GZNitdNJwMbaRloJBW-A?key=MVUMBubVWObqGhv-nBk1M66o)

5.  Upload the files from the data folder, which is inside the resources/day1 directory.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfAKWPidbC1DXTOMj-HOBRujcoh0vEpgIQdJc8vxD8sRchrGEhAJZ3YcKs_zjyYz-hl_x3gZWh3U3a-HTmhv1fTGfh7BHXegUYOtvRpz4RQqQdOLmlhLvul2E4F61FXDtxWXg4J?key=MVUMBubVWObqGhv-nBk1M66o)

  

## Step 3: View Your Data

After you’ve successfully uploaded your CSV files using Neo4j Aura’s Data Importer, the system processes those files and transforms them into graph components - nodes and relationships - based on the headers and structure of the data.

### What Happens in This Step?

-   Neo4j parses your CSV data.
    
-   It creates nodes (e.g., Person, Movie) and relationships based on how you mapped columns in the import tool.
    
-   These components are stored in the graph and are now ready for exploration and querying.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfFuABDsxG5WnWw0EdWUeo9z42KCXXiaqslBzDptDYq_B9KQlg9AHMSye7HfSzCi4edexCT_YpPx7UHo-ZGOxLEuHvJivjPwCCn4AEgjFAAvBHCY1C2HgYpCeu_3MzM6PMhiL1v-Q?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdDHBFasv2Dr6Pg1Ddb0HtwpMUvpIjTrvGQKxBqPM_puxjgVOOI1ZuhESdZapkFOTy-Ya927JNhmYGxgSdrEnqpFYIpZt6o8aVYsfD9RCsKWkbl_5RSC7eZvp51oDcq-R0ZHR8mjA?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf8kFvKegdRTL6DoXbWyHK_gbTzFqTi4EsUlE0fYziEcKQqpxDqdR0EFjJhPThcJsa4SwIQ79FwQCaR5Ya5m80lozFQgo7xybNeJKjUYvB4Wtwpt3dBRUryF7Mp8TydEHFO623S?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdoNWqfAE9hjk8zBlaftoCQdZrXyuBR14SvqfAdLipaBHKFHsfDlsGpbrKn64Fhu1iLckCFtrRZzgKPhTtOQKgHEHj7XQFie7FLVad_baFQEQmw600lavftZ_6NZz987-6Qu08Mng?key=MVUMBubVWObqGhv-nBk1M66o)

## Step 4: Explore the Data Visually

  

1.  After clicking on "Run Import" you will be directed to the Explore section.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeh1nGnszE-0BviAPT9BKJ9D-nG9J14FwjdAWi9x58kUd_UUOkQMbF2MPEVrSyr7b0-DGX972RVi84jfUZSo0rAUmw1LDL2zIQbFO4lmO5g9Q0Z0d_fG6wCYf5yqgiBHPB_JkyyQQ?key=MVUMBubVWObqGhv-nBk1M66o)

The Explore Section is divided into 4 major parts. They are as follows:

2.  Search Bar – This is where you input Cypher queries or use natural language prompts to retrieve data from the graph.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcQ5LXFPiRHIrSaJ3lRw1FIVVY4nuasN1h1AmEy2vEi1TgK-k3hMtMUPUXODvGgCJEi-xvbUPobmF0oxbSYYLao2dZlFQHiklOce7O2OATjZL7tu8ETzGmvMytk2weosp9nzFh3?key=MVUMBubVWObqGhv-nBk1M66o)  
  

3.  Selection Summary – Displays the total number of nodes/relationships shown and how many are currently selected.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfILvA3s53gB39t9ZR0u3jWDLKROfs3rAYiC4TxRutWcm-Z4-w63s0Fyi-nY3AexKHjclevB-fHgK6uDNm6yHOgwHMlExJdd1xnC5VOoZwB8Cx0TM7J5AtSsTA1kg5HyfVii3Y2Vg?key=MVUMBubVWObqGhv-nBk1M66o)

  

The options are clickable and can be expanded to get more information.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeZ4CIySuGXr5NoNCP9cyLZgQz4BgM0TSN33SqFS2AnlNvYOMFoY3cRCiGH12pR9cqFzG2MO8-6bKDI4jNkHmwLuxCrRZ-TBU2_NCAKlqxUHJJ8CarNyZhKySyJ6mHuunrHT5EsRQ?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfieZ-smMfNQILeLo61-FJm6VizjNPrx-p_HLp1zEJiJ5c-8TLKUSSYG3PPCrNh_pArQrpDHoOjsxdVNK6rhZTeQdn7wy12Zfuw8_TsA8eZ5smrXwJs1tTlT7-5kWgd66fFcOFd?key=MVUMBubVWObqGhv-nBk1M66o)  
  

4.  Layout Selector – Allows you to choose different graph layout styles, such as force-based layout, hierarchical, etc. By default it is Forced-based layout.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdD2aZifnCBLX-2c7i64OIW1acu_vibDdF0J6jCP9zuyjjCocxwOUOSZxK8_6_vSVumBRdvrRKTkghiEcr8Qsz8yT2iRdjz1KT9EN5pY0_BHGz1AwCl1PH4NKT5w9VQr-xyFUrMgw?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUyCtW1ZtjPxKq9_FySMR5t5htD7EVH84wuZb4t3vQwP29BTor67nBCa11WPBC-Ac5RuuheOgWKlQjTUZm0rWrYk44Tdp-VSfy7xMLepn0hJVJf9QWSiENZfpvdbJ3C9E5HFr_9A?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcUj3eSXW4hHRuiV5_KTjgWCS2eywiAc2JlqFM8WlGQlEfUFwAROYX62kToMP2kQ_csSXuNy4_459G46Fxy_oTa--U260FLLH7JFAC5QfHW7CuktnmknzbfJ-7yIJmahXa2Lwi5gg?key=MVUMBubVWObqGhv-nBk1M66o)

  
  

5.  Node/Relationship Categories Panel – Provides filtering options by category (like "ActedIn", "Movie", etc.), allowing you to control what’s visible in the graph.
    

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdMEYgegVAtTZTuqXpQUcvIFJpGqvzlMn5CXLOSeruHLDJdfRxL7CFXjINYRccVuMsb6PIWTbKtwgQfLu54qJ_tdtk5XkTow11NNo49GyqPobKBypauLVKkHcH4a_4gOVnsJIf0XQ?key=MVUMBubVWObqGhv-nBk1M66o)

  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdrE_5f6NyzTT743X6gJkpBWxdN3s1TDwsqm6n_EG1YtPuAIgAP5SYaAsNQY3BvSqRtg5pIfXOSjlqhxhWBc7MUJaEQ7fViLmTWmBywlaPpB_VHBo-nlFwXOtvrqioU8XubK5vz?key=MVUMBubVWObqGhv-nBk1M66o)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd9uO8C26J1tdxU3zmWlq2invp2Y58QBh3EMFnQgwBsOvTL-BPpiLOzgmKvLfPxkuDDtwptjIgZLnYZjpKNxhEFIbnbigm2HGtRAafK_9PeT5RB7oj_i5pkbuzC88-fN3zmQbj69g?key=MVUMBubVWObqGhv-nBk1M66o)

  
  
  

## Step 5: Exploring Neo4j Aura

1.  The query section contains the section for running queries on the graph. You can check the nodes , relationships and property keys’ values.
    

  

2.  Database Information Panel (Left Sidebar)  
      
    

1.  Nodes (725): Displays total node count and their labels like ActedIn, Directed, Movie, Person, Rating.  
      
    
2.  Relationships (750): Shows the relationship types like IS_IN_MOVIE, IS_PERSON.  
      
    
3.  Property Keys: Lists the properties (fields) used in the nodes and relationships (e.g., name, genre, imdbRating, etc.).  
      
    

4.  Cypher Query Editor (Top Center)  
      
    

5.  This is where you write and run Cypher queries to interact with the graph database. The prompt (neo4j$) indicates the Cypher shell.
    

These areas help you explore the schema and query structure of your Neo4j database visually and programmatically.

  
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfAF9XxOv4Oso_MnOe-ql0qjIJz3A4Fw-Gj5cPRLYvktT4zojxSnsXWWkTBcv4c14Kf6bMclN7Sdj4FtfeuQ7NAN68KQhhfeLkblrlpp6hB_Q4q8eaykgVOOcAyfgtZefRMfeq8?key=MVUMBubVWObqGhv-nBk1M66o)

  

## Conclusion

In this lab, you learned:

-   How to access and set up Neo4j Aura  
      
    
-   How to upload data using Data Importer  
      
    
-   How to visually explore a graph without writing Cypher