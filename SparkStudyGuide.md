## A Spark Study Guide

Skim and analyze these ideas for an intro to Spark. 
Do this more than once, with a half-day or more between skims.

### **Key Concepts of Using Spark for Data Engineering**

1. **Distributed Computing**: 
   - Spark distributes data and computation across a cluster of machines. Tasks are executed in parallel to achieve high performance and scalability.

2. **Resilient Distributed Dataset (RDD)**:
   - The foundational data structure in Spark, RDD is an immutable, distributed collection of objects that can be processed in parallel. It offers fault tolerance and in-memory computation.

3. **Lazy Evaluation**:
   - Spark transformations (e.g., `map`, `filter`) are not executed immediately. Instead, Spark builds a _Directed Acyclic Graph (DAG)_ of operations and optimizes the execution plan before running the tasks.

4. **Fault Tolerance**:
   - Spark automatically handles failures by recomputing lost RDD partitions using lineage information.

5. **Data Abstraction Layers**:
   - Beyond RDDs, Spark provides higher-level APIs like **DataFrames** and **Datasets** that are optimized for structured and semi-structured data processing.

6. **Unified Engine**:
   - Spark supports a variety of data engineering tasks, such as ETL (Extract, Transform, Load), real-time stream processing, machine learning, and graph analytics, all within a single framework.

### **Primary Interfaces in PySpark**

1. **RDD API**:
   - The lower-level API for working with distributed collections.
   - Best for fine-grained control over distributed computations.
   - Example: 
     ```python
     rdd = sc.parallelize([1, 2, 3, 4])
     rdd.map(lambda x: x * 2).collect()
     ```

2. **DataFrame API**:
   - A higher-level abstraction similar to a relational database table or Pandas DataFrame.
   - Optimized for querying and transforming structured data using SQL-like syntax.
   - Example:
     ```python
     from pyspark.sql import SparkSession
     spark = SparkSession.builder.appName("example").getOrCreate()
     df = spark.read.csv("data.csv", header=True, inferSchema=True)
     df.filter(df["age"] > 30).show()
     ```

3. **Dataset API**:
   - Combines the benefits of RDDs (strong typing) and DataFrames (optimizations) but is not available in PySpark (only in Scala and Java).

4. **SQL API**:
   - Provides SQL-like querying capabilities using `spark.sql()`.
   - Example:
     ```python
     df.createOrReplaceTempView("people")
     spark.sql("SELECT * FROM people WHERE age > 30").show()
     ```

5. **Structured Streaming**:
   - Enables real-time processing of streaming data using DataFrame or Dataset APIs.
   - Example:
     ```python
     stream_df = spark.readStream.format("csv").option("path", "stream_data").load()
     stream_df.writeStream.outputMode("append").format("console").start().awaitTermination()
     ```

### **Primary Data Structures in PySpark**

1. **Resilient Distributed Dataset (RDD)**:
   - Immutable and distributed collection of objects.
   - Used for unstructured or semi-structured data.
   - Operations: Transformations (e.g., `map`, `filter`) and Actions (e.g., `count`, `collect`).

2. **DataFrame**:
   - A distributed collection of data organized into named columns.
   - Optimized for SQL-like operations and works well with structured data.
   - Example:
     ```python
     df = spark.read.json("data.json")
     df.select("name", "age").show()
     ```

3. **Column**:
   - Represents a column in a DataFrame.
   - Used for column-level operations.
   - Example:
     ```python
     df.select(df["age"] + 1)
     ```

4. **Row**:
   - Represents a single row of data in a DataFrame.
   - Useful when working with the contents of a DataFrame programmatically.

5. **Schema**:
   - Defines the structure of DataFrames (column names, data types).
   - Example:
     ```python
     from pyspark.sql.types import StructType, StructField, IntegerType, StringType
     schema = StructType([
         StructField("name", StringType(), True),
         StructField("age", IntegerType(), True)
     ])
     df = spark.read.json("data.json", schema=schema)
     ```

By mastering these concepts, interfaces, and data structures, data engineers can efficiently design and implement scalable data pipelines with PySpark.

### **Contrasting Spark and Pandas Key Data Structures**

Both Spark and Pandas are powerful tools for data analysis, but they are designed for different use cases. Below is a comparison of their key data structures.


