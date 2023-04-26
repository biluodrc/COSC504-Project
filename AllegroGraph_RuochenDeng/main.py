# get metadata about agraph from os
import os
AGRAPH_HOST = os.environ.get('AGRAPH_HOST')
AGRAPH_PORT = int(os.environ.get('AGRAPH_PORT', '10035'))
AGRAPH_USER = "cosc504"
AGRAPH_PASSWORD = "cosc504"

# get access to the server
from franz.openrdf.sail.allegrographserver import AllegroGraphServer
print("Connecting to AllegroGraph server --",
      "host:'%s' port:%s" % (AGRAPH_HOST, AGRAPH_PORT))
server = AllegroGraphServer(AGRAPH_HOST, AGRAPH_PORT,
                            AGRAPH_USER, AGRAPH_PASSWORD)

# show all the catalog in the server
print("Available catalogs:")
for cat_name in server.listCatalogs():
    if cat_name is None:
        print('  - <root catalog>')
    else:
        print('  - ' + str(cat_name))

# open root catalog
catalog = server.openCatalog("")
print("Available repositories in catalog '%s':" % catalog.getName())
for repo_name in catalog.listRepositories():
    print('  - ' + repo_name)

# create a new repository
from franz.openrdf.repository.repository import Repository
repo_name = 'COSC504'
mode = Repository.ACCESS
my_repository = catalog.getRepository(repo_name, mode)
my_repository.initialize()

# get access to the repository
conn = my_repository.getConnection()
print('Repository %s is up!' % my_repository.getDatabaseName())
print('It contains %d statement(s).' % conn.size())

