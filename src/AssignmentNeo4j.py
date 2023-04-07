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


	def loadData(self):
		# TODO : Write function to load data as per given instructions
		"""
		load data as per given instructions

		Keyword arguments:
		None

		:throws: Exception if an error occurs.
		"""

		with self.driver.session(database="neo4j") as session:
			result = session.execute_write(self._load_actor_person)
			for row in result:
				print("We created an actor/person ", row)
	

	@staticmethod
	def _load_actor_person(tx):
		query = ("CREATE(I:Actor:Alien{bio: 'Extraterrestrial', born: '1200-01-01', bornIn: 'Mars', name: 'ET'})\n")
		queryET = ("MATCH(I:Alien)\n"
					"MATCH(M:Movie {title: 'E.T. the Extra-Terrestrial'})\n"
				"MERGE(I)- [:ACTED_IN] -> (M)")
		queryJ = ("MATCH(I:Alien)\n"
				"MATCH(M:Movie{title:'Jumanji'})\n"
				"MERGE (I) - [:ACTED_IN] -> (M)")		
		queryR = (
		"MATCH(p:Person|User)"
		"MATCH(M:Movie{title:'Jumanji'})\n"
		"WHERE ID(p) = 34047\n"
		"MERGE (p) - [:REVIEWED{rating:90,summary:'It was fun to watch in 3D'}]-> (M)")
		# result = tx.run(query)
		# result = tx.run(queryET)
		# result = tx.run(queryJ)
		result = tx.run(queryR)
		try:
			return [row for row in result] #does not do anything because there is nothing to return, just filler
		except ServiceUnavailable as ex:
			logging.error("{query} raised an error: \n {ex}".format(query=query, ex=ex))
			raise		
		
	def query1(self,data_op):
		"""Returns 
		"""
		print("first order query. ")
		with self.driver.session(database="neo4j") as session:
			result = session.execute_read(self._query1helper, data_op)
			#might need a set to avoid dupes
			# result_tup = ()
			# for row in result:
			# 	print(row)
			print(result)
			return result

	@staticmethod
	def _query1helper(tx, data_op):
		if(data_op==0):
			query1=("MATCH (c:squirrel {id:'777'}) -[:s_conn]-(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'})-[:cham_conn]-(r) RETURN count(r);")
		elif(data_op==1):
			query1=("MATCH (c:chameleon {id:'777'})-[:cham_conn]-(r) RETURN count(r);")
		else:
			query1=("MATCH (c:crocodile {id:'777'}) -[:CONS]-(r) RETURN COUNT(r);")
		result1 = tx.run(query1)

			#return({"MovieInfo": row["Names"]["ReleaseDate"]} for row in result1)
		return[row for row in result1]
	


	def query2(self,data_op):
		"""
		"""
		print("2nd order query.")
		with self.driver.session(database="neo4j") as session:
			result = session.execute_read(self._query2helper,data_op)
			#might need a set to avoid dupes
			print(result)		
			return result		
	
	@staticmethod
	def _query2helper(tx,data_op):
		if(data_op==0):
			query2=("MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
				#("MATCH (c:chameleon {id:'777'})-[:cham_conn]-(r) RETURN count(r);")
		elif(data_op==1):
			query2=("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			#("MATCH (c:chameleon {id:'777'})-[:cham_conn]-(r) RETURN count(r);")
		else:
			query2=("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
			#("MATCH (c:Crocodile {id:'777'}) -[:CONS]-(r) RETURN COUNT(r);")
		result2 = tx.run(query2)
		return[row for row in result2]
	
	def query3(self, data_op):
		"""
		"""
		print("3rd order query.")
		with self.driver.session(database="neo4j") as session:
			result = session.execute_read(self._query3helper, data_op)
			result_tup = ()
			#might need a set to avoid dupes
			print(result)		
			return result		
	
	@staticmethod
	def _query3helper(tx, data_op):
		if(data_op==0):
			query3=("MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
			#("MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
		elif(data_op==1):
			query3=("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			#("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
		else:
			query3=("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
			#("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
		result3 = tx.run(query3)

		return[row for row in result3]

	def query4(self,data_op):
		"""
		"""
		print("4th order query.")
		with self.driver.session(database="neo4j") as session:
			result = session.execute_read(self._query4helper,data_op)
			result_tup = ()
			#might need a set to avoid dupes
			print(result)		
			return result		
	
	@staticmethod
	def _query4helper(tx,data_op):
		if(data_op==0):
			query4=("MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
			#MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);
		elif(data_op==1):
			query4=("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			#("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
		else:
			query4=("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
			#("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
		result4 = tx.run(query4)
		# summary = result4.consume()
		# print(summary.profile)
		return[row for row in result4]

	def query5(self,data_op):
		"""
		"""
		print("5th order query.")
		with self.driver.session(database="neo4j") as session:
			result = session.execute_read(self._query5helper,data_op)
			#might need a set to avoid dupes
			print(result)		
			return result		
	
	@staticmethod
	def _query5helper(tx,data_op):
		if(data_op==0):
			query5=("MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
		elif(data_op==1):
			query5=("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			#("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
		else:
			query5=("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
			#("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
		result5 = tx.run(query5)
		# summary = result4.consume()
		# print(summary.profile)
		return[row for row in result5]

	def query6(self,data_op):
		"""
		"""
		print("6th order query.")
		with self.driver.session(database="neo4j") as session:
			result = session.execute_read(self._query6helper,data_op)
			#might need a set to avoid dupes
			print(result)		
			return result		
	
	@staticmethod
	def _query6helper(tx,data_op):
		if(data_op==0):
			query6=("MATCH (c:squirrel {id:'777'}) -[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn]-()-[:s_conn] -(r) RETURN COUNT(r);")
		elif(data_op==1):
			query6=("MATCH (c:squirrel {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
			#("MATCH (c:chameleon {id:'777'}) -[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn]-()-[:cham_conn] -(r) RETURN COUNT(r);")
		else:
			query6=("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
			#("MATCH (c:crocodile {id:'777'}) -[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS]-()-[:CONS] -(r) RETURN COUNT(r);")
		result6 = tx.run(query6)
		# summary = result4.consume()
		# print(summary.profile)
		return[row for row in result6]




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

	print("===== Data set",data, ".=====")
	#app.loadData() # Run only once to avoid duplicate data.
	app.query1(data_option)
	app.query2(data_option)
	app.query3(data_option)
	app.query4(data_option)
	# app.query5(data_option)
	# app.query6(data_option)
	app.close()