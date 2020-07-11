import numpy as np
import imutils
import cv2
import requests
import glob

'''
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--template", required=True, help="Path to template image")
ap.add_argument("-i", "--images", required=True,
	help="Path to images where template will be matched")
ap.add_argument("-v", "--visualize",
	help="Flag indicating whether or not to visualize each iteration")
args = vars(ap.parse_args())
'''


response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('template5.png', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': '5JFrGRc7B9ktsMFwEnB6Pmg'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)

template = cv2.imread('no-bg.png')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template = cv2.Canny(template, 50, 200)
(tH, tW) = template.shape[:2]
cv2.imshow("Template", template)
pt = 'image5.png'

for imagePath in glob.glob(pt):
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	found = None
	for scale in np.linspace(0.2, 1.0, 20)[::-1]:
		resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
		r = gray.shape[1] / float(resized.shape[1])
		if resized.shape[0] < tH or resized.shape[1] < tW:
			break

		edged = cv2.Canny(resized, 50, 200)
		result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
		(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

		if found is None or maxVal > found[0]:
			found = (maxVal, maxLoc, r)

	(_, maxLoc, r) = found
	(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
	(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 10)
	cv2.imwrite("Imagexx.png", image)
	cv2.waitKey(0)