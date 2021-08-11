import glob
import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description='Upload Files')
    parser.add_argument('username', help='Username')
    args = parser.parse_args()

    url = "http://127.0.0.1:5000/upload/{}".format(args.username)
    for file in glob.glob('WP[W,T]*.txt'):
        file_string = {'file': open(file, 'rb')}
        print("Uploading {}".format(file))
        r = requests.post(url, files=file_string)

if __name__ == '__main__':
    main()