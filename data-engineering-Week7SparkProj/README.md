## Data Engineering Week7 Exercises

One of the main obstacles of Data Engineering is the large
and varied technical skills that can be required on a 
day-to-day basis.

This aim of this repository is to help you develop and 
learn those skills. Generally, here are the high level
topics that these practice problems will cover.

- Python data processing.
- csv, flat-file, parquet, json, etc.
- SQL database table design.
- Python + Postgres, data ingestion and retrieval.
- PySpark
- Data cleansing / dirty data.

### How to work on the problems.
You will need two things to work effectively on most all
of these problems. 
- `Docker`
- `docker-compose`

All the tools and technologies you need will be packaged
  into the `dockerfile` for each exercise.

For each exercise you will need to `cd` into that folder and
run the `docker build` command, that command will be listed in
the `README` for each exercise, follow those instructions.

### Weekend Exercises

#### Exercise 6 - Ingestion and Aggregation with PySpark.
The [sixth exercise](https://github.com/kristofer/data-engineering-6-exercises/tree/main/Exercises/Exercise-6) 
Is going to step it up a little and move onto more popular tools. In this exercise we are going
to load some files using `PySpark` and then be asked to do some basic aggregation.
Best of luck!

#### Exercise 7 - Using Various PySpark Functions
The [seventh exercise](https://github.com/kristofer/data-engineering-6-exercises/tree/main/Exercises/Exercise-7) 
Taking a page out of the previous exercise, this one is focus on using a few of the
more common build in PySpark functions `pyspark.sql.functions` and applying their
usage to real-life problems.

Many times to solve simple problems we have to find and use multiple functions available
from libraries. This will test your ability to do that.

#### Exercise 8 - Using DuckDB for Analytics and Transforms.
The [eighth exercise](https://github.com/kristofer/data-engineering-6-exercises/tree/main/Exercises/Exercise-8) 
Using new tools is imperative to growing as a Data Engineer. DuckDB is one of those new tools. In this
exercise you will have to complete a number of analytical and transformation tasks using DuckDB. This
will require an understanding of the functions and documenation of DuckDB.

#### Exercise 9 - Using Polars lazy computation.
The [ninth exercise](https://github.com/kristofer/data-engineering-6-exercises/tree/main/Exercises/Exercise-9) 
Polars is a new Rust based tool with a wonderful Python package that has taken Data Engineering by
storm. It's better than Pandas because it has both SQL Context and supports Lazy evalutation 
for larger than memory data sets! Show your Lazy skills!
