# There needs to be a more intuitive API for interacting with this data
# YAML doesn't accomodate the same key > once
# So - we need a new file format and an intuitive API
import yaml

with open("triples/founders.yaml", "r") as f:
    try:
        parsed_yaml=yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print(exc)

# get the elements that have an acquisition field

# get the founding year

# reverse lookup a founding year from these elements

from collections import defaultdict
res = defaultdict(dict)

for element in parsed_yaml:
    try:
        year = [x["year"] for x in parsed_yaml[element]["acquisition"] if "year" in x.keys()]
        res[element]["acquisition_year"] = year[0]
    except Exception as e:
        # print("Error: " + str(e))
        pass


for element in parsed_yaml:
    try:
        founded_name = [x for x in parsed_yaml[element]["founded"]]
        print(founded_name)
    except Exception as e:
        # print("Error: " + str(e))
        pass

print(dict(res))
