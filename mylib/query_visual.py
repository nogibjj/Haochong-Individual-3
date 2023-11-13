from pyspark.sql import SparkSession
import matplotlib.pyplot as plt


# sample query
def query_transform():
    """
    Run a predefined SQL query on a Spark DataFrame.

    Returns:
        DataFrame: Result of the SQL query.
    """
    spark = SparkSession.builder.appName("Query").getOrCreate()
    query = (
        "SELECT t1.group, "
        "AVG(t1.spi) as avg_soccer_power_in_609,"
        "AVG(t2.spi) as avg_soccer_power_in_613 "
        "FROM wc609_delta t1 "
        "JOIN wc613_delta t2 ON t1.id = t2.id "
        "GROUP BY t1.group, t2.group "
        "ORDER BY avg_soccer_power_in_609 DESC"
    )
    query_result = spark.sql(query)
    return query_result


# sample viz for project
def vis():
    query = query_transform()
    count = query.count()
    if count > 0:
        print(f"Data validation passed. {count} rows available.")
    else:
        print("No data available. Please investigate.")
    plt.figure(figsize=(15, 8))  # Adjusted figure size

    pandas_df = query.select("avg_soccer_power_in_609", 
                             "avg_soccer_power_in_613", 
                             "group").toPandas()

    # Plot a bar plot
    plt.figure(figsize=(15, 8))
    plt.bar(pandas_df["group"], pandas_df["avg_soccer_power_in_609"], color='skyblue')
    plt.title("Avg Soccer Power in Group by Group on 609")
    plt.xlabel("Group")
    plt.ylabel("Avg Soccer Power in Group")
    plt.show()

    # Plot a single histogram for all groups
    plt.figure(figsize=(15, 8))
    plt.hist(pandas_df["avg_soccer_power_in_613"], bins=20, edgecolor='black')  
    # Adjust the number of bins as needed
    plt.title("Avg Soccer Power in Group by Group on 613")
    plt.xlabel("Group")
    plt.ylabel("Avg Soccer Power in Group")
    plt.show()


if __name__ == "__main__":
    query_transform()
    vis()