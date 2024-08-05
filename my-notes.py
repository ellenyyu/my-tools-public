import streamlit as st
import ast

notes = ['''
Here's a Python class that integrates Google BigQuery (GBQ) with AWS Secrets Manager for authentication and data retrieval. This example assumes you're using the `google-cloud-bigquery` package for GBQ and `boto3` for AWS Secrets Manager.

First, you'll need to install the necessary libraries if you haven't already:

```bash
pip install google-cloud-bigquery boto3
```

Here's the class:

```python
import boto3
from google.cloud import bigquery
from google.oauth2 import service_account
import json

class GBQDataRetriever:
    def __init__(self, aws_secret_name, aws_region):
        self.aws_secret_name = aws_secret_name
        self.aws_region = aws_region
        self.credentials = self.get_credentials_from_aws_secrets_manager()
        self.client = bigquery.Client(credentials=self.credentials)

    def get_credentials_from_aws_secrets_manager(self):
        # Create a Secrets Manager client
        client = boto3.client('secretsmanager', region_name=self.aws_region)
        
        # Retrieve the secret
        secret_response = client.get_secret_value(SecretId=self.aws_secret_name)
        
        # Parse the secret (assuming it's stored as a JSON string)
        secret = json.loads(secret_response['SecretString'])
        
        # Create Google OAuth2 credentials from the secret
        credentials = service_account.Credentials.from_service_account_info(secret)
        
        return credentials

    def query_table(self, query):
        # Query GBQ using the BigQuery client
        query_job = self.client.query(query)  # Make an API request.

        # Wait for the query to finish
        result = query_job.result()

        # Convert the result to a list of dictionaries
        rows = [dict(row) for row in result]

        return rows

# Example usage
if __name__ == "__main__":
    aws_secret_name = "your-aws-secret-name"
    aws_region = "your-aws-region"
    query = "SELECT * FROM `your-project.your_dataset.your_table` LIMIT 10"

    gbq_data_retriever = GBQDataRetriever(aws_secret_name, aws_region)
    data = gbq_data_retriever.query_table(query)
    print(data)
```

### Explanation:

1. **AWS Secrets Manager**: The class retrieves Google Cloud service account credentials stored in AWS Secrets Manager.

2. **Google Cloud BigQuery**: The class uses the `google-cloud-bigquery` library to create a client and execute queries.

3. **`get_credentials_from_aws_secrets_manager` method**: This method retrieves and parses the credentials from AWS Secrets Manager.

4. **`query_table` method**: This method takes an SQL query as an argument, runs it against GBQ, and returns the result as a list of dictionaries.

### Setup:

1. **AWS Secrets Manager**: Store your Google Cloud service account key JSON in AWS Secrets Manager. Ensure it’s stored as a JSON string.

2. **Google Cloud**: Make sure you have the necessary permissions to query the BigQuery tables.

This class should be a good starting point for integrating GBQ into your codebase using AWS Secrets Manager for authentication.
''', '''
Here's a more tailored class that fits into your data app for pulling data from Google BigQuery (GBQ). This class handles authentication, querying, and returning results in a convenient format for further processing within your application.

### Requirements

Ensure you have the `google-cloud-bigquery` package installed:

```bash
pip install google-cloud-bigquery
```

### Python Class

```python
from google.cloud import bigquery
from google.oauth2 import service_account
import os

class GBQDataApp:
    def __init__(self, credentials_path=None):
        """
        Initialize the GBQDataApp with credentials.

        :param credentials_path: Path to the service account JSON file. 
                                 If None, it will use the default credentials.
        """
        self.credentials = self._load_credentials(credentials_path)
        self.client = bigquery.Client(credentials=self.credentials)

    def _load_credentials(self, credentials_path):
        """
        Load credentials from a file or use default application credentials.

        :param credentials_path: Path to the service account JSON file.
        :return: Google Cloud credentials object.
        """
        if credentials_path and os.path.exists(credentials_path):
            return service_account.Credentials.from_service_account_file(credentials_path)
        else:
            # If no credentials file is provided, use default application credentials.
            return None

    def query(self, query_string):
        """
        Execute a query and return the results.

        :param query_string: SQL query to execute.
        :return: List of dictionaries containing query results.
        """
        query_job = self.client.query(query_string)
        result = query_job.result()

        return [dict(row) for row in result]

# Example usage
if __name__ == "__main__":
    credentials_path = "path/to/your/service_account.json"
    query_string = "SELECT * FROM `your_project.your_dataset.your_table` LIMIT 10"

    gbq_data_app = GBQDataApp(credentials_path)
    results = gbq_data_app.query(query_string)
    print(results)
```

### Explanation:

1. **Initialization (`__init__`)**: The class can either use a specified service account JSON file or default credentials (if running in an environment where Google Cloud credentials are automatically provided, like on Google Cloud VMs).

2. **Credential Loading (`_load_credentials`)**: Handles loading credentials either from a provided file path or using the default credentials available in the environment.

3. **Query Execution (`query`)**: Takes an SQL query string as input and returns the results as a list of dictionaries, making it easier to work with the data in your app.

### Usage in Your Data App:

1. **Instantiate the Class**: Create an instance of the `GBQDataApp` class, providing the path to your service account credentials if necessary.

2. **Run Queries**: Use the `query` method to execute SQL queries against your GBQ tables and retrieve the results.

This class should integrate smoothly with your existing data app and simplify the process of pulling data from GBQ.
'''
,
'''
When building a cost-efficient data app that queries Google BigQuery (GBQ), there are several strategies you can use to minimize costs. Here are some best practices and tips for optimizing your queries and usage:

### 1. **Use Partitioned and Clustered Tables**
   - **Partitioned Tables**: Partition tables by a date or timestamp column. This allows you to query only the relevant partitions instead of the entire dataset.
   - **Clustered Tables**: Cluster tables by columns that are frequently filtered. This reduces the amount of data BigQuery scans and therefore lowers costs.

### 2. **Optimize Query Performance**
   - **Avoid SELECT \***: Only select the columns you need. This reduces the amount of data processed.
   - **Use Query Caching**: BigQuery caches query results for 24 hours. If your query results don’t change frequently, you can leverage cached results at no cost.
   - **Use LIMIT**: When testing queries, use the `LIMIT` clause to reduce the amount of data processed.
   - **Filter Early**: Apply filters as early as possible in the query to minimize data scanning.

### 3. **Materialized Views and Persistent Derived Tables**
   - **Materialized Views**: If you have complex queries that run frequently, consider using materialized views. These precomputed views save on query costs, as they do not need to recompute results every time.
   - **Persistent Derived Tables**: Store frequently accessed or complex query results in a separate table that you periodically update, rather than running the query each time.

### 4. **Use Presto or Dataflow for Complex Processing**
   - For complex data processing tasks, consider offloading to Presto (for interactive queries) or Dataflow (for batch processing). These tools can be more cost-effective for heavy transformations compared to running them directly in GBQ.

### 5. **Monitor and Budget Costs**
   - **BigQuery Cost Controls**: Set up cost controls like query quotas, budget alerts, and monitoring to prevent unexpected high costs.
   - **Query Execution Dry Runs**: Use dry runs (`--dry-run` flag in the CLI or `dryRun` option in the API) to estimate the query cost before actually running it.

### 6. **Leverage the Free Tier and Flat-Rate Pricing**
   - **Free Tier**: Take advantage of BigQuery's free tier, which provides 1 TB of querying and 10 GB of storage per month at no cost.
   - **Flat-Rate Pricing**: If your usage is consistent and high, consider flat-rate pricing for more predictable costs.

### 7. **Data App Integration**
   - **Batch Queries**: Where possible, batch queries instead of making them on-demand to reduce the number of queries.
   - **Streaming Inserts**: If you're using streaming data, use streaming inserts sparingly as they can be more expensive compared to loading data in batches.
   - **Preprocess Data**: Preprocess and filter data before uploading to BigQuery to reduce the volume of data and the complexity of queries.

### Example Python Code for Cost-Efficient Querying

Here’s how you might set up a class that follows these principles:

```python
from google.cloud import bigquery
from google.oauth2 import service_account
import os

class CostEfficientGBQApp:
    def __init__(self, credentials_path=None):
        self.credentials = self._load_credentials(credentials_path)
        self.client = bigquery.Client(credentials=self.credentials)

    def _load_credentials(self, credentials_path):
        if credentials_path and os.path.exists(credentials_path):
            return service_account.Credentials.from_service_account_file(credentials_path)
        return None

    def run_query(self, query_string, use_cache=True, max_bytes_billed=None):
        job_config = bigquery.QueryJobConfig()

        if use_cache:
            job_config.use_query_cache = True

        if max_bytes_billed:
            job_config.maximum_bytes_billed = max_bytes_billed

        query_job = self.client.query(query_string, job_config=job_config)
        result = query_job.result()

        return [dict(row) for row in result]

# Example usage
if __name__ == "__main__":
    credentials_path = "path/to/your/service_account.json"
    query_string = "SELECT column1, column2 FROM `your_project.your_dataset.your_table` WHERE date_column = '2024-08-01'"

    gbq_app = CostEfficientGBQApp(credentials_path)
    results = gbq_app.run_query(query_string, max_bytes_billed=10**9)  # 1 GB limit
    print(results)
```

### Explanation:

- **`use_cache=True`**: This option ensures that cached results are used if available.
- **`max_bytes_billed=10**9`**: This limits the query cost by setting a cap on the amount of data that can be processed. You can adjust this to control your costs.

By following these strategies, you can optimize the cost of querying data from GBQ while supporting the needs of your data app.
''', 
'''
Setting up a materialized view in Google BigQuery allows you to store the results of a query and automatically refresh them when the underlying data changes. This can significantly improve query performance and reduce costs for frequently run complex queries.

### Steps to Set Up a Materialized View

1. **Write the Base Query**: Identify the complex or frequently run query that you want to materialize.

2. **Create the Materialized View**: Use the `CREATE MATERIALIZED VIEW` statement to define the view.

3. **Query the Materialized View**: Use it like a regular table or view in your queries.

4. **Monitor and Refresh**: BigQuery automatically manages the refresh of materialized views. You can also manually refresh if needed.

### Example

#### 1. Write the Base Query

Suppose you have a table called `sales_data` with columns `product_id`, `sales_date`, `sales_amount`, and `region`, and you frequently run a query to aggregate sales by region and month.

Base Query:
```sql
SELECT 
    region,
    EXTRACT(MONTH FROM sales_date) AS sales_month,
    SUM(sales_amount) AS total_sales
FROM 
    `your_project.your_dataset.sales_data`
GROUP BY 
    region, sales_month
```

#### 2. Create the Materialized View

Use the following SQL to create a materialized view based on the base query:

```sql
CREATE MATERIALIZED VIEW 
    `your_project.your_dataset.sales_summary_mv`
AS 
SELECT 
    region,
    EXTRACT(MONTH FROM sales_date) AS sales_month,
    SUM(sales_amount) AS total_sales
FROM 
    `your_project.your_dataset.sales_data`
GROUP BY 
    region, sales_month
```

- The materialized view will store the aggregated results of the query.

#### 3. Query the Materialized View

You can now use the materialized view in your queries, which will be much faster and cost-effective compared to running the aggregation query every time.

Example Query:
```sql
SELECT 
    region, 
    sales_month, 
    total_sales 
FROM 
    `your_project.your_dataset.sales_summary_mv`
WHERE 
    region = 'North America'
```

#### 4. Monitor and Refresh

- **Automatic Refresh**: BigQuery automatically refreshes the materialized view whenever the underlying data changes. The refresh process is managed by BigQuery, and there's no need for manual intervention in most cases.
- **Manual Refresh**: If needed, you can manually refresh the materialized view using the `REFRESH MATERIALIZED VIEW` statement:
    ```sql
    REFRESH MATERIALIZED VIEW `your_project.your_dataset.sales_summary_mv`
    ```

### Considerations

- **Cost Efficiency**: Materialized views are more cost-efficient for frequently run complex queries, as they reduce the amount of data processed.
- **Data Freshness**: Materialized views may not always reflect the most up-to-date data immediately due to the time taken to refresh. However, the trade-off is often worth it for the performance gain.
- **Limitations**: Materialized views have certain limitations, such as restrictions on the types of queries they can materialize (e.g., no non-deterministic functions, no subqueries in the SELECT clause).

By setting up materialized views for your complex and frequently run queries, you can optimize both performance and cost in your data app.
'''
]
counter = 0 
for note in notes: 
    counter+=1
    st.markdown(f"# Note {counter}")
    st.markdown(note)