import json


def load_verbs():
    try:
        with open('verb.json', 'r', encoding='utf-8') as file:
            verbs = json.load(file)
        return verbs
    except Exception as e:
        print(e)


def load_file(verbs):
    try:
        with open('text.txt', 'r', encoding='utf-8') as file:
            words= {}
            all_words = {}
            for line in file:
                lin = line.strip()
                lin = lin.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace(
                    '"', "").replace(";", "").split(" ")
                for i in lin:
                    if i in verbs:
                        all_words.update({verbs[i]["infinitive"]: verbs[i]})
                        words.update({i:verbs[i]})
        return all_words, words
    except Exception as e:
        print(e)


if __name__ == '__main__':
    verbs = load_verbs()
    all_words, words = load_file(verbs)
    print('Найденные слова:')
    for verb in all_words:
        print("==================================================================")
        print(f"Глагол: {verb} : \n"
              f"{verbs[verb]['infinitive']} | {verbs[verb]['past_simple']} | {verbs[verb]['participle']}\nПеревод:{verbs[verb]['translate']}")
    print("==================================================================")
    print('Проверьте слова в контексте!')
    with open('words.txt','w', encoding='utf-8') as output:
        output.write(json.dumps(words, indent=4,ensure_ascii=False))