import json
import re


def cleanText(readData):
    # 텍스트에 포함되어 있는 특수 문자 제거
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text


def output(file_name):
    with open('output_' + file_name) as json_file:
        json_data = json.load(json_file)
        hash_tag_all = []

        com_hash_tag = []
        j = 0;
        total_len = 0
        for i in json_data:
            try:
                hash_tag = i['description']  # 해시태그만 추출
            except KeyError:  # 해시태그가 없는 데이터도 있어서 제거함
                continue

            hash_tag = hash_tag.split('#')  # 해시태그로 스플릿
            hash_tag = hash_tag[1:]  # 첫번째 원소는 해시태그가 아닌 설명문장이 있으므로 2번째 원소부터 사용
            if len(hash_tag) == 0:
                continue
            j = j + 1
            total_len = total_len + len(hash_tag)
            hash_tag = [line.replace('\n', '').replace(' ', '') for line in hash_tag]
            hash_tag = [cleanText(line) for line in hash_tag]
            for line in hash_tag:
                if len(line) >= 50:
                    hash_tag.remove(line)

            hash_tag_all.append(hash_tag)  # 계속 합치기

        # print(hash_tag_all)
        for inside_list in hash_tag_all:
            hash_tag_inside = []
            for line in inside_list:
                text = re.sub('[^a-zA-Z]', '', line)  # 영문자 뺴고 다 삭제
                text = text.lower()  # 소문자로,
                if '' != text:  # 공백 제거
                    hash_tag_inside.append(text)  # 최종 전처리 완료된 hasg_tag list
            inside_list = hash_tag_inside
            com_hash_tag.append(inside_list)

        print(total_len / j)  # 평균 포스트당 해시태그 사용 갯수
    return com_hash_tag



