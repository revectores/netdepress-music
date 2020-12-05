from __future__ import annotations
import sys
from pathlib import Path
import csv

from pprint import pprint
import happybase


connect = happybase.Connection('47.94.157.129', port=9090)
print(connect.tables())


def init() -> None:
    connect.create_table(
        'comments',
        {
            'cf': dict()
        }
    )


def read_comments() -> list[dict]:
    comments_csv_path = Path('.') / '../data/comments.csv'

    keys = ['id', 'music_id', 'usr_id', 'time', 'content', 'is_host', 'liked_count', 'emotion']
    cf_keys = [f'cf:{key}' for key in keys]
    with open(comments_csv_path) as comments_csv:
        comments_reader = csv.reader(comments_csv)
        comments = [dict(zip(cf_keys, row)) for row in comments_reader]

    return comments


def insert(comments: list[dict]) -> None:
    comments_table = connect.table('comments')

    for comment in comments:
        comments_table.put(
            comment['cf:id'], comment
        )


def scan() -> list[dict]:
    def strip_cf(column_name: str) -> str:
        if (sys.version_info.major >= 3 and sys.version_info.minor >= 9):
            return column_name.removeprefix('cf:')
        else:
            return column_name[len('cf:'):] if column_name.startswith('cf:') else column_name

    comments_table = connect.table('comments')
    comments = []
    for key, comment in comments_table.scan():
            comments.append({strip_cf(key.decode('utf-8')): value.decode('utf-8') for key, value in comment.items()})
        # print(k, v[b'cf:content'].decode('utf-8'))
    return comments


def delete() -> None:
    comments_table = connect.table('comments')
    comments_table.delete('row_1')
    comments_table.delete('row_2')


if __name__ == '__main__':
    # delete()
    # insert()
    # comments = read_comments()
    # insert(comments)
    # print(sys.version_info)
    comments = scan()
    pprint(comments)
