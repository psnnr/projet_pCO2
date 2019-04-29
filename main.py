import toml

params = {}

with open("configuration.toml", 'r', encoding='utf-8') as fp:
    params.update(toml.load(fp))
    print(params)

def load_params(fname = "configuration.toml",param = ""):
    params = {}
    with open(fname, 'r', encoding='utf-8') as fp:
        params.update(toml.load(fp))

