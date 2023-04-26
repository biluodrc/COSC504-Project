from franz.openrdf.connect import ag_connect

# 连接到本地的AllegroGraph实例
conn = ag_connect("agraph", host="localhost", port=10035, user="cosc504", password="cosc504")

# 创建一个新的命名图
with conn:
    new_graph = conn.new_graph("http://example.org/mygraph")

# 向图中添加数据
with conn.get_repository().get_graph("http://example.org/mygraph") as graph:
    graph.add((
        graph.create_uri("http://example.org/subject"),
        graph.create_uri("http://example.org/predicate"),
        graph.create_literal("object")))

# 查询图中的数据
with conn.get_repository().get_graph("http://example.org/mygraph") as graph:
    results = graph.query('SELECT * WHERE {?s ?p ?o}')
    for row in results:
        print(row)
