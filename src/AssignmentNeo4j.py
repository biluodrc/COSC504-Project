from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable
import re
class Neo4jApp:

	# Replace this with your personal uri, user (default: neo4j), password
	uri = "neo4j+s://a08d43bb.databases.neo4j.io:7687" #"neo4j+s://<Bolt url for Neo4j Aura instance>"
	user = "neo4j"
	password = "l1YG5-qlGGqYqiePSRj_da8ucOAadbruhgsjgoVSTn8"

	def __init__(self):
		self.driver = None

	def connect(self, uri=None, user=None, password=None):
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
		# TODO : Complete Method to close the connection to the database
		self.driver.close()

	def query1(self,data_op, id):
		"""Returns 
		"""
		print("***first order query. ")
		with self.driver.session(database="neo4j") as session:
			if(data_op==0):
				query1=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'})-[:cham_conn]-(r) RETURN count(r);")
			elif(data_op==1):
				query1=("MATCH (c:chameleon {id:'"+id+"'})-[:cham_conn]-(r) RETURN count(r);")
			else:
				query1=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-(r) RETURN COUNT(r);")
			
			result = session.run(query1)
			print([row for row in result])
			# Get hte query profile performance.
			query1_profile="PROFILE "+query1
			Profile_result = session.run(query1_profile)
			summary = Profile_result.consume()
			print(summary.profile)

			return[row for row in result]


	def query2(self,data_op,id):
		"""
		"""
		print("***2nd order query.")
		with self.driver.session(database="neo4j") as session:
			if(data_op==0):
				query2=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
					#("MATCH (c:chameleon {id:'777'})-[:cham_conn]-(r) RETURN count(r);")
			elif(data_op==1):
				query2=("MATCH (c:chameleon {id:'"+id+"'}) -[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'})-[:cham_conn]-(r) RETURN count(r);")
			else:
				query2=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
				#("MATCH (c:Crocodile {id:'777'}) -[:CONS]-(r) RETURN COUNT(r);")
			result = session.run(query2)
			print([row for row in result])

			# Get hte query profile performance.
			# query2_profile="PROFILE "+query2
			# Profile_result = session.run(query2_profile)
			# summary = Profile_result.consume()
			# print(summary.profile)
			return[row for row in result]	
	
	
	
	def query3(self, data_op,id):
		"""
		"""
		print("***3rd order query.")
		with self.driver.session(database="neo4j") as session:
			if(data_op==0):
				query3=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
			elif(data_op==1):
				query3=("MATCH (c:chameleon {id:'"+id+"'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			else:
				query3=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
				#("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
			result = session.run(query3)
			print([row for row in result])
			
			# Get hte query profile performance.
			# query3_profile="PROFILE "+query3
			# Profile_result = session.run(query3_profile)
			# summary = Profile_result.consume()
			# print(summary.profile)
		return [row for row in result]			
	
	

	def query4(self,data_op,id):
		"""
		"""
		print("4th order query.")
		with self.driver.session(database="neo4j") as session:
			if(data_op==0):
				query4=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
				#MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);
			elif(data_op==1):
				query4=("MATCH (c:chameleon {id:'"+id+"'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			else:
				query4=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
			result = session.run(query4)
			print([row for row in result])

			# Get hte query profile performance.
			query4_profile="PROFILE "+query4
			Profile_result = session.run(query4_profile)
			summary = Profile_result.consume()
			print(summary.profile)
		return [row for row in result]			

	def query5(self,data_op,id):
		"""
		"""
		print("5th order query.")
		with self.driver.session(database="neo4j") as session:
			if(data_op==0):
				query5=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
			elif(data_op==1):
				query5=("MATCH (c:chameleon {id:'"+id+"'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			else:
				query5=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
			result = session.run(query5)
			print([row for row in result])

			# Get hte query profile performance.
			# query5_profile="PROFILE "+query5
			# Profile_result = session.run(query5_profile)
			# summary = Profile_result.consume()
			# print(summary.profile)
		return [row for row in result]			
	
	def query6(self,data_op,id):
		"""
		"""
		print("***6th order query.")
		with self.driver.session(database="neo4j") as session:
			if(data_op==0):
				query6=("MATCH (c:squirrel {id:'"+id+"'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
			elif(data_op==1):
				query6=("MATCH (c:squirrel {id:'"+id+"'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			else:
				query6=("MATCH (c:crocodile {id:'"+id+"'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
				#("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
			result = session.run(query6)
			print([row for row in result])

			#Get hte query profile performance.
			query6_profile="PROFILE "+query6
			Profile_result = session.run(query6_profile)
			summary = Profile_result.consume()
			print(summary.profile)
		return [row for row in result]			

if __name__ == "__main__":
	# Aura queries use an encrypted connection using the "neo4j+s" URI scheme
	data_option= 2#0:squirrel ; 1:chameleon ; 2: crocodile.
	if data_option==0:
		data='squirrel'
	elif data_option==1:
		data ='chameleon'
	else:
		data='crocodile'
	app = Neo4jApp()
	app.connect()
	# which id 
	id = '777' # which user to experiment.

	print("===== Data set",data, ".=====")
	#app.loadData() # Run only once to avoid duplicate data.
	app.query1(data_option,id)
	app.query2(data_option,id)
	app.query3(data_option,id)
	app.query4(data_option,id)
	# app.query5(data_option)
	# app.query6(data_option)
	app.close()