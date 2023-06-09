from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable
import re
import sys
import time

class Neo4jApp:

	# Put your credential information here
	uri = "neo4j+s://a08d43bb.databases.neo4j.io:7687"
	user = "neo4j"
	password = "l1YG5-qlGGqYqiePSRj_da8ucOAadbruhgsjgoVSTn8"

	def __init__(self):
		self.driver = None

	def connect(self, uri=None, user=None, password=None):
		# connect to the database with the uri, user, password
		if uri is None:
			uri = self.uri
		if user is None:
			user = self.user
		if password is None:
			password = self.password
		self.driver = GraphDatabase.driver(uri, auth=(user, password))
		print(self.driver)
		# TODO : Complete Method to make a connection to the database
	
		
	def close(self):
		# close the connection to the database
		self.driver.close()

	def query1(self,data_op, id, profile):
		print("***1st order query.")
		# Returns the 1st order query.
		with self.driver.session(database="neo4j") as session:
			if(data_op=='0'):
				query1=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-(r) RETURN COUNT(r);")
			elif(data_op=='1'):
				query1=("MATCH (c:chameleon {id:'"+id+"'})-[:cham_conn]-(r) RETURN count(r);")
			else:
				query1=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-(r) RETURN COUNT(r);")
			
			result = session.run(query1)
			print([row for row in result])
			
			if(profile == '1'):
				#Get hte query profile performance.
				query1_profile="PROFILE "+query1
				print(query1_profile)
				Profile_result = session.run(query1_profile)
				summary = Profile_result.consume()
				print(summary.profile['args']['string-representation'])

			return[row for row in result]


	def query2(self,data_op, id, profile):
		print("***2rd order query.")

		# Run the 2nd order query.
		with self.driver.session(database="neo4j") as session:
			if(data_op=='0'):
				print("WOOWOWOOW")
				query2=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
					#("MATCH (c:chameleon {id:'777'})-[:cham_conn]-(r) RETURN count(r);")
			elif(data_op=='1'):
				query2=("MATCH (c:chameleon {id:'"+id+"'}) -[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'})-[:cham_conn]-(r) RETURN count(r);")
			else:
				query2=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
				#("MATCH (c:Crocodile {id:'777'}) -[:CONS]-(r) RETURN COUNT(r);")
			
			result = session.run(query2)
			print([row for row in result])

			if(profile == '1'):
				# Get hte query profile performance.
				query2_profile="PROFILE "+query2
				Profile_result = session.run(query2_profile)
				summary = Profile_result.consume()
				print(summary.profile['args']['string-representation'])
			return[row for row in result]	
	
	
	
	def query3(self, data_op,id, profile):
		print("***3rd order query.")
		# Run the 3rd order query.
		with self.driver.session(database="neo4j") as session:
			if(data_op=='0'):
				print("WOOWOWOOW")
				query3=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
			elif(data_op=='1'):
				query3=("MATCH (c:chameleon {id:'"+id+"'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			else:
				query3=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
				#("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")

			result = session.run(query3)
			print([row for row in result])
			if(profile == '1'):
				# Get hte query profile performance.
				query3_profile="PROFILE "+query3
				Profile_result = session.run(query3_profile)
				summary = Profile_result.consume()
				print(summary.profile['args']['string-representation'])
		return [row for row in result]			
	
	

	def query4(self,data_op,id, profile):
		print("***4th order query.")
		# Run the 4th order query.
		with self.driver.session(database="neo4j") as session:
			if(data_op=='0'):
				query4=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
				#MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);
			elif(data_op=='1'):
				query4=("MATCH (c:chameleon {id:'"+id+"'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			else:
				query4=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")

			result = session.run(query4)
			print([row for row in result])

			if(profile == '1'):
				# Get hte query profile performance.
				query4_profile="PROFILE "+query4
				Profile_result = session.run(query4_profile)
				summary = Profile_result.consume()
				print(summary.profile['args']['string-representation'])
		return [row for row in result]			

	def query5(self,data_op,id, profile):
		# Run the 5th order query.
		print("***5th order query.")
		with self.driver.session(database="neo4j") as session:
			if(data_op=='0'):
				query5=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
			elif(data_op=='1'):
				query5=("MATCH (c:chameleon {id:'"+id+"'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			else:
				query5=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")

			result = session.run(query5)
			print([row for row in result])

			if(profile == '1'):
				# Get hte query profile performance.
				query5_profile="PROFILE "+query5
				Profile_result = session.run(query5_profile)
				summary = Profile_result.consume()
				print(summary.profile['args']['string-representation'])
		return [row for row in result]			
	
	def query6(self,data_op,id, profile):
		print("***6th order query.")
		# Run the 6th order query.
		with self.driver.session(database="neo4j") as session:
			if(data_op=='0'):
				query6=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
			elif(data_op=='1'):
				query6=("MATCH (c:chameleon {id:'"+id+"'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			else:
				query6=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
	
			result = session.run(query6)
			print([row for row in result])
			
			if(profile == '1'):
				#Get the query profile performance.
				query6_profile="PROFILE "+query6
				Profile_result = session.run(query6_profile)
				summary = Profile_result.consume()
				print(summary.profile['args']['string-representation'])
		return [row for row in result]			
	def datasetoverview(self,data_op, profile):
		print("===== Overview of data =====\n")
		# Run the 6th order query.
		with self.driver.session(database="neo4j") as session:
			if(data_op=='0'):
				data_o = ("MATCH (p:squirrel)-[r:s_conn]-(f:squirrel) RETURN count(DISTINCT p) as numOfNodes, count(DISTINCT r) as numOfEdges, count(DISTINCT r)/((count(DISTINCT p)-1) * (count(DISTINCT p) - 1.0)) AS graphDensity")
			elif(data_op=='1'):
				data_o = ("MATCH (p:chameleon)-[r:cham_conn]-(f:chameleon) RETURN count(DISTINCT p) as numOfNodes, count(DISTINCT r) as numOfEdges, count(DISTINCT r)/((count(DISTINCT p)-1) * (count(DISTINCT p) - 1.0)) AS graphDensity")
			else:
				data_o = ("MATCH (p:crocodile)-[r:CONS]-(f:crocodile) RETURN count(DISTINCT p) as numOfNodes, count(DISTINCT r) as numOfEdges, count(DISTINCT r)/((count(DISTINCT p)-1) * (count(DISTINCT p) - 1.0)) AS graphDensity")
	
			result = session.run(data_o)
			print([row for row in result])
			print("============================\n")	
			#whether to profile your query
			if(profile == '1'):
				#Get the query profile performance.
				data_profile="PROFILE "+data_o
				Profile_result = session.run(data_profile)
				summary = Profile_result.consume()
				print(summary.profile['args']['string-representation'])
		return [row for row in result]	
if __name__ == "__main__":
	# Aura queries use an encrypted connection using the "neo4j+s" URI scheme
	data_option= sys.argv[1] #0:squirrel, 1:chameleon, 2: crocodile.
	# which id 
	id = sys.argv[2] # which id to work on.
	# Profile your query 
	profile = sys.argv[3] # 1: Profile the query, 2: Don't profile
	if data_option=='0':
		data='squirrel'
	elif data_option=='1':
		data ='chameleon'
	else:
		data='crocodile'
	app = Neo4jApp()
	app.connect()

	print("===== Data set",data, ".=====")
	app.datasetoverview(data_option, profile)
	app.query1(data_option,id, profile)
	app.query2(data_option,id, profile)
	app.query3(data_option,id, profile)
	app.query4(data_option,id, profile)
	app.query5(data_option,id, profile)
	app.query6(data_option,id, profile)
	app.close()