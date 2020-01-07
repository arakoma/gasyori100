### 次元数3にする

```python
if len(img_.shape) == 3:
    img = img_.copy()
if len(img_.shape) == 2:
    img = img_.copy()
    img = np.expand_dims(img, -1)
H, W, C = img.shape
```

モノクロだと次元数2になってたりする。(ans_03での処理中とか)  
(モノクロでも、一回jpgとして保存すると、3次元にされるっぽい(?))  