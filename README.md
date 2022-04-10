# fastai-multimodal

## Purpose:

To create end-to-end multimodal classifers based on Fastai-tabular, Fastai-text and Fastai-vision.

Specifically, I will construct 3 types of multimodal model:

- `early concat`: concatinate cnt, cat, txt, img after data loading and data preprocessing, followed by a learner of choice (e.g. fastai tabular, TabNet, Deep-RF, GSN-VSN).
- `middle concat`: concatinate the embeddings from each of the trained tab (cnt+cat), txt, img models, followed by a learner of choice.
- `late concat`: concatinate the probability predictions from each of the trained tab(cnt+cat), txt, img models, followed by a learner of choice.

Using a few benchmark datasets, I will compare the 3 types of multimodal models on their

- computation efficiency
- ML performance
- interpretability

Every iteration, I am aiming to make this package 5% better, w.r.t.
  - easy to use
  - efficent
  - stable and ready for production


## Wanna contribute?

Check out this notebook [here](https://github.com/wjlgatech/fastai-multimodal/blob/main/nbs/fastai_multimodal.ipynb). Any advices and comments are welcomed. Please shot me an email [here](wjlgatech@gmail.com).

## Credits & References:

- Zachary Mueller's initiatives https://forums.fast.ai/t/combining-tabular-images-in-fastai2-and-should-work-with-almost-any-other-type/73197

- Morgan McGuire's notebook on **Gradient Blending for Multimodal Model**: https://forums.fast.ai/t/gradient-blending-for-multi-modal-models-in-progress/75645/11

- Yuan Tian's Tabular+image: https://github.com/naity/image_tabular

- John Wu's https://gist.github.com/jwuphysics/f19162d38e1b4fed0030b96411186c3a

- AWS Autogluon multimodal benchmark data: https://auto.gluon.ai/stable/tutorials/tabular_prediction/tabular-multimodal.html

- AutoML multimodal benchmark https://github.com/sxjscience/automl_multimodal_benchmark

- CovidXrayNet: tabular + image https://github.com/MaramMonshi/CovidXrayNet
