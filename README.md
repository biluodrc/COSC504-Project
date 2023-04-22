# COSC504-Project

## Basic Query Performance result 


## Reproduction of the experiment with neo4j 
Assuming you have a neo4j free account, please create an instance by clicking `new instance` and then choose `empty instance`. Download the credentials for the instance to connect to the DB later on. 
Once the instance is up and running, you can go ahead and upload three datasets, including the chameleon, crocodile, and squirrel. 
To reproduce the experiment result, you need to upload their .dump files that we prepared beforehand  in the /Data/WIKI_neo4j/ directory, and we go into the instance and click on the `Import Database`. 


After you successfully import the data, we can run the Neo4j.py code by `python ./src/Neo4j.py 0 777`,  which will run the experiment on the squirrel dataset with the node id as 777. 
The first argument 0 indicates which dataset it's going to run on, and 0, 1, and 2 indicate the squirrel, chameleon, and crocodile, respectively.
The second argument 777 specifies which node id, and you can try a different id around 1 to 2000.

Note that when you run the specific dataset, you need to upload the .dump file to the neo4j database, and `reset to blank` before you upload another dataset because there is a node and relationship limitation in neo4j auraDB.



## OrientDB 

## ArangoDB
