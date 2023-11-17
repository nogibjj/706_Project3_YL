[![CI](https://github.com/nogibjj/706_Week01_YL/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/706_Week01_YL/actions/workflows/cicd.yml)

# 706_Project3_YL

This repository includes the main tasks for Project 3:

* `Makefile` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.
* `.devcontainer` includes a Dockerfile and `devcontainer.json`. The `Dockerfile` within this folder specifies how the container should be built, and other settings in this directory may control development environment configurations.
* `Workflows` includes GitHub Actions, which contain configuration files for setting up automated build, test, and deployment pipelines for your project.
* `.gitignore` is used to specify which files or directories should be excluded from version control when using Git.
* `README.md` is the instruction file for the readers.
* `main.py` is a Python file that contains the main function.
* `test_main.py`  is a test file for `main.py` that can successfully run in IDEs.
* `requirements.txt` is to specify the dependencies (libraries and packages) required to run the project.

## Project description
* Databricks notebook with ETL pipeline
* Delta Lake for data storage
* Spark SQL for data transformation
* Visualization of the transformed data
* Automated trigger to initiate the pipeline

## Project environment

* Use Azure Databricks for scripting
* Link GitHub to Azure Databricks
* Container built in `devcontainers` and virtual environment activated via `requirements.txt`

## Major steps
* Extract data from URL
* Fetch data
* Set up `Global init script` in Databricks
* Transform and load data
* Query transformation and data visualization
* File path checking for `make test`
* Clone repo into Databricks workspace
* Create new cluster
* Create new job to build a new ETL pipeline with automated trigger
* Add `JOB_ID`, `SERVER_HOSTNAME` and `TOKEN` in GitHub settings

## Check format & errors

## Video link


## References