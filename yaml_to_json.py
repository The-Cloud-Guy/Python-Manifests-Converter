import json
import sys
import yaml

in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file) as input_content:
    with open(out_file, "w") as output_content:
        yaml_data = yaml.safe_load(input_content.read())
        converted_json_data = json.dumps(yaml_data, indent=2) 

        output_content.write(converted_json_data)