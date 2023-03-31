# script to inject data into json file

import json
import time


def prometheus_node_add(node_ip):
    # open json file
    with open('targets.json') as json_file:
        data = json.load(json_file)

    # insert node data
    data.append({
        "targets": [ f"{node_ip}" ],
        "labels": {
            "env": "prod",
            "job": "node"
        }
    })

    # write to json file
    with open('targets.json', 'w') as outfile:
        json.dump(data, outfile)
    
    print("Node added")


# script to delete data from json file
def prometheus_node_delete(node_ip):

    with open('targets.json') as json_file:
        data = json.load(json_file)

    # delete node data
    for i in data:
        if i["targets"] == [ f"{node_ip}" ]:
            data.remove(i)

    # write to json file
    with open('targets.json', 'w') as outfile:
        json.dump(data, outfile)

    print("Node deleted")

# main
if __name__ == "__main__":
    while True:
        node_ip = input("Enter node IP: ")
        if node_ip == "exit":
            break
        else:
            node_request = input("Add or delete node? ")
            if node_request == "add":
                prometheus_node_add(node_ip)
            elif node_request == "delete":
                prometheus_node_delete(node_ip)
            else:
                print("Invalid request")
                continue
