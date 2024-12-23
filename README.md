# Social Network Analysis with Barabasi-Albert and Watts-Strogatz Models

This project provides tools for analyzing social networks using two popular network generation models: **Barabasi-Albert (BA)** and **Watts-Strogatz**. The repository includes scripts for analyzing datasets from **Amazon** and **Twitch**, comparing various network metrics, and logging results for further analysis.

## Files

- **amazon.py**: Script for running network analysis on the Amazon dataset.
    - Generates networks using both the Barabasi-Albert and Watts-Strogatz models.
    - Compares metrics with the original Amazon network.
    - Logs results in `test_amazon.log`.

- **twitch.py**: Script for running network analysis on the Twitch dataset.
    - Similar to `amazon.py`, generates networks using both models and logs results in `test_twitch.log`.

## Requirements

- Python 3.x
- **NetworkX**: For generating and analyzing networks.
- **Matplotlib** (optional): For visualizing network metrics (if desired).

You can install the required packages by running:

```bash
pip install -r requirements.txt
```

## Usage

Each script can be executed independently to analyze the respective dataset. To run the analysis:

```bash
python amazon.py
```

or

```bash
python twitch.py
```

### What happens when you run the script:

1. Loads the original social network dataset (Amazon or Twitch).
2. Generates a network using the **Barabasi-Albert model**.
3. Generates a network using the **Watts-Strogatz model**.
4. Calculates key network metrics (average shortest path length, clustering coefficient, and degree distribution) for each network.
5. Logs the output metrics in the corresponding log file (`test_amazon.log` or `test_twitch.log`).

## Output

The script will output the following:

- **test_amazon.log**: Logs metrics for the Amazon dataset.
- **test_twitch.log**: Logs metrics for the Twitch dataset.

### Metrics logged include:

- **Average shortest path length**: The average length of the shortest paths between nodes.
- **Clustering coefficient**: A measure of the degree to which nodes in the network tend to cluster together.
- **Degree distribution**: Distribution of the number of connections (edges) each node has.

These metrics are crucial for comparing the generated networks to the original social networks.
