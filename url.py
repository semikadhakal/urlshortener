import random
import string

url_mapping = {}

def generate_short_url(long_url, length=6):
    while True:
       
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

        if short_url not in url_mapping:
            url_mapping[short_url] = long_url
            return short_url

def main():
    while True:
        long_url = input("Please Enter the long URL (or click 'q' to quit): ")
        if long_url == 'q':
            break

        short_url = generate_short_url(long_url)
        print(f"Shortened URL: http://tinyurl/{short_url}")

if __name__ == "__main__":
    main()

