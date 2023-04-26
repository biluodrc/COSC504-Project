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

### Build Environment
Supposing you have a the Docker client. Run the following script to build a AllegroGraph Database environment:

''
docker pull franzinc/agraph 
''

Then run the agraph container and open http://localhost:10035/ in your browser.

First, we need to build a repository named COSC504 by running the code 'main.py'.

Second, insert data into the repository: 

1. Open http://localhost:10035/ in your browser; 

![image](https://user-images.githubusercontent.com/44452689/234490338-7fef4e13-d6f2-4094-8190-4f17167b5250.png)

2. select Repositories COSC 504;

![image](https://user-images.githubusercontent.com/44452689/234490423-a0eebf5e-b9b9-44f5-8747-dd726a38ef4c.png)

3. Import RDF: from an uploaded file, including chameleon.rdf, crocodile.rdf, and squirrel.rdf. (Choose format as Turtle)

![image](https://user-images.githubusercontent.com/44452689/234490484-7d663601-6002-4e5c-adbd-bc81ff8d9144.png)

### Test Query Performance

Run 'Query.py' to get the query performance for each database.

![image](https://user-images.githubusercontent.com/44452689/234491332-e8a7ea60-4a00-4609-be89-497faf25b94e.png)

**Experiments log is shown on 'log' file.**
