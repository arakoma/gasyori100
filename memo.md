### 次元数3にする

```python
if len(img_.shape) == 2:
    img = img_.copy()
    img = np.expand_dims(img, -1)
else:
    img = img_.copy()
H, W, C = img.shape
```

モノクロだと次元数2になってたりする。(ans_03での処理中とか)  
(モノクロでも、一回jpgとして保存すると、3次元にされるっぽい(?))  

関数内で次元増やした後、  
outputでは次元数3のまま返してるけど、次元数2に戻して返した方がいいかも(?)  
