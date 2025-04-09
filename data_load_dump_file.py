import json
import pandas as pd

def main():
    data = {
            "name": "Alice",
            "age": 25,
            "languages": ["Python", "JavaScript"]
        }

    # Write to file
    with open("data.json", "w") as f:
        json.dump(data, f)

    # Read back from file
    with open("data.json", "r") as f:
        loaded_data = json.load(f)

    # print(loaded_data)
    # print(loaded_data['languages']) 

    frames = pd.DataFrame(loaded_data)
    # for index, row in frames.iterrows():
    #     print(frames.iloc[index]['languages'])

    list_of_lists = frames.values.tolist()

    # for list in list_of_lists:
    #     print(list)

    json_str = frames.to_json()

    for i in range(len(frames)):
        print(frames.iloc[i]['name'])

if __name__ == "__main__":
    main()