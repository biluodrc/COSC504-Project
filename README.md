# COSC504-Project

## Basic Query Performance result 


## Reproduction of the experiment with neo4j 
Assuming you have a neo4j free account, please create an instance by clicking `new instance` and then choose `empty instance`. Download the credentials for the instance to connect to the DB later on. 
Once the instance is up and running, you can go ahead and upload three datasets, including the chameleon, crocodile, and squirrel. 
To reporduce the experiment result, you need to upload their .dump files that we prepared beforehand  in the /Data/WIKI_neo4j/ directory, and we go into the instance and click on the `Import Database`. 


After they successfully import the data, we can run the Neo4j.py code by `python ./src/Neo4j.py 0 777`,  which will run the experiment on the squirrel dataset with the node id as 777. 
The first argument 0 indicate which dataset it's going to run on, and 0, 1, and 2 indicate the suqirrel, chameleon, and crocodile, respectively.
The second argument 777 specify which node id, and you can try different id around 1 to 2000.



## OrientDB 

## ArangoDB
