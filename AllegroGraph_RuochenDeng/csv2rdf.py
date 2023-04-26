import csv
from rdflib import Graph, Namespace, RDF, URIRef

# 定义命名空间
SCHEMA = Namespace('http://schema.org/')


files = ['squirrel', 'crocodile', 'chameleon']
for file in files:
    # 创建RDF图
    g = Graph()

    # 打开CSV文件
    filename = 'musae_' + file + '_edges.csv'
    with open(filename, 'r') as csvfile:
        # 创建CSV读取器
        reader = csv.reader(csvfile)
        # 遍历CSV文件中的每一行
        for row in reader:
            # 获取起点和终点
            start = row[0]
            end = row[1]

            # 创建URI标识符
            start_uri = URIRef('http://example.org/' + file +  '_node/' + start)
            end_uri = URIRef('http://example.org/' + file +  '_node/' + end)

            # 将边转换为RDF三元组
            g.add((start_uri, SCHEMA['link'], end_uri))

    # 保存RDF文件
    g.serialize(destination=file+'.rdf', format='turtle')
