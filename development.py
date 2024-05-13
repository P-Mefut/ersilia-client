from ersilia_client import ErsiliaClient, example_url

example_url = "https://eos43at-boaoi.ondigitalocean.app/"
ec = ErsiliaClient(url=example_url)
input = ["CCCCOC", "CCCCCN"]
result = ec.run(input)
print(result)