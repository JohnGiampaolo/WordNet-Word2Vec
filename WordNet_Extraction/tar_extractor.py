import tarfile

def extract_tar_gz(file_path, extract_path="."):
    try:
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(path=extract_path)
            print(f"Extracted {file_path} to {extract_path}")
    except Exception as e:
        print(f"Error extracting {file_path}: {e}")

# Example usage
extract_tar_gz("wn3.1.dict.tar.gz", "./extracted_files")