import regex as re
import csv 
def reg_parentheses(line):
    pattern = r'(\([^()]*\([^()]*\)[^()]*\)|\([^()]*\))'
    matches = re.findall(pattern, line)
    return matches

def extractor(file_path):
    try:
        with open(file_path, "r") as file:
            #Data will contain a list of dictionary mappings for ease of CSV writing
            definitions = []
            #Extract definitions from each line
            for line in file:
                if line[0] != "(":
                    matches = reg_parentheses(line)
                    for match in matches:
                        regex = re.compile('[,\.!?;""<>\(\)`]')
                        match = regex.sub('', match)
                        if ' ' in match:
                            match_dict = {}
                            match_dict["definition"] = match
                            definitions.append(match_dict)
                  
            # Having grouped all definitions into a list of dictionaries
            # Write each one to CSV file
            with open("test.csv", "w", newline='') as csvfile:
                fieldnames=["definition"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerows(definitions)
                
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        
def main():
    user_input = input("File path of dict.db: ")
    extractor(user_input)
    
main()
