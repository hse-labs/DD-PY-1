Дан json файл `input.txt` содержащий список словарей

```python
[
    ...,
    {
        "score": 0.00040403710013251447,
        "id": 25007,
        "density": 0.002539960237964018,
        "contains_improvement_appeals": 1
    },
    ...
]
```

Считать содержимое файла и найти сумму значений по ключу `"contains_improvement_appeals"`.  

<div class="hint">
  Для суммирования используйте list comprehension и встроенную функцию `sum`.
</div>
