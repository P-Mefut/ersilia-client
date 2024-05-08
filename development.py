from ersilia_client import ErsiliaClient, example_url

ec = ErsiliaClient(url=example_url)
input = ["CCCCOC", "CCCCCN"]
result = ec.run(input)
print(result)