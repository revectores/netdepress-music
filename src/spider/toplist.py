import json

from conf import toplist_path


def get_toplist_ids() -> list[int]:
	toplist = json.load(open(toplist_path))
	toplist_ids = [song['id'] for song in toplist]
	return toplist_ids


if __name__ == '__main__':
	toplist_ids = get_toplist_ids()
	print(len(toplist_ids))
	print(toplist_ids)
	json.dump(toplist_ids, open('toplist_ids.json', 'w'))
