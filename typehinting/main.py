
# check consistency and type with  mypy main.py

def myfunction(params: int) -> str:
    return f"{params + 10}"

def otherfunction(params: str):
    print(params)

def listofint(params: list[int]):
    print(params)

otherfunction(myfunction(400))
listofint([2, 3])