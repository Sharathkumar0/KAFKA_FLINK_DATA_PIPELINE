# KAFKA_FLINK_DATA_PIPELINE
This project demonstrates a real-time data processing pipeline using Apache Kafka and Apache Flink. The pipeline consists of **three components:**

**Kafka Producer** — generates and sends data to a Kafka topic.
**Flink Streaming Job** — consumes the data, filters it based on a condition, and forwards it to another Kafka topic.
**Kafka Consumer** — reads and displays the filtered results from the output topic.

**PIPELINE FLOW:**

**Kafka Producer ───▶ Kafka Topic (input_topic) ───▶ Flink Job ───▶ Kafka Topic (output_topic) ───▶ Kafka Consumer**

**COMPONENTS EXPLAINED:**
**1. KAFKA PRODUCCER - DATA GENERATOR**
  * sends product data (in JSON format) to Kafka topic input_topic.
  * Each message contains fields like title, price, currency, and url.

**2. FLINK STREAMING JON: DATA FILTER:**
   * Reads data from input_topic using the Kafka connector.
   * Filters records where price > 500.
   * Writes the filtered results to output_topic.

**3. KAFKA CONSUMER: FILTERED DATA READER:**
   * Connects to output_topic and reads only the filtered messages.
   * Prints or processes the data as needed.
   * Configured to stop automatically after no new messages are received for a period (optional).

