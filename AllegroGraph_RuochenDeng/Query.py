# get metadata about agraph from os
import os
import time

from franz.openrdf.query.query import QueryLanguage
from franz.openrdf.rio.rdfformat import RDFFormat


def getConnect():
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

    return conn


def query1(conn, dataset, id):
    query = """
    PREFIX : <http://example.org/%s_node/>

    SELECT (COUNT(?neighbor) AS ?count)
    WHERE {
      :%d ?p ?neighbor .
    }
    """ % (dataset, id)
    tuple_query = conn.prepareTupleQuery(QueryLanguage.SPARQL, query)
    start_time = time.time()
    result = tuple_query.evaluate()
    end_time = time.time()

    with result:
        for binding_set in result:
            return binding_set.getValue('count').getValue(), end_time - start_time


def query2(conn, dataset, id):
    query = """
    PREFIX : <http://example.org/%s_node/>

    SELECT (COUNT(DISTINCT ?common_neighbor) AS ?count)
    WHERE {
      :%d ?p1 ?common_neighbor .
      OPTIONAL {
        ?common_neighbor ?p2 ?other_neighbor .
        FILTER (?other_neighbor != :%d)
      }
    }
    """ % (dataset, id, id)
    tuple_query = conn.prepareTupleQuery(QueryLanguage.SPARQL, query)
    start_time = time.time()
    result = tuple_query.evaluate()
    end_time = time.time()

    with result:
        for binding_set in result:
            return binding_set.getValue('count').getValue(), end_time - start_time


def query3(conn, dataset, id):
    query = """
    PREFIX : <http://example.org/%s_node/>
    
    SELECT (COUNT(DISTINCT ?third_neighbor) AS ?count)
    WHERE {
      :%d ?p1 ?common_neighbor .
      ?common_neighbor ?p2 ?second_neighbor .
      OPTIONAL {
        ?second_neighbor ?p3 ?third_neighbor .
        FILTER (?third_neighbor != :%d && ?third_neighbor != ?common_neighbor)
      }
    }
    """ % (dataset, id, id)
    tuple_query = conn.prepareTupleQuery(QueryLanguage.SPARQL, query)
    start_time = time.time()
    result = tuple_query.evaluate()
    end_time = time.time()

    with result:
        for binding_set in result:
            return binding_set.getValue('count').getValue(), end_time - start_time


def query4(conn, dataset, id):
    query = """
    PREFIX : <http://example.org/%s_node/>
    
    SELECT (COUNT(DISTINCT ?fourth_neighbor) AS ?count)
    WHERE {
      :%d ?p1 ?common_neighbor .
      ?common_neighbor ?p2 ?second_neighbor .
      ?second_neighbor ?p3 ?third_neighbor .
      OPTIONAL {
        ?third_neighbor ?p4 ?fourth_neighbor . 
        FILTER (?fourth_neighbor != :%d && ?fourth_neighbor != ?common_neighbor && ?fourth_neighbor != ?second_neighbor)
      }
    }
    """ % (dataset, id, id)
    tuple_query = conn.prepareTupleQuery(QueryLanguage.SPARQL, query)
    start_time = time.time()
    result = tuple_query.evaluate()
    end_time = time.time()

    with result:
        for binding_set in result:
            return binding_set.getValue('count').getValue(), end_time - start_time


def query5(conn, dataset, id):
    query = """
    PREFIX : <http://example.org/%s_node/>
    
    SELECT (COUNT(DISTINCT ?fifth_neighbor) AS ?count)
    WHERE {
      :%d ?p1 ?common_neighbor .
      ?common_neighbor ?p2 ?second_neighbor .   
      ?second_neighbor ?p3 ?third_neighbor .
      ?third_neighbor ?p4 ?fourth_neighbor .
      OPTIONAL {
        ?fourth_neighbor ?p5 ?fifth_neighbor .
        FILTER (?fifth_neighbor != :%d && ?fifth_neighbor != ?common_neighbor && ?fifth_neighbor != ?second_neighbor && ?fifth_neighbor != ?third_neighbor)
      }
    }
    """ % (dataset, id, id)
    tuple_query = conn.prepareTupleQuery(QueryLanguage.SPARQL, query)
    start_time = time.time()
    result = tuple_query.evaluate()
    end_time = time.time()

    with result:
        for binding_set in result:
            return binding_set.getValue('count').getValue(), end_time - start_time


def load_data(conn, dataset, file_name):
    print('Loading data for %s...' % dataset)
    start_time = time.time()
    conn.addFile(file_name, None, format=RDFFormat.TURTLE)
    end_time = time.time()

    return end_time - start_time



if __name__ == '__main__':
    conn = getConnect()

    datasets = ['squirrel', 'chameleon', 'crocodile']
    ids = [777, 2041, 319]

    # cnt = 1
    # # for query in [query1, query2, query3, query4, query5]:
    # for query in [query5]:
    #     for dataset in datasets:
    #         sum_time = 0
    #         sum_value = 0
    #         for id in ids:
    #             result, tt = query(conn, dataset, id)
    #             sum_value += int(result)
    #             sum_time += tt*1000
    #         print('Query %d: %s, %d, %.1f' % (cnt, dataset, sum_value / len(ids), sum_time / len(ids)))
    #     cnt += 1

    for dataset in datasets:
        tt = load_data(conn, dataset, '%s.rdf' % dataset)
        print('Load %s: %.1f' % (dataset, tt))