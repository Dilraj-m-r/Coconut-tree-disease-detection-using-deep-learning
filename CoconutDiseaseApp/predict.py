from tensorflow.keras.models import load_model # type: ignore

from os import getcwd
import cv2 as cv
import imutils


def process(path):

    imagetest = cv.imread(path)
    # test_image = image.img_to_array(test_image)
    # test_image = np.expand_dims(test_image, axis=0)
    classifier = load_model(getcwd() + '\\trained_model_coconut.h5')

    gray = cv.cvtColor(imagetest, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (5, 5), 0)

    thresh = cv.threshold(gray, 45, 255, cv.THRESH_BINARY)[1]
    thresh = cv.erode(thresh, None, iterations=2)
    thresh = cv.dilate(thresh, None, iterations=2)
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv.contourArea)

    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])

    new_image = imagetest[extTop[1]:extBot[1], extLeft[0]:extRight[0]]

    image = cv.resize(new_image, dsize=(150, 150), interpolation=cv.INTER_CUBIC)
    image = image / 255.

    image = image.reshape((1, 150, 150, 3))

    result = classifier.predict(image)

    # training_set.class_indices
    print(result[0][0])
    print(result[0][1])
    print(result[0][2])
    # print(result[0][3])
    index=result[0].tolist().index(max(result[0]))
    print("Result index: ",index)

    return coconut_disease[index]   


coconut_disease = [
    {
        'title': "Eriophyid Mite",
        'description': "Eriophyid mite is a tiny pest that can cause significant damage to coconut palms. It feeds on the plant's sap, leading to stunted growth, yellowing of leaves, and in severe cases, the death of the palm.",
        'remedies': [
            "Spray neem oil or horticultural oil on affected areas to suppress mite populations.",
            "Regularly monitor palms and remove heavily infested fronds.",
            "Ensure proper irrigation and nutrient supply to boost palm health and resistance."
        ]
    },
    {
        'title': "Red Palm Weevil",
        'description': "The red palm weevil is a dangerous pest that tunnels into coconut palm trunks, causing internal damage, leaf wilting, and sometimes total collapse of the palm.",
        'remedies': [
            "Use pheromone traps to detect and reduce adult weevil populations.",
            "Apply systemic insecticides into boreholes in the trunk early in infestation.",
            "Remove and destroy severely infested palms to stop further spread."
        ]
    },
    {
        'title': "Rhinoceros Beetle",
        'description': "Rhinoceros beetles bore into the unopened fronds and crown of coconut palms, leading to V-shaped cuts on leaves and reduced plant vigor.",
        'remedies': [
            "Regularly clean plantations and remove decaying organic matter that serves as breeding grounds.",
            "Apply biocontrol agents like Metarhizium anisopliae or Baculovirus oryctes.",
            "Use mechanical removal or light traps to capture adult beetles during early morning."
        ]
    },
    {
        'title': "Rugose Spiraling Whitefly",
        'description': "Rugose spiraling whitefly is a sap-sucking insect that causes sooty mold and weakens the palm by reducing photosynthesis efficiency.",
        'remedies': [
            "Introduce biological control agents such as Encarsia guadeloupae (parasitic wasp).",
            "Spray neem oil or insecticidal soap to reduce nymph and adult populations.",
            "Use yellow sticky traps to monitor and control flying adults."
        ]
    }
]






