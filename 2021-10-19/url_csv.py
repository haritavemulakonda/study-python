import urllib.request

req = urllib.request.Request(
    url="https://haritavemulakonda.github.io/input_class.csv",
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

with urllib.request.urlopen(req) as response:
    list_header_column_lengths = []
    for record_index, record in enumerate(response.readlines()):
        record_string = record.decode("utf-8", "ignore")
        if record_index == 0:
            header = ""
            for word in record_string.split(sep=','):
                padded_word = word + "".ljust(10)
                header += padded_word
                list_header_column_lengths.append(len(padded_word))

            print(header)
            list_header_column_lengths.append(1)
        else:
            temp_string = ""
            for word_index, word in enumerate(record_string.split(sep=',')[1:]):  # ignore the first empty string
                temp_string += word.ljust(list_header_column_lengths[word_index])
            print(temp_string)
