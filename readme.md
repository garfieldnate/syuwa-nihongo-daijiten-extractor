# Data extractor for 手話・日本語大辞典 (JSL Dictionary)

This repo contains scripts relate to extracting the treasure trove of data from [this Japanese Sign Language dictionary](https://www.amazon.co.jp/%E6%89%8B%E8%A9%B1%E3%83%BB%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%A4%A7%E8%BE%9E%E5%85%B8-%E7%AB%B9%E6%9D%91-%E8%8C%82/dp/4331506800). Data I would like to extract are: Japanese glosses, hand shapes, locations and movements, a prose description of the sign and the illustration.

## What does the data look like?

Obviously I can't upload this information or the PDF's I'm working with, but you'll find sample pages under `sample_data`. The dictionary has three types of entries:
* one-handed signs
* two-handed signs with the same shape for both hands
* two-handed signs with different shapes for each hand.

## What do you plan to do with the data?

I want to play around with newer NLP technologies and multi-modal learning. Some random ideas I have:

* (simplest) generate illustrations from movement descriptions or vise-versa
* collect hand/face/body position data and train a model to convert the dictionary data into the control info for an avatar
* figure out a writing system and automatically generate spellings
