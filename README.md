# python_startup

This is a recomended python project structure and tools.

## tutorial
https://www.w3schools.com/python/default.asp

## libraries

### pip

```
sudo apt update
sudo apt install python3-pip
sudo apt install python3-pip -y
pip3  --version
```

Create python environments

```
sudo apt install python3.12-venv
python3 -m venv /home/kj/python_env/one
/home/kj/python_env/one/bin/pip install pandas
```

### NumPy 
Python library (Numerical Python) used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices. In Python we have lists that serve the purpose of arrays, but they are slow to process. NumPy aims to provide an array object that is up to 50x faster than traditional Python lists. multi-dimensional arrays and matrices. https://www.w3schools.com/python/numpy/default.asp

- create arrays: arr = np.array([1, 2, 3, 4, 5])
- generate random numbers: x = random.randint(100)
- generate array permutations: random.permutation(arr)
- generate normal distribution: x = random.normal(size=(2, 3))
- add the values in arr1 to the values in arr2: newarr = np.add(arr1, arr2)

```
pip install numpy
```

### Pandas
Python library (Python Data Analysis) used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data. https://www.w3schools.com/python/pandas/default.asp
 
 - remove rows that contain empty cells: new_df = df.dropna()
 - convert all cells in the columns into the same format: df['Date'] = pd.to_datetime(df['Date'])
 - fix wrong values: df.loc[7, 'Duration'] = 45
 - remove duplicates: print(df.duplicated())
 - corelations (relationships): df.corr() 
 - plotting: df.plot()

 ```
 sudo pip install pandas
 ```

### SciPy
SciPy is a scientific computation library that uses NumPy underneath. It provides more utility functions for optimization, stats and signal processing. https://www.w3schools.com/python/scipy/scipy_intro.php

- Optimizers are a set of procedures defined in SciPy that find the minimum value of a function, or the root of an equation. 
- NumPy is capable of finding roots for polynomials and linear equations: 
'''
def eqn(x):  return x + cos(x)
myroot = root(eqn, 0)
'''
- Working with Graphs: dijkstra method to find the shortest path in a graph from one element to another: dijkstra(newarr, return_predecessors=True, indices=0)
- depth_first_order() method returns a depth first traversal from a node: depth_first_order(newarr, 1)
- A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon: hull = ConvexHull(points)
- Interpolation: interp_func = interp1d(xs, ys)

### Django
Django is a Python framework that makes it easier to create web sites using Python. Django follows the MVT design pattern (Model View Template). https://www.w3schools.com/django/django_intro.php

- create virtual environment
'''
python -m venv myworld 
source myworld/bin/activate 
'''

### PySpark

#### Install spark using docker-compose

```
docker-compose up
```

Upen UI:
```
http://localhost:8080/
```

#### Install python virtual env

```
python3 -m venv kj
```
or
```
source kj/bin/activate
```

and later
```
kj/bin/pip install pyspark
kj/bin/pip install pytest
```

#### Run pyspark

PySpark RDD (Resilient Distributed Dataset) is a fundamental data structure that is fault-tolerant, immutable, and distributed collections of objects. RDDs are immutable, meaning they cannot be changed once created. You can perform two types of operations on RDD; Transformations and Actions.
RDD transformations in PySpark are lazy operations and they execute only when an action is called on RDD.
Transformation operations are map, filter, flatMap, groupByKey, reduceByKey, join, union, sortByKey, distinct, sample, mapPartitions, and aggregateByKey. These functions transform RDDs by applying computations in a distributed manner across a cluster of machines and return a new RDD

A DataFrame is a distributed dataset comprising data arranged in rows and columns with named attributes.  

With PySpark DataFrames you can efficiently read, write, transform, and analyze data using Python and SQL

https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html

```
pip install pyspark
pip install pytest

docker pull bitnami/spark:3.5.1
docker run -p 7077:7077 bitnami/spark:3.5.1
```

Spark with RDD example:

```
sc = spark.SparkContext()
# Read the input file and Calculating words count
text_file = sc.textFile("words.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
                            .map(lambda word: (word, 1)) \
                           .reduceByKey(lambda x, y: x + y)
output = counts.collect()
```

Spark with DataFrame example:

```
from pyspark.sql.functions import explode,split,col

df=spark.read.text("words.txt")
#Apply Split, Explode and groupBy to get count()
df_count=(
  df.withColumn('word', explode(split(col('value'), ' ')))
    .groupBy('word')
    .count()
    .sort('count', ascending=False)
)

#Display Output
df_count.display()
```

Spark SQL example:

