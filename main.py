from mylib.extract import extract
from mylib.transform_load import load
from mylib.visualization import query_transform, visualization
import os 


if __name__ == "__main__":
    current_directory = os.getcwd()
    print(current_directory)
    extract()
    load()
    query_transform()
    visualization()