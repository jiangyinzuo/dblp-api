import fire
# import json

import dblp
import requests


def main(input: str, with_ccf_class: bool = False):
    results = dblp.search([input])
    if with_ccf_class:
        results = dblp.add_ccf_class(results)
    for result in results:
        print(requests.get(result['bibtex']).text)
    # print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    fire.Fire(main)
