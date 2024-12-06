# Data Engineering Weekend6 and Week 7

There are two labs in here, one for this weekend, and one to use while working on the Spark Week book.

## Note Bene

That's latin-ish for **pay attention now**.

And I realise I _tend to write these READMEs and you never read them carefully._ 
**BUT** there is a lot of important clarifying detail in all the READMEs in this repo. 
You need to **READ them ALL**. 
Yes, there is more than one README in this repo, and you gotta read them all.

### How to work on the problems.

You will need two things to work effectively on most all
of these problems. 
- `Docker`
- `docker-compose`

_if you haven't installed them yet, do so using Brew._

All the tools and technologies you need will be packaged
  into the `dockerfile` for each exercise.

For each exercise you will need to `cd` into that folder and
run the `docker build` command, that command will be listed in
the `README` for each exercise, follow those instructions.

_Read those last 4 paragraphs again. I don't think you internalized them._

## Weekend6

See [README for Weekend6 exercises.](data-engineering-Weekend6/README.md)
Do this one over the weekend.

## Additional Project for Spark Week 7

See [README for Spark Projects](data-engineering-Week7SparkProj/README.md)
Save this one as part of next week's Spark Week work.
And no, this is **not** the only stuff you'll be handling next week in Week 7.

## Postgres

If you do not already have `postgres` on your mac, you can download [Postgres.app - The easiest way to get started with PostgreSQL on the Mac](https://postgresapp.com).
**Yo! PLEASE read and perform the tasks on that Postgres app front page. Especially steps 1, 2, and 3!!**
_if you don't you can count on being teased mercilessly about not RTFMing_ Huh? Don't know what **RTFM** means? _Look it up._

## Spark 

### A Beginner’s Introduction to Apache Spark: The Why, What, and How

#### **Why Apache Spark?**
Modern organizations are awash in data, often requiring real-time insights from vast datasets. Traditional processing systems struggle to handle the speed, volume, and complexity of today’s data. This is where **Apache Spark** shines. It was built to address the limitations of older big data tools like Hadoop, offering faster data processing, ease of use, and flexibility.

The primary reasons for Spark's popularity include:
1. **Speed**: Spark processes data in memory, making it up to 100x faster than Hadoop for certain workloads.
2. **Scalability**: It can scale seamlessly from a single machine to thousands of servers.
3. **Versatility**: Spark supports batch processing, real-time streaming, machine learning, and graph processing—all in one framework.
4. **Ease of Use**: Developers can write Spark applications using familiar programming languages like Python, Scala, Java, and R.

#### **What is Apache Spark?**
Apache Spark is an open-source distributed computing system designed for big data processing. It provides a unified engine for a wide range of data tasks. Key components of Spark include:

1. **Core Engine**: Handles basic functionalities like task scheduling, memory management, and fault recovery.
2. **Spark SQL**: Enables querying structured data using SQL-like syntax.
3. **Spark Streaming**: Processes real-time data streams, such as those from IoT devices or social media.
4. **MLlib (Machine Learning Library)**: Offers scalable machine learning algorithms for tasks like classification, clustering, and recommendation.
5. **GraphX**: Handles graph processing and analysis.
6. **Structured Streaming**: An advanced API for real-time data processing with guaranteed consistency and fault tolerance.

Spark operates on a **Resilient Distributed Dataset (RDD)**, its core abstraction. RDDs enable parallel data processing across clusters while ensuring fault tolerance.

#### **How Does Apache Spark Work?**
At its core, Spark operates in a distributed environment. Here's a high-level overview of how it works:

1. **Cluster Setup**: Spark runs on a cluster of machines. A **driver** program coordinates the tasks, while **worker nodes** execute them.
2. **Data Loading**: Spark can ingest data from multiple sources, such as Hadoop Distributed File System (HDFS), Amazon S3, or Apache Kafka.
3. **Data Processing**: Spark breaks down the data processing task into smaller parallel tasks distributed across the cluster. Using in-memory computation, Spark minimizes disk I/O, enhancing speed.
4. **Execution Model**: Spark uses a Directed Acyclic Graph (DAG) to optimize task execution. It identifies stages, reduces redundant computations, and executes tasks efficiently.
5. **Result Output**: After processing, the results can be stored back into storage systems or served directly to users or downstream applications.

#### **Why Learn Apache Spark?**
For a beginner data engineer, learning Apache Spark opens doors to handling real-world big data challenges. It's a tool used by leading tech companies like Netflix, Uber, and Amazon to process billions of records daily. Understanding Spark equips you to:
- Build scalable data pipelines.
- Enable real-time analytics.
- Collaborate on machine learning and AI projects.

By mastering Spark, you not only become proficient in big data processing but also lay the foundation for exploring advanced analytics and data engineering solutions.

#### **Getting Started**
To begin your Spark journey:
1. Install Spark locally using Docker.
2. Start with the PySpark API for Python-friendly development.
3. Using the Spark Book, explore Spark’s documentation and tutorials to build practical projects.

Apache Spark isn’t just a tool—it’s a gateway to solving big data challenges with speed, flexibility, and intelligence.

Check out the [Spark Study Guide](SparkStudyGuide.md) for more concise concept descriptions with Spark.

_materials in this repo where shamelessly adapted from https://github.com/danielbeach/data-engineering-practice_