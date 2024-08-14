import requests
from bs4 import BeautifulSoup
import json
import urllib.request

BASE_URL = "https://www.google.com/search?sca_upv=1&tbm=isch&sxsrf=ADLYWIKJnFF0lYHl2w4BHP-Yv0o_zOczNw%3A1723578167014&source=hp&biw=1920&bih=959&ei=Nre7ZtapO6DL1sQP_rC1sQQ&iflsig=AL9hbdgAAAAAZrvFR8dxXLbRVJ2ZZR6btHgQMU-68eCk&oq=tesla&gs_lp=EgNpbWciBXRlc2xhKgIIADIEECMYJzIEECMYJzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESPUNUPcCWNkGcAF4AJABAJgBcaABmQSqAQMwLjW4AQPIAQD4AQGKAgtnd3Mtd2l6LWltZ5gCBqACowSoAgrCAgcQIxgnGOoCmAMEkgcDMS41oAf1Iw&sclient=img&q="


def make_request(query):
    return requests.get(BASE_URL + query)

def fetch_one_image():
    car_name_array = list()
    final_result = dict()

    with open("src/cars_data.json", "r") as f:
        cars_data = json.load(f)
        for car in cars_data["cards"]:
            car_name_array.append(f"{car['maker']} {car['model']}")

    for car in car_name_array:
        response = make_request(car)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            images = soup.find_all("img")
            for image in images:
                final_result[car] = image["src"]
                if image["src"].endswith("gif"):
                    continue

                with open(f"src/images/{car}.jpg", "wb") as f:
                    f.write(urllib.request.urlopen(image["src"]).read())

        else:
            print("Error")

def fetch_images_with_amount(amount: int):
    car_name_array = list()
    final_result = dict()

    # Load car data
    with open("src/cars_data.json", "r") as f:
        cars_data = json.load(f)
        for car in cars_data["cards"]:
            car_name_array.append(f"{car['maker']} {car['model']}")

    for car in car_name_array:
        response = make_request(car)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            images = soup.find_all("img")
            count = 0
            for image in images:
                if count >= amount:
                    break
                
                src = image["src"]
                if src.endswith("gif"):
                    continue

                # Generate file name with number
                file_name = f"src/images/{car.replace(' ', '_')}-{count + 1}.jpg"
                try:
                    # Save image
                    with open(file_name, "wb") as f:
                        f.write(urllib.request.urlopen(src).read())
                    final_result[f"{car}-{count + 1}"] = src
                    count += 1
                except Exception as e:
                    print(f"Failed to download image {src} for {car}: {e}")

        else:
            print(f"Error fetching images for {car}")

    return final_result

def main():
    fetch_images_with_amount(3)


if __name__ == "__main__":
    main()
