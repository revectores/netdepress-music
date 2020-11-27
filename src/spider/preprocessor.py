import json
import csv
from pprint import pprint
from pathlib import Path

from conf import comments_root, comments_csv_path


def get_music_ids():
    return [d.name for d in Path(comments_root).iterdir() if d.is_dir() and d.name.isnumeric()]


def read_responses(music_id):
    comments_dict = Path(comments_root) / str(music_id)
    comment_files = [comment_file for comment_file in comments_dict.iterdir() if comment_file.name.endswith('.json')]
    for comment_file in comment_files:
        read_response(comment_file, music_id)


def read_response(comment_file, music_id):
    resp = json.load(open(comment_file))
    if 'hotComments' in resp:
        read_comments(resp['hotComments'], music_id, is_hot=True)

    if 'comments' in resp:
        read_comments(resp['comments'], music_id, is_hot=False)


def read_comments(comments, music_id, is_hot=False):
    if not Path(comments_csv_path).exists():
        with open(comments_csv_path, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(['id', 'music_id', 'user_id', 'time', 'content', 'is_hot', 'liked_count', 'emotion'])

    for comment in comments:
        new_comment = {
            'id':           comment['commentId'],
            'music_id':     music_id,
            'user_id':      comment['user']['userId'],
            'time':         comment['time'],
            'content':      comment['content'],
            'is_hot':       is_hot,
            'liked_count':  comment['likedCount'],
            'emotion':      -1
        }

        with open(comments_csv_path, 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(new_comment.values())


if __name__ == '__main__':
    for music_id in get_music_ids():
        read_responses(int(music_id))