```
input_df = spark.read.text("words.txt")
#Register the DataFrame as a temporary table. so that you can perform SQL queries on tables
input_df.createOrReplaceTempView("words")
word_count_df = spark.sql("""
    SELECT explode(split(value, ' ')) AS word, COUNT(*) AS count
    FROM words
    GROUP BY word
""")
results = word_count_df.collect()
```

#### pyspark examples

With PySpark DataFrames you can efficiently read, write, transform, and analyze data using Python and SQL.

#### structured streaming

Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine. You can express your streaming computation the same way you would express a batch computation on static data. The Spark SQL engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive.

### Polars

Polars was built from the ground up to be blazingly fast and can do common operations around 5–10 times faster than pandas
The memory requirement for Polars operations is significantly smaller than for pandas: 
pandas requires around 5 to 10 times as much RAM as the size of the dataset to carry out operations, compared to the 2 to 4 times needed for Polars.

Polars is that it is written in Rust.
Rust is that it allows for safe concurrency; that is, it is designed to make parallelism as predictable as possible. 
This gives Polars a massive performance boost over pandas, which only uses one core to carry out operations.

Another factor that contributes to Polars’ impressive performance is Apache Arrow, a language-independent memory format.
One of the main advantages of building a data library on Arrow is interoperability. 
Arrow has been designed to standardize the in-memory data format used across libraries.
Arrow also has built-in support for a wider range of data types than pandas. 

As pandas is based on NumPy, it is excellent at handling integer and float columns, but struggles with other data types. 
In contrast, Arrow has sophisticated support for datetime, boolean, binary, and even complex column types, such as those containing lists.

Polars has the ability to do both eager and lazy execution, where a query optimizer will evaluate all of the required operations and map out the most efficient way of executing the code.

Polars is a tool that right now, is made for single node/machine processing. 

https://realpython.com/polars-python/

```
/home/kj/python_env/one/bin/pip install polars
/home/kj/python_env/one/bin/pip install "polars[all]"
or
/home/kj/Desktop/Krzys/git/python_startup/.env/bin/pip install polars
or
pip install polars
```

## run python unit tests with unittest

https://www.pythontutorial.net/python-unit-testing/python-run-unittest/


```
python3 -m unittest test_package.test_module -v
```

## logging

```
import logging
```

## strong typing

Enable type annotations.

String typing:

https://betterdatascience.com/python-statically-typed/

Install

```
pip install mypy
mypy main.py
```

# functional programming

# formatter

```
yapf --in-place --recursive ./src ./tests
```

## linter

```
pylint ./src ./tests
```

## packaging with  pyproject.toml

https://betterprogramming.pub/a-pyproject-toml-developers-cheat-sheet-5782801fb3ed

```
pip install -q build
flit install --deps=develop
```

Create distribution files:

```
python3 -m build
```

# run code

run spark cluster
```
docker-compose up
```

run code

```
/bin/python3 /home/kj/Krzys/git/python_startup/main.py
```

# books

- https://python-course.eu/books/bernd_klein_python_data_analysis_a4.pdf

- https://englishonlineclub.com/pdf/Test-Driven%20Development%20with%20Python%20(Second%20Edition)%20%5BEnglishOnlineClub.com%5D.pdf

- https://pepa.holla.cz/wp-content/uploads/2016/10/functional-programming-python.pdf

## Learning-PySpark.pdf

https://github.com/dinhtuyen/books/blob/master/docs/src/Spark/Learning-PySpark.pdf

#### Spark Jobs and APIs

Any Spark application spins off a single driver process on the master node that then directs executor processes (jobs) distributed to a number of worker nodes (tasks).

A Spark job is associated with a chain of object dependencies (tasks) organized in a direct acyclic graph (DAG).

Resilient Distributed Datasets (RDDs for short): immutable collections of data split into chunks based on some key, are cached, and stored in-memory. 
RDDs expose some coarse-grained transformations such as map(...), reduce(...), and filter(...).

DataFrames, like RDDs, are immutable collections of data distributed among the nodes in a cluster. However, unlike RDDs, in DataFrames data is organized into named columns.

Spark Datasets is to provide an API that allows users to easily express transformations on domain objects and type-safe programming.

Apache Spark 2.0 =  Tungsten Phase 2 (performance improvements) + structured streaming + unifying Datasets and DataFrames (catalyst optimizer).

The SparkSession is now the entry point for reading data, working with metadata, configuring the session, and managing the cluster resources.

Spark Streaming, there is now a single API that addresses both batch and streaming within the Apache Spark 2.0 release 


