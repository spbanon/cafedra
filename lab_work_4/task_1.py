# TODO решите задачу
import json
def task() -> float:
    total = .0
    with open('input.json','r') as f:
        data = json.load(f)
    for el in data:
        res = el.get('score',0)*el.get('weight',0)
        total += res
    return round(total,3)


print(task())