### **1. Basic Collection: RDD vs Pandas Series**
| Feature                | Spark RDD                          | Pandas Series                       |
|------------------------|------------------------------------|-------------------------------------|
| **Definition**         | Resilient Distributed Dataset (RDD) is a low-level distributed collection of objects that supports parallel processing. | A Pandas Series is a one-dimensional labeled array that can hold data of any type. |
| **Use Case**           | Ideal for unstructured or semi-structured data where control over transformations is required. | Used for operations on single-column data in small-to-medium datasets. |
| **Processing**         | Distributed and fault-tolerant; processes data across a cluster. | Single-node, in-memory processing. |
| **API Complexity**     | Requires explicit transformations and actions (e.g., `map`, `filter`). | Simpler syntax with direct operations (e.g., `series + 1`). |


### **2. Tabular Data: DataFrame vs Pandas DataFrame**
| Feature                | Spark DataFrame                   | Pandas DataFrame                   |
|------------------------|------------------------------------|-------------------------------------|
| **Definition**         | A distributed collection of data organized into named columns. Optimized for structured data with SQL-like querying capabilities. | A two-dimensional labeled data structure (rows and columns) that holds data in memory. |
| **Scale**              | Designed for large-scale data, processes data in distributed clusters. | Best for small to medium datasets that fit in memory. |
| **Speed**              | In-memory processing but optimized for parallelism and scalability. | Extremely fast for single-machine operations on small datasets. |
| **Schema**             | Requires a defined schema, inferred or explicitly provided, for operations. | No schema required; data types inferred dynamically. |
| **Fault Tolerance**    | Built-in fault tolerance and recovery. | No fault tolerance; data loss if process fails. |
| **Operations**         | SQL-like API, optimized query execution with Catalyst Optimizer. | Rich, intuitive API for slicing, filtering, and transforming data. |
| **Eager vs Lazy Evaluation** | Lazy evaluation for transformations (execution is deferred until an action is called). | Eager evaluation; operations execute immediately. |


### **3. Streaming: Spark Structured Streaming vs Pandas**
| Feature                | Spark Structured Streaming         | Pandas (No equivalent)             |
|------------------------|------------------------------------|-------------------------------------|
| **Definition**         | A DataFrame-like API designed for continuous, real-time processing of streaming data. | Pandas does not natively support streaming data. |
| **Processing Model**   | Continuous, micro-batch, or real-time data ingestion and processing. | Operations are static and batch-based. |
| **Scalability**        | Processes large streams of data in distributed environments. | Limited to static datasets that fit in memory. |


### **4. Graph Data: GraphX vs Pandas**
| Feature                | Spark GraphX                      | Pandas (No equivalent)             |
|------------------------|------------------------------------|-------------------------------------|
| **Definition**         | A library for graph computation and analysis in Spark. | Pandas lacks built-in support for graph processing. |
| **Use Case**           | Ideal for large-scale graph analytics (e.g., social network analysis). | Requires integration with external libraries like NetworkX for graph operations. |



### **Key Differences in Data Structures**

| Aspect                   | Spark (RDD, DataFrame)              | Pandas (Series, DataFrame)           |
|--------------------------|-------------------------------------|--------------------------------------|
| **Scalability**          | Designed for distributed systems, handles terabytes to petabytes of data. | Limited to data that fits in memory on a single machine. |
| **Fault Tolerance**      | Built-in recovery for failures.    | No fault tolerance or recovery.     |
| **Execution Model**      | Lazy evaluation for transformations, optimized DAG execution. | Eager evaluation, operations execute immediately. |
| **Processing Environment** | Distributed clusters (multi-node). | Single-node, in-memory.             |
| **Ease of Use**          | Requires some understanding of distributed computing principles. | User-friendly for small-to-medium data analytics. |
| **Real-Time Processing** | Supports streaming data.           | No native streaming capabilities.   |


### **When to Use Spark vs Pandas**

| **Use Pandas**                       | **Use Spark**                     |
|--------------------------------------|-----------------------------------|
| Small datasets that fit in memory.  | Large datasets beyond a single machine's capacity. |
| Quick, exploratory data analysis.   | Building scalable data pipelines. |
| Single-node environments.           | Distributed, cluster-based environments. |
| When operations require a rich and simple API. | When processing speed and scalability are critical. |

By understanding these distinctions, data engineers can choose the right tool for their specific use case and leverage Spark and Pandas effectively for data processing.