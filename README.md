# Lab 1

For this lab we will be showing off the capabilities of a tool called [Dagster](https://dagster.io/). Dagster essentially allows users to build analytic pipelines easily with a python based interfaced for interacting. This first lab will go over installation of dagster as well as a brief overview of what is within the user interface for dagster. By the end of the lab you should be familiar with materializing jobs in Dagster

## Getting Started

First clone the lab locally and install the dependencies like so:

```bash
git clone git@github.com:TPL-515/Lab1.git
cd Lab1/
pip install -e ".[dev]"
```

This should install all of the required dependencies for the lab.

## Running the Lab

In order to run the lab just run the following command:

```bash
dagster dev
```

From here you should be able to navigate to the UI hosted at: http://localhost:3000
