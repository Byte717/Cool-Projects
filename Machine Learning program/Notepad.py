import numpy
import pygame
import tensorflow as tf
import numpy as np
import os
import cv2
import time
from PIL import Image
from numpy import asarray



img = None
model = tf.keras.models.load_model('digit1')
pygame.init()
screen = pygame.display.set_mode([560,560])
screen.fill((255, 255, 255))
pygame.display.flip()
path = "/Users/3020601/PycharmProjects/PyTest/test.jpeg"
pygame.display.set_caption('DIGIT RECOGNIZER')
mnist = tf.keras.datasets.mnist
(x,y) = mnist.load_data()
def train(answer):
    img = cv2.imread('test.jpeg')[:, :, 0]
    img = np.invert(np.array([img]))
    ans = np.array([answer])
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f"Wait the answer was {answer}? Let me Memorize that,", True,(0,0,0))
    text2 = font.render("and btw, you have bad handwritting",True, (0,0,0))
    text3 = font.render("and done!", True,(0,0,0))
    screen.blit(text,(30,500))
    screen.blit(text2,(30,520))
    pygame.display.flip()
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    predictions = model(img[:1]).numpy()
    tf.nn.softmax(predictions).numpy()
    loss_fn(ans[:1], predictions).numpy()
    model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
    while model.evaluate(img,ans)[-1] <= 0.5 and model.evaluate(img,ans)[0] > 0.4:
        model.fit(img, ans, epochs=1)
    time.sleep(2)
    screen.blit(text3,(30,535))
    pygame.display.flip()
    screen.fill((255,255,255), rect=(0,500,560,560))
    pygame.display.flip()
    model.fit(img,ans,epochs=1)
    model.save("digit1")

def draw(x,y):
    s = pygame.Surface((40,40))
    s.fill((0,0,0))
    r, r.x, r.y = s.get_rect(), x, y
    screen.blit(s, r)
    pygame.display.flip()

def predict():
    img = cv2.imread('test.jpeg')[:, :, 0]
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(f"the result is: {np.argmax(prediction)}", True,(0,0,0))
    screen.blit(text,(50,30))
    pygame.display.flip()


running = True
correction = False
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            draw(mouse_x,mouse_y)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            img = pygame.transform.smoothscale(screen,(28,28))
            pygame.image.save(img, "test.jpeg")
            predict()
            correction = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            screen.fill((255, 255, 255))
            pygame.display.flip()
            correction = False
        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_0) and correction == True:
            train(0)

        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_1) and correction == True:
            train(1)

        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_2) and correction == True:
            train(2)

        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_3) and correction == True:
            train(3)

        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_4) and correction == True:
            train(4)

        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_5) and correction == True:
            train(5)

        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_6) and correction == True:
            train(6)

        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_7) and correction == True:
            train(7)

        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_8) and correction == True:
            train(8)

        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_9) and correction == True:
            train(9)




pygame.quit()
os.remove(path)
model.evaluate(x,y,verbose=1)
model.save('digit1')
