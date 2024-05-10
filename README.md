# Shadowing Days Matcher

This project is designed to match shadowers with hosts based on their areas of interest. It uses a bipartite graph and a matching algorithm to find the optimal matches.

## Dependencies

- Python 3
- pandas
- networkx
- numpy
- matplotlib

## Files

- `Matcher.ipynb`: This is the main file where the matching algorithm is implemented.

## How to Run

1. Ensure that you have all the dependencies installed.
2. Open `Matcher.ipynb` in your Jupyter notebook environment.
3. Run all the cells in the notebook.

## How it Works

The script reads data from an Excel file which contains information about shadowers and hosts. It cleans the data and creates a bipartite graph where one set of nodes represents the shadowers and the other set represents the hosts. An edge is created between a shadower and a host if they have at least one common area of interest.

The script then uses the Hopcroft-Karp algorithm to find a maximum cardinality matching of the bipartite graph. This matching represents the optimal assignment of shadowers to hosts.

The results are then visualized using a network graph and also outputted as a DataFrame.

## Note

This project assumes that the input data is in a specific format. Please ensure that your data conforms to this format before running the script.
