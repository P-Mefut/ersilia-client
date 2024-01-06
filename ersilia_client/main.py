from fastapi import FastAPI, UploadFile, File
import uvicorn
import json
import os
import argparse
import tempfile
import subprocess
import pandas as pd
from typing import Optional

tmp_folder = tempfile.mkdtemp(prefix="ersilia-")

parser = argparse.ArgumentParser(description="ErsiliaAPI app")

parser.add_argument("--info", default=None, type=str, help="Model information in json format")
parser.add_argument("--port", default=8000, type=int, help="An integer for the port")
parser.add_argument("--host", default="0.0.0.0", type=str, help="Host URL")

args = parser.parse_args()

if args.info is None:
    info_json = os.path.join(tmp_folder, "info.json")
    subprocess.Popen("ersilia info > {0}".format(info_json), shell=True).wait()
    with open(info_json, "r") as f:
        info_data = json.load(f)
else:
    with open(args.info, "r") as f:
        info_data = json.load(f)

app = FastAPI(
    title="{0}:{1}".format(info_data["card"]["Identifier"], info_data["card"]["Slug"]),
    description=info_data["card"]["Description"],
    version="latest")

@app.get("/info", tags=["Metadata"])
def info():
    """
    Get information for the Ersilia Model
    
    """
    return info_data

@app.get("/model_id", tags=["Metadata"])
def model_id():
    """
    Get model identifier

    """
    return info_data["card"]["model_id"]


@app.get("/slug", tags=["Metadata"])
def slug():
    """
    Get the slug
    """

@app.get("/status")
def status():
    """
    Model status
    """

@app.post("/run", tags=["App"])
async def run(file: Optional[UploadFile] = File(...), data: Optional[list] = None):
    """
    Upload a file to the server and run predictions
    """
    input_file = '{0}/{1}'.format(tmp_folder, file.filename)
    with open(input_file, 'wb') as buffer:
        buffer.write(await file.read())
    output_file = '{0}/{1}'.format(tmp_folder, file.filename+".output.csv")
    subprocess.Popen("ersilia api -i {0} -o {1}".format(input_file, output_file), shell=True).wait()
    df = pd.read_csv(output_file)
    return df.to_dict(orient='records')


if __name__ == "__main__":
    uvicorn.run("main:app", host=args.host, port=args.port, reload=True)
