from bs4 import BeautifulSoup
import unittest
import re

def parse(path_to_file):
    with open(f'{path_to_file}', encoding='utf-8') as data:
        soup = BeautifulSoup(data, "html.parser")

    body = soup.find(id="bodyContent")

    imgs = len((body.find_all('img', width=lambda x: int(x or 0) > 199)))
    headers = len([i.text for i in body.find_all(name=re.compile(r'[hH1-6]{2}')) if i.text[0] in 'ETC'])
    linkslen = 0
    link_found = body.find_all('a')
    for i in link_found:
        next = i.find_next_sibling()
        local_linklen = 1
        while next != None:
            if next.name == 'a':
                local_linklen += 1
                next = next.find_next_sibling()
                linkslen = max(linkslen, local_linklen)
            else:
                break
    lists = 0
    html_lists = body.find_all(['ul', 'ol'])
    for html_list in html_lists:
        if not html_list.find_parents(['ul', 'ol']):
            lists += 1

    return [imgs, headers, linkslen, lists]

class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()