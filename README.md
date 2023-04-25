# COSC504-Project
In this project, we expect to compare the query performance on two famous graph databases, Neo4j and AllegreDB with the WIKI dataset. 

## Reproduction of the experiment with neo4j 
Assuming you have a neo4j free account, please create an instance by clicking `new instance` and then choose `empty instance`. Download the credentials for the instance to connect to the DB later on. 
Once the instance is up and running, you can go ahead and upload one of the three datasets, including the chameleon, crocodile, and squirrel. 
To reproduce the experiment result, you need to upload their .dump files that we prepared beforehand  in the /Data/WIKI_neo4j/ directory, and we go into the instance and click on the `Import Database`. 


After you successfully import the data, we can run the Neo4j.py code by `python ./src/Neo4j.py 0 777 0`,  which will run the experiment on the squirrel dataset with the node id as 777. 
The first argument 0 indicates which dataset it's going to run on, and 0, 1, and 2 indicate the squirrel, chameleon, and crocodile, respectively.
The second argument 777 specifies which node id, and you can try a different id around 1 to 2000.
The last argument 0 indicates whether we want to look into the query plan, and 0 means don't show the query plan, while 1 means show the query plan.

Note that when you want to run the query on a particular dataset, you need to `reset to blank` before you upload the corresponding dataset because there is a node and relationship limitation in neo4j auraDB.

## AllegroDB
