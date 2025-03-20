# run this to generate the processed data
from project_package.data import import_data

if __name__ == "__main__":
    print("processing raw data")
    import_data.process_rawdata()
    print("done")
