#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 as cv


# In[ ]:


#increasing_two_images
img = cv.imread("mide.jpg")
img1 = cv.resize(img, (600,600))

imge = cv.imread("mido.jpg")
imge1 = cv.resize(imge, (600,600))

increased = cv.add(img1, imge1)

cv.imshow("increased image", increased)

if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()


# In[ ]:


#decreasing_two_images
img = cv.imread("mide.jpg")
img1 = cv.resize(img, (600,600))

imge = cv.imread("mido.jpg")
imge1 = cv.resize(imge, (600,600))

decreased = cv.subtract(img1, imge1)

cv.imshow("decreased image", decreased)

if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()


# In[ ]:


#increasing_one_images
img = cv.imread("mido.jpg")
increased = cv.add(img, (70, 70, 120 ,70))
cv.imshow("increased image", increased)

if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()


# In[ ]:


#decreasing_one_images
img1 = cv.imread("mido.jpg")
decreased = cv.subtract(img1, (30, 30, 80 ,30))
cv.imshow("decreased image", decreased)

if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()


# In[ ]:




