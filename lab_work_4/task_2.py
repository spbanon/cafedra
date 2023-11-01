# TODO импортировать необходимые молули
import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    delimiter = ','
    newline = '\n'
    with open(INPUT_FILENAME, 'r', newline=newline, encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=delimiter)
        for row in csvreader:
            data.append(row)
    json_string = json.dumps(data, indent=4, ensure_ascii=False)

    with open(OUTPUT_FILENAME,'w') as f:
        f.write(json_string)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
