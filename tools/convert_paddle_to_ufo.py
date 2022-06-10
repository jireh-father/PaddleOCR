import argparse
import json
import os


def main(args):
    ufo_dict = {"images": {}}
    with open(args.paddle_path, encoding='utf-8') as f:
        for line in f:
            file_name, points_list = line.split("\t")
            points_list = json.loads(points_list)
            ufo_dict["images"][file_name] = {
                "words": {str(i): {"points": points} for i, points in enumerate(points_list)}
            }
    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)
    json.dump(ufo_dict, open(args.output_path, "w+"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--paddle_path', default='/Users/ilseo/Documents/paddle_ic1517total.txt', type=str)
    parser.add_argument('--output_path', default='/Users/ilseo/Documents/paddle_ic1517total.csv', type=str)
    main(parser.parse_args())
