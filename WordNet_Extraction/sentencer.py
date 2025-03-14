import regex as re
import csv 
import os

def reg_parentheses(line):
    pattern = r'(\([^()]*\([^()]*\)[^()]*\)|\([^()]*\))'
    matches = re.findall(pattern, line)
    return matches

def extractor(dir_path):
    try:
        #Data will contain a list of dictionary mappings for ease of CSV writing
        definitions = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, "r") as file:
                    #Extract definitions from each line
                    for line in file:
                        if line[0] != "(":
                            matches = reg_parentheses(line)
                            for match in matches:
                                regex = re.compile(r'[,\.\!?;""<>\(\)`]')
                                match = regex.sub('', match)
                                if ' ' in match:
                                    match_dict = {}
                                    match_dict["definition"] = match
                                    definitions.append(match_dict)
                        
        # Having grouped all definitions into a list of dictionaries
        # Write each one to CSV file
        with open("definitions.csv", "w", newline='') as csvfile:
            fieldnames=["definition"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerows(definitions)
                
    except Exception as e:
        print(f"Error reading {dir_path}: {e}")
        
def main():
    user_input = input("Directory path: ")
    extractor(user_input)
    
main()
