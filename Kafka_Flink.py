import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings

os.environ['FLINK_HOME'] = r'C:\flink-1.19.0'
'

env = StreamExecutionEnvironment.get_execution_environment()
settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
table_env = StreamTableEnvironment.create(env, environment_settings=settings)


# Kafka source table
table_env.execute_sql("""
    CREATE TABLE input_table (
        title STRING,
        price FLOAT,
        currency STRING,
        url STRING       
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'input_topic',
        'properties.bootstrap.servers' = 'localhost:9092',
        'format' = 'json',
        'properties.group.id' = 'flink-group-2',
        'scan.startup.mode' = 'earliest-offset' 
    )
""")

# Define Kafka sink table
table_env.execute_sql("""
    CREATE TABLE output_table (
        title STRING,
        price FLOAT,
        currency STRING,
        url STRING
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'output_topic',
        'properties.bootstrap.servers' = 'localhost:9092',
        'format' = 'json'
    )
""")

# Insert data from source to sink
table_env.execute_sql("""
    INSERT INTO output_table
    SELECT *
    FROM input_table
    WHERE price > 500
""")
