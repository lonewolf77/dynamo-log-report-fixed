Analyze the Apache-style access log located at `/app/access.log`. Parse the data to summarize the traffic, and output your findings to a JSON file located at `/app/report.json`.

To succeed, your report must meet the following criteria:
1. The report contains a `total_requests` key with the exact integer value of the total HTTP requests in the log.
2. The report contains a `unique_ips` key with the exact integer value of the total unique client IP addresses.
3. The report contains a `top_path` key with the exact string value of the most frequently requested path.
