from fastapi import FastAPI
app = FastAPI()

@app.get("/hello/")
def items():
    return {"message": "Hello World"}

print('git')
print ('git2....')





