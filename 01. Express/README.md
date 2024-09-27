# Express App

## Construir la imágen
```
docker build -t my-express-app . ​
```
Si hay un punto al final!

-t hace referencia a una etiqueta (tag)

## Correr la imágen
```
docker run -d -p 3000:3000 my-express-app​
```

-d hace referencia a modo descoplado (detached).

-p hace referencia a los puertos

Se usa el tag del paso anterior